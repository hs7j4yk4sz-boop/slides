import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('fp', 'FAIR PLAY — the art show you can play')

cover(d, 'cover', VID('art-factory-a'), 'Lisbon · February — October 2027', 'FAIR PLAY',
      'An art exhibition you can play. Artists build the rides, AI runs inside.', 'By NFC Summit, the digital art festival of Lisbon',
      'FAIR PLAY is an art exhibition in the shape of a fairground. Artists build the rides, AI runs inside them, and every visitor leaves with an artwork. It opens at NFC Summit in Lisbon, 27 to 29 May 2027, and lives through the year until Devcon week in October. The footage is the Art Factory at NFC Summit 2026.',
      'A visitor in front of an immersive artwork in the Art Factory at NFC Summit 2026')
vstatement(d, 'lisbon', VID('place-totem-et-mur'), 'In 2027, Lisbon is the city of AI and creativity.', 'A museum show on AI, Devcon, Web Summit and NFC Summit, in one year.',
      'Why now and why here. In 2027 Lisbon hosts, in the same year: NFC Summit in May, the opening of the exhibition “Energies of AI” at MAAT in September, Devcon in October and Web Summit in November. The whole world of art, AI and technology walks through one city.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement(d, 'show', VID('art-factory-b'), 'FAIR PLAY is its art show.', 'The one you can play.',
      'Museums will show the critical side of AI. FAIR PLAY shows the side where people put their hands on it: a gamified, joyful, AI-positive exhibition, for locals and for every crowd that comes to Lisbon in 2027.',
      'Three artworks on screens in the Art Factory at NFC Summit 2026')
rows = ''.join(f'<div class="row g32 rule" style="padding:26px 0;align-items:baseline"><h3 class="t t48" style="width:330px;flex:none">{t}</h3><p class="body">{s}</p></div>' for t, s in [
      ('An art exhibition', 'Curated. Every ride is a work by an artist.'),
      ('You can play', 'One minute per ride. AI turns your game into an artwork.'),
      ('For everyone', 'Locals, families and every crowd that visits Lisbon in 2027.'),
      ('All year', 'From February to October, with a premiere at NFC Summit.')])
statement_light(d, 'short', 'In short', 'What it is', rows,
      'The summary. FAIR PLAY is first an art exhibition, with a curator and artists. It is gamified: each work is a ride you play for a minute, and AI turns what you did into an artwork you take home. It is made for a wide public, not only for the art world. And it is a season, not a three-day stand.', 4)
timeline(d, 'year', 'Why Lisbon, why 2027', 'One city, one year', [
      ('February', 'Online hackathon and art jams open the season'),
      ('27 — 29 May', 'Premiere at NFC Summit, with the Hackathon · AI Day'),
      ('15 September', 'MAAT opens “Energies of AI”. We host a panel and activations'),
      ('12 — 14 October', 'Devcon, at the Lisbon Congress Centre. Our finale'),
      ('8 — 11 November', 'Web Summit')],
      'One calendar for the city and for FAIR PLAY. February: an online hackathon and four art jams open the season; the best prototypes win a residency. March to May: residencies, eight to twelve projects built with the partner’s tools. 27 to 29 May: the fair opens on the central plaza of NFC Summit, at the Unicorn Factory, with the Hackathon · AI Day on site. Summer: the fair travels across Lisbon. 15 September: MAAT, the Museum of Art, Architecture and Technology, opens “Energies of AI”, curated by Antonio Somaini, with Hito Steyerl, Trevor Paglen, Kate Crawford and Vladan Joler; we host a panel and activations of our own that week. 12 to 14 October: Devcon IX, at the Lisbon Congress Centre, and our finale that week. 8 to 11 November: Web Summit.', 5,
      line='Residencies from March to May. The fair travels across Lisbon all summer.')
pause_video(d, 'rule', VID('art-factory-c'), 'The rule', 'Everyone leaves<br>with art.',
      'You always pay for an artwork, never for a chance. Every play gives a print. The target score gives an edition. The best score of the day takes the 1/1.', 'An artwork on a screen set into a flour mill machine in the Art Factory at NFC Summit 2026')
