# NFC Summit 2027 — shared deck kit: deck.css + the slide templates as functions.
# Used by build_site.py (the team website) and, in the Claude cloud session, to publish the claude.ai Slides copies.
import json, os, re, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(ROOT, 'media')
DS_URL = 'https://claude.ai/artifact/L4i5auskPTefAo6LXeNFkB'
DSB = {}   # claude.ai design-system asset ids, only needed when publishing to claude.ai
LOCAL = {}   # media key ('dragons-2027/dragon-parties.png') -> file in media/
for _dp, _dn, _fn in os.walk(MEDIA):
    for _f in _fn:
        _rel = os.path.relpath(os.path.join(_dp, _f), MEDIA)
        LOCAL[_rel] = os.path.join(_dp, _f)
        if _f.endswith('.webp'):   # PNGs are stored as WebP for the web; keep the original key working
            LOCAL[_rel[:-5] + '.png'] = os.path.join(_dp, _f)

DECK_CSS = r''':root {
  --ink: #0B0B0B; --graphite: #1A1A1A; --chalk: #F2F0EB; --grey: #B0ACA2; --grey-deep: #6B685F;
  --paper: #FFFFFF; --paper-2: #F3F6FF; --rule-paper: #D5DCEE;
  --yellow: #F6B800; --blue: #1442B2; --ink-blue: #0E2A6E;
}
body { font-family: 'Space Grotesk', Arial, sans-serif; }
section.s { background: var(--ink); color: var(--chalk); padding: 96px 96px 160px; display: flex; flex-direction: column; justify-content: space-between; }
section.paper { background: var(--paper); color: var(--ink); }
section.paper2 { background: var(--paper-2); color: var(--ink); }
section.yellow { background: var(--yellow); color: var(--ink-blue); }
section.blue { background: var(--blue); color: var(--paper); }
section.bottom { justify-content: flex-end; }
.bg { position: absolute; left: 0px; top: 0px; width: 1920px; height: 1080px; object-fit: cover; }
.shade-l { position: absolute; left: 0px; top: 0px; width: 1920px; height: 1080px; background: linear-gradient(90deg, rgba(11,11,11,0.9) 0%, rgba(11,11,11,0.55) 45%, rgba(11,11,11,0) 75%); }
.shade-b { position: absolute; left: 0px; top: 0px; width: 1920px; height: 1080px; background: linear-gradient(0deg, rgba(11,11,11,0.92) 0%, rgba(11,11,11,0.45) 40%, rgba(11,11,11,0) 70%); }
.shade-r { position: absolute; left: 0px; top: 0px; width: 1920px; height: 1080px; background: linear-gradient(270deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0.97) 42%, rgba(11,11,11,0.6) 60%, rgba(11,11,11,0) 80%); }
.shade-dark { position: absolute; left: 0px; top: 0px; width: 1920px; height: 1080px; background: linear-gradient(0deg, rgba(11,11,11,0.96) 0%, rgba(11,11,11,0.8) 60%, rgba(11,11,11,0.45) 100%); }
.t { font-family: 'Anton', Arial, sans-serif; font-weight: 400; text-transform: uppercase; line-height: 0.86; }
.t200 { font-size: 200px; letter-spacing: -4px; line-height: 0.84; }
.t168 { font-size: 168px; letter-spacing: -3px; }
.t150 { font-size: 150px; letter-spacing: -3px; }
.t120 { font-size: 120px; letter-spacing: -2px; }
.t112 { font-size: 112px; letter-spacing: -2px; line-height: 0.9; }
.t88 { font-size: 88px; letter-spacing: -2px; line-height: 0.9; }
.t64 { font-size: 64px; letter-spacing: -1px; line-height: 0.92; }
.t48 { font-size: 48px; letter-spacing: -1px; line-height: 0.95; }
.t36 { font-size: 36px; line-height: 1; }
section.paper .t, section.paper2 .t { color: var(--ink-blue); }
.lab { font-size: 26px; font-weight: 600; line-height: 1.2; }
.acc { color: var(--yellow); }
section.paper .acc, section.paper2 .acc { color: var(--blue); }
section.yellow .acc { color: var(--ink-blue); }
.lead { font-size: 40px; font-weight: 300; line-height: 1.3; }
.body { font-size: 28px; font-weight: 400; line-height: 1.4; }
.small { font-size: 24px; font-weight: 400; line-height: 1.35; }
.mute { color: var(--grey); }
section.paper .mute, section.paper2 .mute { color: var(--grey-deep); }
.foot { position: absolute; left: 96px; bottom: 56px; width: 1300px; font-size: 24px; font-weight: 500; line-height: 1.2; color: var(--grey); }
.pg { position: absolute; left: 1704px; bottom: 56px; width: 120px; text-align: right; font-size: 24px; font-weight: 500; line-height: 1.2; color: var(--grey); }
section.paper .foot, section.paper .pg, section.paper2 .foot, section.paper2 .pg { color: var(--grey-deep); }
section.yellow .foot, section.yellow .pg { color: var(--ink-blue); }
section.blue .foot, section.blue .pg { color: var(--paper); }
section.yellow .mute { color: #3C4658; }
section.yellow .rule, section.yellow .rule-d { border-top-color: rgba(14,42,110,0.28); }
section.yellow .bar, section.yellow .sq, section.yellow .ysq { background: var(--blue); }
section.yellow .frame { border-color: var(--ink-blue); }
.col { display: flex; flex-direction: column; }
.row { display: flex; flex-direction: row; }
.g8 { gap: 8px; } .g12 { gap: 12px; } .g16 { gap: 16px; } .g20 { gap: 20px; } .g24 { gap: 24px; } .g32 { gap: 32px; } .g40 { gap: 40px; } .g48 { gap: 48px; } .g64 { gap: 64px; }
.bar { width: 72px; height: 6px; background: var(--yellow); }
section.paper .bar, section.paper2 .bar { background: var(--blue); }
.sq { width: 20px; height: 20px; background: var(--yellow); }
.bsq { width: 12px; height: 12px; background: var(--blue); margin-top: 14px; flex: none; }
.ysq { width: 12px; height: 12px; background: var(--yellow); margin-top: 14px; flex: none; }
.rule { border-top: 1px solid var(--rule-paper); }
.rule-d { border-top: 1px solid #2E2E2E; }
.panel { position: absolute; left: 880px; top: 96px; width: 3px; height: 824px; background: var(--ink-blue); }
.frame { border: 2px solid var(--chalk); }
@keyframes rise { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: translateY(0px); } }
@keyframes fade { from { opacity: 0; } to { opacity: 1; } }
.in { animation: rise 600ms ease-out both; }
.in2 { animation: rise 600ms ease-out 180ms both; }
.in3 { animation: rise 600ms ease-out 360ms both; }
'''

