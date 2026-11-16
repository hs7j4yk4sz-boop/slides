import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('cs', 'NFC Summit 2027 — CryptoStamp Corner')
X = {'cs/aerial.jpg': MEDIA + '/cs/aerial.jpg', 'cs/booth-stamps.jpg': MEDIA + '/cs/booth-stamps.jpg',
     'cs/meetup.jpg': MEDIA + '/cs/meetup.jpg', 'cs/crowd.jpg': MEDIA + '/cs/crowd.jpg'}
cover(d, 'cover', PH('stand-la-poste-cryptostamps'), 'NFC Summit 2027', 'CryptoStamp Corner',
      'Discover CryptoStamps, understand how they work, collect them on site.', '27 — 29 May 2027 · Unicorn Factory, Beato, Lisbon',
      'The French Post’s CryptoStamps booth at NFC Summit 2026.', 'The French Post’s CryptoStamps booth at NFC Summit 2026')
vstatement(d, 'back', VID('salle-kawaii-cartes-et-stamps'), 'CryptoStamp Corner is back.', 'Bigger area, bigger programme, more collectors.',
      'NFC aims to introduce and trial new practices around digital collectibles. CryptoStamps are a key focus this year: we’re enlarging the area and programme so more digital art collectors can try and collect them, while the emerging Digital Stamp Collectibles community gathers to share and discuss together.',
      'The Kawaii Summit hall in 2026: card sellers, game tables and stamps')
vstatement(d, 'meets', VID('place-totem-et-mur'), 'When philately meets digital art.', 'Discover, understand, collect. On site.',
      'Visitors discover the series, understand how they work, then buy at the booth or online.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
facts = [('Where', 'Unicorn Factory, Beato, Lisbon'), ('When', '27 & 28 May 2027, 10:00 — 18:00. 29 May: closing day in Caparica'), ('Who', 'Digital art fans and digital stamp collectors')]
fc = ''.join(f'<div class="col g16 rule-d" style="padding-top:28px"><p class="lab acc">{a}</p><p class="lead" style="font-size:36px;line-height:1.25">{b}</p></div>' for a, b in facts)
pause_dragon(d, 'small', 'kawaii-summit', 'CryptoStamp Corner · 2027', 'Small stamps.<br>Big collectors.',
      'A pause. The smallest artworks of the festival draw some of its most dedicated collectors.', side='right', h=980)
d.add('corner', sec('corner', '', f'''{photo(d, 'cs/crowd.jpg', 'The CryptoStamp Corner at NFC Summit 2026, full of visitors')}
<div class="shade-dark"></div>
<div class="col g32 in" style="width:1400px">
<p class="lab acc">Sixth edition · 2027</p>
<h2 class="t t120">A whole corner for digital stamps</h2>
<p class="lead">Following the success of last year’s edition, NFC is back in 2027 with a dedicated area where visitors discover CryptoStamps, understand how they work, and buy them on site.</p>
</div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{fc}</div>
{d.foot(4)}''', 'Who: digital art fans and digital stamp collectors. The emerging Digital Stamp Collectibles community gathers to share and discuss together.'))
programme(d, 'corner3', 'CryptoStamp Corner', 'On site, three ways', [
      ('cs/aerial.jpg', 'Aerial view of the Unicorn Factory in Beato', 'Prime location', 'The most visible zone', ['Next to the main art exhibition', 'Next to the main stage']),
      ('cs/booth-stamps.jpg', 'CryptoStamps on a booth table', 'The booths', 'Exhibit, sell, activate', ['Packaged booths for postal services', 'Discover the series, buy on site or online']),
      ('cs/meetup.jpg', 'A talk at the CryptoStamp meetup', 'The meetup', 'Talks on 27 May', ['Why CryptoStamps matter', 'Case studies and best practices', 'A late-afternoon collectors’ meet-up'])],
      'Prime location: CryptoStamp Corner containers will sit in the most visible zone, next to the main art exhibition and the main stage. The booths: on site, postal services book packaged booths where they can exhibit, sell, and support activations. The visitor journey is straightforward: discover the series, then buy at the booth or online. The meetup: on 27 May we run a focused programme of talks and panels: an opening session on why CryptoStamps matter; case studies from leading postal services, a panel with best practices and a late-afternoon collectors’ meet-up.', 5)
pause_video(d, 'meet', VID('expo-art-factory-etage'), '27 — 29 May 2027 · Lisbon', 'Meet the collectors.',
      'Three days in front of the people who collect digital stamps and digital art.', 'Visitors in an exhibition room at NFC Summit 2026', poster='px/expo-crowd.jpg')
value_offer(d, 'offer', 'Pre-packed booth · Bronze sponsorship', 'Your booth in the corner', 'Next to the main art exhibition and the main stage',
      [('1.5', 'm²', 'A furnished booth: table, screen, backdrop, power, internet'), ('4', 'tickets', 'NFC tickets for your team'),
       ('3', 'logos', 'On CryptoStamp prints, NFC websites, the meetup page'), ('1', 'tweet', 'A dedicated post by NFC Summit, and a spot in the April newsletter')],
      '€6,000', 'Before 31 Dec 2026',
      'Special offer for sign-up before 31 December 2026. For national post services, collectors’ associations and independent artists with a digital stamps project in 2027. Who can apply: national post services, collectors’ associations, independent artists. Applicants need at least one digital stamps project released or planned for release in 2027. Newsletter: up to 400 characters. Custom offers: if you want a larger footprint, a co-produced stamp drop with NFC, special collaborations with NFC artists, speaking slots on the main stage or side stages, or a private event produced by NFC, contact us and we will tailor a proposal.',
      full=[('The booth', ['Footprint 1.0 m × 1.5 m', '2 stools, 1 table, 1 screen, 1 printed backdrop', 'Power and stable internet', 'Setup and teardown included']),
            ('Bronze sponsorship', ['Your logo on all CryptoStamp on-site prints', 'Your logo on the NFC websites', 'Your logo on the meetup webpage', 'One dedicated tweet by NFC Summit', 'A spot in the CryptoStamp newsletter, April 2027', 'Four NFC tickets for your team'])])
d.add('contact', sec('contact', 'bottom', f'''{video(d, VID('salle-kawaii-cartes-et-stamps'), 'The Kawaii Summit hall in 2026')}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g32 in" style="width:1400px">
<p class="lab acc">CryptoStamp Corner · NFC Summit 2027</p>
<h2 class="t t150">Talk to John</h2>
<div class="col g12"><p class="lead">John Karp</p><p class="lab">john@nonfungibleconference.com · t.me/thejonnkarp</p></div>
</div>
{d.foot(7)}''', 'Custom offers on request: larger footprint, co-produced stamp drop, artist collaborations, speaking slots, private events.'))
SECTIONS = {"intro": {"description": "CryptoStamp Corner is back for the sixth edition.", "start": "cover"},
            "corner": {"description": "Where, when and how the corner works.", "start": "corner"},
            "offer": {"description": "The booth, the sponsorship and the contact.", "start": "offer"}}
