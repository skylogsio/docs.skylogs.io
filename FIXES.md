# Revision 2 — installation/quick-start merge + deployment restructure (delete after review)

Structure changes (as requested):
- Quick Start (docs/getting-started/quickstart.md) is now the single install+first-alert guide
  at /quick-start; heading hierarchy normalized (Steps 1-4); added Next Steps linking to /deployment
- Deployment is now the home of advanced installation, with a generated section index at /deployment:
  1. Docker Compose (production) - NEW page: pinned releases, config, persistence, TLS, upgrades
  2. Kubernetes / Helm (draft stub)
  3. Multi-zone & HA (moved to /deployment/multi-zone-ha)
  4. Sizing  5. Upgrades  6. Reference architectures
- getting-started order: overview(1), quickstart(2), datasource(3, new draft stub - was an empty file),
  endpoint(4, new draft stub - was an empty file), first-integration(5), migrating(6), demo(7)

Repairs:
- Re-applied deletions lost when the fixed zip was extracted over the old checkout (zip overwrites,
  never deletes): docs/intro.md, docs/api.md, docs/contributing.md, docs/integrations/other-platforms.md,
  docs/getting-started/quick-start.md, docs/quick-start.md (stray copy at docs root),
  root strays (ingestion.md, overview.md, rest-api.md), src/pages/markdown-page.md
  -- this also re-fixes the /quick-start duplicate-route build failure
- Restored the 4 alert-management screenshots and corrected their paths (../../images/ - the images
  live in docs/images/, two levels up from that page)
- All internal /installation links now point to /quick-start
- nginx.conf: 301 /installation -> /quick-start (keeps the main repo README link working)

Tip for next time: apply changes with rsync --delete or git, not zip extraction over a checkout.