FONTS = {"anton": {"family": "Anton", "href": "https://fonts.googleapis.com/css2?family=Anton&display=swap"},
         "space-grotesk": {"family": "Space Grotesk", "href": "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap"}}

def esc(t): return t  # texts are authored here; keep typographic characters as is

class Deck:
    def __init__(self, name, footer):
        self.name, self.footer = name, footer
        self.slides, self.media = [], {}   # media key -> url (deck blob) set later
    def m(self, key):
        self.media.setdefault(key, None); return '{{' + key + '}}'
    def add(self, sid, html): self.slides.append((sid, html))
    def foot(self, n, left=None, start=96):
        st = '' if start == 96 else f' style="left:{start}px;width:{1600-start}px"'
        return f'<p class="foot"{st}>{left or self.footer}</p>\n<p class="pg">{n:02d}</p>'
    def num(self, sid): return [s for s, _ in self.slides].index(sid) + 1 if sid in [s for s, _ in self.slides] else len(self.slides) + 1

# ---------------- media helpers ----------------
def video(d, key, alt, cls='bg'):
    return f'<img class="{cls}" src="{d.m(key + ".jpg")}" data-video="{d.m(key + ".mp4")}" alt="{alt}">'
def photo(d, key, alt, cls='bg', style=''):
    st = f' style="{style}"' if style else ''
    return f'<img class="{cls}" src="{d.m(key)}" alt="{alt}"{st}>'
def notes(t): return f'<aside>{t}</aside>'
def sec(sid, cls, body, note, extra=''):
    if cls in ('paper', 'paper2'): cls = 'yellow'   # 15 Nov 2026: no more white slides, light pages are yellow
    return f'<section id="{sid}" class="s {cls}" data-transition="fade"{extra}>\n{body}\n{notes(note)}\n</section>\n'
VID = lambda k: 'videos-2026/' + k
PH = lambda k: 'photos-2026/' + k + '.jpg'
DR = lambda k: 'dragons-2027/dragon-' + k + '.png'
RATIO = {'art-factory': 1086/1248, 'art-fun-fair': 1088/1213, 'conference': 1074/1353, 'hackathon-ai-day': 1085/1108, 'kawaii-summit': 1048/1160, 'parties': 1087/1380, 'ringmaster-hero': 1274/1033}

