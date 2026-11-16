"""Build the NFC Summit 2027 team website from the deck sources.

    python3 src/build_site.py          # writes index.html and decks/<slug>/index.html
    node src/render.js                 # then: thumbnails, covers and PDFs (needs Playwright)

Each deck is a Python spec in src/ (gp.py, cs.py, ac.py, cc.py, sa.py) built with the templates of src/nfclib.py.
Media keys in the specs ('photos-2026/scene-speaker.jpg') point to files in media/.
"""
import datetime, html, importlib, json, os, re, sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC)
os.chdir(SRC)   # the deck specs import nfclib from the current folder
from nfclib import DECK_CSS, LOCAL, MEDIA   # noqa: E402

# The five decks, in the order the team sees them. 'claude' is the editable original on claude.ai (John's account).
DECKS = [
    dict(slug='general-presentation', mod='gp', title='General Presentation',
         audience='Tout le monde : partenaires, presse, sponsors, speakers',
         desc='Le festival en une traversée : la vision, 2026 en chiffres, les six univers, le site, les trois jours de mai.',
         claude='https://claude.ai/artifact/PyY8ZiYEzwmsxWSxPL2YTT'),
    dict(slug='cryptostamp-corner', mod='cs', title='CryptoStamp Corner',
         audience='Postes et émetteurs de timbres numériques',
         desc='Le corner des timbres numériques, sixième édition : le lieu, le meetup du 27 mai, le stand pré-équipé.',
         claude='https://claude.ai/artifact/BRmKeS1PLUSXbYPYccMKp1'),
    dict(slug='artist-cards', mod='ac', title='NFC Artist Cards — Kawaii × PHANTASM',
         audience='Artistes invités à dessiner une carte',
         desc='Une carte PHANTASM dessinée avec Polygon1993, éditée, géante au mur, révélée sur scène le 27 mai.',
         claude='https://claude.ai/artifact/SJKvtPbYDA2RSVChtMvYmj'),
    dict(slug='collection-cards', mod='cc', title='NFC Collection Cards',
         audience='Collections NFT et PFP',
         desc='La carte d’une collection : deux façons d’entrer, trois vies, le partage des ventes et le calendrier.',
         claude='https://claude.ai/artifact/Y6P6MjqFHPssV83iATjxBR'),
    dict(slug='street-activations', mod='sa', title='NFC Street Activations — On The Wall',
         audience='Sponsors, galeries, plateformes, communautés',
         desc='Les murs du festival : le mural phare, les murals d’artistes, les maisons communautaires, les murs PFP et des noms.',
         claude='https://claude.ai/artifact/KQPvnq4mh9NKDwVif9UWAV'),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@300..700&display=swap">'
MONTHS = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']
ICON = {
    'back': '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
    'prev': '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
    'next': '<svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>',
    'grid': '<svg viewBox="0 0 24 24"><path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/></svg>',
    'notes': '<svg viewBox="0 0 24 24"><path d="M5 4h14v16H5zM8 9h8M8 13h8M8 17h5"/></svg>',
    'pdf': '<svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>',
    'fs': '<svg viewBox="0 0 24 24"><path d="M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5"/></svg>',
}


def today_fr():
    t = datetime.date.today()
    return f'{t.day} {MONTHS[t.month - 1]} {t.year}'


def media_url(key, prefix):
    """'photos-2026/x.jpg' -> '<prefix>media/photos-2026/x.jpg' (PNG keys resolve to their WebP file)."""
    if key not in LOCAL:
        raise SystemExit(f'Missing media file for "{key}": add it with  python3 src/tools/optimize_media.py <file> {key}')
    return prefix + 'media/' + os.path.relpath(LOCAL[key], MEDIA).replace(os.sep, '/')


def load(spec):
    mod = importlib.import_module(spec['mod'])
    return mod.d


def slide_html(d, prefix):
    out = []
    for i, (sid, h) in enumerate(d.slides, 1):
        h = re.sub(r'<p class="pg">\d+</p>', f'<p class="pg">{i:02d}</p>', h)
        h = re.sub(r'\{\{([^}]+)\}\}', lambda m: media_url(m.group(1), prefix), h)
        out.append(h)
    return ''.join(out)


def deck_page(spec, d):
    n = len(d.slides)
    grid = ''.join(f'<li><button type="button" data-i="{i}"><img src="thumbs/{i + 1:02d}.jpg" alt="Slide {i + 1}" loading="lazy" width="480" height="270">{i + 1:02d}</button></li>'
                   for i in range(n))
    title = html.escape(spec['title'])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{title} · NFC Summit 2027</title>
<meta property="og:title" content="{title} · NFC Summit 2027">
<meta property="og:image" content="cover.jpg">
<link rel="icon" href="../../assets/favicon.png">
{FONTS}
<link rel="stylesheet" href="../../assets/viewer.css">
<style>
{DECK_CSS}
</style>
</head>
<body>
<div id="stage"><div id="deck">
{slide_html(d, '../../')}
</div></div>

<nav class="v-bar v-top" aria-label="Deck">
  <a class="v-btn" href="../../" title="Tous les decks">{ICON['back']}<span class="v-hide-sm">Tous les decks</span></a>
  <span class="v-sep"></span>
  <span class="v-title">{title}</span>
</nav>
<nav class="v-bar v-bottom" aria-label="Navigation">
  <button class="v-btn" id="v-prev" type="button" title="Précédente (←)" aria-label="Slide précédente">{ICON['prev']}</button>
  <span class="v-count" id="v-count" aria-live="polite">1 / {n}</span>
  <button class="v-btn" id="v-next" type="button" title="Suivante (→)" aria-label="Slide suivante">{ICON['next']}</button>
  <span class="v-sep"></span>
  <button class="v-btn" id="v-grid" type="button" title="Vue d’ensemble (G)" aria-pressed="false">{ICON['grid']}<span class="v-hide-sm">Slides</span></button>
  <button class="v-btn" id="v-notes" type="button" title="Notes (N)" aria-pressed="false">{ICON['notes']}<span class="v-hide-sm">Notes</span></button>
  <a class="v-btn" href="{spec['slug']}.pdf" download title="Télécharger le PDF">{ICON['pdf']}<span class="v-hide-sm">PDF</span></a>
  <button class="v-btn" id="v-fs" type="button" title="Plein écran (F)" aria-label="Plein écran">{ICON['fs']}</button>
</nav>
<div class="v-progress" id="v-progress"></div>

<aside id="notes" hidden><h4>Notes · à dire</h4><p></p></aside>

<div id="grid" hidden>
  <div class="g-head"><h2>{title}</h2><button class="v-btn" type="button" data-close>Fermer · Esc</button></div>
  <ol>{grid}</ol>
</div>

<script src="../../assets/viewer.js"></script>
</body>
</html>
'''


def hub_page(entries):
    # the seven dragons along the bottom of the header, as on the closing slides
    order = [('art-fun-fair', 70), ('kawaii-summit', 70), ('conference', 72), ('ringmaster-hero', 92), ('art-factory', 70), ('hackathon-ai-day', 66), ('parties', 74)]
    dragons = ''.join(f'<img src="{media_url("dragons-2027/dragon-" + k + ".png", "")}" alt="" style="height:{h}%">' for k, h in order)
    cards = []
    for i, (spec, d) in enumerate(entries, 1):
        slug, n = spec['slug'], len(d.slides)
        strip = ''.join(f'<img src="decks/{slug}/thumbs/{j:02d}.jpg" alt="" loading="lazy" width="480" height="270">' for j in range(2, min(n, 6) + 1))
        cards.append(f'''
<li class="deck">
  <a class="thumb" href="decks/{slug}/" aria-label="Présenter {html.escape(spec['title'])}">
    <img src="decks/{slug}/cover.jpg" alt="" width="1280" height="720" loading="{'eager' if i == 1 else 'lazy'}">
    <span class="play">Présenter</span>
  </a>
  <div class="info">
    <p class="num">{i:02d}</p>
    <h2>{html.escape(spec['title'])}</h2>
    <p class="aud">{html.escape(spec['audience'])}</p>
    <p class="desc">{html.escape(spec['desc'])}</p>
    <p class="meta">{n} slides · en anglais · notes de présentation incluses</p>
    <div class="actions">
      <a class="btn primary" href="decks/{slug}/">Présenter</a>
      <a class="btn" href="decks/{slug}/{slug}.pdf" download>PDF</a>
      <button class="btn" type="button" data-copy="decks/{slug}/">Copier le lien</button>
    </div>
    <div class="strip" aria-hidden="true">{strip}</div>
  </div>
</li>''')
    total = sum(len(d.slides) for _, d in entries)
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>Decks NFC Summit 2027</title>
<meta name="description" content="Les présentations officielles de NFC Summit 2027, pour l’équipe.">
<link rel="icon" href="assets/favicon.png">
{FONTS}
<link rel="stylesheet" href="assets/hub.css">
</head>
<body>
<header class="hero">
  <div class="hero-in">
    <img class="logo" src="{media_url('logos-2027/logo-nfc-jaune.png', '')}" alt="NFC Summit">
    <p class="lab">Usage interne · équipe NFC Summit</p>
    <h1>Les decks 2027</h1>
    <p class="lead">Sixième édition, cinquième anniversaire. 27 — 29 mai 2027, Unicorn Factory, Beato, Lisbonne.</p>
    <p class="sub">{len(entries)} decks · {total} slides · mis à jour le {today_fr()}</p>
  </div>
  <div class="dragons" aria-hidden="true">{dragons}</div>
</header>

<section class="howto" aria-label="Comment présenter">
  <div class="howto-in">
    <p class="howto-t">Pour présenter</p>
    <ul>
      <li><kbd>F</kbd> plein écran</li>
      <li><kbd>←</kbd> <kbd>→</kbd> changer de slide</li>
      <li><kbd>N</kbd> notes : ce qu’il faut dire</li>
      <li><kbd>G</kbd> toutes les slides</li>
      <li>Sur téléphone : glisser</li>
    </ul>
  </div>
</section>

<main>
  <ol class="decks">{''.join(cards)}
  </ol>
</main>

<footer>
  <div class="foot-in">
    <div>
      <p class="lab">Contact sur tous les decks</p>
      <p class="contact">John Karp · john@nonfungibleconference.com · t.me/thejonnkarp</p>
    </div>
    <div>
      <p class="lab">À savoir</p>
      <p>Ce site est réservé à l’équipe : on envoie un deck à l’extérieur en PDF ou avec le lien de ce deck seul. Les originaux modifiables sont sur claude.ai, dans le compte de John.</p>
    </div>
  </div>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>
document.addEventListener('click', function (e) {{
  var b = e.target.closest('[data-copy]'); if (!b) return;
  var url = new URL(b.getAttribute('data-copy'), location.href).href;
  var t = document.getElementById('toast');
  function done(msg) {{ t.textContent = msg; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(function () {{ t.classList.remove('on'); }}, 2200); }}
  if (navigator.clipboard && navigator.clipboard.writeText) {{
    navigator.clipboard.writeText(url).then(function () {{ done('Lien copié'); }}, function () {{ prompt('Lien du deck', url); }});
  }} else {{ prompt('Lien du deck', url); }}
}});
</script>
</body>
</html>
'''


def main():
    entries = []
    for spec in DECKS:
        d = load(spec)
        out = os.path.join(ROOT, 'decks', spec['slug'])
        os.makedirs(os.path.join(out, 'thumbs'), exist_ok=True)
        open(os.path.join(out, 'index.html'), 'w').write(deck_page(spec, d))
        entries.append((spec, d))
        print(f"decks/{spec['slug']}/  {len(d.slides)} slides")
    open(os.path.join(ROOT, 'index.html'), 'w').write(hub_page(entries))
    json.dump([dict(slug=s['slug'], slides=len(d.slides), title=s['title']) for s, d in entries],
              open(os.path.join(ROOT, 'decks', 'decks.json'), 'w'), ensure_ascii=False, indent=1)
    print('index.html')


if __name__ == '__main__':
    main()