rows = ''.join(f'<div class="row g32 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc">{n}</p><div class="col g8"><h3 class="t t48">{t}</h3><p class="small">{s}</p></div></div>' for n, t, s in [
      ('01', 'Pay', 'Tap a card or a phone. No app, no account.'), ('02', 'Play', 'Sixty to ninety seconds. A camera watches you.'),
      ('03', 'Generate', 'AI turns your face and your score into a piece in the artist’s world.'), ('04', 'Win', 'Everyone gets a print. Beat the target for an edition.')])
statement_light(d, 'how', 'How every ride works', '<span style="display:block;line-height:1">One minute,<br>one artwork</span>', rows,
      'Same four beats on every ride. Pay: tap a card or a phone. Play: sixty to ninety seconds, filmed. Generate: the partner’s model turns the player’s photo and performance into a piece in the artist’s style. Win: everyone gets a print, the target score gives an edition, the best score of the day a 1/1.', 7,
      sentence='You pay for an artwork, never for a chance.')
mach = [('fp/photobooth.jpg', 'Concept visual: an Art Deco photobooth wrapped in an abstract artwork, a visitor stepping in', 'Ten photobooths', 'You sit down. The artist’s model remakes your portrait.'),
        ('fp/arcade.jpg', 'Concept visual: an Art Deco arcade cabinet wrapped in an abstract artwork, a player at the joystick', 'Ten arcades', 'You play for 90 seconds. Your score generates your artwork.')]
mm = ''.join(f'<div class="col g16"><img src="{d.m(k)}" alt="{a}" style="width:100%;height:400px;object-fit:cover;object-position:88% 50%"><h3 class="t t64">{t}</h3><p class="body mute">{s}</p></div>' for k, a, t, s in mach)
d.add('machines', sec('machines', '', f'''<div class="col g24 in"><p class="lab acc">The machines that make the crowd · concept visuals</p><h2 class="t t120">One artist per machine</h2>
<p class="lead">The same booth, a different world each time. Then claws, shooting galleries, a paintball roll, darts.</p></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(2, 1fr);column-gap:48px">{mm}</div>
{d.foot(8)}''', 'The crowd comes for simple machines, made in series, one artist per machine: about ten photobooths and ten arcade cabinets to start with, then ten claws. Same hardware, a different artist’s world each time. Photobooth: the artist brings ten to twenty works that define a style; the model is tuned on them, with their agreement; your portrait comes out in that style. Arcade: a short game designed with the artist; the score decides the artwork, generated on the spot. Around them, the classics remade by artists: claws full of capsules, shooting galleries where the piece mixes your score and a capture of the moment, a paintball roll, darts, a knock-down, a pixel wall.'))
sig = [('The Oracle', 'Why do we trust a voice?', 'A fortune-teller that shows how it thinks.'),
       ('The Hall of Doubles', 'What am I to a model?', 'Every mirror remakes you differently.'),
       ('The Wheel of Odds', 'Chance or prediction?', 'The AI calls the result. You bet with it or against it.'),
       ('The Robot Portraitist', 'Who is the author?', 'A robot looks at you and draws.')]
sg = ''.join(f'<div class="row g32 rule" style="padding:18px 0;align-items:baseline"><h3 class="t t48" style="width:400px;flex:none">{t}</h3><div class="col g8"><p class="lab acc">{q}</p><p class="small">{b}</p></div></div>' for t, q, b in sig)
d.add('rides', sec('rides', '', f'''{photo(d, 'fp/oracle.jpg', 'Concept visual: an Art Deco fortune-teller booth with a glowing generative screen, a visitor at the handle')}
<div class="shade-l"></div>
<div class="col g24 in" style="width:1000px"><p class="lab acc">Signature rides · concept visual</p><h2 class="t t120">Play the question</h2></div>
<div class="col in2" style="width:900px;margin-top:28px">{sg}
<p class="small mute rule" style="padding-top:18px">And the Two-Hand Claw, the Agents’ Arena, the Train of Layers…</p></div>
{d.foot(9)}''', 'Next to the machines, the signature rides: each takes a fairground classic and turns it into a question about how AI decides. The Oracle comes in three characters: a slightly scary fortune-teller who asks you questions and names your best match; one who tells your future from nothing; and one who, with your consent and on a private screen, shows what the public web says about you from your name alone. The Hall of Doubles: a corridor of mirrors, each one a different model’s idea of you. The Wheel of Odds: the model announces its prediction before each spin; bets are in points, never money. The Robot Portraitist: a drawing robot on the path of the fair. Also in development: the Two-Hand Claw (you, the AI or the crowd at the controls), the Train of Layers (a dark ride through a model, in a shipping container), the Agents’ Arena (agents under rules the crowd rewrites) and the Dance Mirror (a choreography to copy).'))
pause_video(d, 'builders', VID('art-factory-d'), 'Who builds it', 'The artists.',
      'Three slides on the artists: who already shows at NFC, who we want to build the signature rides with, and who could sign the machines.', 'A generative artwork on a tall LED screen in the Art Factory at NFC Summit 2026')
