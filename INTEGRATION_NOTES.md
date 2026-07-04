# How to integrate these files into docs.skylogs.io

This bundle is a complete `docs/` tree for your Docusaurus site plus `sidebars.js`.
It contains **59 pages**: ~20 fully written, the rest structured stubs.

## Written vs. stub pages

- **Written pages** are ready to publish (grep for `{/* TODO` for product details to verify).
- **Stub pages** have `draft: true` in their frontmatter: Docusaurus EXCLUDES them from
  production builds but shows them in local dev (`yarn start`). Each stub contains its
  purpose and a planned outline. To publish a page: write it, delete the `draft: true` line.

List all remaining drafts:   grep -rln "draft: true" docs/
List all remaining TODOs:    grep -rn "TODO" docs/

## Setup (same as before)

1. Replace your repo's `docs/` folder and `sidebars.js` with this bundle's
   (delete the default Docusaurus tutorial folders).
2. In `docusaurus.config.js`: set `routeBasePath: '/'` for docs, `blog: false` (or keep it),
   `url: 'https://docs.skylogs.io'`, `baseUrl: '/'`, and delete `src/pages/index.js`
   (intro.md has `slug: /` and becomes the landing page).

## Sidebar structure (positions)

1. What is Skylogs? (intro)
2. Getting started — installation ✅, quick-start ✅, first-integration, migrating, demo
3. Concepts — core-concepts ✅, architecture ✅, shared-responsibility, alert-lifecycle,
   root-cause-analysis, incident-simulation, security-model
4. Deployment — multi-zone-ha ✅, kubernetes, sizing, upgrades, reference-architectures
5. Guides — user-guide ✅, admin-guide ✅, oncall-schedules, escalation-patterns,
   status-pages, notification-channels, backup-restore, monitoring-skylogs, game-days
6. Integrations — overview ✅, prometheus-alertmanager ✅, grafana ✅, zabbix ✅,
   datadog ✅, splunk ✅, elastic ✅, pmm ✅, generic-webhook ✅, then draft stubs:
   nagios-icinga, checkmk, cloudwatch, azure-monitor, google-cloud, sentry, new-relic,
   uptime-kuma, netdata, outbound
7. API reference — rest-api ✅ (skeleton), openapi, authentication, ingestion,
   webhook-events, rate-limits, scenario-file
8. Troubleshooting — faq, installation, notifications, cluster (all stubs)
9. Contributing — overview ✅, integration-authoring (stub)

✅ = written. Everything else is a draft stub with a planned outline.

## Stable URLs (linked from the main README — must keep working)

/ , /installation , /quick-start , /concepts , /architecture , /deployment ,
/integrations , /user-guide , /admin-guide , /api , /contributing

## Suggested writing order for the stubs

1. /migrating (Opsgenie/PagerDuty) — captures people actively shopping
2. /deployment/kubernetes — your audience deploys on k8s
3. /guides/monitoring-skylogs — the question every serious evaluator asks
4. /guides/notification-channels — needed by every real install
5. /troubleshooting/notifications — the most critical support path
Then follow demand: turn every repeated GitHub issue/discussion into a page.
