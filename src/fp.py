import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('fp', 'FAIR PLAY — the art show you can play')

cover(d, 'cover', 'px/factory-immersive.jpg', 'Lisbon · February — October 2027', 'FAIR PLAY',
      'An art exhibition you can play. Artists build the rides, AI runs inside.', 'By NFC Summit, the digital art festival of Lisbon',
      'FAIR PLAY is an art exhibition in the shape of a fairground. Artists build the rides, AI runs inside them, and every visitor leaves with an artwork. It opens at NFC Summit in Lisbon, 27 to 29 May 2027, and lives through the year until Devcon week in October.',
      'An immersive artwork in the Art Factory at NFC Summit 2026')
vstatement(d, 'lisbon', VID('place-totem-et-mur'), 'In 2027, Lisbon is the city of AI and creativity.', 'A museum show on AI, Devcon, Web Summit and NFC Summit, in one year.',
      'Why now and why here. In 2027 Lisbon hosts, in the same year: NFC Summit in May, the opening of the exhibition “Energies of AI” at MAAT in September, Devcon in October and Web Summit in November. The whole world of art, AI and technology walks through one city.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement(d, 'show', VID('mur-crane-pixel'), 'FAIR PLAY is its art show.', 'The one you can play.',
      'Museums will show the critical side of AI. FAIR PLAY shows the side where people put their hands on it: a gamified, joyful, AI-positive exhibition, for locals and for every crowd that comes to Lisbon in 2027.',
      'A giant pixel skull painted on a facade at the Unicorn Factory, filmed by drone')
rows = ''.join(f'<div class="row g32 rule" style="padding:26px 0;align-items:baseline"><h3 class="t t48" style="width:330px;flex:none">{t}</h3><p class="body">{s}</p></div>' for t, s in [
      ('An art exhibition', 'Curated. Every ride is a work by an artist.'),
      ('You can play', 'One minute per ride. AI turns your game into an artwork.'),
      ('For everyone', 'Locals, families and every crowd that visits Lisbon in 2027.'),
      ('All year', 'From February to October, with a premiere at NFC Summit.')])
statement_light(d, 'short', 'In short', 'What it is', rows,
      'The summary. FAIR PLAY is first an art exhibition, with a curator and artists. It is gamified: each work is a ride you play for a minute, and AI turns what you did into an artwork you take home. It is made for a wide public, not only for the art world. And it is a season, not a three-day stand.', 4)
timeline(d, 'year', 'Why Lisbon, why 2027', 'One city, one year', [
      ('27 — 29 May', 'NFC Summit, sixth edition: digital art and culture'),
      ('15 September', 'MAAT opens “Energies of AI”: Steyerl, Paglen, Crawford & Joler'),
      ('October', 'Devcon: the Ethereum world comes to Lisbon'),
      ('November', 'Web Summit')],
      'The calendar of the city in 2027. NFC Summit, 27 to 29 May, at the Unicorn Factory. MAAT, the Museum of Art, Architecture and Technology, opens “Energies of AI” on 15 September, curated by Antonio Somaini, with Hito Steyerl, Trevor Paglen, Kate Crawford and Vladan Joler. Devcon, the Ethereum developer conference, in October. Web Summit in November. FAIR PLAY runs through all of it.', 5,
      line='FAIR PLAY is the thread between them.')
pause_dragon(d, 'rule', 'art-fun-fair', 'The rule', 'Everyone leaves<br>with art.',
      'You always pay for an artwork, never for a chance. Every play gives a print. The target score gives an edition. The best score of the day takes the 1/1.', side='right', h=980)
rows = ''.join(f'<div class="row g32 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc">{n}</p><div class="col g8"><h3 class="t t48">{t}</h3><p class="small">{s}</p></div></div>' for n, t, s in [
      ('01', 'Pay', 'Tap a card or a phone. No app, no account.'), ('02', 'Play', 'Sixty to ninety seconds. A camera watches you.'),
      ('03', 'Generate', 'AI turns your face and your score into a piece in the artist’s world.'), ('04', 'Win', 'Everyone gets a print. Beat the target for an edition.')])
statement_light(d, 'how', 'How every ride works', '<span style="display:block;line-height:1">One minute,<br>one artwork</span>', rows,
      'Same four beats on every ride. Pay: tap a card or a phone. Play: sixty to ninety seconds, filmed. Generate: the partner’s model turns the player’s photo and performance into a piece in the artist’s style. Win: everyone gets a print, the target score gives an edition, the best score of the day a 1/1.', 7,
      sentence='You pay for an artwork, never for a chance.')
sig = [('The Oracle', 'Why do we trust a voice?'), ('The Wheel of Odds', 'Chance or prediction?'), ('The Two-Hand Claw', 'When do you delegate?'), ('The Hall of Doubles', 'What am I to a model?'),
       ('The Train of Layers', 'What happens inside?'), ('The Agents’ Arena', 'What is a fair rule?'), ('The Robot Portraitist', 'Who is the author?'), ('The Dance Mirror', 'Who leads, who follows?')]