names = ['XCOPY', 'Dmitri Cherniak', 'Larva Labs', 'Jack Butcher', 'Kim Asendorf', 'Gretchen Andrew', 'Vhils', 'Hackatao', 'Botto', 'Efdot', 'Coldie', 'Operator']
nn = ' <span style="color:var(--yellow)">·</span> '.join(names)
d.add('artists', sec('artists', 'bottom', f'''{photo(d, PH('art-factory-vhils-boldtron'), 'A visitor at an artwork on a screen set into a flour mill machine, installation by Vhils and BOLDTRON at NFC Summit 2026. Photo: Guillermo Vidal')}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g32 in" style="width:1728px">
<p class="lab acc">On the walls and screens of NFC Summit 2026</p>
<h2 class="t t120">The artists are already here</h2>
<p class="t t64" style="line-height:1.18">{nn}</p>
<p class="lead">More than 200 artists exhibited in 2026, in a four-floor Art Factory.</p>
</div>
{d.foot(11, 'Photo: Guillermo Vidal · installation by Vhils and BOLDTRON, NFC Summit 2026')}''', 'FAIR PLAY grows out of a festival that already shows the artists who matter in digital art. In 2026 at NFC Summit: a three-screen LED installation of Dmitri Cherniak’s Ringers; the exhibition SYSTEMS, curated by Nina Roehrs and presented by Arab Bank Switzerland, with Kim Asendorf, Jack Butcher, Linda Dounia and Larva Labs; Gretchen Andrew won the ABS Digital Art Prize; a mural of XCOPY’s The Doomed; site-specific installations by Vhils and BOLDTRON; Efdot in an OpenSea container gallery; a Botto pop-up; Hackatao and Coldie on screen; Operator on stage. These names are the 2026 programme.'))
six = [('Sasha Stiles', 'The Oracle', 'A poet who writes with AI.'),
       ('Patrick Tresset', 'The Robot Portraitist', 'His robots draw the people who sit for them.'),
       ('Trevor Paglen', 'The Hall of Doubles', 'He shows what machines see. Also in MAAT’s show.'),
       ('Botto', 'The Agents’ Arena', 'An AI artist governed by the votes of its community.'),
       ('Dmitri Cherniak', 'The Two-Hand Claw', 'Automation as an artistic medium.'),
       ('Gretchen Andrew', 'The Wheel of Odds', 'ABS Digital Art Prize 2026, at NFC Summit.')]
