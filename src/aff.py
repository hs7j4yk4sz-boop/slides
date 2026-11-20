import sys; sys.path.insert(0, '.')
from nfclib import *
# FAIR PLAY for artists and galleries: the fair, the machines, and the three ways in.
d = Deck('aff', 'NFC Summit 2027 — FAIR PLAY · Build a ride')

def credit(sid, text='Filmed at NFC Summit 2026, Lisbon'):
    """A discreet credit on a video slide, bottom right."""
    i = [x for x, _ in d.slides].index(sid); h = d.slides[i][1]; k = h.rindex('</section>')
    d.slides[i] = (sid, h[:k] + f'<p class="small" style="position:absolute;right:96px;bottom:64px;margin:0;opacity:.72;text-align:right">{text}</p>\n' + h[k:])

def screen(text, size=150, fs=30, style=''):
    """A small square screen on the side of a machine: what the AI does, in three words."""
    return (f'<div style="width:{size}px;height:{size}px;flex:none;box-sizing:border-box;border:4px solid var(--yellow);border-radius:14px;background:#0B0B0B '
            f'repeating-linear-gradient(0deg, rgba(246,184,0,.10) 0 2px, transparent 2px 6px);box-shadow:0 0 28px rgba(246,184,0,.35);display:flex;align-items:center;justify-content:center;{style}">'
            f'<p class="t" style="font-size:{fs}px;line-height:1.06;letter-spacing:0;text-align:center;color:var(--yellow)">{text}</p></div>')

cover(d, 'cover', VID('art-factory-c'), 'New at NFC Summit 2027 · 27 — 29 May · Lisbon', 'FAIR PLAY',
      'An art fairground that runs on AI. Every ride is built by an artist. Build yours.', 'For artists and galleries',
      'FAIR PLAY is new in 2027: an art fairground that runs on AI. Artists build the rides, AI runs inside them, and every player leaves with an artwork. It opens on the central plaza of the Unicorn Factory during NFC Summit, 27 to 29 May 2027, then lives through the year in Lisbon. This deck is for artists and galleries: the fair, the machines, who does what, then the three ways in. The offers in this deck are for NFC Summit, 27 to 29 May. The partner deck of the season is a separate deck, without prices. The footage is the Art Factory at NFC Summit 2026.',
      'An artwork on a screen set into a flour mill machine, in the Art Factory at NFC Summit 2026')
credit('cover')
vstatement(d, 'plaza', VID('place-totem-et-mur'), 'Everyone walks through it.', 'The fair sits on the central plaza, between the stages and the Art Factory.',
      'Location: the central plaza of the Unicorn Factory. Every visitor crosses it between the main stage, the Art Factory and Kawaii Summit. 2,740 visitors in 2026, from 79 countries.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement(d, 'built', VID('mur-crane-pixel'), 'Every ride is built by an artist.', 'Not a game with art on it. An artwork you can play.',
      'The idea: digital artists already make worlds. The fair gives each of them a machine, a booth and a crowd for three days.',
      'A giant pixel skull painted on a facade at the Unicorn Factory, filmed by drone')
credit('plaza'); credit('built')
family = [('1926', 'Calder’s Circus', 'A miniature fair, performed by the artist himself.', ''),
          ('1959', 'Tinguely’s machines', 'Machines that draw. Visitors made 4,000 drawings.', ''),
          ('1987', 'Luna Luna', 'Haring’s carousel, Basquiat’s Ferris wheel, Dalí’s pavilion.', ''),
          ('2027', 'FAIR PLAY', 'The same fair, with the machines of our time.', ' acc')]
