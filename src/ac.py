import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('ac', 'NFC Summit 2027 — NFC Artist Cards')
PC = MEDIA + '/pc/'
X = {f'pc/{n}.jpg': PC + n + '.jpg' for n in ['new-world', 'balan', 'march-of-the-demons', 'card-wall', 'polygon1993', 'glitch-artwork', 'giant-framed', 'paris-expo', 'glitch-room', 'kawaii-poster', 'stage-speaker']}

# 01 cover — an artwork as the cover
cover(d, 'cover', 'pc/glitch-room.jpg', 'NFC Summit 2027 · 27 — 29 May · Unicorn Factory, Lisbon', 'NFC Artist Cards',
      'Your art becomes a collectible card, unveiled at Europe’s leading festival for digital creative communities.', 'Kawaii Summit × PHANTASM',
      'An invitation to draw one card for PHANTASM, the card game made by Polygon1993, and to reveal it on stage at NFC Summit 2027.',
      'A blue glitch artwork filling the room')

# 02 this is NFC — video + strong sentence
vstatement_figs(d, 'nfc', VID('place-totem-et-mur'), 'Sixth edition · 27 — 29 May 2027 · Lisbon', 'This is NFC.',
      'The annual home of digital artists, collectors and builders. Three days, one venue.',
      [('2,740', 'attendees in 2026'), ('79', 'countries'), ('6M+', 'organic impressions')],
      'NFC Summit is the annual home of digital artists, collectors and builders: three days at the Unicorn Factory in Lisbon. In 2026: 2,740 attendees from 79 countries, more than 6 million organic impressions.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')

# 03 Kawaii Summit — video + strong sentence
vstatement_figs(d, 'kawaii', VID('salle-kawaii-cartes-et-stamps'), 'Inside NFC', 'Kawaii Summit.<br>Where cards become art.',
      'Tournaments and players on one side. Original artworks and artists on the other.', None,
      'Kawaii Summit is the part of NFC dedicated to trading cards. In 2026: 20 exhibitors, 3 TCG tournaments and its own stage.',
      'The TCG trades and tournaments hall at NFC Summit 2026, players at the tables', poster='pc/kawaii-poster.jpg')

# 04 the partner — Polygon1993
d.add('artist', sec('artist', '', f'''<img src="{d.m('pc/glitch-artwork.jpg')}" alt="Blue glitch profile, an artwork by Polygon1993" style="position:absolute;left:840px;top:0px;width:1080px;height:1080px;object-fit:cover">
<div style="position:absolute;left:840px;top:0px;width:360px;height:1080px;background:linear-gradient(90deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0) 100%)"></div>
<div class="col g24 in" style="width:860px">
<p class="lab acc">Your partner</p>
<h2 class="t t150">Polygon1993</h2>
<p class="lead">An artist who grew up with cards. A French artist and a leading figure of glitch art.</p>
</div>
<div class="row g40 in2" style="width:860px;align-items:flex-end">
<img src="{d.m('pc/polygon1993.jpg')}" alt="Polygon1993 in the gallery" class="frame" style="width:240px;height:320px;object-fit:cover;flex:none">
<div class="col g16"><p class="lab acc">Has worked with</p><p class="lead" style="font-size:36px;line-height:1.3">OpenAI · Bandai Namco · Grimes · Tame Impala · Pantone</p></div>
</div>
{d.foot(4)}''', 'Polygon1993 is a French artist and a leading figure of glitch art. He has worked with OpenAI, Bandai Namco, A$AP Rocky, Grimes, Tame Impala, Charli XCX and Pantone. Exhibitions: Tokyo 2025, Paradigm Shifters at The Harmonyst Gallery. Paris 2026, Koi No Yokan at ArtVerse Gallery, 500 people at the opening.'))

pause_dragon(d, 'artwork', 'kawaii-summit', 'Kawaii Summit × PHANTASM', 'Every card<br>is an artwork.',
      'A pause before the game: in PHANTASM, every card is drawn by an artist and shown in galleries.', side='right', h=980)

