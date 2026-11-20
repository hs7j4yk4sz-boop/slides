import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('gp', 'NFC Summit 2027 — General presentation')

cover(d, 'cover', VID('art-factory-rez-de-chaussee'), 'Sixth edition · fifth anniversary', 'NFC Summit 2027',
      'The Digital Pop Culture Festival', '27 — 29 May 2027 · Unicorn Factory, Beato, Lisbon',
      'Sixth edition, fifth anniversary. 27 to 29 May 2027, Unicorn Factory, Beato, Lisbon. The film behind the title is the Art Factory in 2026.',
      'The flour mill machines of the Art Factory at NFC Summit 2026')
vstatement(d, 'belief', VID('place-totem-et-mur'), 'The future belongs to crossovers.', 'Five years later, this community has an address.',
      'Our belief. Between communities. Between artists and collectors. Between technology and culture. Between the digital and the real world. Five years later, this community turned that belief into a place. Three days a year, it has an address.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement(d, 'thesis', VID('mur-crane-pixel'), 'Art at the service of entertainment.', '2027, our fifth anniversary: the festival becomes a fairground.',
      'The line for 2027, the fifth anniversary: art at the service of entertainment. The festival becomes a fairground: Play the art.',
      'A giant pixel skull painted on a facade at the Unicorn Factory, filmed by drone')
spr = ''.join(f'<img src="{d.m(f"people-of-the-wall/wall-{i:02d}.png")}" alt="" style="width:52px;height:80px;image-rendering:pixelated">' for i in range(1, 59))
d.add('started', sec('started', '', f"""<div class="col g24 in">
<p class="lab acc">On The Wall · since September 2026</p>
<h2 class="t t150">It has already started.</h2>
</div>
<p class="in2" style="font-size:56px;font-weight:300;line-height:1.18;letter-spacing:-.5px;max-width:1560px">We asked the community to fund the festival and put their name on its walls. <b style="font-weight:500">More than 325 people already did, giving from $150 to $25,000.</b></p>
<div class="col g32">
<div aria-label="People of the Wall pixel avatars" style="display:grid;grid-template-columns:repeat(29, 1fr);row-gap:14px;justify-items:start">{spr}</div>
<p class="lead mute">It keeps going, every week: <a href="https://onthewall.nfcsummit.com" target="_blank" rel="noopener" style="color:var(--yellow);text-decoration:none">onthewall.nfcsummit.com</a></p>
</div>
{d.foot(4)}""",
      'On The Wall is our crowdfunding: people pay to have their name, their portrait or their house painted by hand on the walls of NFC 2027. More than 325 people have joined so far, from $150 for a name to $25,000 for the biggest wall. The pixel portraits are theirs: the 58 members who have drawn their sprite so far. The campaign opened on 10 September 2026 and reached “Today’s News” on X on its last day, 30 October. Since then, something happens every week with this community: People of the Wall, the podcast, every Friday, 32 episodes so far; new video games; new ideas brought by the members. The Yearbook is made with Alpha Labs and handed out on 27 May.'))
pairs = [('Art', 'Finance'), ('Builders', 'Creators'), ('Communities', 'Institutions'), ('Internet', 'Real life'), ('Technology', 'Culture'), ('Collecting', 'Belonging')]
rows = ''.join(f'<div class="row g20 rule" style="padding:22px 0;align-items:center"><h3 class="t t48">{a}</h3><p class="lead acc" style="line-height:1">×</p><h3 class="t t48">{b}</h3></div>' for a, b in pairs)
statement_light(d, 'definition', 'Definition', 'Digital Pop Culture', rows,
      'Not an industry. A method. Culture is no longer handed down by one world at a time. It is assembled where two worlds meet, by people who were never supposed to be in the same room. Digital Pop Culture is what happens when the internet stops being a channel and becomes a co-author. Every crossover already has an audience. None of them has a home. That is the gap NFC fills.', 5,
      sentence='Culture is now made where two worlds meet.')
pause_video(d, 'address', VID('expo-art-factory-etage'), 'Sixth edition · fifth anniversary', 'Five years.<br>One address.',
      'A pause. Five years after the first edition, the community has a home in Lisbon: the Unicorn Factory, every May.', 'Visitors in an exhibition room of the Art Factory at NFC Summit 2026', poster='px/expo-crowd.jpg')
figures(d, 'numbers', PH('place-centrale-visiteuses'), '2026 edition — final report', 'What one edition holds',
      [('2 740', 'Visitors'), ('150+', 'Speakers'), ('79', 'Countries'), ('75', 'Sponsors'), ('200+', 'Artists exhibited'), ('30+', 'Side events'), ('6M+', 'Organic impressions')],
      'All figures come from the NFC Summit 2026 final report.', 'Visitors on the central plaza of the Unicorn Factory, NFC Summit 2026', 6, 'Source: NFC Summit 2026 final report')