ff = ''.join(f'<div class="col g16"><div class="bar"></div><p class="t t150{c}" style="line-height:.9">{y}</p><h3 class="t t64{c}">{n}</h3><p class="body">{b}</p></div>' for y, n, b, c in family)
d.add('family', sec('family', '', f"""<div class="col g24 in"><p class="lab acc">Our family in art history</p><h2 class="t t120">Artists have always played</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:56px">{ff}</div>
<p class="lead">The next ride in this family could be yours.</p>
{d.foot(4)}""",
      'FAIR PLAY belongs to a family, and we say so. 1926: Alexander Calder builds his Circus in Paris, a miniature fair he performs himself; it is now at the Whitney Museum. 1959: Jean Tinguely shows his Méta-Matics at Galerie Iris Clert in Paris, machines that draw; visitors make about 4,000 drawings. 1961: Niki de Saint Phalle turns the shooting gallery into painting with her Tirs. 1987: Luna Luna, in Hamburg, by André Heller, the first art amusement park, with a carousel by Keith Haring, a Ferris wheel by Jean-Michel Basquiat and a pavilion by Salvador Dalí; restored and shown in Los Angeles in 2023 and New York in 2024. Every ride of ours has an ancestor: the photobooth and the Surrealists’ Photomaton portraits (1929), the shooting gallery and Niki de Saint Phalle, the arcade and the video games collected by MoMA since 2012. Sources: Whitney Museum; Wikipedia (Métamatic, Luna Luna); Smithsonian Magazine.'))
rows = ''.join(f'<div class="row g32 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc">{n}</p><div class="col g8"><h3 class="t t48">{t}</h3><p class="small">{s}</p></div></div>' for n, t, s in [
      ('01', 'Pay', 'Tap a card or a phone. No app, no account.'), ('02', 'Play', 'Sixty to ninety seconds. A camera watches you.'),
      ('03', 'Generate', 'AI turns your face and your score into a piece in the artist’s world.'), ('04', 'Win', 'Everyone gets a print. Beat the target for an edition.')])
statement_light(d, 'how', 'How every ride works', '<span style="display:block;line-height:1">One minute,<br>one artwork</span>', rows,
      'Same four beats on every ride. Pay: tap a card or a phone, no app, no account. Play: sixty to ninety seconds, a camera watches you. Generate: AI turns the player’s photo and score into a piece in the artist’s style. Win: everyone gets a print, the target score gives an edition, the best score of the day a 1/1. You pay for an artwork, never for a chance: that is the rule of the fair.', 5,
      sentence='You pay for an artwork, never for a chance.')
pause_dragon(d, 'rule', 'art-fun-fair', 'The rule', 'Everyone leaves<br>with art.',
      'You always pay for an artwork, never for a chance. Every play gives a print. The target score gives an edition. The best score of the day takes the 1/1.', side='right', h=980)
mach = [('fp/cut-photobooth.png', 'Photobooth', 'AI<br>photo<br>booth', 'Pull the curtain, sit down. Your portrait comes out in the artist’s world.', 'You bring 10 to 20 works and a print frame.', 'Concept model of a handmade photobooth in black and yellow plywood'),
        ('fp/cut-arcade.png', 'Arcade', 'Play<br>to<br>art', 'A 90-second game with your name on it. The better they play, the better the artwork.', 'You bring a game on our template, or the art.', 'Concept model of a handmade arcade cabinet in black and yellow plywood'),
        ('fp/cut-claw.png', 'Claw', 'Grab<br>a<br>print', 'A real crane machine. People fish for a print that exists only once.', 'You bring your works, a few editions and one unique piece.', 'Concept model of a handmade claw machine filled with rolled prints')]
mm = ''.join(f'<div class="col g16"><div class="row" style="align-items:flex-start;height:380px"><img src="{d.m(k)}" alt="{a}" style="height:380px;width:auto;flex:none">{screen(sc, 160, 32, "margin:40px 0 0 -18px")}</div><h3 class="t t64">{t}</h3><p class="body mute">{l}</p><p class="small">{b}</p></div>' for k, t, sc, l, b, a in mach)
d.add('machines', sec('machines', '', f"""<div class="col g24 in"><p class="lab acc">Any artist can take one · concept models</p><h2 class="t t120">Three machines</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:56px;align-items:start">{mm}</div>
{d.foot(7)}""", 'Three machines any artist can take, each with a small screen on its side that says what the AI does. Photobooth: pull the curtain, sit down, your portrait comes out in the artist’s world; the artist brings 10 to 20 works and a print frame, no code, no game. Arcade: a cabinet in your colours, a 90-second game with your name on it, and the score shapes the artwork; bring a game on our template, or the art and we pair you with a developer. Claw: a real crane machine, people fish for a print that exists only once; bring your works, a few editions and one unique piece. The machines are built by hand, in plywood. The objects shown are concept models, not built yet, and the screens are illustrations.'))
wild = [('The Oracle', 'A fortune-teller cabin. Behind the curtain, a voice answers, and shows why.'),
        ('Shooting gallery', 'Targets painted by you. Each shot is caught on camera and becomes the piece.'),
        ('Paintball roll', 'Players shoot paint at your printed roll. The splashes become a new piece.'),
        ('The mirror', 'A tall screen. Your algorithm follows the visitor’s moves.'),
        ('Your own machine', 'Bring it: we plug it into the fair.')]
