import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('ks', 'NFC Summit 2027 — Kawaii Summit')

cover(d, 'cover', 'pc/glitch-room.jpg', 'Inside NFC Summit 2027 · 27 — 29 May · Lisbon', 'Kawaii Summit',
      'Where cards become art. Your card game, collection or character becomes a real card, drawn with an artist.', 'Kawaii Summit × PHANTASM',
      'Kawaii Summit is the part of NFC dedicated to trading cards. This deck presents the event, PHANTASM and Polygon1993, then the offer: your card, made with an artist, sold four ways.',
      'A blue glitch artwork filling the room')
vstatement_figs(d, 'nfc', VID('place-totem-et-mur'), 'Sixth edition · 27 — 29 May 2027 · Lisbon', 'This is NFC.',
      'The annual home of digital artists, collectors and builders. Three days, one venue.',
      [('2,740', 'attendees in 2026'), ('79', 'countries'), ('6M+', 'organic impressions')],
      'NFC Summit is the annual home of digital artists, collectors and builders: three days at the Unicorn Factory in Lisbon. In 2026: 2,740 attendees from 79 countries, more than 6 million organic impressions.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement_figs(d, 'kawaii', VID('salle-kawaii-cartes-et-stamps'), 'Inside NFC', 'Kawaii Summit.<br>Where cards become art.',
      'Tournaments and players on one side. Original artworks and artists on the other.',
      [('20', 'exhibitors in 2026'), ('3', 'TCG tournaments'), ('1', 'stage of its own')],
      'Kawaii Summit is the part of NFC dedicated to trading cards. In 2026: 20 exhibitors, 3 TCG tournaments and its own stage.',
      'The TCG trades and tournaments hall at NFC Summit 2026, players at the tables', poster='pc/kawaii-poster.jpg')
rows = ''.join(f'<div class="row g32 rule" style="padding:28px 0;align-items:baseline"><p class="lab acc">{n}</p><div class="col g8"><h3 class="t t64">{t}</h3><p class="small">{s}</p></div></div>' for n, t, s in [
      ('01', 'The arena', 'Tournaments at the tables all weekend: One Piece, Pokémon, Yu-Gi-Oh! and more.'),
      ('02', 'The gallery', 'PHANTASM, the card game by Polygon1993: you play it, you collect it, you hang it.'),
      ('03', 'The stage', 'Talks, reveals and signings on the Kawaii Stage.')])
statement_light(d, 'sides', 'Kawaii Summit 2027', 'Players and artists, one room', rows,
      'Two sides of one room. The arena: tournaments at the tables all weekend, One Piece, Pokémon, Yu-Gi-Oh! and more. The gallery: PHANTASM, the card game by Polygon1993, 140 cards by 30+ artists. And the Kawaii Stage for talks, card reveals and signings.', 4)
