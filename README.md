# Handoff: NFC Street Activations deck — v7 (25 slides)

`index.html` is an identical copy of the deck for hosts that need a default document.

## What this is
A finished, self-contained slide deck (`NFC Street Activations.dc.html`) built as a static HTML file — not a component to reimplement, just a file to deploy as-is. It renders correctly when opened directly in a browser as long as its relative asset paths (`compressed/`, `assets/`, `_ds/`, `uploads/`, and the loose `.js` files at the root) stay in the same relative positions to it.

## What to do with it
1. `git init` this folder (or copy its contents into an existing repo).
2. Commit everything, `git push` to the target GitHub repo (`hs7j4yk4sz-boop/slides`, branch `main`, already holds the 6 background videos this deck links to via `raw.githubusercontent.com` — no video files are duplicated in this bundle).
3. Deploy the repo to Vercel (or any static host) with no build step — it's plain HTML/CSS/JS, served as-is. The entry file is `NFC Street Activations.dc.html`; you may want to rename/symlink it to `index.html` depending on the host's default-document rules.

## Structure
- `NFC Street Activations.dc.html` — the deck. Navigation: arrow keys / click-drag on a deck-stage web component (`deck-stage.js`).
- `compressed/` — optimized JPGs used by several slides.
- `assets/dragons/`, `assets/logo-*` — NFC Summit design-system illustration assets.
- `_ds/` — the bound NFC Summit 2027 design system bundle (fonts/colors/typography CSS + a JS bundle the deck's `<helmet>` loads).
- `uploads/` — remaining source photos referenced directly by the deck.
- `deck-stage.js`, `image-slot.js`, `support.js` — plain JS web components the deck's `<helmet>`/template load; no build step, no bundler.
- The six background videos (art wrap, Normies flyover, OpenSea loop, courtyard clip, two mural clips) are NOT included here — the deck's `<video>` tags already point at `https://raw.githubusercontent.com/hs7j4yk4sz-boop/slides/main/...`, so they load from that repo at runtime.

## v7 changes (2026-09-10)
Copy-only pass: cover subtitle, "one of our artists", houses installed 27–28 May (two days), "painted on one exterior side", "One shell, five ways", PFP copy (prominent position, hand-painted), 500 names, email john@nonfungibleconference.com, flagship XCOPY sentence without the 20,000 stat. Slide layouts unchanged. No new video files — the six raw.githubusercontent.com links are unchanged.

## Fidelity
This is the final, approved design — not a wireframe. Deploy it as-is; no restyling or recreation needed.
