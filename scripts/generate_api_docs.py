#!/usr/bin/env python3
"""Generate Docusaurus API reference pages from the Skylogs OpenAPI spec (docs.json).

Usage: python3 generate_api_docs.py <path-to-docs.json> <output-docs-dir>
Regenerate whenever the API changes; commit the output.
"""
import json, sys, re
from collections import OrderedDict

SPEC_PATH = sys.argv[1] if len(sys.argv) > 1 else 'docs.json'
OUT_DIR = sys.argv[2] if len(sys.argv) > 2 else 'docs/api'

spec = json.load(open(SPEC_PATH))
SCHEMAS = spec.get('components', {}).get('schemas', {})

# Page plan: (filename, id, title, sidebar_position, slug, [tags], intro)
PAGES = [
    ("alert-rules.md", "api-alert-rules", "Alert rules", 4, "/api/alert-rules",
     ["AlertRule", "AlertRule Behavior Rules"],
     "Alert rules are the core object of the Skylogs API: each rule defines what to match from a source "
     "(Prometheus, Zabbix, Grafana, an inbound API alert, …), who owns it, and how to notify. "
     "Creation uses a single endpoint with a `type` discriminator selecting the body shape. "
     "Behavior rules attach notification, template, or silence behavior to an alert rule."),
    ("users-teams.md", "api-users-teams", "Users & teams", 5, "/api/users-teams",
     ["Users", "Teams"],
     "Manage users, teams, and ownership transfer."),
    ("endpoints.md", "api-endpoints", "Notification endpoints", 6, "/api/endpoints",
     ["Endpoints"],
     "Endpoints are the channels through which a user or flow is notified (SMS, call, email, Telegram, …). "
     "Endpoints are verified with an OTP before they can carry alerts."),
    ("data-sources.md", "api-data-sources", "Data sources & Prometheus", 7, "/api/data-sources",
     ["Data Sources", "Prometheus"],
     "Data sources connect Skylogs to monitoring systems. The Prometheus endpoints let clients browse "
     "labels, rules, and currently firing alerts of a connected Prometheus."),
    ("configuration.md", "api-configuration", "Notification provider configs", 8, "/api/configuration",
     ["ConfigCall", "ConfigEmail", "ConfigSms", "ConfigTelegram", "ConfigSkylogs"],
     "Instance-wide provider configuration for call, email, SMS, and Telegram delivery, plus the Skylogs "
     "cluster configuration. Providers support a **default** and a **backup** config — if the default "
     "provider fails, delivery falls back to the backup."),
    ("status-pages.md", "api-status-pages", "Status pages", 9, "/api/status-pages",
     ["Status"],
     "Create and manage status pages."),
    ("instances-assets.md", "api-instances-assets", "Instances & profile assets", 10, "/api/instances-assets",
     ["SkylogsInstance", "ProfileAsset"],
     "Skylogs instances represent connected Skylogs deployments (e.g. zones). Profile assets provision "
     "alert rules from asset definitions."),
]

def deref(schema, depth=0):
    """Resolve $ref and merge allOf into a flat dict with properties/required."""
    if not isinstance(schema, dict) or depth > 8:
        return schema or {}
    if '$ref' in schema:
        name = schema['$ref'].split('/')[-1]
        resolved = deref(SCHEMAS.get(name, {}), depth + 1)
        resolved = dict(resolved)
        resolved.setdefault('x-name', name)
        return resolved
    if 'allOf' in schema:
        merged = {'type': 'object', 'properties': OrderedDict(), 'required': []}
        for part in schema['allOf']:
            r = deref(part, depth + 1)
            merged['properties'].update(r.get('properties', {}))
            merged['required'] += r.get('required', [])
        for k in ('title', 'description'):
            if k in schema:
                merged[k] = schema[k]
        return merged
    return schema

def type_str(s):
    s = s or {}
    t = s.get('type', '')
    if t == 'array':
        return f"array of {type_str(s.get('items', {})) or 'object'}"
    if 'enum' in s:
        return f"{t} ({' | '.join(map(str, s['enum']))})"
    return t or ('object' if 'properties' in s or '$ref' in s or 'allOf' in s else '')

def esc(text):
    return str(text).replace('|', '\\|').replace('\n', ' ').strip()