# ---------------- the 12 templates ----------------
def cover(d, sid, media, label, title, lead, line, note, alt):
    bg = video(d, media, alt) if not media.endswith('.jpg') else photo(d, media, alt)
    logo = f'<div style="position:absolute;left:96px;top:96px;width:176px;height:100px;overflow:hidden"><img src="{d.m("logos-2027/logo-nfc-blanc.png")}" alt="NFC Summit logo" style="position:absolute;left:-10px;top:-47px;width:196px;height:196px;object-fit:contain"></div>'
    body = f'''{bg}
<div class="shade-l"></div>
<div class="shade-b"></div>
{logo}
<div class="col g32 in" style="width:1500px">
<p class="lab acc">{label}</p>
<h1 class="t t200">{title}</h1>
<p class="lead">{lead}</p>
<p class="lab">{line}</p>
</div>'''
    d.add(sid, sec(sid, 'bottom', body, note, ''))

def vstatement(d, sid, vid, title, line, note, alt):
    body = f'''{video(d, vid, alt)}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g40 in" style="width:1500px">
<h2 class="t t150">{title}</h2>
<p class="lead">{line}</p>
</div>'''
    d.add(sid, sec(sid, 'bottom', body, note, ' style="padding-bottom:144px"'))

def pstatement(d, sid, ph, title, line, note, alt, n):
    body = f'''{photo(d, ph, alt)}
<div class="shade-b"></div>
<div class="shade-l"></div>
<div class="col g32 in" style="width:1400px">
<h2 class="t t150">{title}</h2>
<p class="lead">{line}</p>
</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, 'bottom', body, note))

def figures(d, sid, ph, label, title, figs, note, alt, n, foot=None):
    cells = ''.join(f'<div class="col g16"><div class="bar"></div><p class="t t112">{v}</p><p class="lab mute">{l}</p></div>' for v, l in (figs or []))
    body = f'''{photo(d, ph, alt)}
<div class="shade-dark"></div>
<div class="col g24 in">
<p class="lab acc">{label}</p>
<h2 class="t t120">{title}</h2>
</div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);row-gap:56px;column-gap:48px">{cells}</div>
{d.foot(n, foot)}'''
    d.add(sid, sec(sid, '', body, note))

def dragon_img(d, k, x, h, cut=40, alt=''):
    w = round(h * RATIO[k])
    return f'<img src="{d.m(DR(k))}" alt="{alt}" style="position:absolute;left:{x}px;top:{1080 - h + cut}px;width:{w}px;height:{h}px;object-fit:contain">'

def quote(d, sid, ph, q1, q2, name, role, note, alt, n):
    """Quote staged with three dragons on ink (DS Slide05Quote, 15 Nov 2026). ph and alt are kept for old calls and unused."""
    trio = dragon_img(d, 'art-factory', 1150, 540, 60) + '\n' + dragon_img(d, 'parties', 1610, 560, 60) + '\n' + dragon_img(d, 'conference', 1300, 660, 50, 'The conference dragon at the microphone, with the art factory and parties dragons')
    body = f'''{trio}
<div class="col in" style="width:1060px">
<p class="t" style="font-size:320px;line-height:0.62;height:160px;color:var(--yellow)">“</p>
<p style="font-size:80px;font-weight:300;line-height:1.1;letter-spacing:-1px">{q1} <b style="font-weight:500">{q2}</b></p>
<div class="col g12" style="margin-top:56px">
<p class="t t64">{name}</p>
<p class="lab mute">{role}</p>
</div>
</div>'''
    d.add(sid, sec(sid, '', body, note, ' style="justify-content:center;padding-bottom:150px"'))

def stage(d, sid, label, sentence, note, size=132, bg=''):
    """One dream sentence carried by the seven dragons on yellow (DS Slide13Stage)."""
    order = [('art-fun-fair', 360), ('kawaii-summit', 360), ('conference', 360), ('ringmaster-hero', 450), ('art-factory', 360), ('hackathon-ai-day', 340), ('parties', 380)]
    cw = 1920 / 7; imgs = ''
    for i, (k, h) in enumerate(order):
        w = round(h * RATIO[k]); x = round(cw * i + cw / 2 - w / 2)
        imgs += dragon_img(d, k, max(0, x), h, 40, 'The seven NFC dragons lined up' if k == 'ringmaster-hero' else '') + '\n'
    body = f'''{imgs}<div class="col g28 in" style="width:1728px;gap:28px">
<p class="lab acc">{label}</p>
<h2 class="t" style="font-size:{size}px;line-height:0.88;letter-spacing:-2px">{sentence}</h2>
</div>
<div style="height:420px"></div>'''
    d.add(sid, sec(sid, bg, body, note, ' style="justify-content:flex-start;padding-bottom:0px"'))

def world(d, sid, media, label, title, line, note, alt, n):
    bg = photo(d, media, alt) if media.endswith('.jpg') else video(d, media, alt)
    body = f'''{bg}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g32 in" style="width:1180px">