d.add('artist', sec('artist', '', f'''<img src="{d.m('pc/glitch-artwork.jpg')}" alt="Blue glitch profile, an artwork by Polygon1993" style="position:absolute;left:840px;top:0px;width:1080px;height:1080px;object-fit:cover">
<div style="position:absolute;left:840px;top:0px;width:360px;height:1080px;background:linear-gradient(90deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0) 100%)"></div>
<div class="col g24 in" style="width:860px">
<p class="lab acc">The artist behind PHANTASM</p>
<h2 class="t t150">Polygon1993</h2>
<p class="lead">An artist who grew up with cards. A French artist and a leading figure of glitch art.</p>
</div>
<div class="row g40 in2" style="width:860px;align-items:flex-end">
<img src="{d.m('pc/polygon1993.jpg')}" alt="Polygon1993 in the gallery" class="frame" style="width:240px;height:320px;object-fit:cover;flex:none">
<div class="col g16"><p class="lab acc">Has worked with</p><p class="lead" style="font-size:36px;line-height:1.3">OpenAI · Bandai Namco · Grimes · Tame Impala · Pantone</p></div>
</div>
{d.foot(5)}''', 'Polygon1993 is a French artist and a leading figure of glitch art. He has worked with OpenAI, Bandai Namco, A$AP Rocky, Grimes, Tame Impala, Charli XCX and Pantone. Exhibitions: Tokyo 2025, Paradigm Shifters at The Harmonyst Gallery. Paris 2026, Koi No Yokan at ArtVerse Gallery, 500 people at the opening.'))
cards = [('pc/new-world.jpg', 'NEW WORLD card by CA Chou', 'CA Chou'), ('pc/balan.jpg', 'BALAN card by Jeff Aphisit', 'Jeff Aphisit'), ('pc/march-of-the-demons.jpg', 'MARCH OF THE DEMONS card by Ahad', 'Ahad')]
cc = ''.join(f'<div class="col g16"><img src="{d.m(k)}" alt="{a}" style="width:312px;height:434px;object-fit:cover"><p class="lab mute">{n}</p></div>' for k, a, n in cards)
pts = [('01', 'You play it', 'A real game, with real tournaments.'), ('02', 'You collect it', 'Numbered editions, rare cards, foil. In print and online.'), ('03', 'You hang it', 'Every card is an artwork, shown in galleries.')]
pp = ''.join(f'<div class="row g24 rule" style="padding:20px 0"><p class="lab acc" style="width:44px;flex:none">{a}</p><div class="col g8"><h3 class="t t36">{b}</h3><p class="small mute">{c}</p></div></div>' for a, b, c in pts)
d.add('game', sec('game', 'paper', f'''<div class="col" style="width:640px;justify-content:space-between">
<div class="col g24 in"><p class="lab acc">The game · PHANTASM</p><h2 class="t t88">A card game made by an artist.</h2><p class="lead">Half trading card game, half art. 140 cards. More than 30 artists.</p></div>
<div class="col in2">{pp}</div>
</div>
<div class="col g24 in3" style="flex:1;justify-content:center">
<p class="lab acc">From the game</p>
<div class="row" style="gap:24px">{cc}</div>
</div>
{d.foot(6)}''', 'PHANTASM is half trading card game, half art: 140 cards by more than 30 artists. You play it (a real game, with real tournaments), you collect it (numbered editions, rare cards, foil; each card exists in print and online), you hang it (every card is an artwork, shown in galleries). Already in the game: CA Chou, Jeff Aphisit, Ahad.', ' style="flex-direction:row;gap:96px"'))
pause_dragon(d, 'deserve', 'kawaii-summit', 'Kawaii Summit 2027', 'Your card<br>is waiting.',
      'A pause before the offer: one special card for your game, your collection or your character, made with an artist.', side='right', h=980)
d.add('idea', sec('idea', 'yellow', f'''{card_mock(d, 1240, 150, 500, 'YOUR<br>CHARACTER', 'YOUR COLLECTION', 'Kawaii Summit')}
<p class="lab acc in">The idea</p>
<div class="col g40 in2" style="width:1060px">
<h2 class="t t150">Your character.<br>A real card.</h2>
<p class="lead">Your card game, collection or character becomes a real card, drawn with an artist, unveiled in Lisbon on 27 May 2027.</p>
</div>
{d.foot(8)}''', 'The idea: one special card for your game, collection or character, made with an artist, unveiled on stage at NFC Summit, Lisbon, on 27 May 2027. Then we sell it together.'))
cw = 380; ch = round(cw / 0.718); top = 1080 - 160 - ch
ways = [('A', 'Enter PHANTASM', 'Polygon1993 or one of its artists draws your character into the game. Played, collected, exhibited.'),
        ('B', 'Your Kawaii Summit special', 'An artist of the NFC crew draws the special card of the event with you. Your universe, your style.')]
def way(i, img):
    a, b, c = ways[i]
    return f'''<div class="row g40" style="width:816px;align-items:flex-end">{img}
<div class="col g16" style="width:{816 - cw - 40}px"><p class="t t120 acc">{a}</p><h3 class="t t48">{b}</h3><p class="body mute">{c}</p></div></div>'''
d.add('ways', sec('ways', '', f'''{card_mock(d, 1008, top, cw, 'YOUR<br>CHARACTER', 'YOUR COLLECTION', 'Kawaii Summit')}
<div class="col g24 in"><p class="lab acc">Choose your card</p><h2 class="t t120">Two ways in.</h2></div>
<div class="row in2" style="gap:96px">
{way(0, f'<img src="{d.m("pc/balan.jpg")}" alt="BALAN, a PHANTASM card by Jeff Aphisit" class="frame" style="width:{cw}px;height:{ch}px;object-fit:cover;flex:none">')}
{way(1, f'<div style="width:{cw}px;height:{ch}px;flex:none"></div>')}
</div>
{d.foot(9)}''', 'Two ways in. A, enter PHANTASM: your character drawn into the game of Polygon1993 by one of its artists, then played, collected and exhibited. B, your Kawaii Summit special: an artist of the NFC crew draws the special card of the event with you, a promo card for your own game if you have one.'))
sell = [('01', 'Online, before', 'Pre-sale and online pack openings, months before Lisbon.'), ('02', 'At the event', 'Pack reveals live on site, signings at the table.'),
        ('03', 'As art', 'The one-of-one original and a framed giant, on the gallery wall.'), ('04', 'In the game', 'A playable card, in decks and in tournaments.')]
