import sys; sys.path.insert(0, '.')
from nfclib import *
# FAIR PLAY: the season deck, one version for every partner.
TOOLS = 'the partner’s tools'
MODEL = 'the partner’s model'
d = Deck('fp', 'FAIR PLAY — the art show you can play')


cover(d, 'cover', VID('art-factory-a'), 'Lisbon · 2027', 'FAIR PLAY',
      'An art fairground that runs on AI. Artists build the rides, you play, you leave with art.', 'By NFC Summit, the digital art festival of Lisbon',
      'FAIR PLAY is an art exhibition in the shape of a fairground, in the line of Calder’s Circus, Tinguely’s drawing machines and Luna Luna, with the machines of our time: AI. Artists build the rides, AI runs inside them, and every visitor leaves with an artwork. It starts online in January 2027, opens at NFC Summit in Lisbon, 27 to 29 May, and lives through the year until Devcon week in October. The footage is the Art Factory at NFC Summit 2026.',
      'A visitor in front of an immersive artwork in the Art Factory at NFC Summit 2026')
vstatement(d, 'lisbon', VID('place-totem-et-mur'), 'In 2027, Lisbon is the city of AI and creativity.', 'A museum show on AI, Devcon, Web Summit and NFC Summit, in one year.',
      'Why now and why here. In 2027 Lisbon hosts, in the same year: NFC Summit in May, the opening of the exhibition “Energies of AI” at MAAT in September, Devcon in October and Web Summit in November. The whole world of art, AI and technology walks through one city.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement(d, 'show', VID('art-factory-b'), 'FAIR PLAY is its art show.', 'The one you can play.',
      'Most exhibitions about AI ask the public to look, and to worry. FAIR PLAY asks you to play: a joyful, optimistic exhibition where people put their hands on the machines, for locals and for every crowd that comes to Lisbon in 2027.',
      'Three artworks on screens in the Art Factory at NFC Summit 2026')
firsts = [('1926', 'Calder’s Circus', 'Paris. A miniature fair, performed by the artist himself.', ''),
          ('1959', 'Tinguely’s machines', 'Paris. Machines that draw. Visitors made 4,000 drawings.', ''),
          ('1968', 'Cybernetic Serendipity', 'London. Art made with computers. The public plays with it.', ''),
          ('1987', 'Luna Luna', 'Hamburg. Haring’s carousel, Basquiat’s Ferris wheel, Dalí’s pavilion.', ''),
          ('2027', 'FAIR PLAY', 'Lisbon. The same fair, with the machines of our time.', ' acc')]
ff = ''.join(f'<div class="col g16"><div class="bar"></div><p class="t t112{c}">{y}</p><h3 class="t t48{c}" style="line-height:1.08;min-height:104px">{n}</h3><p class="body">{b}</p></div>' for y, n, b, c in firsts)
d.add('first', sec('first', '', f"""<div class="col g24 in"><p class="lab acc">Our family in art history</p><h2 class="t t120">Artists have always played</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(5, 1fr);column-gap:48px">{ff}</div>
<p class="lead">FAIR PLAY is the next chapter: art about machines, made with machines, for everyone.</p>
{d.foot(4)}""",
      'FAIR PLAY belongs to a family, and we say so. 1926: Alexander Calder builds his Circus in Paris, a miniature fair he performs himself; it is now at the Whitney Museum. 1959: Jean Tinguely shows his Méta-Matics at Galerie Iris Clert in Paris, machines that draw; visitors make about 4,000 drawings, with a prize judged by Hans Arp, Yves Klein and Pierre Restany. 1961: Niki de Saint Phalle turns the shooting gallery into painting with her Tirs, and lets the public shoot. 1968: Cybernetic Serendipity, at the ICA in London, curated by Jasia Reichardt, the first large exhibition of art made with computers, with Tinguely’s painting machines and Nam June Paik’s robot; a joyful show where visitors left with drawings made by machines. 1987: Luna Luna, in Hamburg, by André Heller, the first art amusement park, with a carousel by Keith Haring, a Ferris wheel by Jean-Michel Basquiat, a pavilion by Salvador Dalí and works by Hockney, Lichtenstein, Delaunay and Tinguely again; restored and shown in Los Angeles in 2023 and New York in 2024. 2015: Banksy’s Dismaland, the dark version of the fair. 2026: Dataland opens in Los Angeles as the first museum of AI art, with Google Arts &amp; Culture among its partners. FAIR PLAY is the next chapter and the optimistic one: the same fair, with the machines of our time. For the press: to our knowledge, it is the first art fairground that runs on AI. Sources: Whitney Museum; Wikipedia (Métamatic, Cybernetic Serendipity, Luna Luna); Smithsonian Magazine; The Art Newspaper, 18 June 2026.'))
