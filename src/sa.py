import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('sa', 'NFC Summit 2027 — NFC Street Activations')
SA = MEDIA + '/sa/'
X = {f'sa/{f}': SA + f for f in os.listdir(SA)}

# 01 cover — graded photo of the 2026 murals
cover(d, 'cover', 'sa/cover-murals.jpg', 'NFC Summit 2027 · 27 — 29 May · Unicorn Factory, Lisbon', 'NFC Street Activations',
      'Containers, murals and street art take over Europe’s leading festival for digital creative communities.', 'On The Wall',
      'NFC Street Activations: the containers, the murals and the street art of NFC Summit 2027, and how the community paid to be on the walls before the festival.',
      'The central plaza of NFC Summit 2026, with its pixel murals')

# 02 this is NFC — video + strong sentence
vstatement_figs(d, 'nfc', VID('place-totem-et-mur'), 'Sixth edition · 27 — 29 May 2027 · Unicorn Factory, Lisbon', 'This is NFC.',
      'The annual home of digital creative communities.',
      [('2,740', 'attendees in 2026'), ('79', 'countries'), ('6M+', 'organic impressions')],
      'The annual home of digital creative communities: artists, collectors, builders. Three days, one venue. In 2026: 2,740 attendees from 79 countries, more than 6 million organic impressions.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')

# 03 the museum — video + strong sentence
vstatement_figs(d, 'museum', VID('mur-crane-pixel'), 'NFC, year after year, became', 'An open-air digital art museum.',
      'The most photographed square metres of NFC.', None,
      'Flying over the 2026 murals. 01: it started two years ago with the containers. 02: the 2026 murals became the most loved part of NFC. 03: they are still on the walls today. 04: street-art tour agencies now include the site.',
      'A pixel skull mural on the walls of NFC Summit 2026')

# 04 the community went first
world(d, 'community', 'sa/painter.jpg', 'On The Wall · 10 Sept — 30 Oct 2026', 'The community went first.',
      'From 10 September to 30 October 2026, we opened the walls of NFC to the community.',
      'From 10 September to 30 October 2026, we opened the walls of NFC to the community: five walls, five ways in.',
      'An artist painting a container at NFC Summit 2026', 4)

# 05 they made NFC 2027 happen
facts_row(d, 'happened', 'On The Wall · the campaign', 'They made NFC 2027 happen.',
      ['325 mints in seven weeks', '311 names and 14 portraits to be hand-painted on the walls', 'House 01 taken by JPEG FRENS', 'People of the Wall, the podcast: every Friday, 32 episodes so far'],
      'The community did not wait for May.',
      '325 mints in seven weeks. 311 names and 14 portraits to be hand-painted on the walls of NFC 2027. House 01 taken by JPEG FRENS. People of the Wall, the podcast, every Friday: 32 episodes so far. The final day reached Today’s News on X. The Yearbook, made with Alpha Labs, is handed out on 27 May.', 5)

pause_video(d, 'street', VID('mur-crane-pixel'), 'On The Wall', 'The street<br>is the gallery.',
      'A pause. Containers, murals and street art: the whole site becomes the exhibition.', 'A drone flight over the courtyard and its pixel mural at NFC Summit 2026', poster='px/courtyard-drone.jpg', clip='px/courtyard-drone.mp4')

# 06 why take one
why = [('Painted for real', 'Your mark, hand-painted on the venue. Still there after the festival.'),
       ('A post-ready card', 'Your azulejo card: name, spot, made to share.'),
       ('On-chain, yours to keep', 'An NFT that proves your place on the wall.'),
       ('Part of the museum', 'Inside the open-air museum, photographed all year, on the street-art tour route.'),
       ('Holder exclusives & surprises', 'Drops, access and surprises for everyone on the wall, during the campaign and at NFC 2027.'),
       ('A ticket in every tier', 'From 1 GA with a name to 70 tickets with the flagship.'),
       ('The higher, the bigger', 'Passes, events, status, keynotes: the bigger your wall, the bigger your role.')]