sx = ''.join(f'<div class="col g12 rule-d" style="padding:24px 0 28px"><h3 class="t t64">{a}</h3><p class="lab acc">{r}</p><p class="body mute">{b}</p></div>' for a, r, b in six)
d.add('six', sec('six', '', f'''<div class="col g24 in"><p class="lab acc">First ideas · the artists we want to build with</p><h2 class="t t120">Six artists, six rides</h2></div>
<div class="col g24 in2"><div style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{sx}</div>
<p class="small mute">A wish list, not a line-up. Conversations start in December, and the curator has the last word.</p></div>
{d.foot(12)}''', 'Our first ideas for the signature rides: who we want to work with, and on what. Sasha Stiles, poet and AI researcher, for the Oracle. Patrick Tresset, whose robots draw portraits, for the Robot Portraitist. Trevor Paglen, whose work shows what machines see and who is part of MAAT’s “Energies of AI”, for the Hall of Doubles. Botto, the AI artist governed by a community, for the Agents’ Arena. Dmitri Cherniak, whose Ringers were shown on LED at NFC Summit 2026, for the Two-Hand Claw. Gretchen Andrew, winner of the ABS Digital Art Prize 2026 at NFC Summit, for the Wheel of Odds. This is a wish list: none of them has been asked yet, and the independent curator has the last word.'))
cols = [('Photobooths', ['Mr Richi', 'Efdot', 'Coldie', 'Emi Kusano', 'Amrit Pal Singh', 'Kim Asendorf']),
        ('Arcades', ['Polygon1993', 'Cypherdudes', 'DeafBeef', 'Nicolas Sassoon', 'Bryan Brinkman', 'Zach Lieberman', 'Snowfro']),
        ('Claws, shooting galleries and more', ['Hackatao', 'Karmic', 'Tschuuuly', 'die with the most likes', 'Mad Dog Jones', 'Trevor Jones', 'Operator', 'beeple'])]
cc = ''.join(f'<div class="col g16 rule-d" style="padding-top:24px"><p class="lab acc">{h}</p><div class="col">{"".join(f"<p class=\'t t48\' style=\'line-height:1.22\'>{x}</p>" for x in xs)}</div></div>' for h, xs in cols)
d.add('thirty', sec('thirty', '', f'''<div class="col g24 in"><p class="lab acc">From the NFC network · wish list</p><h2 class="t t120">And thirty machines to sign</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px;align-items:start">{cc}</div>
{d.foot(13)}''', 'The machines are signed one by one by artists of the NFC network. These are the artists we want to invite, sorted by the machine we imagine for each. Most of them have shown, spoken or collected at NFC Summit. It is a wish list: the final line-up is the curator’s.'))
vstatement_figs(d, 'who', VID('mur-crane-pixel'), 'Who is behind it', 'NFC Summit', 'The digital art and culture festival of Lisbon. Sixth edition in 2027.',
      [('2,740', 'Visitors in 2026'), ('79', 'Countries'), ('200+', 'Artists exhibited'), ('150+', 'Speakers'), ('6M+', 'Organic impressions')],
      'NFC Summit is the digital art and culture festival of Lisbon, founded by John Karp, in its sixth edition in 2027. In 2026: 2,740 visitors from 79 countries, more than 200 artists exhibited, more than 150 speakers, 6M+ organic impressions, at the Unicorn Factory, a former flour mill. In 2026 OpenSea ran two container galleries and Arab Bank Switzerland presented the exhibition SYSTEMS. Around 1,000 artists in the network, many already fluent with AI. Source: NFC Summit 2026 final report.',
      'A giant pixel skull painted on a facade at the Unicorn Factory, filmed by drone')
deal(d, 'partner', ['Your models inside the rides.', 'Your team in the residencies.', 'Your name on the season.'],
     [('The artists', 'A curated line-up, paid and credited.'), ('The fair', 'Machines, booths, staff, payment and printing.'), ('The audiences', 'Digital art in May, Lisbon all year, Ethereum and tech in the autumn.')],
     'For one founding partner. Your part: your models generate the artworks inside the rides, your engineers and artists take part in the hackathon and the residencies, your name signs the season. Our part: the artists, the production of the fair, and the audiences. An independent curator chooses the artists; the partner does not choose them and does not review the works. Nothing is used to train a model without the written agreement of the artist.', 15, label='For a founding partner')
closing(d, 'close', 'FAIR PLAY · Lisbon 2027', 'Build a ride', ['A 20-minute call, then a proposal made for your team.'],
      'Next step: a 20-minute call with John, then a proposal.', contact='John Karp · john@nonfungibleconference.com · t.me/thejonnkarp')
SECTIONS = {"idea": {"description": "What FAIR PLAY is, and why Lisbon in 2027.", "start": "cover"},
            "rides": {"description": "How a ride works, the machines and the signature rides.", "start": "rule"},
            "artists": {"description": "The artists of NFC, six first ideas and the wish list.", "start": "builders"},
            "partner": {"description": "Who is behind it, the partnership and the contact.", "start": "who"}}