ss = ''.join(f'<div class="col g16 rule-d" style="padding-top:28px"><p class="lab acc">{a}</p><h3 class="t t64">{b}</h3><p class="body mute">{c}</p></div>' for a, b, c in sell)
d.add('sell', sec('sell', '', f'''<img src="{d.m('pc/giant-framed.jpg')}" alt="A giant backlit framed artwork by Polygon1993" style="position:absolute;left:1380px;top:0px;width:540px;height:560px;object-fit:cover">
<div class="col g24 in" style="width:1200px"><p class="lab acc">One collab</p><h2 class="t t120">Four ways to sell.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px">{ss}</div>
{d.foot(10)}''', 'One card, four ways to sell. Online, before: pre-sale and online pack openings, months before Lisbon. At the event: pack reveals live on site, signings at the table. As art: the one-of-one original and a framed giant on the gallery wall. In the game: a playable card, in decks and in tournaments.'))
pause_video(d, 'reveal', VID('art-factory-rez-de-chaussee'), 'Kawaii Summit 2027', 'Revealed on stage.<br>27 May.',
      'Your card is revealed on stage in Lisbon on 27 May 2027, in front of everyone.', 'An immersive installation in the Art Factory at NFC Summit 2026', poster='px/factory-immersive.jpg')
deal(d, 'deal', ['Bring your character and approve the card.', 'Come to Lisbon for the reveal.', 'Tell your community.'],
     [('Before', 'We find the artist, make the card, announce it and open the pre-sale.'), ('During', 'A slot on stage, a table to show the card, sales on site.'), ('After', 'Your card joins the PHANTASM exhibition: two months in a Lisbon gallery.')],
     'Your part: bring your character and approve the card, come to Lisbon for the reveal, tell your community. Our part: before, we find the artist, make the card, announce it and open the pre-sale. During, a slot on stage, a table to show the card, sales on site. After, your card joins the PHANTASM exhibition, two months in a Lisbon gallery.', 12)
visual_offer(d, 'offer', f'<img src="{d.m("pc/new-world.jpg")}" alt="NEW WORLD, a PHANTASM card by CA Chou" class="frame" style="height:640px;width:auto">',
      'Your card · Kawaii Summit 2027', 'One card. Three lives.', 'Enter PHANTASM, or your own Kawaii Summit special. Revealed on stage on 27 May',
      [('100', 'cards', 'Numbered printed cards, and their online twins'), ('1', 'giant', 'Framed and lit, on the gallery wall'),
       ('40%', 'to you', 'Of every sale, once production is covered')],
      'From €5,000', 'Bronze and up', 'Bronze',
      ['Logo: website and sponsor wall', 'Shared post on social media', '6 three-day passes', '10 codes at −50%'],
      'From €5,000, Bronze level and up. The card is revealed on stage in Lisbon on 27 May 2027. Sales split once production is covered: 40% to you, 30% to the artist, 30% to NFC, on the edition, the giant and the signings. Production of the edition and the giant is quoted per card, before you commit. Bronze perks: your logo on the website and the sponsor wall, a shared post, 6 three-day passes, 10 codes at −50% for your community. A bigger package moves you to the next level and its perks.',
      cta='Early-bird price until 31 December, excl. VAT')
more = [('ks/stand.jpg', 'Render of one Bronze stand: a barrel table with your brand, a stool, under spotlights', 'A stand', 'The Bronze stand: 2.25 m² in a shared container, barrel table, stool, your roll-up.', '€3,000', 'Bronze'),
        ('ks/play.jpg', 'Players around a table during a tournament at Kawaii Summit 2026', 'A tournament', 'One tournament of the weekend in your name, with its final on the Kawaii Stage.', '€5,000', 'Bronze'),
        ('ks/stand-silver.jpg', 'Render of one Silver stand: branded wall, screen and counter', 'A play stand', 'The Silver stand, 7 m², with a play table. Or your own container as a play room, at Gold.', '€7,500', 'Silver, or Gold'),
        ('photos-2026/kawaii-stage.jpg', 'A host on the Kawaii Stage at NFC Summit 2026', 'The Kawaii Stage', 'The stage in your name all weekend: talks, card reveals, tournament finals.', '€15,000', 'Gold')]