ww = ''.join(f'<div class="col g8 rule" style="padding-top:20px"><p class="lab acc">{i:02d}</p><h3 class="t t36">{a}</h3><p class="small mute">{b}</p></div>' for i, (a, b) in enumerate(why, 1))
d.add('why', sec('why', 'paper', f'''<div class="col" style="width:600px;justify-content:space-between">
<p class="lab acc in">Why take one</p>
<div class="col g32 in"><h2 class="t t120">These spaces build the festival.</h2><p class="lead">The community funded the edition early, and got more than a thank-you.</p></div>
</div>
<div class="in2" style="flex:1;display:grid;grid-template-columns:1fr 1fr;column-gap:56px;row-gap:28px;align-content:end">{ww}</div>
{d.foot(6)}''', 'The community funded the edition early, and got more than a thank-you. Every mark on the wall comes with: 01 Painted for real: your mark, hand-painted on the venue, still there after the festival. 02 A post-ready card: your azulejo card, name, spot, made to share. Your face on our channels, not just our logo on yours. 03 On-chain, yours to keep: an NFT that proves your place on the wall. 04 Part of the museum: inside the open-air museum, photographed all year, on the street-art tour route. 05 Holder exclusives and surprises: drops, access and surprises for everyone on the wall, during the campaign and at NFC 2027. 06 A ticket in every tier: from 1 GA with a name to 70 tickets with the flagship. 07 The higher, the bigger: passes, events, status, keynotes; the bigger your wall, the bigger your role.', ' style="flex-direction:row;gap:96px"'))

# 07 John Karp — the seven dragons carry his sentence
stage(d, 'quote', 'John Karp · founder', 'NFC exists because people like you decide it should. Be the one for 2027.',
      'NFC exists because people like you decide it should. Be the one for 2027. John Karp, founder of NFC Summit.')

# 08 how it happens
steps = [('Pick your wall', 'Choose your Mural. Four houses exist, 2 Murals, 1 Flagship.'), ('Send the artwork', 'Yours, your artist’s, or a piece from your collection.'),
         ('Adapt & validate', 'Re-composed for the wall’s real proportions. You sign it off.'), ('Built & delivered', 'Hand-painted on site before doors, your credit beside it.')]
dates = [('10 Sept — 30 Oct 2026', 'Campaign window: the mint was open'), ('Winter 2026 — 27', 'Customization and validation'), ('Before 27 May 2027', 'Build, paint, install on the plaza'), ('27 May 2027', 'Your mural is painted')]
st = ''.join(f'<div class="col g12"><p class="lab acc">{i:02d}</p><h3 class="t t48">{a}</h3><p class="small mute">{b}</p></div>' for i, (a, b) in enumerate(steps, 1))
dt = ''.join(f'<div class="col g12"><div class="sq"></div><p class="lab">{a}</p><p class="small mute">{b}</p></div>' for a, b in dates)
d.add('how', sec('how', '', f'''<div class="col g24 in"><p class="lab acc">How it happens</p><h2 class="t t120">Four steps, one delivery date.</h2></div>
<div class="col g48">
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px">{st}</div>
<div class="in3" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px;border-top:2px solid var(--graphite);padding-top:32px">{dt}</div>
</div>
{d.foot(8)}''', 'Four steps, one delivery date. 01 Pick your wall: choose your Mural; four houses exist, 2 Murals, 1 Flagship. 02 Send the artwork: yours, your artist’s, or a piece from your collection. 03 Adapt and validate: re-composed for the wall’s real proportions; you sign it off. 04 Built and delivered: hand-painted on site before doors, your credit beside it. Dates: the campaign window and mint ran from 10 September to 30 October 2026; customization and validation in winter 2026 — 27; build, paint and install on the plaza before 27 May 2027; your mural is painted for 27 May 2027.'))