quote(d, 'voices', PH('visiteur-casque-ar'), 'Amazing 48 hours at NFC Summit in Lisbon.', 'One of the best 2 days of my life.', 'Adam Weitsman', 'Collector · Gold sponsor 2027',
      'Other voices from 2026. DANAE.io: “NFC Summit exceeded everything we hoped for. The crowd, the wonder, the children’s laughter echoing in the room, moments we won’t forget.” Matt Medved: “NFC’s always been an important event for digital art, bringing Europe and the Americas together.” Giannis Sourdis: “A level up compared to the last few years. The vibes are also better than last year.”',
      'A visitor trying an augmented reality headset at NFC Summit 2026', 7)
worlds = [('01', 'FAIR PLAY', 'Art × Play'), ('02', 'Kawaii Summit', 'Cards × Art'), ('03', 'Conference', 'Ideas × Action'), ('04', 'Art Factory', 'Art × Collecting'), ('05', 'Hackathon · AI Day', 'Builders × AI'), ('06', 'Parties', 'Internet × Real life')]
cells = ''.join(f'<div class="col g12 rule-d" style="padding-top:28px"><p class="lab mute">{n}</p><h3 class="t t64">{w}</h3><p class="lab acc">{c}</p></div>' for n, w, c in worlds)
pause_dragon(d, 'welcome', 'ringmaster-hero', 'Six worlds · 27 — 29 May 2027', 'Welcome to the fairground.',
      'The ringmaster opens the six worlds of 2027: FAIR PLAY, Kawaii Summit, Conference, Art Factory, Hackathon · AI Day, Parties.', side='right', h=980)
d.add('worlds', sec('worlds', '', f'''<div class="col g24 in"><p class="lab acc">The programme</p><h2 class="t t120">Six worlds</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:64px;row-gap:56px">{cells}</div>
{d.foot(8)}''', 'The six worlds of the site, each with its crossover. The containers now live in the On The Wall story (slide 4).'))
nm = lambda name, tag: f'<span class="acc" style="display:block;line-height:1;margin-bottom:12px">{name}</span><span style="display:block;line-height:1">{tag}</span>'
divider(d, 'fair', '', 'art-fun-fair', 'World 01 · Art × Play', nm('FAIR PLAY', 'Play the art.'), 'A fairground where artists build the rides: a screen, a score, a print to take home.',
      'Every stand is an Artistic Digital Activation: play, win, keep. Photobooths, arcades, claws and shooting stands designed by artists.', 'The FAIR PLAY dragon, riso-printed in yellow and blue', 9)
world(d, 'kawaii', VID('salle-kawaii-cartes-et-stamps'), 'World 02 · Cards × Art', nm('Kawaii Summit', 'Where cards become art.'), 'Tournaments on the tables, the card as an artwork on the walls.',
      'Kawaii Summit 2026: 20 exhibitors, 3 TCG tournaments, its own stage. Trading floors next to drawing tables. Collectors of ten and collectors of forty, trading with each other.', 'The Kawaii Summit hall in 2026: card sellers, game tables and tournaments', 10)
world(d, 'conference', PH('scene-speakeuse'), 'World 03 · Ideas × Action', nm('Conference', 'One day to think. One day to listen.'), 'Day one, working groups. Day two, the symposium and the big names.',
      'Stage time is earned: we book people who shipped the thing, not people who predict it. Conversations continue in the corridor and end in decisions.', 'A speaker on the main stage of NFC Summit 2026', 11)
world(d, 'artfactory', VID('art-factory-premier-etage'), 'World 04 · Art × Collecting', nm('Art Factory', 'The museum of the summit.'), 'Four floors of a former flour mill, the machines still in place.',
      'World 04 · Art × Collecting. Artists work in the open: nothing sits behind glass. The person who made the piece is standing next to it, and the person buying it asks in person.',
      'Artworks shown on the first floor of the Art Factory in 2026', 14)
world(d, 'hackathon', PH('gaming-enfant'), 'World 05 · Builders × AI', nm('Hackathon · AI Day', 'Build it in two days.'), 'In the Escola 42 building, on site, 27 and 28 May. The best projects demo on the main stage.',
      'Teams build in the same place where the work will be shown. On the last afternoon they demo to the people who would actually use it.', 'A young visitor playing a game at NFC Summit 2026', 13)
world(d, 'parties', PH('fete-dj-palmiers'), 'World 06 · Internet × Real life', nm('Parties', 'Every night, everywhere.'), 'A party every evening, and 29 May is the party day.',
      'One party every night, one big one, and the whole of 29 May given to the party.', 'A DJ set under the palm trees, NFC Summit 2026', 14)
pause_video(d, 'play', VID('mur-crane-pixel'), 'Every stand is an artistic activation', 'Play. Win. Keep.',
      'Play the art, win a prize, keep a print. Every stand of the fair is designed by an artist.', 'A pixel skull mural on the walls of NFC Summit 2026')