ww = ''.join(f'<div class="row g32 rule" style="padding:18px 0;align-items:baseline"><h3 class="t t48" style="width:440px;flex:none">{t}</h3><p class="body mute">{s}</p></div>' for t, s in wild)
d.add('wild', sec('wild', '', f"""<div class="col g24 in"><p class="lab acc">For those who want more · concept model</p><h2 class="t t120">The signature rides</h2></div>
<div class="row in2" style="gap:72px;align-items:flex-start;margin-top:40px">
<div class="row" style="align-items:flex-start;flex:none"><img src="{d.m('fp/cut-oracle.png')}" alt="Concept model of a handmade fortune-teller cabin with a curtain and stars" style="height:440px;width:auto;flex:none">{screen('Ask<br>the<br>AI', 160, 32, 'margin:48px 0 0 -18px')}</div>
<div class="col" style="flex:1">{ww}</div></div>
{d.foot(8)}""", 'The signature rides, for artists and galleries who want a bigger show. Same camera, payment and print as the first three. The Oracle: a fortune-teller cabin where a voice answers behind a curtain. A shooting gallery: targets painted by the artist, each shot caught on camera and turned into the piece. A paintball roll: the splashes on the printed work become a new digital piece. The mirror: no game, the artist’s algorithm follows the visitor. Or bring your own machine: we plug it into the fair. These are built with the artist, on a quote.'))
deal(d, 'split', ['10 to 20 works that define your style.', 'The art for your booth and your print frame.', 'The price of a play, on your own ride.'],
     [('The machine', 'Built, tested, and a wooden booth dressed in your colours.'), ('The tech', 'Contactless payment and colour printing.'), ('The crowd', 'The software, the staff and every visitor of NFC.')],
     'Who does what. You bring the world: 10 to 20 works that define your style, the art for your booth and your print frame, the prizes on your own ride (a small edition and a 1/1), and for the arcade a game or its art. On your own ride you set the price of a play, and you can sell your works at your stand. We bring the machine: built and tested, a wooden booth in your colours, contactless payment and colour printing, the software, the staff and the crowd. The ask is files, not hardware.', 9, label='Who does what')
pause_video(d, 'ways', VID('art-factory-rez-de-chaussee'), 'Our partners fund the fair · artists only cover the costs', 'Three ways in.',
      'Three ways in: a shared machine for artists, your own stand for artists and galleries, and the fair at NFC Summit for one brand. The partners of FAIR PLAY fund the fair; what an artist pays is only the cost of the package: the place, the machine, the passes. Every way in comes with a sponsor level of NFC Summit and its perks.', 'The flour mill machines of the Art Factory at NFC Summit 2026', poster='px/factory-immersive.jpg')
credit('ways')
cut = lambda k, sc, h=560: f'<div class="row" style="align-items:flex-start"><img src="{d.m(k)}" alt="" style="height:{h}px;width:auto;flex:none">{screen(sc, 150, 30, "margin:56px 0 0 -18px")}</div>'
four = '<div style="display:grid;grid-template-columns:auto auto;gap:28px 36px;justify-items:center;align-items:end">' + ''.join(f'<img src="{d.m(k)}" alt="" style="height:300px;width:auto">' for k in ['fp/cut-photobooth.png', 'fp/cut-arcade.png', 'fp/cut-claw.png', 'fp/cut-oracle.png']) + '</div>'
EARLY = 'Early-bird price until 31 December, excl. VAT'
visual_offer(d, 'shared', cut('fp/cut-arcade.png', 'Play<br>to<br>art'), 'For artists · 1 of 3', 'Shared attraction', 'The easy way in: your art inside a machine you share with other artists',
      [('1', 'machine', 'Your world on a machine shared with other artists'), ('50/50', 'plays', 'The revenue of your plays, shared with NFC'),
       ('3', 'days', 'Thursday to Saturday. We run the machine')],
      '€250', 'Per artist', 'Exhibited artist',
      ['1 three-day pass', 'Your name on the website', 'In the official artist list', 'Shared post on social media'],
      'Shared attraction, €250 per artist, 50 places: your art on the machine and on the prints players win; the revenue of your plays is shared 50/50 with NFC; open the three days, Thursday to Saturday, and we run the machine. Your level is Exhibited artist of NFC Summit 2027: one three-day pass, your name on the website and in the official artist list, a shared post on social media.', cta=EARLY)