pause_dragon(d, 'waiting', 'ringmaster-hero', 'Five ways in', 'Your wall<br>is waiting.',
      'The ringmaster opens the offers: the flagship mural, two artist murals, the community houses, the PFP wall and the name wall.', side='right', h=980)

# 09 the offers
offers = [('01', 'Flagship Mural', '40 ETH', '1 of 1', 'The most visible wall of NFC 2027. Keynote, 20 VIP + 50 GA.', 'Platinum · Co-organizer'),
          ('02', 'Artist Murals', '15 ETH', '2 walls', 'Main Stage or North Wall, painted by one of our artists. 8 VIP + 20 GA.', 'Platinum Sponsor'),
          ('03', 'Community House', '9 ETH', '4 houses', 'Your container on the central plaza, in your colour. 4 VIP + 10 GA.', 'Gold Sponsor · Top 14'),
          ('04', 'The PFP Wall', '0.6 ETH', '50 squares', 'Your PFP hand-painted at the top of the wall. 2 VIP passes.', 'onthewall.nfcsummit.com'),
          ('05', 'The Name Wall', '0.06 ETH', '500 names', 'Your name hand-painted on the façade. 1 GA ticket.', 'onthewall.nfcsummit.com')]
oo = ''.join(f'''<div class="rule" style="display:grid;grid-template-columns:56px 380px 240px 160px 1fr 340px;column-gap:24px;align-items:center;padding:20px 0">
<p class="lab acc">{a}</p><h3 class="t t48">{b}</h3><p class="t t64">{c}</p><p class="lab mute">{q}</p><p class="small">{t}</p><p class="lab mute">{s}</p></div>''' for a, b, c, q, t, s in offers)
d.add('offers', sec('offers', 'paper', f'''<div class="col g24 in"><p class="lab acc">Five ways in · the offers · Mint 10 Sept — 30 Oct 2026</p><h2 class="t t120">Five offers, one wall each.</h2><p class="lead">From a hand-painted name at 0.06 ETH to the flagship mural at 40. Anyone can own a piece.</p></div>
<div class="col in2">{oo}</div>
{d.foot(9, 'This deck details offers 01 — 03 · 04 and 05 live on the site')}''', 'Five offers, one wall each, from a hand-painted name at 0.06 ETH to the flagship mural at 40 ETH. This deck details offers 01 to 03; offers 04 and 05 are on onthewall.nfcsummit.com.'))

# 10 Flagship Mural — the wall
d.add('flagship', sec('flagship', 'bottom', f'''<img src="{d.m('sa/flagship-passage.jpg')}" alt="The courtyard passage where the Flagship Mural will be painted" style="position:absolute;left:1312px;top:0px;width:608px;height:1080px;object-fit:cover">
<div class="col g32 in" style="width:1120px">
<p class="lab acc">Offer 01 · 1 of 1</p>
<h2 class="t t200">Flagship Mural</h2>
<p class="lead">Above the courtyard passage.</p>
</div>
{d.foot(10)}''', 'Offer 01: the Flagship Mural, 1 of 1, 40 ETH, above the courtyard passage.'))

# 11 Flagship Mural — the 2026 precedent
d.add('flag-wall', sec('flag-wall', 'bottom', f'''{photo(d, 'sa/xcopy-passage.jpg', 'Visitors in the XCOPY passage at NFC Summit 2026')}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g32 in" style="width:1200px">
<p class="lab acc">Flagship Mural · 1 of 1</p>
<h2 class="t t120">The most visible wall of NFC 2027.</h2>
<p class="lead">Every edition has one wall everyone sees. In 2026, it was XCOPY’s.</p>
<p class="body mute">In 2027 the festival reorganises around the courtyard, and its most visible wall is this one. Painted from your artwork. Yours takes the role.</p>
</div>
{d.foot(11, 'The 2026 precedent: the XCOPY passage')}''', 'Every edition has one wall everyone sees. In 2026, it was XCOPY’s. In 2027 the festival reorganises around the courtyard, and its most visible wall is this one. Painted from your artwork. Yours takes the role.'))