rows = ''.join(f'<div class="row g32 rule" style="padding:26px 0;align-items:baseline"><h3 class="t t48" style="width:330px;flex:none">{t}</h3><p class="body">{s}</p></div>' for t, s in [
      ('An art exhibition', 'Curated. Every ride is a work by an artist.'),
      ('You can play', 'One minute per ride. AI turns your game into an artwork.'),
      ('For everyone', 'Locals, families and every crowd that visits Lisbon in 2027.'),
      ('All year', 'Online from January. In Lisbon from May to October.')])
statement_light(d, 'short', 'In short', 'What it is', rows,
      'The summary. FAIR PLAY is first an art exhibition, with a curator and artists. It is gamified: each work is a ride you play for a minute, and AI turns what you did into an artwork you take home. It is made for a wide public, not only for the art world. And it is a season, not a three-day stand: it starts online in January with workshops, opens in Lisbon in May and ends in Devcon week in October.', 5)
timeline(d, 'year', 'Why Lisbon, why 2027', 'One city, one year', [
      ('From January', 'Online workshops, art jams and a hackathon open the season'),
      ('27 — 29 May', 'Premiere at NFC Summit, with the Hackathon · AI Day'),
      ('15 September', 'MAAT opens “Energies of AI”. We host a panel and activations'),
      ('12 — 14 October', 'Devcon, at the Lisbon Congress Centre. Our finale'),
      ('8 — 11 November', 'Web Summit')],
      f'One calendar for the city and for FAIR PLAY. From January: monthly online workshops and initiations, four art jams, and an online hackathon in February; the best prototypes win a residency. March to May: residencies, eight to twelve projects built with {TOOLS}. 27 to 29 May: the fair opens on the central plaza of NFC Summit, at the Unicorn Factory, with the Hackathon · AI Day on site. Summer: the fair travels across Lisbon. 15 September: MAAT, the Museum of Art, Architecture and Technology, opens “Energies of AI”, curated by Antonio Somaini, with Hito Steyerl, Trevor Paglen, Kate Crawford and Vladan Joler; we host a panel and activations of our own that week. 12 to 14 October: Devcon IX, at the Lisbon Congress Centre, and our finale that week. 8 to 11 November: Web Summit.', 5,
      line='Residencies from March to May. The fair travels across Lisbon all summer.')
pause_video(d, 'rule', VID('art-factory-c'), 'The rule', 'Everyone leaves<br>with art.',
      'You always pay for an artwork, never for a chance. Every play gives a print. The target score gives an edition. The best score of the day takes the 1/1.', 'An artwork on a screen set into a flour mill machine in the Art Factory at NFC Summit 2026')
rows = ''.join(f'<div class="row g32 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc">{n}</p><div class="col g8"><h3 class="t t48">{t}</h3><p class="small">{s}</p></div></div>' for n, t, s in [
      ('01', 'Pay', 'Tap a card or a phone. No app, no account.'), ('02', 'Play', 'Sixty to ninety seconds. A camera watches you.'),
      ('03', 'Generate', 'AI turns your face and your score into a piece in the artist’s world.'), ('04', 'Win', 'Everyone gets a print. Beat the target for an edition.')])
statement_light(d, 'how', 'How every ride works', '<span style="display:block;line-height:1">One minute,<br>one artwork</span>', rows,
      f'Same four beats on every ride. Pay: tap a card or a phone. Play: sixty to ninety seconds, filmed. Generate: {MODEL} turns the player’s photo and performance into a piece in the artist’s style. Win: everyone gets a print, the target score gives an edition, the best score of the day a 1/1.', 7,
      sentence='You pay for an artwork, never for a chance.')
