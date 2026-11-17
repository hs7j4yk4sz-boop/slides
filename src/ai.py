import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('ai', 'NFC Residency 27 — for AI labs')

cover(d, 'cover', VID('art-factory-premier-etage'), 'NFC Summit 2027 · for AI labs', 'NFC Residency 27',
      'Put your model in the hands of the best artists of their generation.', '90 days online · 100 artists · an exhibition in Lisbon, 27 — 29 May 2027',
      'NFC Residency 27, presented by one AI lab. Ninety days online, from late February to 27 May 2027: one hundred artists from the NFC community create with the lab’s tools, with a weekly session. It ends with an exhibition during NFC Summit in Lisbon, prizes on the main stage, content and creators who talk about it.',
      'Artworks shown on the first floor of the Art Factory in 2026')
vstatement(d, 'demo', VID('mur-crane-pixel'), 'The best demo of a model is an artwork.', 'Made by an artist people already follow.',
      'What image, video and code labs already pay for elsewhere: artists who adopt their tool, and works that show what the tool can do. Higgsfield, Runway, Google, OpenAI all run artist programmes. NFC has both: artists who are already committed, and a stage in Lisbon to show the result.',
      'A giant pixel skull painted on a facade at the Unicorn Factory, filmed by drone')
vstatement(d, 'community', VID('place-totem-et-mur'), 'A community that pays to be here.', '325 patrons paid to be painted on our walls in seven weeks.',
      'You can buy ads and prizes. You cannot buy a community of artists who already know each other. 325 people paid to be painted on the Wall in seven weeks; around 1,000 artists in the NFC network, many already fluent with AI; 200+ artists exhibited in 2026.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
figures(d, 'assets', PH('place-centrale-visiteuses'), 'What NFC brings', 'Artists, a stage, an audience',
      [('1,000', 'Artists in the NFC network'), ('325', 'Patrons on the Wall'), ('200+', 'Artists exhibited in 2026'), ('2,740', 'Visitors in 2026'),
       ('79', 'Countries'), ('6M+', 'Organic impressions'), ('32', 'People of the Wall podcast episodes')],
      'Artists already committed, not free sign-ups. A public ending in Lisbon: 2,740 visitors from 79 countries in 2026, a four-floor Art Factory to exhibit, a main stage for the awards. Our own media: People of the Wall (32 episodes), NFT Morning (the first French-language NFT podcast, close to 1,000 episodes), 6M+ organic impressions in 2026. Collectors: the NFC audience buys digital art, so residency works can sell. Europe: most of these programmes happen in New York, Los Angeles or Seoul; Lisbon in May is a ready-made European date.',
      'Visitors on the central plaza of the Unicorn Factory, NFC Summit 2026', 4, 'Source: NFC Summit 2026 final report and On The Wall season 1')
pause_dragon(d, 'pause', 'hackathon-ai-day', 'NFC Residency 27', 'Ninety days.<br>One exhibition.',
      'A pause before the programme. One lab, one hundred artists, three months online, three days in Lisbon.', side='right', h=980)
timeline(d, 'how', 'The residency', 'Ninety days, then Lisbon', [
      ('February', 'Open call: 100 artists from the Wall and the NFC network'),
      ('Every week', 'One live session: a masterclass by your team, peer critique'),
      ('Every month', 'An open studio, live. Three submissions in all'),
      ('27 — 29 May', 'The exhibition at NFC, prizes on the main stage, editions for sale')],
      'Format: 90 days online, from late February to 27 May. 100 artists selected from the Wall and the NFC network, on application, never by default. Rhythm: one online session a week (a masterclass by an engineer or an artist of the lab, peer critique), a live open studio every month, three submissions. The end: a selection of 20 to 30 works shown during NFC on a floor of the Art Factory in the lab’s name, prizes on the main stage, editions for sale.', 6,
      line='Selected on application. The artists keep their rights.')
rows = ''.join(f'<div class="row g32 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc">{n}</p><h3 class="t t48">{t}</h3></div>' for n, t in [
      ('01', '100 artists trained on your tool'), ('02', 'Hundreds of signed works'), ('03', 'A licence to use them in your marketing'),
      ('04', 'Structured product feedback'), ('05', 'A floor of the Art Factory in your name'), ('06', 'A keynote on the main stage')])
statement_light(d, 'getback', 'What your lab gets', 'Adoption you can show', rows,
      'What the lab gets back: 100 artists trained on its tool, hundreds of signed works, a licence to reuse them in marketing (limited to promoting the programme), structured product feedback, a keynote. Nothing is used to train a model without the written agreement of the artist.', 7,
      sentence='Not a logo on a wall. Proof, made by artists.')
world(d, 'noise', PH('scene-speakeuse'), 'The noise', 'Three months of stories.', 'One podcast episode a month, ten creators who make and tell, a live at every submission.',
      'Media and influence: one People of the Wall episode a month, 10 creator-influencers who create during the programme and tell the story, a live at every submission, then the exhibition and the awards in Lisbon.',
      'A speaker on the main stage of NFC Summit 2026', 8)
value_offer(d, 'residency', 'NFC Residency 27 · presented by your lab', 'One lab. One residency.', '90 days online, then the exhibition at NFC Summit, 27 — 29 May 2027',
      [('100', 'artists', 'Selected from the Wall and the NFC network, on application'), ('90', 'days', 'Weekly sessions, monthly open studios, three submissions'),
       ('€30K', 'to artists', '20 grants of €1,000 and €10,000 in prizes'), ('1', 'floor', 'Of the Art Factory, in your name, for the exhibition')],
      '€90,000', 'Platinum · 1 lab',
      'Where the €90,000 goes, roughly: €30,000 to the artists (20 grants of €1,000 and €10,000 in prizes), about €15,000 of exhibition production, about €10,000 of media and influence, the rest for NFC (one full-time person for three months to run the programme, the platform, curation). Exclusive: one lab only. 50% at signature. Must be signed before the end of January, or the open call cannot go out in time.',
      cta='Signed before 31 January →')
pause_video(d, 'more', VID('art-factory-rez-de-chaussee'), 'Not a residency?', 'Four more<br>ways in.',
      'For labs that do not take the residency: a hackathon, the engine of the fair, a model launch, an academy.', 'The flour mill machines of the Art Factory at NFC Summit 2026')
fmts = [('02', 'Build the fair', 'Online hackathon', 'Artist and developer teams build the games of the Art Fun Fair with your model or API. The winners run in the fair for three days.'),
        ('03', 'Powered by', 'The engine of the fair', 'Every machine turns the player’s photo and score into a printed artwork, generated by your model.'),
        ('04', 'Model launch', 'On the main stage', 'Announce or demo a new model at NFC: keynote, demo in the Art Factory, a 48-hour sprint with the artists.'),
        ('05', 'Academy', 'For 1,000 artists', 'Four online masterclasses, recorded, with a “Certified artist” badge. Or a squad of 10 creators for three months.')]
cells = ''.join(f'<div class="col g16 rule-d" style="padding-top:28px"><p class="lab mute">{n}</p><h3 class="t t64">{t}</h3><p class="lab acc">{s}</p><p class="body mute">{b}</p></div>' for n, t, s, b in fmts)
d.add('formats', sec('formats', '', f'''<div class="col g24 in"><p class="lab acc">One lab per format</p><h2 class="t t120">Four more formats</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px">{cells}</div>
{d.foot(11)}''', 'One principle for every format: put the lab’s tool in the hands of the best artists of the community, and end with public proof at NFC. One lab per format, so exclusivity means something. Build the fair: six to eight weeks before NFC; the final runs during the Hackathon · AI Day at Escola 42, on site; the ideal format for a code lab. Powered by: “Powered by” on every machine and print, a demo screen, generation figures shared after the event; one category per lab (image, video, sound). Model launch: May is a release season; can be sold alone or as an option of the residency. Academy: four masterclasses for the 1,000 artists of the network. Creator squad: 10 to 20 NFC artist-influencers who create with the tool for three months and post on a fixed calendar, plus two podcast episodes.'))
value_offer(d, 'founding', 'Founding lab · the whole programme', 'Own the season.', 'The residency, the hackathon and the engine of the fair, for one lab',
      [('100', 'artists', 'The residency, 90 days online'), ('1', 'hackathon', 'Build the fair, presented by you'),
       ('1', 'engine', 'Every print of the fair, generated by your model'), ('€45K', 'to artists', 'Grants and prizes')],
      '€150,000', 'Platinum · 1 lab',
      'Founding lab: residency + hackathon + fair engine, one lab only. €45,000 goes to the artists as grants and prizes. Platinum perks: category exclusivity, a talk on the main stage, 20 three-day passes, 8 VIP passes. 50% at signature.',
      cta='Talk to John first →')
prices = [('Founding lab', 'Residency + hackathon + fair engine', '1 lab', 'Platinum', '€150,000'),
          ('NFC Residency 27', '100 artists, 90 days, the exhibition', '1 lab', 'Platinum', '€90,000'),
          ('Build the fair', 'Online hackathon, final on site', '1 lab', 'Platinum', '€50,000'),
          ('Powered by', 'The engine of the fair', '1 per category', 'Platinum', '€40,000'),
          ('Model launch', 'Keynote, demo, 48-hour sprint', '1 per day', 'Platinum', '€35,000'),
          ('Tool partner', 'Of the residency or the hackathon', '3 max', 'Gold', '€25,000'),
          ('Academy', '4 masterclasses, 1,000 artists', '1 lab', 'Gold', '€20,000'),
          ('Creator squad', '10 creators, 3 months', 'Open', 'Silver', '€15,000')]
pr = ''.join(f'''<div style="display:grid;grid-template-columns:420px 1fr 240px 200px 260px;column-gap:24px;align-items:baseline;padding:16px 0;border-top:1px solid rgba(14,42,110,0.28)">
<h3 class="t t48" style="color:var(--ink)">{a}</h3><p class="body">{b}</p><p class="body">{c}</p><p class="lab">{e}</p><p class="t t48" style="color:var(--ink);text-align:right">{p}</p></div>''' for a, b, c, e, p in prices)
d.add('prices', sec('prices', 'yellow', f'''<div class="col g16 in" style="color:var(--ink)"><p class="lab">Every format · excl. VAT</p><h2 class="t t120" style="color:var(--ink)">The price list</h2></div>
<div class="col in2" style="color:var(--ink)">{pr}</div>
{d.foot(13)}''', 'Anchor high, show where the money goes, one lab per format. Labs do not compare NFC with €3,000 stands; they compare it with their own six- or seven-figure festivals. Model launch: €20,000 as an option of the residency. Tool partner: a €5,000 “Best use of your tool” prize. Creator squad: €5,000 shared between the creators. Early-bird until 31 December like the rest of the catalogue, 50% at signature.', ' style="justify-content:flex-start;gap:40px"'))
timeline(d, 'calendar', 'The calendar', 'Signed by 31 January', [
      ('December', 'Proposals to two or three labs'), ('31 January', 'The residency is signed'), ('February', 'The open call goes out'),
      ('March — May', 'Ninety days online'), ('27 — 29 May', 'The exhibition at NFC')],
      'Everything is decided before the end of January: without a lab signed by then, the open call cannot go out in time and the residency moves to 2028. The hackathon, shorter, can still be signed until the end of February. The academy, the creator squad and the fair engine can sell until April.', 14,
      line='The residency has one seat. The hackathon can wait until February.')
d.add('contact', sec('contact', 'bottom', f'''<img class="bg" src="{d.m('px/expo-crowd.jpg')}" data-video="{d.m(VID('expo-art-factory-etage') + '.mp4')}" alt="Visitors in an exhibition room at NFC Summit 2026">
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g32 in" style="width:1400px">
<p class="lab acc">NFC Residency 27 · NFC Summit 2027</p>
<h2 class="t t150">Talk to John</h2>
<div class="col g12"><p class="lead">John Karp</p><p class="lab">john@nonfungibleconference.com · t.me/thejonnkarp</p></div>
</div>
{d.foot(15)}''', 'Next step: a 20-minute call, then a proposal for your lab, with your format first and the Founding lab as an option.'))
SECTIONS = {"why": {"description": "Why an AI lab works with NFC artists.", "start": "cover"},
            "residency": {"description": "The residency: format, what the lab gets, the noise, the offer.", "start": "pause"},
            "formats": {"description": "Four more formats, the founding lab and the price list.", "start": "more"},
            "next": {"description": "The calendar and the contact.", "start": "calendar"}}