# 12 Flagship Mural — the role
role = [('Category exclusivity', 'No competitor in your category sponsors NFC.'), ('Co-build', 'Influence the programme, editorial line, speakers and formats.'),
        ('You make it happen', 'Your commitment secures the edition. The patron of patrons.'), ('100 % integrated', 'Shared goals, clear KPIs, measurable ROI. Everything adjustable.'),
        ('100 % custom', 'Content, production, data, CTAs and calendar built for you.'), ('Year-round', 'A 2026 / 2027 partnership: before, during and after the event.'),
        ('Community trust', 'Build trust and engage your community where it lives.'), ('On-chain', 'Your products integrated into the NFC registration flow.')]
rr = ''.join(f'<div class="col g12 rule-d" style="padding-top:24px"><h3 class="t t36">{a}</h3><p class="small mute">{b}</p></div>' for a, b in role)
d.add('flag-role', sec('flag-role', '', f'''<div class="col g24 in"><p class="lab acc">Flagship Mural · the role</p><h2 class="t t120">You don’t sponsor NFC 2027.<br>You co-organize it.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px;row-gap:40px">{rr}</div>
{d.foot(12, 'Co-organizer of NFC 2027')}''', 'You don’t sponsor NFC 2027. You co-organize it: category exclusivity, co-build, you make it happen, 100% integrated, 100% custom, year-round, community trust, on-chain.'))

OFFER_VALUES.update({
    'flag-offer': dict(label='Offer 01 · Platinum + Co-organizer', title='Flagship Mural', anchor='NFC 2026: 2,740 attendees from 79 countries', vals=[
        ('1', 'wall', 'The most visible wall of NFC 2027, painted from your artwork'), ('1', 'keynote', 'An opening slot on the main stage'),
        ('70', 'tickets', '20 VIP + 50 GA, from January 2027'), ('#1', 'partner', 'Co-organizer of NFC 2027, top line of nfcsummit.com')]),
    'murals-offer': dict(label='Offer 02 · Platinum Sponsor', title='Artist Murals', anchor='NFC 2026: 2,740 attendees from 79 countries', vals=[
        ('1', 'wall', 'Main stage or north wall, painted from your artwork by one of our artists'), ('1', 'event', 'A dedicated community event at your mural, 27 — 29 May'),
        ('28', 'tickets', '8 VIP + 20 GA, from January 2027'), ('1', 'credit', 'Your “Presented by” credit, hand-painted on the wall')]),
    'house-offer': dict(label='Offer 03 · Gold Sponsor · Top 14', title='Community House', anchor='NFC 2026: 2,740 attendees from 79 countries', vals=[
        ('14.4', 'm²', 'A 20-ft container on the central plaza, 100% painted in your colour'), ('2', 'days', 'Your own programme in the house, 27 — 28 May'),
        ('14', 'tickets', '4 VIP + 10 GA, from January 2027'), ('6', 'screens', 'Six 42" screens, power, Wi-Fi and air conditioning')]),
    'pfp-offer': dict(label='Offer 04 · on the wall', title='The PFP Wall', anchor='NFC 2026: 2,740 attendees from 79 countries', vals=[
        ('1', 'square', 'Your PFP hand-painted at the top of the wall'), ('2', 'VIP', 'Tickets for NFC 2027, you and your plus-one'),
        ('1', 'hour', 'A private hour at the venue before doors open'), ('1', 'brunch', 'The Wall private brunch, holders only')]),
    'names-offer': dict(label='Offer 05 · on the wall', title='The Name Wall', anchor='NFC 2026: 2,740 attendees from 79 countries', vals=[
        ('1', 'name', 'Hand-painted on the façade of Armazém 0108'), ('1', 'GA', 'General Admission ticket for NFC 2027'),
        ('1', 'card', 'Your azulejo card, ready to share from day one'), ('1', 'brunch', 'The Wall private brunch, holders only')])})
