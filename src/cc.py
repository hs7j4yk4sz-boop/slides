import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('cc', 'NFC Summit 2027 — NFC Collection Cards')
PC = MEDIA + '/pc/'
X = {f'pc/{n}.jpg': PC + n + '.jpg' for n in ['new-world', 'balan', 'march-of-the-demons', 'polygon1993', 'glitch-artwork', 'giant-framed', 'glitch-room', 'kawaii-poster']}

# 01 cover
cover(d, 'cover', 'pc/glitch-room.jpg', 'NFC Summit 2027 · 27 — 29 May · Unicorn Factory, Lisbon', 'NFC Collection Cards',
      'Your collection becomes a real card, unveiled at Europe’s leading festival for digital creative communities.', 'Kawaii Summit 2027',
      'An invitation for digital collections: one special card made with an artist, revealed on stage at NFC Summit 2027.',
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

# 04 Polygon1993
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
{d.foot(4)}''', 'Polygon1993 is a French artist and a leading figure of glitch art. He has worked with OpenAI, Bandai Namco, A$AP Rocky, Grimes, Tame Impala, Charli XCX and Pantone. Exhibitions: Tokyo 2025, Paradigm Shifters at The Harmonyst Gallery. Paris 2026, Koi No Yokan at ArtVerse Gallery, 500 people at the opening.'))

# 05 the game
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
{d.foot(5)}''', 'PHANTASM is half trading card game, half art: 140 cards by more than 30 artists. You play it (a real game, with real tournaments), you collect it (numbered editions, rare cards, foil; each card exists in print and online), you hang it (every card is an artwork, shown in galleries).', ' style="flex-direction:row;gap:96px"'))

pause_dragon(d, 'deserve', 'kawaii-summit', 'Kawaii Summit 2027', 'Your collection deserves a card.',
      'A pause before the idea: one special card for your collection, made with an artist.', side='right', h=980)

# 06 the idea — the card mock-up
d.add('idea', sec('idea', 'yellow', f'''{card_mock(d, 1240, 150, 500, 'YOUR<br>CHARACTER', 'YOUR COLLECTION', 'Kawaii Summit')}
<p class="lab acc in">The idea</p>
<div class="col g40 in2" style="width:1060px">
<h2 class="t t150">Your character.<br>A real card.</h2>
<p class="lead">One special card for your collection, made with an artist, unveiled in Lisbon on 27 May 2027.</p>
</div>
{d.foot(6)}''', 'The idea: one special card for your collection, made with an artist, unveiled on stage at NFC Summit, Lisbon, on 27 May 2027.'))