mach = [('fp/photobooth.jpg', 'Concept visual: two friends laughing at their printed portraits in front of an Art Deco photobooth wrapped in an abstract artwork', 'Ten photobooths', 'You sit down. The artist’s model remakes your portrait.'),
        ('fp/arcade.jpg', 'Concept visual: a teenager playing at an Art Deco arcade cabinet wrapped in an abstract artwork, his father watching', 'Ten arcades', 'You play for 90 seconds. Your score generates your artwork.')]
mm = ''.join(f'<div class="col g16"><img src="{d.m(k)}" alt="{a}" style="width:100%;height:400px;object-fit:cover;object-position:88% 50%"><h3 class="t t64">{t}</h3><p class="body mute">{s}</p></div>' for k, a, t, s in mach)
d.add('machines', sec('machines', '', f'''<div class="col g24 in"><p class="lab acc">The machines that make the crowd · concept visuals</p><h2 class="t t120">One artist per machine</h2>
<p class="lead">The same booth, a different world each time. Then claws, shooting galleries, a paintball roll, darts.</p></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(2, 1fr);column-gap:48px">{mm}</div>
{d.foot(8)}''', 'The crowd comes for simple machines, made in series, one artist per machine: about ten photobooths and ten arcade cabinets to start with, then ten claws. Same hardware, a different artist’s world each time. Photobooth: the artist brings ten to twenty works that define a style; the model is tuned on them, with their agreement; your portrait comes out in that style. Arcade: a short game designed with the artist; the score decides the artwork, generated on the spot. Around them, the classics remade by artists: claws full of capsules, shooting galleries where the piece mixes your score and a capture of the moment, a paintball roll, darts, a knock-down, a pixel wall.'))
sig = [('The Oracle', 'Why do we trust a voice?', 'Behind the curtain, a fortune-teller that shows how it thinks.'),
       ('The Hall of Doubles', 'What am I to a model?', 'Every mirror remakes you differently.'),
       ('The Wheel of Odds', 'Chance or prediction?', 'The AI calls the result. You bet with it or against it.'),
       ('The Robot Portraitist', 'Who is the author?', 'A robot looks at you and draws.')]
sg = ''.join(f'<div class="row g32 rule" style="padding:18px 0;align-items:baseline"><h3 class="t t48" style="width:400px;flex:none">{t}</h3><div class="col g8"><p class="lab acc">{q}</p><p class="small">{b}</p></div></div>' for t, q, b in sig)
d.add('rides', sec('rides', '', f'''{photo(d, 'fp/oracle.jpg', 'Concept visual: an Art Deco fortune-teller cabin, its star-covered curtain almost closed on a visitor, a glowing screen in a round window')}
<div class="shade-l"></div>
<div class="col g24 in" style="width:1000px"><p class="lab acc">Signature rides · concept visual</p><h2 class="t t120">Play the question</h2></div>
<div class="col in2" style="width:900px;margin-top:28px">{sg}
<p class="small mute rule" style="padding-top:18px">And the Two-Hand Claw, the Agents’ Arena, the Train of Layers…</p></div>
{d.foot(9)}''', 'Next to the machines, the signature rides: each takes a fairground classic and turns it into a question about how AI decides. The Oracle is a fortune-teller’s cabin: you step in and the curtain closes behind you, so what it tells you is for you alone. It comes in three characters: a slightly scary fortune-teller who asks you questions and names your best match; one who tells your future from nothing; and one who, with your consent, shows what the public web says about you from your name alone. The Hall of Doubles: a corridor of mirrors, each one a different model’s idea of you. The Wheel of Odds: the model announces its prediction before each spin; bets are in points, never money. The Robot Portraitist: a drawing robot on the path of the fair. Also in development: the Two-Hand Claw (you, the AI or the crowd at the controls), the Train of Layers (a dark ride through a model, in a shipping container), the Agents’ Arena (agents under rules the crowd rewrites) and the Dance Mirror (a choreography to copy).'))
anc = [('The photobooth', 'The Surrealists’ Photomaton portraits', '1929'),
       ('The arcade', 'MoMA collects Pac-Man and Tetris', '2012'),
       ('The Hall of Doubles', 'Yayoi Kusama’s Infinity Mirror Room', '1965'),
       ('The Wheel of Odds', 'Marcel Duchamp’s roulette, the Monte Carlo Bond', '1924'),
       ('The Robot Portraitist', 'Jean Tinguely’s drawing machines, the Méta-Matics', '1959'),
       ('The shooting gallery', 'Niki de Saint Phalle’s Tirs, paintings made by rifle shots', '1961'),
       ('The fair itself', 'Luna Luna, by Haring, Basquiat, Dalí and thirty artists', '1987')]