# 13 Flagship Mural — the package
offer_page(d, 'flag-offer', 'Flagship Mural · the package', 'Platinum +<br>Co-organizer', '40 ETH', '1 of 1', [
    ('The wall', ['The main artwork of NFC 2027, the most visible wall of the festival', 'Artist and artwork chosen together, nothing painted without your sign-off', 'The flagship unveiling: a dedicated event at the mural', 'The NFT: the 1 of 1 of the on-chain network artwork']),
    ('The role', ['Co-organizer of NFC 2027, top line of nfcsummit.com', 'Platinum Sponsor status', 'Category exclusivity', 'An opening keynote slot on the main stage', '20 VIP + 50 GA tickets, claimable from January 2027', 'Your profile put forward across NFC 2027 communications', 'One hour before + the holders’ brunch, as guest of honour'])],
    'Flagship Mural, 40 ETH, 1 of 1: Platinum + Co-organizer. Talk to John first.', 13)

# 14 Artist Murals — intro
offer_intro(d, 'murals', 'sa/van-street-art.jpg', 'Offer 02 · 2 available', 'Artist Murals', '15 ETH', 'Your artwork, painted for real.',
      'Offer 02: the Artist Murals, 2 available, 15 ETH. Your artwork, painted for real.', 'Street art on a wall behind a painted van', 14)

# 15 Artist Murals — the two walls
walls = [('Main Stage Artist Mural', '4.2 × 3.4', 'Metres · faces the main stage'), ('North Wall Artist Mural', '3.0 × 3.3', 'Metres · on the praça')]
wl = ''.join(f'<div class="col g16"><div class="bar"></div><p class="lab acc">{a}</p><p class="t t120">{b}</p><p class="body mute">{c}</p></div>' for a, b, c in walls)
d.add('murals-walls', sec('murals-walls', '', f'''<img src="{d.m('sa/main-stage-wall.jpg')}" alt="The site of the Main Stage Artist Mural" style="position:absolute;left:1280px;top:0px;width:640px;height:1080px;object-fit:cover">
<div class="col g24 in" style="width:1080px"><p class="lab acc">Artist Murals · 2 available · 15 ETH</p><h2 class="t t120">Two walls, measured.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:1fr 1fr;column-gap:64px;width:1080px">{wl}</div>
<div class="col g16 in3" style="width:1060px"><p class="lead">Painted by one of our artists from your artwork, with your credit painted beside it.</p><p class="body mute">The 2026 murals are still on the walls: that is what a mural here means.</p></div>
{d.foot(15)}''', 'Two walls, measured. Main Stage Artist Mural: 4.2 × 3.4 m, faces the main stage. North Wall Artist Mural: 3.0 × 3.3 m, on the praça. Painted by one of our artists from your artwork, with your credit painted beside it. The 2026 murals are still on the walls: that is what a mural here means.'))

# 16 Artist Murals — your event
ev = ['A slot in the festival programme at your wall', 'Promoted to the full audience as part of the festival programme', '2026 precedent: the XCOPY passage became the busiest photo spot of the festival']
evv = ''.join(f'<div class="row g20 rule-d" style="padding:18px 0"><div class="ysq"></div><p class="body">{x}</p></div>' for x in ev)
d.add('murals-event', sec('murals-event', '', f'''<img src="{d.m('sa/mural-event.jpg')}" alt="A crowd in front of a black and white mural at NFC Summit 2026" style="position:absolute;left:1120px;top:0px;width:800px;height:1080px;object-fit:cover">
<div style="position:absolute;left:1120px;top:0px;width:320px;height:1080px;background:linear-gradient(90deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0) 100%)"></div>
<div class="col g32 in" style="width:960px"><p class="lab acc">Artist Murals · your event</p><h2 class="t t120">A community event at your mural.</h2>
<p class="lead">We organise a meetup and unveiling moment at the wall with you: your community in front of your piece, drinks, photos, the artist on site.</p></div>
<div class="col in2" style="width:940px">{evv}</div>
{d.foot(16)}''', 'A community event at your mural: we organise a meetup and unveiling moment at the wall with you; your community in front of your piece, drinks, photos, the artist on site. A slot in the festival programme at your wall, promoted to the full audience. 2026 precedent: the XCOPY passage became the busiest photo spot of the festival.'))

