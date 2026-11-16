---
description: Change an NFC 2027 deck (text, slide, image, order), rebuild the site, check it and push it live
argument-hint: <which deck and what to change, in plain words>
---

Change requested: $ARGUMENTS

Follow these steps in order. Read `CLAUDE.md` first if you have not in this session: it holds the layout of the repo and the design rules.

1. **Find the deck.** Map the request to its spec: general presentation → `src/gp.py`, CryptoStamp → `src/cs.py`, Artist Cards → `src/ac.py`, Collection Cards → `src/cc.py`, Street Activations / On The Wall → `src/sa.py`. If the request names no deck and it is not obvious, ask which one.

2. **Make the change in the spec**, never in `decks/` or `index.html` (they are generated).
   - Text: edit the strings of the template call. Keep the notes (last text argument) in sync with the slide.
   - New slide: add a template call at the right place, reusing a template already used in that deck when possible (`pause_video`, `pause_dragon`, `value_offer`, `vstatement`, `world`…). Give it a new unique id.
   - Remove or move a slide: delete or move its call.
   - New image or video: `python3 src/tools/optimize_media.py <file> <group/name.ext>` then use that key. Ask for the file if it was not given.
   - Respect the design rules of `CLAUDE.md` (two typefaces, yellow not white, dragons on black, one pause every three or four slides, value before price, no price on offer intros, artworks never graded). If the request breaks one, say which rule and ask before doing it.

3. **Build**: `python3 src/build_site.py` then `python3 src/render.py <slug>` for each deck you touched.

4. **Check what you changed.** Open the thumbnails of the changed slides (`decks/<slug>/thumbs/NN.jpg`) and look at them: no text running out of the frame, no overlap, the title in the same place as on similar slides. Fix and rebuild until it is clean. If the slide count changed, check that the home page still reads well (`python3 -m http.server 8000`).

5. **Commit and push**: one commit per request, message in English starting with the deck, e.g. `street-activations: new pause slide before the offers`. Then `git push`. Vercel deploys `main` by itself within a minute.

6. **Report** in two or three short lines, in the language the request was written in: what changed, on which slides (numbers), and the deck link on the site. Mention that the claude.ai copy of the deck was not updated, if the change matters there too.