aa = ''.join(f'<div class="row g32 rule" style="padding:13px 0;align-items:baseline"><h3 class="t" style="font-size:40px;line-height:1.1;width:520px;flex:none">{r}</h3><p class="body" style="flex:1">{w}</p><p class="t acc" style="font-size:40px;line-height:1.1;width:120px;flex:none;text-align:right">{y}</p></div>' for r, w, y in anc)
d.add('ancestors', sec('ancestors', '', f"""<div class="col g24 in"><p class="lab acc">In art history</p><h2 class="t t120">Every ride has an ancestor</h2></div>
<div class="col in2">{aa}</div>
{d.foot(11)}""", 'None of these rides comes from nowhere. The photobooth: in 1928 the Photomaton arrives in Paris and the Surrealists adopt it; their booth portraits are published in La Révolution surréaliste in 1929. The arcade: in 2012 the Museum of Modern Art in New York acquires fourteen video games, Pac-Man and Tetris among them. The Hall of Doubles: Yayoi Kusama’s first Infinity Mirror Room, 1965. The Wheel of Odds: in 1924 Marcel Duchamp issues his Monte Carlo Bond to finance a system for playing roulette. The Robot Portraitist: Jean Tinguely’s Méta-Matics, 1959, machines that draw. The shooting gallery: Niki de Saint Phalle’s Tirs, from 1961, where the shot makes the painting. The fair itself: Luna Luna, 1987. FAIR PLAY does not copy these works: each ride answers one of them with the machines of 2027.'))
pause_video(d, 'builders', VID('art-factory-d'), 'Who builds it', 'The artists.',
      'Three slides on the artists: who already shows at NFC, the rides one by one with the artist we imagine for each, and who could sign the machines.', 'A generative artwork on a tall LED screen in the Art Factory at NFC Summit 2026')
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
rides = [('The photobooth', 'An image model remakes your portrait in their style.', 'Mr Richi, Efdot, Coldie…'),
         ('The arcade', 'An image model turns your score into an artwork.', 'Polygon1993, DeafBeef…'),
         ('The Oracle', 'A language and voice model answers, and shows why.', 'Sasha Stiles'),
         ('The Hall of Doubles', 'Several image models, each with its own idea of you.', 'Trevor Paglen'),
         ('The Wheel of Odds', 'A prediction model calls the result before the spin.', 'Gretchen Andrew'),
         ('The Robot Portraitist', 'A vision model guides the drawing arm.', 'Patrick Tresset'),
         ('The Two-Hand Claw', 'An agent steers the claw. You can take over.', 'Dmitri Cherniak'),
         ('The Agents’ Arena', 'Agents compete under rules the crowd rewrites.', 'Botto')]