# 17 Artist Murals — the offer
offer_page(d, 'murals-offer', 'Artist Murals · the offer', 'Platinum Sponsor', '15 ETH', '2 available', [
    ('The wall', ['One wall: main stage (4.2 × 3.4 m) or north wall (3.0 × 3.3 m)', 'Painted from your artwork by one of our artists', 'Artwork adaption approved by you before painting', 'Your “Presented by” credit, hand-painted on the wall', 'The NFT: your mural in the on-chain network artwork']),
    ('The status', ['Platinum Sponsor status, live on nfcsummit.com', 'A dedicated community event at your mural, 27 — 29 May', '8 VIP + 20 GA tickets, claimable from January 2027', 'Presence across NFC 2027 communications', 'One hour before + the holders’ brunch'])],
    'Artist Murals, 15 ETH, 2 available: Platinum Sponsor. Talk to John first.', 17)

# 18 Community House — intro
offer_intro(d, 'house', 'sa/house-opensea.jpg', 'Offer 03 · 4 available', 'Community House', '9 ETH', 'Your house on the central plaza.',
      'Offer 03: the Community House, 4 available, 9 ETH. Your house on the central plaza.', 'A container painted for OpenSea at NFC Summit 2026', 18)

# 19 Community House — what it becomes
ways = [('sa/way-gallery.jpg', 'A gallery inside a container', 'Gallery', 'Hang the collection, sell in the room.'), ('sa/way-installation.jpg', 'An immersive installation inside a container', 'Installation', 'One immersive piece people queue for.'),
        ('sa/way-clubhouse.jpg', 'A visitor walking through a container', 'Clubhouse', 'Where your community finds each other.'), ('sa/way-live.jpg', 'An artist painting live on a container', 'Live activation', 'Painting and drops in front of the crowd.'),
        ('sa/way-party.jpg', 'A painted container on the plaza', 'Party spot', 'Doors open, sound on, the plaza fills up.')]
wy = ''.join(f'<div class="col"><img src="{d.m(k)}" alt="{a}" style="width:320px;height:240px;object-fit:cover"><h3 class="t t36" style="margin-top:24px">{b}</h3><p class="small mute" style="margin-top:8px">{c}</p></div>' for k, a, b, c in ways)
d.add('house-ways', sec('house-ways', '', f'''<div class="col g24 in"><p class="lab acc">Community House · what it becomes · photos, edition 2026</p><h2 class="t t120">One shell, five ways.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(5, 1fr);column-gap:32px">{wy}</div>
<p class="body mute in3">For galleries · platforms · marketplaces · projects · curators · studios · foundations · museums · brands · communities</p>
{d.foot(19)}''', 'One shell, five ways: a gallery (hang the collection, sell in the room), an installation (one immersive piece people queue for), a clubhouse (where your community finds each other), a live activation (painting and drops in front of the crowd), a party spot (doors open, sound on, the plaza fills up). For galleries, platforms, marketplaces, projects, curators, studios, foundations, museums, brands and communities.'))

