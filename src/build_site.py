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

# The five decks, in the order the team sees them. Everything shown on the site is in English. 'claude' is the editable original on claude.ai (John's account).
DECKS = [
    dict(slug='general-presentation', mod='gp', title='General Presentation',
         audience='Everyone: partners, press, sponsors, speakers',
         desc='The festival in one journey: the vision, 2026 in figures, the six worlds, the venue, the three days in May.',
         claude='https://claude.ai/artifact/PyY8ZiYEzwmsxWSxPL2YTT'),
    dict(slug='ai-residency', mod='ai', title='NFC Residency 27 — for AI labs',
         audience='AI labs: image, video, code',
         desc='One hundred NFC artists create with your model for 90 days, then an exhibition in Lisbon. Plus four more formats and the price list.',
         claude=''),
    dict(slug='cryptostamp-corner', mod='cs', title='CryptoStamp Corner',
         audience='Postal services and digital stamp issuers',
         desc='The digital stamp corner, sixth edition: the place, the 27 May meetup, the turnkey booth.',
         claude='https://claude.ai/artifact/BRmKeS1PLUSXbYPYccMKp1'),
    dict(slug='artist-cards', mod='ac', title='NFC Artist Cards — Kawaii × PHANTASM',
         audience='Artists invited to draw a card',
         desc='A PHANTASM card drawn with Polygon1993: a numbered edition, a giant on the wall, revealed on stage on 27 May.',
         claude='https://claude.ai/artifact/SJKvtPbYDA2RSVChtMvYmj'),
    dict(slug='collection-cards', mod='cc', title='NFC Collection Cards',
         audience='NFT and PFP collections',
         desc='A card for your collection: two ways in, three lives, the revenue split and the timeline.',
         claude='https://claude.ai/artifact/Y6P6MjqFHPssV83iATjxBR'),
    dict(slug='street-activations', mod='sa', title='NFC Street Activations — On The Wall',
         audience='Sponsors, galleries, platforms, communities',
         desc='The walls of the festival: the flagship mural, the artist murals, the community houses, the PFP and Name walls.',
         claude='https://claude.ai/artifact/KQPvnq4mh9NKDwVif9UWAV'),
]