# 07 two ways in
cw = 380; ch = round(cw / 0.718); top = 1080 - 160 - ch
ways = [('A', 'Enter PHANTASM', 'Polygon1993 redraws your character in his style. It becomes a playable PHANTASM card.'),
        ('B', 'Your own event card', 'An artist from the NFC scene draws a Kawaii Summit 2027 special. Your universe, your style, a promo card for your own game.')]
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
{d.foot(7)}''', 'Two ways in. A, enter PHANTASM: Polygon1993 redraws your character in his style, and it becomes a playable PHANTASM card. B, your own event card: an artist from the NFC scene draws a Kawaii Summit 2027 special for your collection. Your universe, your style, a promo card for your own game if you have one.'))

# 08 one card, three lives
lives = [(f'<div style="width:528px;height:400px;background:var(--graphite);display:flex;align-items:center;justify-content:center"><img src="{d.m("pc/new-world.jpg")}" alt="NEW WORLD, a PHANTASM card by CA Chou" style="width:258px;height:360px;object-fit:cover"></div>', '01', 'The edition', '100 numbered printed cards, and their online twins.'),
         (f'<img src="{d.m("pc/giant-framed.jpg")}" alt="A giant backlit framed artwork by Polygon1993" style="width:528px;height:400px;object-fit:cover">', '02', 'The giant', 'One large version, framed and lit, on the exhibition wall.'),
         (f'<img src="{d.m(PH("scene-speakeuse"))}" alt="A speaker on stage at NFC Summit 2026" style="width:528px;height:400px;object-fit:cover">', '03', 'The reveal', 'On stage in Lisbon, 27 May 2027.')]
ll = ''.join(f'<div class="col">{im}<p class="lab acc" style="margin-top:28px">{a}</p><h3 class="t t48" style="margin-top:8px">{b}</h3><p class="body mute" style="margin-top:12px">{c}</p></div>' for im, a, b, c in lives)
d.add('lives', sec('lives', '', f'''<div class="col g24 in"><p class="lab acc">What you get</p><h2 class="t t120">One card. Three lives.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{ll}</div>
{d.foot(8)}''', 'One card, three lives. The edition: 100 numbered printed cards, and their online twins. The giant: one large version, framed and lit, on the exhibition wall. The reveal: on stage in Lisbon, 27 May 2027.'))

# 09 for your holders
hold = ['A physical collectible, signed by an artist.', 'A reason to meet in Lisbon.', 'A new audience: digital art collectors and card players, in the same room.']
hh = ''.join(f'<div class="row g24 rule-d" style="padding:24px 0"><p class="lab acc" style="width:44px;flex:none;margin-top:8px">{i:02d}</p><p class="lead" style="font-size:36px">{t}</p></div>' for i, t in enumerate(hold, 1))
d.add('holders', sec('holders', '', f'''<img src="{d.m(PH('kawaii-stage'))}" alt="A talk on the Kawaii Stage at NFC Summit 2026" style="position:absolute;left:1120px;top:0px;width:800px;height:1080px;object-fit:cover">
<div style="position:absolute;left:1120px;top:0px;width:320px;height:1080px;background:linear-gradient(90deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0) 100%)"></div>
<div class="col g24 in" style="width:960px"><p class="lab acc">For your holders</p><h2 class="t t120">Something your holders can hold.</h2></div>
<div class="col in2" style="width:900px">{hh}</div>
{d.foot(9)}''', 'For your holders: a physical collectible, signed by an artist. A reason to meet in Lisbon. And a new audience: digital art collectors and card players, in the same room.'))

pause_video(d, 'meet', VID('art-factory-premier-etage'), '27 May 2027 · Lisbon', 'Meet your holders<br>in Lisbon.',
      'The card is a reason for your holders to come and meet you in Lisbon, at Europe’s leading festival for digital creative communities.', 'Visitors on the first floor of the Art Factory at NFC Summit 2026', poster='px/premier-crowd.jpg')

# 10 the deal
deal(d, 'deal', ['Bring your character and approve the card.', 'Cover the production of the card and your trip.', 'Tell your community.'],
     [('Before', 'We find the artist, make the card, announce it and open the pre-sale.'), ('During', 'A slot on stage, a table to show the card, sales on site.'), ('After', 'Your card joins the exhibition: two months in a Lisbon gallery.')],
     'Your part: bring your character and approve the card, cover the production of the card and your trip, tell your community. Our part: before, we find the artist, make the card, announce it and open the pre-sale. During, a slot on stage, a table to show the card, sales on site. After, your card joins the exhibition, two months in a Lisbon gallery.', 10)

# 11 we share it
split = [('40%', 'your collection'), ('30%', 'the artist'), ('30%', 'NFC')]
sp = ''.join(f'<div class="col g12"><p class="t t150" style="color:var(--yellow)">{a}</p><p class="lab">{b}</p></div>' for a, b in split)
d.add('share', sec('share', 'blue', f'''<div class="col g32 in" style="width:1300px">
<p class="lab acc">The split</p>
<h2 class="t t150">We make it together.<br>We share it.</h2>
<p class="lead">Once production is covered, every sale is shared: the edition, the giant, the signings.</p>
</div>
<div class="col g32 in2">
<div class="row" style="gap:120px">{sp}</div>
<p class="lab">Production cost quoted per card, before you commit.</p>
</div>
{d.foot(11)}''', 'Once production is covered, every sale is shared: the edition, the giant, the signings. 40% to your collection, 30% to the artist, 30% to NFC. The production cost of the edition and the giant is quoted per card, before you commit.'))

# 12 your card in 2027
tl = [('Now', 'We talk, you pick A or B.'), ('January', 'The artist is chosen, the subject is set.'), ('March', 'The card is announced, pre-sale opens.'), ('27 May', 'The card is revealed in Lisbon.'), ('June — July', 'The exhibition, in a Lisbon gallery.')]
tt = ''.join(f'<div class="col g16"><div class="sq"></div><p class="t t48">{a}</p><p class="small mute">{b}</p></div>' for a, b in tl)
w = 330; h = round(w / RATIO['kawaii-summit'])
d.add('next', sec('next', '', f'''<img src="{d.m(DR('kawaii-summit'))}" alt="The Kawaii Summit dragon" style="position:absolute;left:{1824 - w}px;top:64px;width:{w}px;height:{h}px;object-fit:contain">
<div class="col g24 in" style="width:1300px"><p class="lab acc">How it happens</p><h2 class="t t168">Your card in 2027.</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(5, 1fr);column-gap:40px">{tt}</div>
<div class="col g12 in3"><p class="t t64">Talk to John first.</p><p class="lab">john@nonfungibleconference.com · t.me/thejonnkarp</p></div>
{d.foot(12)}''', 'Now: we talk, you pick A or B. January: the artist is chosen, the subject is set. March: the card is announced, pre-sale opens. 27 May: the card is revealed in Lisbon. June and July: the exhibition, in a Lisbon gallery. Talk to John Karp first.'))

SECTIONS = {"nfc": {"description": "NFC Summit and Kawaii Summit.", "start": "cover"},
            "game": {"description": "Polygon1993 and PHANTASM, the card game.", "start": "artist"},
            "card": {"description": "Your collection’s card: the idea, two ways in, what it becomes.", "start": "idea"},
            "deal": {"description": "The deal, the split and the timeline.", "start": "deal"}}

if __name__ == '__main__':
    render_html(d, 'cc_preview.html', X)
    print(list(d.media))