<p class="lab acc">{label}</p>
<h2 class="t t120">{title}</h2>
<p class="lead">{line}</p>
</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, 'bottom', body, note))

def divider(d, sid, color, dragon, label, title, line, note, alt, n):
    w = 897; h = round(w / RATIO[dragon])
    body = f'''<img src="{d.m(DR(dragon))}" alt="{alt}" style="position:absolute;left:{1920-200-w}px;top:190px;width:{w}px;height:{h}px;object-fit:contain">
<p class="lab acc" style="width:720px">{label}</p>
<div class="col g32 in" style="width:720px">
<h2 class="t t168">{title}</h2>
<p class="lead">{line}</p>
</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, color, body, note))

def statement_light(d, sid, label, title, rows, note, n, sentence=None):
    """A light page: label + title on the left, rows on the right (definition, reasons)."""
    body = f'''<div class="col" style="width:760px;justify-content:space-between">
<p class="lab acc">{label}</p>
<div class="col g32"><h2 class="t t150">{title}</h2>{f'<p class="lead">{sentence}</p>' if sentence else ''}</div>
</div>
<div class="col in2" style="flex:1;justify-content:flex-end">{rows}</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, 'paper', body, note, ' style="flex-direction:row;gap:96px"'))

def facts_row(d, sid, label, title, facts, line, note, n, sprites=12):
    cells = ''.join(f'<div class="col g16"><div class="sq"></div><p class="lead" style="font-size:36px;line-height:1.25">{t}</p></div>' for t in facts)
    spr = ''.join(f'<img src="{d.m(f"people-of-the-wall/sprite-{i:02d}.png")}" alt="" style="width:96px;height:96px">' for i in range(sprites))
    body = f'''<div class="col g24 in">
<p class="lab acc">{label}</p>
<h2 class="t t150">{title}</h2>
</div>
<div class="in2" style="display:grid;grid-template-columns:repeat({len(facts)}, 1fr);column-gap:48px">{cells}</div>
<div class="col g32">
<p class="lead mute">{line}</p>
<div class="row g24" aria-label="People of the Wall pixel avatars">{spr}</div>
</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, '', body, note))

def mapslide(d, sid, label, title, zones, note, n, labs=None):
    px0, py0, pw = 40, 160, 1130; ph = round(pw / 1.5)
    labs = labs or [('Art Factory', 44, 28, 0), ('The Wall', 61.6, 43, 0), ('Main stage', 23, 75.5, 0), ('Kawaii Summit', 46, 86.5, 0), ('FAIR PLAY', 55.4, 57.6, 1), ('Side events', 47, 10.5, 0), ('Parties', 82.5, 31, 0), ('Galleries', 24.7, 52.6, 0)]
    lab = ''
    for name, x, y, hi in labs:
        w = round(len(name) * 15 + 40); X = px0 + x / 100 * pw; Y = py0 + y / 100 * ph
        bg = 'var(--ink-blue)' if hi else 'var(--blue)'
        lab += f'<p style="position:absolute;left:{round(X - w / 2)}px;top:{round(Y - 46)}px;width:{w}px;font-size:24px;font-weight:600;line-height:1;text-align:center;padding:10px 0;background:{bg};color:var(--paper);border:2px solid var(--ink-blue)">{name}</p>\n'
    zl = ''.join(f'<div class="col g8 rule" style="padding:14px 0"><h3 class="t t36">{a}</h3><p class="small mute">{b}</p></div>' for a, b in zones)
    body = f'''<img src="{d.m("decors/plan-unicorn-factory-transparent.png")}" alt="Riso drawing of the Unicorn Factory site in Beato" style="position:absolute;left:{px0}px;top:{py0}px;width:{pw}px;height:{ph}px;object-fit:contain">
{lab}<div style="width:1124px;flex:none"></div>
<div class="col" style="flex:1;justify-content:space-between">
<div class="col g20"><p class="lab acc">{label}</p><h2 class="t t88">{title}</h2></div>
<div class="col">{zl}</div>
</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, 'paper', body, note, ' style="flex-direction:row;padding-bottom:140px"'))

