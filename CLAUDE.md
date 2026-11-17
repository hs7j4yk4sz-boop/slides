# NFC Summit 2027 — team deck site

This repo (`hs7j4yk4sz-boop/slides`, **public**) is the internal website where the NFC team finds, presents and shares the five 2027 decks.
It is a static site (no framework, no build on the server): Vercel serves the files as they are.
The decks themselves are generated from Python specs in `src/`, so every change goes through the source, never through the generated HTML.

**The repo is public**: never commit private data (personal emails or phone numbers, contracts, client lists, unpublished deals beyond what the decks already show).

## Layout

| Path | What it is | Edit by hand? |
|---|---|---|
| `src/gp.py` `src/cs.py` `src/ac.py` `src/cc.py` `src/sa.py` | One spec per deck: the slides in order, their text, their media and their speaker notes | **Yes — this is where content changes** |
| `src/nfclib.py` | The slide templates (cover, statement, pause_video, pause_dragon, value_offer, closing…) and `DECK_CSS` | Only for a design change that applies to every deck |
| `src/build_site.py` | Builds `index.html` and `decks/<slug>/index.html`; the `DECKS` list holds titles, audiences and descriptions shown on the home page | Yes, for the home page texts or a new deck |
| `src/render.py` | Thumbnails, covers and PDFs (Playwright) | Rarely |
| `src/tools/optimize_media.py` | Adds a photo, video or drawing to `media/`, made light for the web | Run it, don't edit media by hand |
| `media/` | Every image and video the decks use, already graded and compressed | Through `optimize_media.py` |
| `assets/` | Viewer (`viewer.js`, `viewer.css`), home page style (`hub.css`), favicon | For viewer or home page changes |
| `decks/`, `index.html` | **Generated.** Never edit: rebuild instead | No |
| `offers/<slug>/` | The vertical partner-offer decks (catalogue + one deck per offer, 1080 × 1920): `pages/NN.jpg`, thumbnails `NN-s.jpg`, `cover.jpg`, the PDF and `pages.json`, exported from their Claude Design canvases. `index.html` in each folder is generated (`OFFERS` in `src/build_site.py`) | No: export the pages again from the canvas |
| `NFC Street Activations.dc.html`, root `*.mp4`, `compressed/`, `uploads/`, `_ds/`, `assets/dragons/`, `deck-stage.js`, `image-slot.js`, `support.js` | The old Street Activations v7 deck (Sept 2026), still online at its own address. Its videos load from `raw.githubusercontent.com/hs7j4yk4sz-boop/slides/main/…` | **No — never move, rename or delete** |

Deck slugs: `general-presentation` (gp), `cryptostamp-corner` (cs), `artist-cards` (ac), `collection-cards` (cc), `street-activations` (sa).

## Build

```bash
python3 src/build_site.py      # HTML for the home page and the five decks
python3 src/render.py          # thumbnails, covers, PDFs (all decks)
python3 src/render.py street-activations   # or only the deck you touched
python3 -m http.server 8000    # preview at http://localhost:8000
```

First time on a machine: `pip3 install playwright pillow && python3 -m playwright install chromium` (and `ffmpeg` for videos: `brew install ffmpeg`).

Always run both build steps before committing: the PDFs and thumbnails must match the slides.
Pushing to `main` deploys on Vercel by itself.

## How a slide is written

Each spec calls template functions from `nfclib.py`, for example:

```python
pause_dragon(d, 'waiting', 'ringmaster-hero', 'Five ways in', 'Your wall<br>is waiting.', 'Speaker notes…', side='right', h=980)
pause_video(d, 'street', 'videos-2026/mur-crane-pixel', 'On The Wall', 'The street<br>is the gallery.', 'Notes…', 'Alt text', poster='px/courtyard-drone.jpg')
```

- The first argument is always the deck `d`, the second the slide id (unique in the deck, lowercase, hyphens).
- The order of the calls is the order of the slides. Page numbers are recomputed at build time.
- Media are referenced by key, the path under `media/` (`photos-2026/scene-speaker.jpg`, `dragons-2027/dragon-parties.png`). A PNG key finds its `.webp` file automatically.
- The last text argument of most templates is the speaker note: it is what the presenter says, and what the team reads with **N** in the viewer. Details, full lists and figures go there, not on the slide.

## Design rules (from the NFC Summit 2027 design system — keep them)

- **Two typefaces only**: Anton (titles, figures) and Space Grotesk (everything else). Nothing under 24 px on a 1920 × 1080 slide.
- **One idea per slide**: a label, a title, one sentence. The rest goes in the notes.
- **Slides 2 and 3** of every deck: a 2026 video full frame and one strong sentence.
- **No white slides.** A light slide is yellow (`#F6B800`) with ink text. A deck has at least three yellow slides.
- **Dragons on black.** The riso dragons are yellow: they stand out on ink `#0B0B0B`, not on yellow. Always cut by an edge of the frame, never floating, never on a photo.
- **Breathe**: about one slide in four says almost nothing — `pause_video` (a title alone on a 2026 video) or `pause_dragon` (one statement, one dragon, on black). Four to six words. One before each dense part (programme, offers, deal).
- **Offers, value first**: `value_offer` shows four concrete benefits in big figures; the price sits small (112 px max) in the black stub at the bottom. Never a price on an offer's intro slide.
- **Never grade or recolour artworks** (Polygon1993, PHANTASM cards). 2026 photos and videos are already graded in their files: never grade them twice.
- **No protected characters** (mascots, cartoon characters, brand figures) drawn or added.
- **Contact on every deck**: John Karp · john@nonfungibleconference.com · t.me/thejonnkarp. No phone number.
- **English only for anything public or shared with the team**: decks, home page, viewer labels, README, commit messages, pull requests. (Chat with John can stay in French.)

## The claude.ai copies

The vertical offer decks (`offers/`) have no Python spec: their source is a Claude Design canvas on claude.ai (links in `OFFERS` in `src/build_site.py`). Each canvas has two pages: Yellow (the one on this site) and a colour variant. To change one, change the canvas, export its pages into `offers/<slug>/`, then run `python3 src/build_site.py`.


Each deck also exists as an editable Slides artifact on claude.ai (links in `DECKS` in `src/build_site.py`, John's account), linked to the NFC Summit 2027 Design System artifact.
This repo does not update them. When a change made here should also appear there, ask Claude in the "Nfc 27" project to republish that deck from the same spec.
