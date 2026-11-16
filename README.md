# NFC Summit 2027 — team decks

The internal website where the NFC team finds, presents and shares the five 2027 decks:

| Deck | For | Slides |
|---|---|---|
| General Presentation | Everyone: partners, press, sponsors, speakers | 23 |
| CryptoStamp Corner | Postal services and digital stamp issuers | 9 |
| NFC Artist Cards — Kawaii × PHANTASM | Artists invited to draw a card | 11 |
| NFC Collection Cards | NFT and PFP collections | 14 |
| NFC Street Activations — On The Wall | Sponsors, galleries, platforms, communities | 29 |

Every deck plays full screen in the browser (arrow keys, **F** full screen, **N** speaker notes, **G** all slides, swipe on a phone), downloads as a PDF, and has its own link to send.

## Going live

The site is static: the home page is `index.html` at the root, each deck lives in `decks/<name>/`.
The repo is connected to Vercel (team `nfcsummit`, project `slides`): every push to `main` updates the site within a minute.

The site is not indexed by search engines (`noindex`), but anyone with the link can open it, and **this repo is public**: everything committed here can be read on GitHub. A password on the site needs Vercel's *Deployment Protection* (Pro plan).

## Changing a deck with Claude Code

In the repo folder, run `claude`, then for example:

```
/update-deck Street Activations: replace "Your wall is waiting." with "Pick your wall."
/update-deck General Presentation: add a pause slide with the Parties dragon before "Every night, everywhere."
```

Claude edits the deck source, rebuilds the site and the PDFs, checks the slides it touched, then pushes: Vercel publishes within a minute.
Everything Claude needs is in `CLAUDE.md` (repo layout, design-system rules).

Without Claude Code:

```bash
pip3 install playwright pillow && python3 -m playwright install chromium   # first time only
python3 src/build_site.py && python3 src/render.py
git add -A && git commit -m "…" && git push
```

## The originals on claude.ai

The five decks also exist as editable Slides on claude.ai (John's account), linked to the NFC Summit 2027 Design System. This repo does not update them: to carry a change over, ask Claude in the "Nfc 27" project.

## The old Street Activations v7 deck (September 2026)

The files that were at the root before the site (`NFC Street Activations.dc.html`, the `.mp4` files, `compressed/`, `uploads/`, `_ds/`, `assets/dragons/`, `deck-stage.js`, `image-slot.js`, `support.js`) make up the old v7 deck. It stays online at its own address (`/NFC Street Activations.dc.html`); only the root of the site now shows the team page. Do not move these files: the deck loads its videos from `raw.githubusercontent.com/hs7j4yk4sz-boop/slides/main/…`. The current version of the deck is `decks/street-activations/`.