# 20 Community House — your canvas
models = [('sa/model-a.jpg', 'Model A', 'The gallery front'), ('sa/model-b.jpg', 'Model B', 'The walk-in'), ('sa/model-c.jpg', 'Model C', 'On quote')]
mm = ''.join(f'<div class="col"><img src="{d.m(k)}" alt="Render of the Community House {a}, {b}" style="width:528px;height:297px;object-fit:cover"><p class="lab acc" style="margin-top:24px">{a}</p><h3 class="t t48" style="margin-top:8px">{b}</h3></div>' for k, a, b in models)
facts = [('Your artwork, painted on one exterior side', 'Paintable face ~6 × 2.5 m · to confirm'), ('Everything else in your colour', '100 % painted, inside and out'), ('Central plaza · highest-traffic', 'Next to the main stage')]
ff = ''.join(f'<div class="col g8 rule-d" style="padding-top:20px"><p class="lab">{a}</p><p class="small mute">{b}</p></div>' for a, b in facts)
d.add('house-canvas', sec('house-canvas', '', f'''<div class="col g24 in"><p class="lab acc">Community House · your canvas · 14.4 sqm · 27 — 28 May</p><h2 class="t t120">Three shells, one canvas: yours.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{mm}</div>
<div class="in3" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{ff}</div>
{d.foot(20, 'Painted, not wrapped')}''', 'Three shells, one canvas: yours. 14.4 sqm, 27 — 28 May. Model A, the gallery front. Model B, the walk-in. Model C, on quote. Your artwork, painted on one exterior side (paintable face about 6 × 2.5 m, to confirm). Everything else in your colour: 100% painted, inside and out. Central plaza, highest-traffic, next to the main stage. Painted, not wrapped.'))

# 21 Community House — the offer
offer_page(d, 'house-offer', 'Community House · the offer', 'Gold Sponsor · Top 14', '9 ETH', '4 available', [
    ('The space', ['A 20-ft container on the central plaza, 27 — 28 May', 'Model A or B included, Model C on quote', '100% painted in your colour, inside and out', 'Your artwork hand-painted on one exterior side, approved by you', 'Six 42" screens · power, Wi-Fi and air conditioning', 'Lighting, stools and barrel tables']),
    ('The status', ['Gold Sponsor status: Top 14 partners of the edition', '4 VIP + 10 GA tickets, claimable from January 2027', 'Your own programme in the house, both days', 'Your community put forward: photo session, spotlights through 2027', 'One hour before + the holders’ brunch', 'The NFT: your house in the on-chain network artwork'])],
    'Community House, 9 ETH, 4 available: Gold Sponsor, Top 14. Talk to John first.', 21)

pause_video(d, 'anyone', VID('place-totem-et-mur'), 'Offers 04 and 05', 'Anyone can<br>own a piece.',
      'From a hand-painted name to a painted portrait: the walls of NFC are open to everyone.', 'The pixel portraits of the Wall at NFC Summit 2026')

# 22 The PFP Wall — intro
d.add('pfp', sec('pfp', 'bottom', f'''<img src="{d.m('sa/pfp-wall.jpg')}" alt="The On The Wall façade with its grid of painted portraits" style="position:absolute;left:960px;top:0px;width:960px;height:1080px;object-fit:cover">
<div style="position:absolute;left:960px;top:0px;width:320px;height:1080px;background:linear-gradient(90deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0) 100%)"></div>
<div class="col g32 in" style="width:800px">
<p class="lab acc">Offer 04 · sold on the site</p>
<h2 class="t t150">The PFP Wall.</h2>
<p class="lead">50 squares, hand-painted in a prominent position at the top of the wall. Your PFP becomes part of the museum.</p>
<p class="lab mute">Mint → upload your PFP → hand-painted for real</p>
</div>
{d.foot(22)}''', 'Offer 04, sold on the site: the PFP Wall. 50 squares, hand-painted in a prominent position at the top of the wall. Your PFP becomes part of the museum. Mint, upload your PFP, hand-painted for real. 0.6 ETH each.'))

# 23 The PFP Wall — the offer
offer_page(d, 'pfp-offer', 'The PFP Wall · the offer', 'On the wall', '0.6 ETH', '50 squares', [
    ('The wall', ['One square in a prominent position at the top of the wall', 'Your PFP hand-painted by one of our artists, before doors open', 'Replaceable until 30 October', 'The NFT: your square among the fifty faces']),
    ('The perks', ['2 VIP tickets for NFC 2027, you and your plus-one', 'Your profile put forward: official picture, spotlights through 2027', 'One hour before: a private hour at the venue', 'The Wall private brunch, holders only', 'The post-event pack'])],
    'The PFP Wall, 0.6 ETH, 50 squares. Mint 10 Sept — 30 Oct 2026 on onthewall.nfcsummit.com.', 23, cta='Mint 10 Sept — 30 Oct 2026 · onthewall.nfcsummit.com')