mo = ''.join(f'''<div class="col g12"><img src="{d.m(k)}" alt="{a}" style="width:100%;height:250px;object-fit:cover;object-position:{p}">
<h3 class="t t48" style="padding-top:8px">{t}</h3><p class="small mute" style="min-height:98px">{l}</p>
<div class="row g16" style="align-items:center"><p class="t t64 acc" style="white-space:nowrap">{pr}</p><p class="lab" style="border:2px solid var(--chalk);padding:4px 12px 3px">{lv}</p></div></div>'''
     for (k, a, t, l, pr, lv), p in zip(more, ['50% 50%', '50% 62%', '50% 50%', '50% 28%']))
d.add('more', sec('more', '', f'''<div class="col g24 in"><p class="lab acc">Beyond the card · four more ways into Kawaii Summit</p><h2 class="t t120">Take your place.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:40px;align-items:start">{mo}</div>
<p class="small in3">The stands are the stands of NFC Summit, at the same price. Bronze: logo, shared post, 6 passes, 10 codes at −50%. Silver: 10 passes, 2 VIP, a 10-minute talk. Gold: 15 passes, 4 VIP, a feature in the newsletter.</p>
{d.foot(14)}''', 'Beyond the card, four more ways into Kawaii Summit, to take alone or with the card. The stands are the stands of NFC Summit, the same as in the catalogue, placed in the Kawaii hall. A stand, €3,000, Bronze: 2.25 m² in a shared container, with a barrel table, a stool and your roll-up. A tournament, €5,000, Bronze: one tournament of the weekend carries your name, on the tables, the bracket screens and the prize ceremony, with its final on the Kawaii Stage; you bring the prizes. A play stand, from €7,500: the Silver stand, 7 m² in a 20 ft container with a branded wall, a 43-inch screen and a counter, plus a play table where visitors learn your game with demo decks; or, at Gold, €15,000, your own 20 ft container set up as a play room. The Kawaii Stage, €15,000, Gold, one brand: the stage carries your name all weekend, on its backdrop, in the agenda and between the talks, the card reveals and the tournament finals, with a slot of your own. Perks by level. Bronze: logo on the website and the sponsor wall, a shared post, 6 three-day passes, 10 codes at −50%. Silver: a post of your own, a mention in the newsletter, 10 passes, 2 VIP passes, 20 codes, a 10-minute talk. Gold: 2 posts of your own, a feature in the newsletter, 15 passes, 4 VIP passes, 30 codes, a 10-minute talk. More ideas on request: the official playmat on every tournament table, a promo card handed to every visitor, a collectors’ trade night, the cosplay contest in your name, a live pack-opening studio.'))
tl = [('Now', 'We talk, you pick A or B.'), ('January', 'The artist is chosen, the subject is set.'), ('March', 'The card is announced, pre-sale opens.'), ('27 May', 'The card is revealed in Lisbon.'), ('June — July', 'The exhibition, in a Lisbon gallery.')]
tt = ''.join(f'<div class="col g16"><div class="sq"></div><p class="t t48">{a}</p><p class="small mute">{b}</p></div>' for a, b in tl)
w = 330; h = round(w / RATIO['kawaii-summit'])
d.add('next', sec('next', '', f'''<img src="{d.m(DR('kawaii-summit'))}" alt="The Kawaii Summit dragon" style="position:absolute;left:{1824 - w}px;top:64px;width:{w}px;height:{h}px;object-fit:contain">
<div class="col g24 in" style="width:1300px"><p class="lab acc">How it happens</p><h2 class="t t168">Your card in 2027.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(5, 1fr);column-gap:40px">{tt}</div>
<div class="col g12 in3"><p class="t t64">Let’s make your card.</p><p class="lab">John Karp · john@nonfungibleconference.com · t.me/thejonnkarp</p></div>
{d.foot(15)}''', 'Now: we talk, you pick A or B. January: the artist is chosen, the subject is set. March: the card is announced, pre-sale opens. 27 May: the card is revealed in Lisbon. June and July: the exhibition, in a Lisbon gallery. Artists invited to draw a card follow the same calendar, with the drawing due at the end of February.'))
SECTIONS = {"event": {"description": "NFC Summit and Kawaii Summit.", "start": "cover"},
            "game": {"description": "Polygon1993 and PHANTASM, the card game.", "start": "artist"},
            "card": {"description": "Your card: two ways in, four ways to sell.", "start": "deserve"},
            "offer": {"description": "The deal, the price, four more ways in and the timeline.", "start": "reveal"}}