def programme(d, sid, label, title, days, note, n):
    cols = ''.join(f'''<div class="col">
<img src="{d.m(p if "/" in p else PH(p))}" alt="{alt}" style="width:528px;height:300px;object-fit:cover">
<p class="lab acc" style="margin-top:32px">{day}</p>
<h3 class="t t48" style="margin-top:12px">{t}</h3>
<div class="col g8" style="margin-top:20px">{''.join(f'<p class="body mute">— {b}</p>' for b in bl)}</div>
</div>''' for p, alt, day, t, bl in days)
    body = f'''<div class="col g24 in"><p class="lab acc">{label}</p><h2 class="t t120">{title}</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{cols}</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, '', body, note))

def offer(d, sid, label, title, price, caption, cols, note, n, foot=None, extra_left=''):
    def col(head, items):
        li = ''.join(f'<div class="row g20 rule" style="padding:18px 0"><div class="bsq"></div><p class="body" style="font-size:28px;line-height:1.3">{x}</p></div>' for x in items)
        return f'<div class="col"><div class="bar" style="width:56px"></div><h3 class="t t48" style="margin-top:24px">{head}</h3><div class="col" style="margin-top:28px">{li}</div></div>'
    body = f'''<div class="panel"></div>
<div class="col" style="width:680px;justify-content:space-between">
<div class="col g24"><p class="lab acc">{label}</p><h2 class="t t88">{title}</h2>{extra_left}</div>
<div class="col g16"><p class="t t200" style="color:var(--ink-blue)">{price}</p><p class="lab mute">{caption}</p></div>
</div>
<div style="width:136px;flex:none"></div>
<div style="flex:1;display:grid;grid-template-columns:{' '.join(['1fr'] * len(cols))};column-gap:64px;align-items:start">{''.join(col(h, i) for h, i in cols)}</div>
{d.foot(n, foot)}'''
    d.add(sid, sec(sid, 'paper', body, note, ' style="flex-direction:row"'))

def timeline(d, sid, label, title, steps, note, n, line=None):
    st = ''.join(f'<div class="col g20"><div class="sq"></div><p class="t t48">{a}</p><p class="body mute">{b}</p></div>' for a, b in steps)
    body = f'''<div class="col g24 in"><p class="lab acc">{label}</p><h2 class="t t120">{title}</h2></div>
<div class="col g40">
<div class="in2" style="display:grid;grid-template-columns:repeat({len(steps)}, 1fr);column-gap:40px;border-top:2px solid var(--graphite);padding-top:0px">{st}</div>
{f'<p class="lead">{line}</p>' if line else ''}
</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, '', body, note))

def closing(d, sid, label, title, lines, note, contact=None):
    order = [('art-fun-fair', 380), ('kawaii-summit', 380), ('conference', 380), ('ringmaster-hero', 470), ('art-factory', 380), ('hackathon-ai-day', 360), ('parties', 400)]
    cw = 1920 / 7; imgs = ''
    for i, (k, h) in enumerate(order):
        w = round(h * RATIO[k]); x = round(cw * i + cw / 2 - w / 2)
        imgs += f'<img src="{d.m(DR(k))}" alt="" style="position:absolute;left:{max(0, x)}px;top:{1080 - h + 40}px;width:{w}px;height:{h}px;object-fit:contain">\n'
    body = f'''{imgs}<div class="col g32 in" style="width:1728px">
<p class="lab acc">{label}</p>
<h2 class="t t150">{title}</h2>
{''.join(f'<p class="body mute">{l}</p>' for l in lines)}
{f'<p class="lab">{contact}</p>' if contact else ''}
</div>
<div style="height:420px"></div>'''
    d.add(sid, sec(sid, '', body, note, ' style="justify-content:flex-start;padding-bottom:0px"'))

# ---------------- build / publish / render ----------------
def build(d, root, title, sections, cover_id, ds_version, url=None):
    os.makedirs(root + '/project/slides', exist_ok=True)
    order = [s for s, _ in d.slides]
    def fill(h):
        def rep(m):
            k = m.group(1)
            v = d.media.get(k)
            if not v: raise SystemExit('no url for ' + k)
            return v
        return re.sub(r'\{\{([^}]+)\}\}', rep, h)
    for i, (sid, h) in enumerate(d.slides, 1):
        h = re.sub(r'<p class="pg">\d+</p>', f'<p class="pg">{i:02d}</p>', h)
        open(f'{root}/project/slides/{sid}.html', 'w').write(fill(h))
    open(root + '/project/deck.css', 'w').write(DECK_CSS)
    idx = {"v": 5, "createdOnFiles": {"v": 1, "at": "2026-11-14T17:00:00Z"}, "lists": "css",
           "format": {"v": 1, "shared": ["project/deck.css"]}, "title": title, "cover": cover_id, "order": order,
           "sections": sections, "faces": FONTS,
           "designSystems": [{"title": "NFC Summit 2027 Design System", "namespace": "nfc", "artifact": DS_URL, "version": ds_version, "copiedAt": "2026-11-14T17:00:00Z"}]}
    json.dump(idx, open(root + '/project/deck.json', 'w'), ensure_ascii=False, indent=1)
    files = {"project/deck.css": "project/deck.css", "project/ds/nfc/tokens.json": {"artifact": DS_URL, "path": "project/tokens.json"}}
    for sid in order: files[f'project/slides/{sid}.html'] = f'project/slides/{sid}.html'
    json.dump(files, open(root + '/files.json', 'w'), ensure_ascii=False)
    return order