# 24 The Name Wall — intro
nw = ['500 names, hand-painted on the venue.', 'Your number is your spot on the wall.', 'Editable until 30 October. One General Admission ticket included.', 'Each name gets a shareable azulejo card.']
nn = ''.join(f'<div class="row g20 rule-d" style="padding:16px 0"><p class="lab acc" style="width:40px;flex:none">{i:02d}</p><p class="body">{t}</p></div>' for i, t in enumerate(nw, 1))
d.add('names', sec('names', '', f'''<img src="{d.m('sa/name-wall-site.jpg')}" alt="The On The Wall site, with the names on the wall" class="frame" style="position:absolute;left:1104px;top:150px;width:720px;height:628px;object-fit:cover">
<div class="col g24 in" style="width:920px"><p class="lab acc">Offer 05 · sold on the site</p><h2 class="t t150">The Name Wall.</h2></div>
<div class="col in2" style="width:920px">{nn}</div>
<div class="row g40 in3" style="align-items:flex-end;width:1728px;justify-content:space-between"><p class="lead" style="width:1100px">You won’t just sponsor NFC 2027. You’ll stand on its walls with 500 others.</p></div>
{d.foot(24)}''', 'Offer 05, sold on the site: the Name Wall. 500 names, hand-painted on the venue. Your number is your spot on the wall. Editable until 30 October; one General Admission ticket included. Each name gets a shareable azulejo card. You won’t just sponsor NFC 2027. You’ll stand on its walls with 500 others. 0.06 ETH.'))

# 25 The Name Wall — the offer
offer_page(d, 'names-offer', 'The Name Wall · the offer', 'On the wall', '0.06 ETH', '500 names', [
    ('The wall', ['Your name hand-painted on the façade of Armazém 0108', 'Editable until 30 October', 'Your azulejo card, ready to share from day one', 'The NFT: your name and panel number, on-chain']),
    ('The perks', ['1 General Admission ticket for NFC 2027', 'Your profile put forward: official picture, spotlights through 2027', 'One hour before: a private hour at the venue', 'The Wall private brunch, holders only', 'The post-event pack'])],
    'The Name Wall, 0.06 ETH, 500 names. Mint 10 Sept — 30 Oct 2026 on onthewall.nfcsummit.com.', 25, cta='Mint 10 Sept — 30 Oct 2026 · onthewall.nfcsummit.com')

# 26 Talk to John — the seven dragons
closing(d, 'contact', 'NFC Street Activations · On The Wall', 'Talk to John.', ['John Karp · onthewall.nfcsummit.com'],
      'Talk to John Karp: john@nonfungibleconference.com, t.me/thejonnkarp. The walls of the campaign: onthewall.nfcsummit.com.',
      contact='john@nonfungibleconference.com · t.me/thejonnkarp')

SECTIONS = {"story": {"description": "NFC, the open-air museum and the On The Wall campaign.", "start": "cover"},
            "how": {"description": "Why take a wall, and how it happens.", "start": "why"},
            "flagship": {"description": "The offers, and Offer 01: the Flagship Mural.", "start": "offers"},
            "murals": {"description": "Offer 02: the Artist Murals.", "start": "murals"},
            "houses": {"description": "Offer 03: the Community Houses.", "start": "house"},
            "walls": {"description": "Offers 04 and 05: the PFP Wall and the Name Wall, and the contact.", "start": "pfp"}}

if __name__ == '__main__':
    render_html(d, 'sa_preview.html', X)
    print(len(d.slides), list(d.media))
