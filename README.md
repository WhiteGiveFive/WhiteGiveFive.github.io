# Personal site — prototype

Astro 7, static, deployed to GitHub Pages. Governed by [`../SPEC.md`](../SPEC.md).

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # -> dist/
```

## Publishing a note (spec C4)

Create one file. Nothing else.

```bash
cat > src/content/notes/2026-08-25-something.md <<'MD'
---
title: "Title"
date: 2026-08-25
summary: "One line for the index and the RSS feed."
tags: ["ai-hab"]
---

Body. LaTeX works: $\alpha$ inline, $$…$$ for display.
MD
git add -A && git commit -m "note: something" && git push
```

Indexes, the homepage "Highlights" block, the RSS feed and the sitemap all update
themselves. Set `draft: true` in the frontmatter to keep an entry out of the
build. Long-form pieces are identical but live in `src/content/writing/`.

## Where things are defined — one place each

| Thing | File |
|---|---|
| Name, positioning, bio, links, email | `src/site.config.ts` |
| Homepage Recent activities log | `src/data/activities.json` |
| Publications (drives /research and /cv) | `src/data/publications.json` |
| Projects (drives /projects) | `src/data/projects.json` |
| Everything else on the CV | `src/data/cv.json` |
| Visual system | `src/styles/global.css` |
| Downloadable CV generator | `scripts/generate_cv_pdf.py` |

## Logging a recent activity

Add an entry to `src/data/activities.json` with `date`, `kind`, `title`,
`summary` and `url` (use an empty string when there is no link). Entries appear
on the homepage newest first. Use `YYYY`, `YYYY-MM` or `YYYY-MM-DD` to match
the date you know; entries with the same date keep their order in the file.
Add an optional `links` array of `{ "label": "…", "url": "…" }` objects for
supporting resources such as code or demonstrators.
Summaries can be plain strings or arrays of text and `{ "label": "…", "url": "…" }`
objects to link names within the description.

The log can include publications, talks, workshops, funding awards, project
updates and other activities. It is separate from the full publication and
project listings, so an activity can be a short update rather than a citation.

## Regenerating the PDF CV

The downloadable PDF is generated from the same `cv.json` and
`publications.json` files used by the HTML CV:

```bash
python3 scripts/generate_cv_pdf.py
```

The script requires ReportLab and writes
`public/cv/Hongrui-Shi-CV.pdf`. Regenerate it after material CV edits.

## Design note

The one deliberate move (spec C7) is the **monospace date gutter**: every dated
entry hangs its date in the left margin, so the site reads as a logbook rather
than a blog. Below 44rem, the date and content type become a compact inline
stamp above the title. If you want a different memorable move, this is the
thing to replace — do not add a second one.

## Future asset swaps

- `public/favicon.svg` is a placeholder letterform.
- `public/profile.jpg` is the current profile photo, sourced from
  `../metadata/avatar/photo.jpg`.
