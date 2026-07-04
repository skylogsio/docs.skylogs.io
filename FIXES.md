# Fixes applied (delete this file after review)

Build breakers:
1. docusaurus.config.js: navbar sidebarId "tutorialSidebar" -> "docsSidebar" (sidebars.js exports docsSidebar; mismatch fails the build)
2. Duplicate slug collisions resolved (kept the authored/categorized page, removed the superseded one):
   - "/"            kept docs/introduction.md            removed docs/intro.md
   - "/api"         kept docs/api/rest-api.md            removed docs/api.md
   - "/deployment"  kept docs/deployment/multi-zone-ha.md removed docs/deployment.md
   - "/contributing" kept docs/contributing/overview.md   removed docs/contributing.md
   - quickstart: kept docs/getting-started/quickstart.md (Discord guide), removed placeholder quick-start.md,
     and gave quickstart.md slug /quick-start so existing links keep working
3. docs/api/alert-rules.md + configuration.md: <details> JSX (MDX end-tag-mismatch) — replaced
   scripts/generate_api_docs.py with the version that emits #### headings and regenerated all 7 API pages
4. docs/getting-started/installation.md: bold **http://localhost:PORT** -> code span (URL-parse failure)
5. docs/guides/alert-management/alert-management.md: 4 references to non-existent ../images/*.png
   replaced with {/* TODO: add screenshot ... */} comments — restore them when the screenshots exist

Cleanup / correctness:
6. Removed stray root files not part of the site: ingestion.md, overview.md, rest-api.md, src/pages/markdown-page.md
7. Removed docs/integrations/other-platforms.md (superseded by per-tool pages; nothing linked to it)
8. docker-compose.yml: docs-dev port mapping 3000:3000 -> 3000:80 (package.json start uses --port 80);
   added optional typesense service under profile "search" (the search theme expects host typesense:8108;
   you still need to run the docsearch scraper and replace the "xyz" API key)
9. Config polish: tagline ("Dinosaurs are cool" -> real tagline), footer Intro link /docs/introduction -> /,
   copyright "My Project, Inc." -> Skylogs

Recommendations (not applied):
- Switch onBrokenLinks from "warn" to "throw" once content stabilizes, so broken links fail CI
- The typesense apiKey "xyz" in docusaurus.config.js is a placeholder; use a search-only key in production