cells = ''.join(f'<div class="col g12 rule-d" style="padding:24px 0 28px"><p class="lab mute">{i:02d}</p><h3 class="t t48">{t}</h3><p class="lab acc">{q}</p></div>' for i, (t, q) in enumerate(sig, 1))
d.add('rides', sec('rides', '', f'''<div class="col g24 in"><p class="lab acc">The fair</p><h2 class="t t120">Thirty machines, eight rides</h2>
<p class="lead">Ten photobooths, ten arcades, ten claws: one artist per machine. And eight signature rides that each ask a question.</p></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px">{cells}</div>
{d.foot(8)}''', 'Two families. The machines that make the crowd: about ten photobooths, ten arcade cabinets and ten claws, the same hardware with thirty different artists. And eight signature rides, each one a fairground classic turned into a question about how AI decides. The Oracle: three fortune-tellers, one finds your match, one tells your future, one shows, with your consent and on a private screen, what the web says about you. The Wheel of Odds: the AI calls the result before the spin. The Two-Hand Claw: you, the AI or the crowd at the controls. The Hall of Doubles: mirrors that each remake you differently. The Train of Layers: a dark ride through a model. The Agents’ Arena: agents under rules the crowd rewrites. The Robot Portraitist: a robot draws you. The Dance Mirror: a choreography to copy. Around them, the classics remade by artists: shooting gallery, paintball roll, knock-down, darts, the punch, duck pond, pixel wall, scratch wall.'))
pause_video(d, 'upclose', VID('art-factory-premier-etage'), 'Up close', 'Three<br>examples.',
      'Three machines, one after the other, to show what a visitor lives in one minute.', 'Artworks shown on the first floor of the Art Factory at NFC Summit 2026')
def example(sid, n, img, alt, k, title, lead, steps, leave, note):
    st = ''.join(f'<div class="row g32 rule" style="padding:22px 0;align-items:baseline"><p class="lab acc" style="width:44px;flex:none">{i:02d}</p><p class="body">{s}</p></div>' for i, s in enumerate(steps, 1))
    d.add(sid, sec(sid, '', f'''<img src="{d.m(img)}" alt="{alt}" style="position:absolute;left:0;top:0;width:840px;height:1080px;object-fit:cover">
<div class="col g24 in" style="margin-left:840px"><p class="lab acc">Example {k} of 3 · concept visual</p><h2 class="t t120">{title}</h2><p class="lead">{lead}</p></div>
<div class="col in2" style="margin-left:840px">{st}
<div class="row g32 rule" style="padding:22px 0;align-items:baseline"><p class="lab acc" style="width:44px;flex:none">→</p><p class="lead">{leave}</p></div></div>
{d.foot(n, start=936)}''', note))
example('ex-photobooth', 10, 'aff/at-photobooth.jpg', 'Concept visual: an artist photobooth, a wooden cabin wrapped in artwork', 1, 'The photobooth',
      'A wooden cabin, a curtain, an artist’s world.',
      ['You sit down and pull the curtain.', 'The camera takes your portrait.', 'The artist’s model remakes it in their style.'],
      'You leave with your portrait, printed.',
      'The simplest machine and the one everybody understands. The artist brings ten to twenty works that define a style; the model is tuned on them, with their agreement. One portrait in ten comes out as a rare edition.')
example('ex-arcade', 11, 'aff/at-arcade.jpg', 'Concept visual: an arcade cabinet wrapped in an artist’s work', 2, 'The arcade',
      'A cabinet in the artist’s colours, a 90-second game.',
      ['You play a short game designed with the artist.', 'Your score and your face go to the model.', 'It generates a piece that only this game could make.'],
      'You leave with the artwork your score made.',
      'Ten cabinets, ten artists, ten games. The score decides the artwork: a low score and a high score do not give the same piece. Beat the target score for an edition, top the board of the day for a 1/1.')
example('ex-claw', 12, 'aff/at-claw.jpg', 'Concept visual: a claw machine full of capsules, wrapped in an artist’s work', 3, 'The claw',
      'A real claw machine, presented as an installation.',
      ['You steer the claw over a sea of capsules.', 'Each capsule holds a work: a print, an object, an edition.', 'One capsule holds a unique piece.'],
      'You leave with what you caught.',
      'The claw is the most popular machine of any fair. Here every capsule is an artwork. In its signature version, the Two-Hand Claw, you can let the AI steer, or let the crowd vote, and compare the three success rates on the board.')