mapslide(d, 'venue', 'The venue', 'One site, one fairground',
      [('FAIR PLAY', 'The fair, at the heart of the plaza'), ('Art Factory', 'Four floors of exhibitions'), ('Main stage', 'Two days of conference'), ('Kawaii Summit', 'Cards, players, artists'), ('The Wall', 'The names of the community'), ('Escola 42', 'Hackathon · AI Day')],
      'The Unicorn Factory in Beato: the Art Factory on the left, the Wall along the right building, the main stage and the Kawaii Summit at the bottom, the fair in the middle of the plaza. The hackathon is in the Escola 42 building, on site.', 15)
programme(d, 'days', '27 — 29 May 2027', 'Three days in May', [
      ('hall-galeries', 'The galleries hall of NFC Summit 2026', 'Thursday 27', 'The working day', ['Working groups', 'Fair, cards and Art Factory open', 'The hackathon starts']),
      ('scene-speaker', 'A speaker on the main stage of NFC Summit 2026', 'Friday 28', 'The symposium', ['Main stage, big names', 'Tournaments and fair all day', 'Hackathon demos']),
      ('fete-dj-palmiers', 'A DJ set under the palm trees, NFC Summit 2026', 'Saturday 29', 'The party day', ['No talks, no stage', 'FAIR PLAY open all day', 'The final party'])],
      'Thursday is the working day, Friday the symposium, Saturday the party day. FAIR PLAY stays open on the plaza in Beato on Saturday.', 16)
stage(d, 'stage', '2027 · our fifth anniversary', 'Just wait until you see what we’ve built.',
      'Five years of bringing together artists, collectors, builders and fans in Lisbon. To celebrate our birthday, we are not just doing more of the same: we are taking things to a whole new level. Just wait until you see what we’ve built.', size=168)
pstatement(d, 'lisbon', PH('terrasse-tage-fete'), 'The city was already here', 'Artists, founders and collectors moved to Lisbon before anyone called it a scene.',
      'The festival did not import an audience: it set a date for the one living here. A former factory in Beato holds the programme. The city holds the rest: studios, rooftops, the river at four in the morning. Nobody stays a stranger in a walkable city.',
      'A rooftop party above the Tagus during NFC Summit 2026', 18)
reasons = [('01', 'You meet the people you only knew online'), ('02', 'You see ideas before they become trends'), ('03', 'You leave with something started')]
rr = ''.join(f'<div class="row g32 rule" style="padding:28px 0;align-items:baseline"><p class="lab acc">{n}</p><h3 class="t t64">{t}</h3></div>' for n, t in reasons)
statement_light(d, 'comeback', 'Why people come back', 'Three days people keep', rr,
      '01 — Years of messages, one handshake. It changes how you work with them afterwards. 02 — The work shown in May is the work everyone quotes in November. 03 — A project, a friendship, a collaboration. Usually all three, decided on a staircase.', 19)
d.add('partner', sec('partner', '', f'''<div class="col in" style="width:1500px">
<p class="lab acc" style="margin-bottom:56px">Partner with NFC</p>
<p class="t" style="font-size:320px;line-height:0.62;height:160px;color:var(--yellow)">“</p>
<p style="font-size:84px;font-weight:300;line-height:1.1;letter-spacing:-1px">For six editions, we have built <b style="font-weight:500">a custom format with every partner.</b> Tell us what you want to do.</p>
<div class="col g12" style="margin-top:56px">
<p class="t t64">John Karp</p>
<p class="lab mute">Founder, NFC Summit</p>
</div>
<p class="lab acc" style="margin-top:56px">john@nonfungibleconference.com · t.me/thejonnkarp</p>
</div>''', 'How to be part of NFC 2027. We do not sell a grid: since the first edition, every partnership has been built with the partner, around what they want to do. The ways in for 2027: FAIR PLAY, Kawaii Summit, On The Wall, side events, CryptoStamp Corner, AI Residency, stands and branding, and co-organizer. Each has its own deck, and the catalogue gathers them all with the partner levels and how to book. No prices in this presentation: they are in the catalogue and in each deck.', ' style="justify-content:center;padding-bottom:150px"'))
closing(d, 'close', '27 — 29 May 2027 · Unicorn Factory, Beato, Lisbon', 'See you in Beato', [],
      'Close on the dates and the seven dragons: the ringmaster in the middle, one dragon per world around him.')
# fix page numbers of slides built with explicit numbers (world slides etc. use their position)
SECTIONS = {"idea": {"description": "What NFC Summit is, what it believes, and why it already lives before May.", "start": "cover"},
            "proof": {"description": "The 2026 edition in figures and in the words of people who came.", "start": "definition"},
            "worlds": {"description": "The six worlds of the site, one page each.", "start": "worlds"},
            "practical": {"description": "The venue, the three days, Lisbon, and why people come back.", "start": "venue"}}