head = '<div class="row g32" style="padding:0 0 10px"><p class="lab mute" style="width:420px;flex:none">The ride</p><p class="lab mute" style="flex:1">What the AI does</p><p class="lab mute" style="width:440px;flex:none">The artist we imagine</p></div>'
rr = ''.join(f'<div class="row g32 rule" style="padding:10px 0;align-items:baseline"><h3 class="t" style="font-size:40px;line-height:1.1;width:420px;flex:none">{r}</h3><p class="body" style="flex:1">{w}</p><p class="t acc" style="font-size:40px;line-height:1.1;width:440px;flex:none">{a}</p></div>' for r, w, a in rides)
d.add('ridelist', sec('ridelist', '', f'''<div class="col g24 in"><p class="lab acc">First ideas · a wish list, not a line-up</p><h2 class="t t120">Every ride, its AI, its artist</h2></div>
<div class="col in2">{head}{rr}</div>
{d.foot(12)}''', 'The rides one by one: what the AI does in each, and the artist we imagine for it. Photobooths and arcades are made in series, one artist per machine. For the signature rides: Sasha Stiles, poet and AI researcher, for the Oracle. Trevor Paglen, whose work shows what machines see and who is part of MAAT’s “Energies of AI”, for the Hall of Doubles. Gretchen Andrew, winner of the ABS Digital Art Prize 2026 at NFC Summit, for the Wheel of Odds. Patrick Tresset, whose robots draw portraits, for the Robot Portraitist. Dmitri Cherniak, whose Ringers were shown on LED at NFC Summit 2026, for the Two-Hand Claw. Botto, the AI artist governed by a community, for the Agents’ Arena. This is a wish list: none of them has been asked yet, conversations start in December, and the independent curator has the last word. No product is named on purpose: the partner’s models take these roles.'))
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
d.add('crowd', sec('crowd', 'bottom', f"""{photo(d, PH('terrasse-tage-fete'), 'A rooftop party above the Tagus during NFC Summit 2026, Lisbon in the background')}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g24 in" style="width:1600px"><p class="lab acc">The audience</p><h2 class="t" style="font-size:200px;line-height:.92">Now think<br>in millions.</h2></div>""",
      'A breath before the numbers. Two kinds of figures follow, and the slide keeps them apart: the crowds that are in Lisbon anyway, with their sources, and the goals we set for the season. The photo: a rooftop party above the Tagus during NFC Summit 2026.', ' style="padding-bottom:144px"'))
facts = [('3M+', 'Tourists in Lisbon during the six months of the fair'), ('86,000', 'People at Web Summit, Devcon and NFC Summit')]
goals = [('1M', 'Artworks made by the public, on site and online'), ('50M', 'Impressions across the season')]
cell = lambda v, l, c='': f'<div class="col g16"><div class="bar"></div><p class="t t112{c}">{v}</p><p class="body">{l}</p></div>'
d.add('millions', sec('millions', '', f"""<div class="col g24 in"><p class="lab acc">The audience</p><h2 class="t t120">A season in millions</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px;row-gap:28px">
<p class="lab mute" style="grid-column:span 2">Already in Lisbon · sourced</p><p class="lab acc" style="grid-column:span 2">Our goals for the season</p>
{''.join(cell(v, l) for v, l in facts)}{''.join(cell(v, l, ' acc') for v, l in goals)}</div>
<p class="lead">Art you can play fills museums: teamLab’s two museums in Tokyo had 4.2 million visitors in 2025.</p>
{d.foot(17, 'Sources: INE · Web Summit 2025 · Devcon 2024 · NFC Summit 2026 · teamLab')}""",
      'Two kinds of numbers, kept apart. Already in Lisbon, with sources. Tourists: 3.3 million guests stayed in the city in the first half of 2025 alone (INE, Statistics Portugal), and the fair is open during the busier half of the year. Tech and art crowds: Web Summit 71,386 attendees from 157 countries in 2025, Devcon 12,500 in 2024, NFC Summit 2,740 in 2026, about 86,000 together. Lisbon families already go out for this kind of visit: 380,000 visitors at MAAT and 312,000 at the Pavilhão do Conhecimento science centre in 2024, where families buy two tickets out of three. And art you can play is what draws the biggest crowds: teamLab’s two museums in Tokyo had more than 4.2 million visitors in 2025. Our goals for the season, which are goals and not forecasts. One million artworks made by the public: on site, about forty machines and rides, around a hundred plays each per day, sixty open days between May and October, so about 200,000 plays; the rest comes from the online rides, played from a phone. Fifty million impressions: NFC Summit 2026 reached more than 6 million organic impressions in three days; the season lasts nine months, about forty artists share it with their own audiences, and every artwork is made to be shared by the person who made it. Third goal, not on the slide: 100,000 visitors on site.'))