def render_html(d, out, extra_local=None):
    """Local preview: all slides stacked, media mapped to local files."""
    loc = dict(LOCAL); loc.update(extra_local or {})
    secs = []
    for i, (sid, h) in enumerate(d.slides, 1):
        h = re.sub(r'<p class="pg">\d+</p>', f'<p class="pg">{i:02d}</p>', h)
        h = re.sub(r'\{\{([^}]+)\}\}', lambda m: 'file://' + loc[m.group(1)], h)
        h = re.sub(r'<aside>.*?</aside>', '', h, flags=re.S)
        secs.append(h)
    doc = f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@300..700&display=swap">
<style>{DECK_CSS}
html,body{{margin:0;background:#333}} section{{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box;margin:0 0 20px 0}}
section *{{box-sizing:content-box;margin:0}} section > *{{position:relative}} h1,h2,h3,p{{margin:0}} .in,.in2,.in3{{animation:none}}</style></head><body>
{''.join(secs)}</body></html>'''
    open(out, 'w').write(doc)

def media_from_copies(d, path):
    src2dst = {}
    for line in open(path):
        if line.strip():
            dst, src = line.split(); src2dst[src] = '/_blob/' + dst
    for k in d.media:
        if k in DSB and DSB[k][0] in src2dst: d.media[k] = src2dst[DSB[k][0]]
    missing = [k for k, v in d.media.items() if not v]
    return missing

# ---------------- cards decks: the riso card mock-up ----------------
def card_mock(d, x, y, w=500, word='YOUR CARD', name='YOUR NAME', header='Phantasm', word_size=84):
    """A card drawn in riso blue and yellow, with an ink-blue offset print behind it. Scales with w (text never under 24px)."""
    k = w / 500; h = round(w / 0.718); px = round(44 * k); aw = w - 2 * px; ah = round(h * 0.52); top = round(118 * k)
    f = lambda v: max(24, round(v * k))
    lines = word.count('<br>') + 1; ws = round(word_size * k); wy = top + ah // 2 - round(ws * lines * 0.95 / 2)
    tex = d.m('decors/texture-trame-points-bleus.png')
    return f'''<div style="position:absolute;left:{x + round(28 * k)}px;top:{y + round(28 * k)}px;width:{w}px;height:{h}px;background:var(--ink-blue)"></div>
<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:var(--blue)">
<div style="position:absolute;left:{round(20 * k)}px;top:{round(20 * k)}px;width:{w - round(46 * k)}px;height:{h - round(46 * k)}px;border:3px solid var(--yellow)"></div>
<p class="t" style="position:absolute;left:{px}px;top:{round(46 * k)}px;width:{aw}px;font-size:{f(44)}px;line-height:1;color:var(--yellow)">{header}</p>
<p style="position:absolute;left:{px}px;top:{round(56 * k)}px;width:{aw}px;text-align:right;font-size:24px;font-weight:600;line-height:1;color:var(--paper)">UNIQUE</p>
<div style="position:absolute;left:{px}px;top:{top}px;width:{aw}px;height:{ah}px;overflow:hidden;background:var(--yellow)">
<img src="{tex}" alt="" style="position:absolute;left:0px;top:0px;width:{aw}px;height:{ah}px;object-fit:cover">
<p class="t" style="position:absolute;left:0px;top:{wy - top}px;width:{aw}px;text-align:center;font-size:{ws}px;line-height:0.95;color:var(--blue)">{word}</p>
</div>
<p class="t" style="position:absolute;left:{px}px;top:{top + ah + round(36 * k)}px;width:{aw}px;font-size:{f(56)}px;line-height:1;color:var(--paper)">{name}</p>
<div style="position:absolute;left:{px}px;top:{top + ah + round(112 * k)}px;width:{aw}px;height:3px;background:var(--yellow)"></div>
<p style="position:absolute;left:{px}px;top:{top + ah + round(138 * k)}px;width:{aw}px;font-size:{f(26)}px;font-weight:600;line-height:1;color:var(--yellow)">??? / 100</p>
</div>'''

def deal(d, sid, yours, ours, note, n, label='The deal'):
    yy = ''.join(f'<div class="row g24 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc" style="width:44px;flex:none">{a:02d}</p><h3 class="t t{"64" if max(len(x) for x in yours) < 24 else "48"}">{x}</h3></div>' for a, x in enumerate(yours, 1))
    oo = ''.join(f'<div class="col g12 rule" style="padding:24px 0"><p class="lab acc">{a}</p><p class="body">{b}</p></div>' for a, b in ours)
    d.add(sid, sec(sid, 'paper', f'''<div class="panel"></div>
<div class="col" style="width:688px;justify-content:space-between">
<div class="col g24 in"><p class="lab acc">{label}</p><h2 class="t t120">Your part.</h2></div>
<div class="col in2">{yy}</div>
</div>
<div style="width:192px;flex:none"></div>
<div class="col" style="flex:1;justify-content:space-between">
<div class="col g24 in"><p class="lab acc">&nbsp;</p><h2 class="t t120">Our part.</h2></div>
<div class="col in3">{oo}</div>
</div>
{d.foot(n)}''', note, ' style="flex-direction:row"'))

def vstatement_figs(d, sid, vid, label, title, line, figs, note, alt, poster=None):
    """Video statement with a small row of figures under the sentence."""
    bg = video(d, vid, alt) if not poster else f'<img class="bg" src="{d.m(poster)}" data-video="{d.m(vid + ".mp4")}" alt="{alt}">'
    cells = ''.join(f'<div class="col g8"><p class="t t64">{v}</p><p class="lab mute">{l}</p></div>' for v, l in (figs or []))
    body = f'''{bg}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g40 in" style="width:1500px">
{f'<p class="lab acc">{label}</p>' if label else ''}
<h2 class="t t150">{title}</h2>
<p class="lead">{line}</p>
{f'<div class="row in2" style="gap:80px;margin-top:16px">{cells}</div>' if figs else ''}
</div>'''
    d.add(sid, sec(sid, 'bottom', body, note, ' style="padding-bottom:144px"'))

# ---------------- Street Activations: offer pages ----------------
def offer_intro(d, sid, ph, label, title, price, line, note, alt, n):
    body = f'''{photo(d, ph, alt)}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g32 in" style="width:1500px">
<p class="lab acc">{label}</p>
<h2 class="t t200">{title}</h2>
<p class="lead">{line}</p>
</div>
{d.foot(n)}'''
    d.add(sid, sec(sid, 'bottom', body, note))

OFFER_PERKS = {}   # sid -> (title override or None, four perks), set by the deck spec
def offer_page(d, sid, label, title, price, caption, cols, note, n, cta='Talk to John first →', foot=None):
    """Street Activations offer pages, now drawn as price posters (15 Nov 2026). The full columns go to the notes."""
    t, perks = OFFER_PERKS.get(sid, (None, None))
    perks = perks or [x for _, items in cols for x in items][:4]
    price_poster(d, sid, label, t or title, price, caption, perks, note, cta or 'Talk to John first →', full=cols)

# ---------------- price poster (15 Nov 2026): yellow field, giant black price ----------------
W100 = {'40 ETH': 241, '15 ETH': 225, '9 ETH': 193, '0.6 ETH': 262, '0.06 ETH': 309, '€6,000': 262}  # Anton width at 100px, -0.02em
def giant_price(price, color, left=70, maxw=1780, top_min=520, bottom=1032, fs=400):
    """Price set at 400px (Slides' cap) then enlarged with transform:scale; baseline kept inside the frame."""
    w0 = W100.get(price, len(price) * 46) * fs / 100; h0 = fs * 0.86
    s = min(maxw / w0, (bottom - top_min) / h0)
    vw, vh = w0 * s, h0 * s
    cx, cy = left + vw / 2, bottom - vh / 2
    return f'<p class="t" style="position:absolute;left:{cx - w0 / 2:.0f}px;top:{cy - h0 / 2:.0f}px;width:{w0 + 8:.0f}px;font-size:{fs}px;line-height:0.86;letter-spacing:-0.02em;white-space:nowrap;color:{color};transform:scale({s:.3f})">{price}</p>'

def price_poster(d, sid, label, title, price, stamp, perks, note, cta='Talk to John first →', full=None):
    """The price page: yellow field, the price huge in black along the bottom, a tilted stamp, four perks. Full lists go to the notes."""
    pk = ''.join(f'<div class="row g16" style="align-items:center"><div style="width:12px;height:12px;flex:none;background:var(--ink)"></div><p class="lab">{x}</p></div>' for x in perks)
    st = f'<p class="t" style="align-self:flex-start;font-size:56px;line-height:1;padding:12px 22px 10px;background:var(--ink);color:var(--yellow);transform:rotate(-3deg)">{stamp}</p>'
    body = f'''{giant_price(price, 'var(--ink)')}
<div class="row" style="justify-content:space-between;align-items:flex-start;color:var(--ink)">
<div class="col g24 in" style="width:960px"><p class="lab">{label}</p><h2 class="t t120" style="color:var(--ink)">{title}</h2></div>
<div class="col g24 in2" style="width:700px">{st}<div class="col g12">{pk}</div>{f'<p class="lab" style="margin-top:8px">{cta}</p>' if cta else ''}</div>
</div>'''
    if full: note = note + ' Full list. ' + ' '.join(f'{h}: ' + '; '.join(i) + '.' for h, i in full)
    d.add(sid, sec(sid, 'yellow', body, note, ' style="justify-content:flex-start"'))

# ---------------- value-first offer (15 Nov 2026, late): the value is the hero, the price sits in a black stub ----------------
def value_offer(d, sid, label, title, anchor, vals, price, stamp, note, cta='Talk to John first →', full=None):
    """Yellow field: what you get as four big figures; a black band at the bottom holds the price, the stamp and the call to action."""
    vv = ''.join(f'''<div class="col g12" style="border-top:3px solid var(--ink);padding-top:24px">
<div class="row g12" style="align-items:baseline"><p class="t" style="font-size:150px;line-height:0.84;color:var(--ink)">{a}</p><p class="t t48" style="color:var(--ink)">{b}</p></div>
<p class="body" style="color:var(--ink)">{c}</p></div>''' for a, b, c in vals)
    body = f'''<div style="position:absolute;left:0px;top:850px;width:1920px;height:230px;background:var(--ink)"></div>
<div class="col g16 in" style="color:var(--ink)"><p class="lab">{label}</p><h2 class="t t120" style="color:var(--ink)">{title}</h2><p class="lab">{anchor}</p></div>
<div class="in2" style="display:grid;grid-template-columns:repeat({len(vals)}, 1fr);column-gap:48px">{vv}</div>
<div class="row in3" style="position:absolute;left:96px;top:850px;width:1728px;height:230px;align-items:center;justify-content:space-between">
<div class="row" style="align-items:center;gap:40px"><p class="t" style="font-size:112px;line-height:0.86;color:var(--yellow)">{price}</p>
<p class="t" style="font-size:44px;line-height:1;padding:10px 18px 8px;background:var(--yellow);color:var(--ink);transform:rotate(-3deg)">{stamp}</p></div>
<p class="lab" style="color:var(--yellow);text-align:right;width:640px">{cta}</p></div>'''
    if full: note = note + ' Full list. ' + ' '.join(f'{h}: ' + '; '.join(i) + '.' for h, i in full)
    d.add(sid, sec(sid, 'yellow', body, note, ' style="padding-bottom:300px"'))

OFFER_VALUES = {}   # sid -> dict(label, title, anchor, vals), set by the deck spec
def offer_page(d, sid, label, title, price, caption, cols, note, n, cta='Talk to John first →', foot=None):
    """Street Activations offer pages, drawn value-first (15 Nov 2026, late). The full columns go to the notes."""
    o = OFFER_VALUES[sid]
    value_offer(d, sid, o['label'], o['title'], o['anchor'], o['vals'], price, caption, note, cta or 'Talk to John first →', full=cols)


# ---------------- breathing slides (16 Nov 2026): almost nothing on screen ----------------
def pause_video(d, sid, vid, label, title, note, alt, size=200, poster=None, clip=None):
    """A pause: the video full bleed, one title, a small label. No sentence, no footer."""
    bg = f'<img class="bg" src="{d.m(poster or vid + ".jpg")}" data-video="{d.m(clip or vid + ".mp4")}" alt="{alt}">'
    body = f'''{bg}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g24 in" style="width:1600px">
<p class="lab acc">{label}</p>
<h2 class="t" style="font-size:{size}px;line-height:0.88;letter-spacing:-4px">{title}</h2>
</div>'''
    d.add(sid, sec(sid, 'bottom', body, note, ' style="padding-bottom:110px"'))

def pause_dragon(d, sid, k, label, title, note, side='right', h=1000, size=150):
    """A pause: one dragon, huge, cut by the bottom edge, and one statement on black."""
    w = round(h * RATIO[k]); top = 1080 - h + 130
    x = 1920 - w + 70 if side == 'right' else -70
    tx = 96 if side == 'right' else 1920 - 96 - 900
    body = f'''{dragon_img(d, k, x, h, 130, 'The ' + k.replace('-', ' ') + ' dragon')}
<div class="col g24 in" style="position:absolute;left:{tx}px;top:0px;width:1000px;height:1080px;justify-content:center">
<p class="lab acc">{label}</p>
<h2 class="t" style="font-size:{size}px;line-height:0.92;letter-spacing:-3px">{title}</h2>
</div>'''
    d.add(sid, sec(sid, '', body, note))