def props_table(schema, out):
    schema = deref(schema)
    props = schema.get('properties', {})
    required = set(schema.get('required', []))
    if not props:
        if schema.get('description'):
            out.append(schema['description'])
        return
    out.append("| Field | Type | Required | Description |")
    out.append("|---|---|---|---|")
    for name, ps in props.items():
        ps_r = ps if isinstance(ps, dict) and '$ref' not in ps and 'allOf' not in ps else deref(ps)
        desc = ps_r.get('description', '')
        ex = ps_r.get('example')
        if ex is not None:
            desc = f"{desc} Example: `{json.dumps(ex) if not isinstance(ex, str) else ex}`".strip()
        out.append(f"| `{name}` | {esc(type_str(ps_r))} | {'✅' if name in required else ''} | {esc(desc)} |")

def request_body_md(op, out):
    rb = op.get('requestBody')
    if not rb:
        return
    for ctype, c in rb.get('content', {}).items():
        schema = c.get('schema', {})
        out.append(f"**Request body** (`{ctype}`)")
        out.append("")
        if 'oneOf' in schema:
            disc = schema.get('discriminator', {})
            prop = disc.get('propertyName')
            if prop:
                out.append(f"The body is selected by the `{prop}` discriminator:")
                out.append("")
            for variant in schema['oneOf']:
                v = deref(variant)
                title = v.get('title') or v.get('x-name', 'variant')
                out.append(f"<details><summary><b>{title}</b>" +
                           (f" — {esc(v.get('description',''))}" if v.get('description') else "") +
                           "</summary>")
                out.append("")
                if 'oneOf' in v:  # nested discriminator (queryType)
                    ndisc = v.get('discriminator', {}).get('propertyName', '')
                    for nv in v['oneOf']:
                        nvr = deref(nv)
                        out.append(f"*Variant `{ndisc}`: **{nvr.get('title') or nvr.get('x-name','')}***")
                        out.append("")
                        props_table(nvr, out)
                        out.append("")
                else:
                    props_table(v, out)
                out.append("")
                out.append("</details>")
                out.append("")
        else:
            props_table(schema, out)
            out.append("")

def params_md(op, out):
    params = op.get('parameters', [])
    if not params:
        return
    out.append("**Parameters**")
    out.append("")
    out.append("| Name | In | Required | Type | Description |")
    out.append("|---|---|---|---|---|")
    for p in params:
        s = p.get('schema', {})
        out.append(f"| `{p.get('name')}` | {p.get('in')} | {'✅' if p.get('required') else ''} | "
                   f"{esc(type_str(s))} | {esc(p.get('description',''))} |")
    out.append("")

def responses_md(op, out):
    resp = op.get('responses', {})
    if not resp:
        return
    lines = []
    for code, r in resp.items():
        lines.append(f"`{code}` {esc(r.get('description',''))}")
    out.append("**Responses:** " + " · ".join(lines))
    out.append("")

def anchor(m, p):
    return re.sub(r'[^a-z0-9]+', '-', f"{m}-{p}".lower()).strip('-')

# Collect ops by tag preserving path order
by_tag = {}
for path in spec['paths']:
    for method, op in spec['paths'][path].items():
        if not isinstance(op, dict):
            continue
        for t in op.get('tags', ['Untagged']):
            by_tag.setdefault(t, []).append((method, path, op))

def security_note(op):
    sec = op.get('security', None)
    if sec == []:
        return "No auth"
    return "Bearer JWT"

for fname, pid, title, pos, slug, tags, intro in PAGES:
    out = []
    out.append("---")
    out.append(f"id: {pid}")
    out.append(f"title: {title}")
    out.append(f"sidebar_position: {pos}")
    out.append(f"slug: {slug}")
    out.append("---")
    out.append("")
    out.append(f"# {title}")
    out.append("")
    out.append(":::note Generated reference")
    out.append("This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). "
               "Do not edit by hand — regenerate when the API changes.")
    out.append(":::")
    out.append("")
    out.append(intro)
    out.append("")
    out.append("All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).")
    out.append("")
    for tag in tags:
        ops = by_tag.get(tag, [])
        if not ops:
            continue
        if len(tags) > 1:
            out.append(f"## {tag}")
            out.append("")
        # summary table
        out.append("| Endpoint | Summary |")
        out.append("|---|---|")
        for m, p, op in ops:
            out.append(f"| [`{m.upper()} {p}`](#{anchor(m,p)}) | {esc(op.get('summary',''))} |")
        out.append("")
        for m, p, op in ops:
            out.append(f"### `{m.upper()} {p}` {{#{anchor(m,p)}}}")
            out.append("")
            if op.get('summary'):
                out.append(f"**{op['summary']}**")
                out.append("")
            if op.get('description'):
                out.append(op['description'])
                out.append("")
            params_md(op, out)
            request_body_md(op, out)
            responses_md(op, out)
    with open(f"{OUT_DIR}/{fname}", "w") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"wrote {OUT_DIR}/{fname}")