names = ['XCOPY', 'Dmitri Cherniak', 'Larva Labs', 'Jack Butcher', 'Kim Asendorf', 'Gretchen Andrew', 'Vhils', 'Hackatao', 'Botto', 'Efdot', 'Coldie', 'Operator']
nn = ' <span style="color:var(--yellow)">·</span> '.join(names)
d.add('artists', sec('artists', 'bottom', f'''{photo(d, 'px/expo-crowd.jpg', 'Visitors in an exhibition room at NFC Summit 2026')}
<div class="shade-dark"></div>
<div class="col g32 in" style="width:1728px">
<p class="lab acc">On the walls and screens of NFC Summit 2026</p>
<h2 class="t t120">The artists are already here</h2>
<p class="t t64" style="line-height:1.18">{nn}</p>
<p class="lead">The FAIR PLAY line-up is chosen by an independent curator, from this network and beyond.</p>
</div>
{d.foot(13)}''', 'FAIR PLAY grows out of a festival that already shows the artists who matter in digital art. In 2026 at NFC Summit: a three-screen LED installation of Dmitri Cherniak’s Ringers; the exhibition SYSTEMS, curated by Nina Roehrs and presented by Arab Bank Switzerland, with Kim Asendorf, Jack Butcher, Linda Dounia and Larva Labs; Gretchen Andrew won the ABS Digital Art Prize; a mural of XCOPY’s The Doomed; site-specific installations by Vhils; Efdot in an OpenSea container gallery; a Botto pop-up; Hackatao and Coldie on screen; Operator on stage. These names are the 2026 programme, not the FAIR PLAY line-up: that one is chosen by an independent curator. The partner does not choose the artists and does not review the works.'))
timeline(d, 'calendar', 'The season', 'A year of moments', [
      ('February', 'Online hackathon and art jams: anyone can prototype a ride'),
      ('March — May', 'Residencies: the artists build with the partner’s tools'),
      ('27 — 29 May', 'Premiere at NFC Summit, with the Hackathon · AI Day'),
      ('September', 'A panel and activations as MAAT opens “Energies of AI”'),
      ('October', 'Finale during Devcon week')],
      'February: an online hackathon and four art jams open the season; the best prototypes win a residency. March to May: eight to twelve projects built with the partner’s tools and engineers. 27 to 29 May: the fair opens on the central plaza of NFC Summit, with the Hackathon · AI Day on site. Summer: the fair travels across Lisbon. September: when MAAT opens its exhibition on AI, we host a panel and activations of our own. October: the finale, during Devcon week. Web Summit follows in November.', 14,
      line='In between, the fair travels across Lisbon. Web Summit follows in November.')
figures(d, 'who', PH('place-centrale-visiteuses'), 'Who is behind it', 'NFC Summit, sixth edition in 2027',
      [('2,740', 'Visitors in 2026'), ('79', 'Countries'), ('200+', 'Artists exhibited'), ('150+', 'Speakers'),
       ('1,000', 'Artists in the NFC network'), ('6M+', 'Organic impressions')],
      'NFC Summit is the digital art and culture festival of Lisbon, founded by John Karp, in its sixth edition in 2027. In 2026: 2,740 visitors from 79 countries, more than 200 artists exhibited, more than 150 speakers, 6M+ organic impressions, at the Unicorn Factory, a former flour mill. In 2026 OpenSea ran two container galleries and Arab Bank Switzerland presented the exhibition SYSTEMS. Around 1,000 artists in the network, many already fluent with AI.',
      'Visitors on the central plaza of the Unicorn Factory, NFC Summit 2026', 15, 'In 2026: container galleries by OpenSea, the exhibition SYSTEMS presented by Arab Bank Switzerland')
deal(d, 'partner', ['Your models inside the rides.', 'Your team in the residencies.', 'Your name on the season.'],
     [('The artists', 'A curated line-up, paid and credited.'), ('The fair', 'Machines, booths, staff, payment and printing.'), ('The audiences', 'Digital art in May, Lisbon all year, Ethereum and tech in the autumn.')],
     'For one founding partner. Your part: your models generate the artworks inside the rides, your engineers and artists take part in the hackathon and the residencies, your name signs the season. Our part: the artists, the production of the fair, and the audiences. Nothing is used to train a model without the written agreement of the artist.', 16, label='For a founding partner')
closing(d, 'close', 'FAIR PLAY · Lisbon 2027', 'Build a ride', ['A 20-minute call, then a proposal made for your team.'],
      'Next step: a 20-minute call with John, then a proposal.', contact='John Karp · john@nonfungibleconference.com · t.me/thejonnkarp')
SECTIONS = {"idea": {"description": "What FAIR PLAY is, and why Lisbon in 2027.", "start": "cover"},
            "rides": {"description": "How a ride works, the fair, and three examples up close.", "start": "rule"},
            "season": {"description": "The artists, the calendar, who is behind it and the partnership.", "start": "artists"},
            "close": {"description": "Contact.", "start": "close"}}