rows = ''.join(f'<div class="row g32 rule" style="padding:26px 0;align-items:baseline"><h3 class="t t48" style="width:330px;flex:none">{t}</h3><p class="body">{s}</p></div>' for t, s in [
      ('Workshops', 'Every month, an artist shows how to make art with the partner’s tools. Live, free, replayed.'),
      ('Initiations', 'A first try for beginners and families. No code, one artwork at the end.'),
      ('Hackathon', 'In February, online. The best prototypes win a residency in Lisbon.'),
      ('Online rides', 'The photobooths open on your phone, months before the fair.')])
statement_light(d, 'online', 'It starts in January', '<span style="display:block;line-height:1">Online<br>first</span>', rows,
      f'The season does not wait for May. From January, online: a monthly workshop where an artist of the season shows how they make art with {TOOLS}, live, free and replayed; initiations for people who have never touched an AI tool, with one artwork at the end; an online hackathon in February, whose best prototypes win a residency in Lisbon from March to May; and the first rides opened online, starting with the photobooths, so anyone can play from a phone and get an artwork. For a partner, this is where the return starts: a public, usage and content from the first month, long before the premiere.', 18,
      sentence='A public before the doors open.')
gets = [('1M', 'People make an artwork with your model. Our goal for the season.'),
        ('40', 'Artists build with your tools, in public, and show how.'),
        ('4', 'Moments on stage in Lisbon: NFC Summit, MAAT week, Devcon, Web Summit.'),
        ('1', 'Founding lab. Your models inside the rides, all season.')]
d.add('return', sec('return', '', f"""<div class="col g24 in"><p class="lab acc">For a founding partner</p><h2 class="t t120">What you get</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px">{''.join(cell(v, l) for v, l in gets)}</div>
<p class="lead">Your model is credited on every artwork. You get the real numbers after every stop.</p>
{d.foot(19)}""",
      f'The return, in four figures. One: usage. Each play is one person who makes an artwork with {MODEL}, in a minute, and takes it home; the season goal is one million, on site and online. Two: artists. About forty artists build with {TOOLS} and say so, in the workshops, in the residencies and on their machines; each one is a case study and a film. Three: stage. Four moments with press and an audience in Lisbon: the premiere at NFC Summit in May, MAAT week in September, the finale in Devcon week in October, Web Summit in November. Four: one founding lab on the season. Every artwork carries the credit “made by the artist, with” the model. After every stop the partner gets a report: plays, artworks made, visitors, reach, press. The figures on this slide are goals for the season.'))
deal(d, 'partner', ['Your models inside the rides.', 'Your team in the workshops.', 'Your name on the season.'],
     [('The artists', 'A curated line-up, paid and credited.'), ('The fair', 'Machines, booths, staff, payment and printing.'), ('The audiences', 'Digital art in May, Lisbon all year, Ethereum and tech in the autumn.')],
     'For one founding partner. Your part: your models generate the artworks inside the rides, your engineers and artists take part in the workshops, the hackathon and the residencies, your name signs the season. Our part: the artists, the production of the fair, and the audiences. An independent curator chooses the artists; the partner does not choose them and does not review the works. Nothing is used to train a model without the written agreement of the artist. The same season is open to other partners, who can sign a moment, a stop or a set of machines.', 20, label='For a founding partner')
d.add('close', sec('close', 'bottom', f'''{video(d, VID('art-factory-a'), 'A visitor in front of an immersive artwork in the Art Factory at NFC Summit 2026')}
<div class="shade-l"></div>
<div class="shade-b"></div>
<div class="col g32 in" style="width:1500px">
<p class="lab acc">FAIR PLAY · Lisbon 2027</p>
<h2 class="t t150">Build a ride</h2>
<p class="lead">A 20-minute call, then a proposal made for your team.</p>
<p class="lab">John Karp · john@nonfungibleconference.com · t.me/thejonnkarp</p>
</div>''', 'Next step: a 20-minute call with John, then a proposal.', ' style="padding-bottom:144px"'))

SECTIONS = {"idea": {"description": "What FAIR PLAY is, and why Lisbon in 2027.", "start": "cover"},
            "rides": {"description": "How a ride works, the machines and the signature rides.", "start": "rule"},
            "artists": {"description": "The artists of NFC, every ride with its AI and its artist, and the wish list.", "start": "builders"},
            "partner": {"description": "Who is behind it, the audience in millions, the online start, what a partner gets and the contact.", "start": "who"}}