# The vertical partner-offer decks (1080 × 1920). Their source is a Claude Design canvas on claude.ai (John's account):
# the pages are exported as images into offers/<slug>/pages/NN.jpg (+ NN-s.jpg thumbnails), with cover.jpg and nfc27-<slug>.pdf.
# To update one: export its pages again from the canvas, then run this script.
OFFERS = [
    dict(slug='catalogue', title='NFC Catalogue 27', audience='Every partner, first',
         desc='The whole offer, one page per way in: why, what, from how much. Then the perks by level and how to book.',
         claude='https://claude.ai/artifact/GJ6ioVUkjnRqteGzEKqWPK'),
    dict(slug='art-fun-fair', title='Art Fun Fair', audience='Artists, galleries and brands',
         desc='The fairground at the heart of NFC: a shared machine, your own attraction, or the whole fair in your name.',
         claude='https://claude.ai/artifact/UfidEw1U8GBT2v21KCwe12'),
    dict(slug='attractions', title='Attractions', audience='Artists who want to build a ride',
         desc='How every machine works, the three to start with, the wild ones, who does what, and the two ways in.',
         claude='https://claude.ai/artifact/TQDjVcmtETSZEg1h6xExQf'),
    dict(slug='kawaii-summit', title='Kawaii Summit', audience='Card games, collections and characters',
         desc='Your card, made with an artist and sold together: four ways to sell it, two ways in, the split.',
         claude='https://claude.ai/artifact/S5uQG7teB1fPz1YtVEG8q4'),
    dict(slug='side-events', title='Side Events', audience='Brands and projects that want their own moment',
         desc='Five venues inside NFC, from a shared event at Casa Capitão to your own stage: packages, menus, prices.',
         claude='https://claude.ai/artifact/5g3jCjirNMkr644jmZQgYv'),
    dict(slug='on-the-wall', title='On The Wall', audience='Supporters, collectors and brands',
         desc='Season 1 in figures, your name on the wall, the Supporter pack and your own mural.',
         claude='https://claude.ai/artifact/6dDpjp4yzYCnL8HjWEQ1Qe'),
    dict(slug='cryptostamp-corner', title='CryptoStamp Corner', audience='Postal services and stamp collectors',
         desc='A whole corner for digital stamps: three ways in, a ready-to-use booth at Bronze, and bigger custom formats.',
         claude='https://claude.ai/artifact/TEw6o6H57ctfDETihDicFY'),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@300..700&display=swap">'
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ICON = {
    'back': '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
    'prev': '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
    'next': '<svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>',
    'grid': '<svg viewBox="0 0 24 24"><path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/></svg>',
    'notes': '<svg viewBox="0 0 24 24"><path d="M5 4h14v16H5zM8 9h8M8 13h8M8 17h5"/></svg>',
    'pdf': '<svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>',
    'fs': '<svg viewBox="0 0 24 24"><path d="M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5"/></svg>',
}


def today_en():
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
  <a class="v-btn" href="../../" title="All decks">{ICON['back']}<span class="v-hide-sm">All decks</span></a>
  <span class="v-sep"></span>
  <span class="v-title">{title}</span>
</nav>
<nav class="v-bar v-bottom" aria-label="Slide controls">
  <button class="v-btn" id="v-prev" type="button" title="Previous (←)" aria-label="Previous slide">{ICON['prev']}</button>
  <span class="v-count" id="v-count" aria-live="polite">1 / {n}</span>
  <button class="v-btn" id="v-next" type="button" title="Next (→)" aria-label="Next slide">{ICON['next']}</button>
  <span class="v-sep"></span>
  <button class="v-btn" id="v-grid" type="button" title="All slides (G)" aria-pressed="false">{ICON['grid']}<span class="v-hide-sm">Slides</span></button>
  <button class="v-btn" id="v-notes" type="button" title="Notes (N)" aria-pressed="false">{ICON['notes']}<span class="v-hide-sm">Notes</span></button>
  <a class="v-btn" href="{spec['slug']}.pdf" download title="Download the PDF">{ICON['pdf']}<span class="v-hide-sm">PDF</span></a>
  <button class="v-btn" id="v-fs" type="button" title="Full screen (F)" aria-label="Full screen">{ICON['fs']}</button>
</nav>
<div class="v-progress" id="v-progress"></div>

<aside id="notes" hidden><h4>Notes · what to say</h4><p></p></aside>

<div id="grid" hidden>
  <div class="g-head"><h2>{title}</h2><button class="v-btn" type="button" data-close>Close · Esc</button></div>
  <ol>{grid}</ol>
</div>

<script src="../../assets/viewer.js"></script>
</body>
</html>
'''


def offer_pages(spec):
    info = os.path.join(ROOT, 'offers', spec['slug'], 'pages.json')
    if not os.path.exists(info):
        raise SystemExit(f"Missing offers/{spec['slug']}/pages.json: export the pages of this deck first")
    return json.load(open(info))['pages']


def offer_page(spec, n):
    title, slug = html.escape(spec['title']), spec['slug']
    imgs = ''.join(f'<img {"src" if i == 1 else "data-src"}="pages/{i:02d}.jpg" alt="{title}, page {i}" width="1080" height="1920" draggable="false">'
                   for i in range(1, n + 1))
    grid = ''.join(f'<li><button type="button" data-i="{i - 1}"><img src="pages/{i:02d}-s.jpg" alt="" loading="lazy" width="360" height="640">{i:02d}</button></li>'
                   for i in range(1, n + 1))
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
<link rel="stylesheet" href="../../assets/offers.css">
</head>
<body>
<div id="pages">{imgs}</div>

<nav class="v-bar v-top" aria-label="Deck">
  <a class="v-btn" href="../../#offers" title="All decks">{ICON['back']}<span class="v-hide-sm">All decks</span></a>
  <span class="v-sep"></span>
  <span class="v-title">{title}</span>
</nav>
<nav class="v-bar v-bottom" aria-label="Page controls">
  <button class="v-btn" id="v-prev" type="button" title="Previous (←)" aria-label="Previous page">{ICON['prev']}</button>
  <span class="v-count" id="v-count" aria-live="polite">01 / {n:02d}</span>
  <button class="v-btn" id="v-next" type="button" title="Next (→)" aria-label="Next page">{ICON['next']}</button>
  <span class="v-sep"></span>
  <button class="v-btn" id="v-grid" type="button" title="All pages (G)" aria-pressed="false">{ICON['grid']}<span class="v-hide-sm">Pages</span></button>
  <a class="v-btn" href="nfc27-{slug}.pdf" download title="Download the PDF">{ICON['pdf']}<span class="v-hide-sm">PDF</span></a>
  <button class="v-btn" id="v-fs" type="button" title="Full screen (F)" aria-label="Full screen">{ICON['fs']}</button>
</nav>
<div class="v-progress" id="v-progress"></div>

<div id="o-grid" hidden>
  <div class="g-head"><h2>{title}</h2><button class="v-btn" type="button" data-close>Close · Esc</button></div>
  <ol>{grid}</ol>
</div>

<script src="../../assets/offers.js"></script>
</body>
</html>
'''


def offers_section(offers):
    cards = []
    for i, (spec, n) in enumerate(offers, 1):
        slug, title = spec['slug'], html.escape(spec['title'])
        cards.append(f'''
<li class="offer">
  <a class="o-thumb" href="offers/{slug}/" aria-label="Open {title}">
    <img src="offers/{slug}/cover.jpg" alt="" width="540" height="960" loading="lazy">
  </a>
  <p class="num">{i:02d}</p>
  <h3>{title}</h3>
  <p class="aud">{html.escape(spec['audience'])}</p>
  <p class="desc">{html.escape(spec['desc'])}</p>
  <p class="meta">{n} pages · vertical · prices excl. VAT</p>
  <div class="actions">
    <a class="btn primary" href="offers/{slug}/">Open</a>
    <a class="btn" href="offers/{slug}/nfc27-{slug}.pdf" download>PDF</a>
    <button class="btn" type="button" data-copy="offers/{slug}/">Copy link</button>
  </div>
</li>''')
    return f'''
<section class="offers-sec" id="offers" aria-labelledby="offers-t">
  <div class="offers-head">
    <p class="lab">Vertical · for partners</p>
    <h2 id="offers-t">Business</h2>
    <p class="lead">One deck per business, with prices excl. VAT. Send the catalogue first, then the deck of the business they want. Early-bird prices until 31 December.</p>
  </div>
  <ol class="offers">{''.join(cards)}
  </ol>
</section>'''


def hub_page(entries, offers=()):
    # the seven dragons along the bottom of the header, as on the closing slides
    order = [('art-fun-fair', 70), ('kawaii-summit', 70), ('conference', 72), ('ringmaster-hero', 92), ('art-factory', 70), ('hackathon-ai-day', 66), ('parties', 74)]
    dragons = ''.join(f'<img src="{media_url("dragons-2027/dragon-" + k + ".png", "")}" alt="" style="height:{h}%">' for k, h in order)
    cards = []
    for i, (spec, d) in enumerate(entries, 1):
        slug, n = spec['slug'], len(d.slides)
        strip = ''.join(f'<img src="decks/{slug}/thumbs/{j:02d}.jpg" alt="" loading="lazy" width="480" height="270">' for j in range(2, min(n, 6) + 1))
        cards.append(f'''
<li class="deck">
  <a class="thumb" href="decks/{slug}/" aria-label="Present {html.escape(spec['title'])}">
    <img src="decks/{slug}/cover.jpg" alt="" width="1280" height="720" loading="{'eager' if i == 1 else 'lazy'}">
    <span class="play">Present</span>
  </a>
  <div class="info">
    <p class="num">{i:02d}</p>
    <h2>{html.escape(spec['title'])}</h2>
    <p class="aud">{html.escape(spec['audience'])}</p>
    <p class="desc">{html.escape(spec['desc'])}</p>
    <p class="meta">{n} slides · speaker notes included</p>
    <div class="actions">
      <a class="btn primary" href="decks/{slug}/">Present</a>
      <a class="btn" href="decks/{slug}/{slug}.pdf" download>PDF</a>
      <button class="btn" type="button" data-copy="decks/{slug}/">Copy link</button>
    </div>
    <div class="strip" aria-hidden="true">{strip}</div>
  </div>
</li>''')
    total = sum(len(d.slides) for _, d in entries)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>NFC Summit 2027 Decks</title>
<meta name="description" content="The official NFC Summit 2027 decks, for the team.">
<link rel="icon" href="assets/favicon.png">
{FONTS}
<link rel="stylesheet" href="assets/hub.css">
</head>
<body>
<header class="hero">
  <div class="hero-in">
    <img class="logo" src="{media_url('logos-2027/logo-nfc-jaune.png', '')}" alt="NFC Summit">
    <p class="lab">Internal · NFC Summit team</p>
    <h1>The 2027 decks</h1>
    <p class="lead">Sixth edition, fifth anniversary. 27 — 29 May 2027, Unicorn Factory, Beato, Lisbon.</p>
    <p class="sub">{len(entries)} presentations · {len(offers)} business decks · updated {today_en()}</p>
    <p class="jump"><a href="#decks">Presentations</a><a href="#offers">Business</a></p>
  </div>
  <div class="dragons" aria-hidden="true">{dragons}</div>
</header>

<section class="howto" aria-label="How to present">
  <div class="howto-in">
    <p class="howto-t">To present</p>
    <ul>
      <li><kbd>F</kbd> full screen</li>
      <li><kbd>←</kbd> <kbd>→</kbd> change slide</li>
      <li><kbd>N</kbd> notes: what to say</li>
      <li><kbd>G</kbd> all slides</li>
      <li>On a phone: swipe</li>
    </ul>
  </div>
</section>

<main>
  <div class="offers-head floor" id="decks">
    <p class="lab">Horizontal · for everyone</p>
    <h2>Presentations</h2>
    <p class="lead">To present on a screen or send to anyone: speakers, press, artists, partners. No prices. The event decks include their offers.</p>
  </div>
  <ol class="decks">{''.join(cards)}
  </ol>
{offers_section(offers) if offers else ''}
</main>

<footer>
  <div class="foot-in">
    <div>
      <p class="lab">Contact on every deck</p>
      <p class="contact">John Karp · john@nonfungibleconference.com · t.me/thejonnkarp</p>
    </div>
    <div>
      <p class="lab">Good to know</p>
      <p>This site is for the team. To share a deck outside, send its PDF or the link to that deck only. The editable originals are on claude.ai, in John’s account.</p>
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
    navigator.clipboard.writeText(url).then(function () {{ done('Link copied'); }}, function () {{ prompt('Deck link', url); }});
  }} else {{ prompt('Deck link', url); }}
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
    offers = []
    for spec in OFFERS:
        n = offer_pages(spec)
        open(os.path.join(ROOT, 'offers', spec['slug'], 'index.html'), 'w').write(offer_page(spec, n))
        offers.append((spec, n))
        print(f"offers/{spec['slug']}/  {n} pages")
    open(os.path.join(ROOT, 'index.html'), 'w').write(hub_page(entries, offers))
    json.dump([dict(slug=s['slug'], slides=len(d.slides), title=s['title']) for s, d in entries],
              open(os.path.join(ROOT, 'decks', 'decks.json'), 'w'), ensure_ascii=False, indent=1)
    print('index.html')


if __name__ == '__main__':
    main()