# 05 the game — PHANTASM
cards = [('pc/new-world.jpg', 'NEW WORLD card by CA Chou', 'CA Chou'), ('pc/balan.jpg', 'BALAN card by Jeff Aphisit', 'Jeff Aphisit'), ('pc/march-of-the-demons.jpg', 'MARCH OF THE DEMONS card by Ahad', 'Ahad')]
cc = ''.join(f'<div class="col g16"><img src="{d.m(k)}" alt="{a}" style="width:312px;height:434px;object-fit:cover"><p class="lab mute">{n}</p></div>' for k, a, n in cards)
pts = [('01', 'You play it', 'A real game, with real tournaments.'), ('02', 'You collect it', 'Numbered editions, rare cards, foil. In print and online.'), ('03', 'You hang it', 'Every card is an artwork, shown in galleries.')]
pp = ''.join(f'<div class="row g24 rule" style="padding:20px 0"><p class="lab acc" style="width:44px;flex:none">{a}</p><div class="col g8"><h3 class="t t36">{b}</h3><p class="small mute">{c}</p></div></div>' for a, b, c in pts)
d.add('game', sec('game', 'paper', f'''<div class="col" style="width:640px;justify-content:space-between">
<div class="col g24 in"><p class="lab acc">The game · PHANTASM</p><h2 class="t t88">A card game made by an artist.</h2><p class="lead">Half trading card game, half art. 140 cards. More than 30 artists.</p></div>
<div class="col in2">{pp}</div>
</div>
<div class="col g24 in3" style="flex:1;justify-content:center">
<p class="lab acc">Already in the game</p>
<div class="row" style="gap:24px">{cc}</div>
</div>
{d.foot(5)}''', 'PHANTASM is half trading card game, half art: 140 cards by more than 30 artists. You play it (a real game, with real tournaments), you collect it (numbered editions, rare cards, foil; each card exists in print and online), you hang it (every card is an artwork, shown in galleries). Already in the game: CA Chou, Jeff Aphisit, Ahad.', ' style="flex-direction:row;gap:96px"'))

# 06 the invitation — the card mock-up
d.add('invite', sec('invite', 'yellow', f'''{card_mock(d, 1240, 150, 500)}
<p class="lab acc in">The invitation</p>
<div class="col g40 in2" style="width:1000px">
<h2 class="t t168">Let’s draw a card together.</h2>
<p class="lead">Your drawing. A PHANTASM card. Unveiled in Lisbon on 27 May 2027, in front of everyone.</p>
</div>
{d.foot(6)}''', 'The invitation: you draw one card for PHANTASM. It is unveiled on stage at NFC Summit, Lisbon, on 27 May 2027.'))

# 07 one drawing, one card, one giant
steps = [('01', 'You draw', 'One original illustration. Your subject, your style.'), ('02', 'It becomes a card', 'Polygon1993 adds the frame, the foil, your name.'),
         ('03', 'It exists twice', '100 numbered printed cards, and their online twins.'), ('04', 'It goes big', 'One giant version, framed and lit, on the exhibition wall.')]
ss = ''.join(f'<div class="col g12 rule-d" style="padding-top:24px"><p class="lab acc">{a}</p><h3 class="t t36">{b}</h3><p class="small mute">{c}</p></div>' for a, b, c in steps)
d.add('giant', sec('giant', '', f'''<img src="{d.m('pc/giant-framed.jpg')}" alt="A giant backlit framed artwork by Polygon1993" style="position:absolute;left:1180px;top:0px;width:740px;height:1080px;object-fit:cover">
<img src="{d.m('pc/new-world.jpg')}" alt="NEW WORLD card by CA Chou" class="frame" style="position:absolute;left:1040px;top:500px;width:300px;height:418px;object-fit:cover">
<div class="col g24 in" style="width:880px"><p class="lab acc">How a card is born</p><h2 class="t t112">One drawing.<br>One card.<br>One giant.</h2></div>
<div class="col g32" style="width:880px">
<div class="in2" style="display:grid;grid-template-columns:1fr 1fr;column-gap:48px;row-gap:32px">{ss}</div>
<p class="lab">Revealed on stage in Lisbon, 27 May 2027.</p>
</div>
{d.foot(7)}''', 'You draw one original illustration, your subject, your style. Polygon1993 turns it into a PHANTASM card: frame, foil, your name on it. It exists twice: 100 numbered printed cards, and their online twins. And it goes big: one giant version, framed and lit, on the exhibition wall. Revealed on stage in Lisbon, 27 May 2027.'))