visual_offer(d, 'dedicated', cut('fp/cut-photobooth.png', 'AI<br>photo<br>booth', 480), 'For artists and galleries · 2 of 3', 'Your own ride', 'A stand in your name: we bring the machine, you bring the world',
      [('2 m²', 'stand', 'A 1 × 2 m stand, a claw, an arcade or a photobooth'), ('100%', 'yours', 'Every play, and every work you sell at your stand'),
       ('Your', 'price', 'You set the price of a play. Prints included')],
      '€3,000', 'Bronze', 'Bronze',
      ['Logo: website and sponsor wall', 'Shared post on social media', '6 three-day passes', '10 codes at −50%'],
      'Your own ride, €3,000, Bronze sponsor of NFC Summit 2027: your own 1 × 2 m stand dressed in your world, one machine built on our base (a claw, an arcade or a photobooth). You set the price of a play and keep 100% of it. You can also sell your works and editions at your stand: 100% yours. Colour prints are included, and your best score wins a 1/1. Bronze perks: your logo on the website and on the sponsor wall, 6 three-day passes, 10 codes at −50% for your community, a shared post on social media.', cta=EARLY)
visual_offer(d, 'presenting', four, 'For brands · 3 of 3', 'Presenting partner', '“FAIR PLAY at NFC Summit, presented by you”. One brand only',
      [('3', 'days', 'The fair at NFC Summit, 27 to 29 May, in your name'), ('All', 'signage', 'On the fair, the agenda, Luma and the posts'),
       ('10', 'minutes', 'On the main stage')],
      '€30,000', 'Platinum · 1 partner', 'Platinum',
      ['Logo: website and sponsor wall', '4 posts and 1 video', 'Dedicated email', '20 three-day passes', '8 VIP passes', '40 codes at −50%', '10-minute talk, main stage', 'Category exclusivity on the fair'],
      'Presenting partner, €30,000, Platinum sponsor, one brand only: “FAIR PLAY at NFC Summit, presented by you”, for the three days of the festival, 27 to 29 May, on the signage of the fair, the agenda, Luma and the posts. Category exclusivity on the fair during NFC Summit. Platinum perks: logo on the website and the sponsor wall, 4 posts and 1 video, a dedicated email, 20 three-day passes, 8 VIP passes, 40 codes at −50%, a 10-minute talk on the main stage. The season of FAIR PLAY, online from January and in Lisbon from May to November, is a separate partnership: see the FAIR PLAY season deck. Bigger machines, like a shooting gallery or paintball, or a ride built by an artist in your brand’s world: on request.', cta=EARLY)
closing(d, 'close', 'FAIR PLAY · NFC Summit 2027', 'Build a ride', ['Early-bird prices until 31 December, excl. VAT. From 1 January, every price goes up by 25%.'],
      'Next step: tell us which way in you want. We confirm what is left and send the contract. The fair is open the three days of NFC Summit, Thursday 27 to Saturday 29 May, on the central plaza in Beato.', contact='John Karp · john@nonfungibleconference.com · t.me/thejonnkarp')
SECTIONS = {"fair": {"description": "The fair: where it is and the family it belongs to.", "start": "cover"},
            "machines": {"description": "The machines and who does what.", "start": "how"},
            "offers": {"description": "Three ways in, from €250 to €30,000.", "start": "ways"},
            "close": {"description": "Contact.", "start": "close"}}