pause_video(d, 'reveal', VID('art-factory-rez-de-chaussee'), 'Kawaii Summit 2027', 'Revealed on stage.<br>27 May.',
      'Your card is revealed on stage in Lisbon on 27 May 2027, in front of everyone.', 'An immersive installation in the Art Factory at NFC Summit 2026', poster='px/factory-immersive.jpg')

# 08 the deal
yours = [('01', 'Draw the card.'), ('02', 'Come to Lisbon.'), ('03', 'Tell your community.')]
ours = [('Before', 'We announce your card and open the pre-sale.'), ('During', 'We fly you to Lisbon and host you. You speak on stage, you get your own table to show and sign your card. We sell it on site.'), ('After', 'Your card joins the PHANTASM exhibition: two months in a Lisbon gallery.')]
yy = ''.join(f'<div class="row g24 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc" style="width:44px;flex:none">{a}</p><h3 class="t t64">{b}</h3></div>' for a, b in yours)
oo = ''.join(f'<div class="col g12 rule" style="padding:24px 0"><p class="lab acc">{a}</p><p class="body">{b}</p></div>' for a, b in ours)
d.add('deal', sec('deal', 'paper', f'''<div class="panel"></div>
<div class="col" style="width:688px;justify-content:space-between">
<div class="col g24 in"><p class="lab acc">The deal</p><h2 class="t t120">Your part.</h2></div>
<div class="col in2">{yy}</div>
</div>
<div style="width:192px;flex:none"></div>
<div class="col" style="flex:1;justify-content:space-between">
<div class="col g24 in"><p class="lab acc">&nbsp;</p><h2 class="t t120">Our part.</h2></div>
<div class="col in3">{oo}</div>
</div>
{d.foot(8)}''', 'Your part: draw the card, come to Lisbon, tell your community. Our part: before, we announce your card and open the pre-sale. During, we fly you to Lisbon and host you; you speak on stage; you get your own table to show and sign your card; we sell it on site. After, your card joins the PHANTASM exhibition, two months in a Lisbon gallery.', ' style="flex-direction:row"'))

# 09 be the next card
tl = [('Now', 'We talk and pick the subject of your card.'), ('End of February', 'You deliver the drawing.'), ('March', 'Your card is announced, pre-sale opens.'), ('27 May', 'Your card is revealed in Lisbon.'), ('June — July', 'The PHANTASM exhibition, in a Lisbon gallery.')]
tt = ''.join(f'<div class="col g16"><div class="sq"></div><p class="t t48">{a}</p><p class="small mute">{b}</p></div>' for a, b in tl)
w = 330; h = round(w / RATIO['kawaii-summit'])
d.add('next', sec('next', '', f'''<img src="{d.m(DR('kawaii-summit'))}" alt="The Kawaii Summit dragon" style="position:absolute;left:{1824 - w}px;top:64px;width:{w}px;height:{h}px;object-fit:contain">
<div class="col g24 in" style="width:1300px"><p class="lab acc">How it happens</p><h2 class="t t168">Be the next card.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(5, 1fr);column-gap:40px">{tt}</div>
<div class="row in3" style="justify-content:space-between;align-items:flex-end">
<p class="t t64" style="width:900px">Three new cards in 2027.<br>One of them is yours.</p>
<div class="col g8" style="width:760px"><p class="lab acc">Talk to John first</p><p class="lab">john@nonfungibleconference.com · t.me/thejonnkarp</p></div>
</div>
{d.foot(9)}''', 'Three new cards in 2027, one of them is yours. Now: we talk and pick the subject. End of February: you deliver the drawing. March: your card is announced and the pre-sale opens. 27 May: revealed in Lisbon. June and July: the PHANTASM exhibition in a Lisbon gallery. Talk to John Karp first.'))

SECTIONS = {"nfc": {"description": "NFC Summit and Kawaii Summit.", "start": "cover"},
            "partner": {"description": "Polygon1993 and PHANTASM, the card game.", "start": "artist"},
            "invitation": {"description": "Your card: how it is made and the deal.", "start": "invite"},
            "next": {"description": "Timeline and contact.", "start": "next"}}

if __name__ == '__main__':
    render_html(d, 'ac_preview.html', X)
    print(list(d.media))
