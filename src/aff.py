import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('aff', 'NFC Summit 2027 — Art Fun Fair')

cover(d, 'cover', 'aff/fair-drone.jpg', 'New at NFC Summit 2027 · 27 — 29 May · Lisbon', 'Art Fun Fair',
      'Play the art. A fairground in the middle of the festival, where every ride is built by an artist.', 'Concept visual · the fair at sunset',
      'Art Fun Fair is new in 2027: a fairground on the central plaza of the Unicorn Factory, open all three days. Every ride is built with an artist: a claw, an arcade, a photobooth. Every player leaves with a print. This deck presents the fair, then the three ways in: for artists, for galleries, for one brand.',
      'Concept visual: the Art Fun Fair at sunset, seen from above, its stalls wrapped in artwork')
vstatement(d, 'plaza', VID('place-totem-et-mur'), 'Everyone walks through it.', 'The fair sits on the central plaza, between the stages and the Art Factory.',
      'Location: the central plaza of the Unicorn Factory. Every visitor crosses it between the main stage, the Art Factory and Kawaii Summit. 2,740 visitors in 2026, from 79 countries.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement(d, 'built', VID('mur-crane-pixel'), 'Every ride is built by an artist.', 'Not a game with art on it. An artwork you can play.',
      'The idea: digital artists already make worlds. The fair gives each of them a machine, a booth and a crowd for three days.',
      'A giant pixel skull painted on a facade at the Unicorn Factory, filmed by drone')
rows = ''.join(f'<div class="row g32 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc">{n}</p><div class="col g8"><h3 class="t t48">{t}</h3><p class="small">{s}</p></div></div>' for n, t, s in [
      ('01', 'Pay', 'Tap a card or a phone. No app, no account.'), ('02', 'Play', 'Sixty to ninety seconds. A camera watches you.'),
      ('03', 'Print', 'Your face and your score become a piece in the artist’s world.'), ('04', 'Win', 'Beat the target for an edition. Top the board for a 1/1.')])
statement_light(d, 'how', 'How every attraction works', 'One minute, one artwork', rows,
      'Same four beats on every machine. Pay: tap a card or a phone, no app, no account. Play: sixty to ninety seconds, a camera watches you. Print: your face and your score become a piece in the artist’s world. Win: beat the target score for an edition, top the board of the day for a 1/1.', 4,
      sentence='Open all three days, on the central plaza.')
pause_dragon(d, 'rule', 'art-fun-fair', 'The rule', 'Everyone leaves<br>with art.',
      'You always pay for an artwork, never for a chance. Every play gives a print. The target score gives an edition. The best score of the day takes the 1/1.', side='right', h=980)
mach = [('aff/at-photobooth.jpg', 'Concept visual: an artist photobooth, a wooden cabin wrapped in artwork', '01', 'Photobooth', 'Pull the curtain, sit down. Your portrait comes out in the artist’s world.', 'You bring 10 to 20 works and a print frame.'),
        ('aff/at-arcade.jpg', 'Concept visual: an arcade cabinet wrapped in an artist’s work', '02', 'Arcade', 'A cabinet in your colours, a 90-second game with your name on it.', 'You bring a game on our template, or the art.'),
        ('aff/at-claw.jpg', 'Concept visual: a claw machine full of capsules, wrapped in an artist’s work', '03', 'Claw', 'A real crane machine. People fish for capsules full of your work.', 'You bring small objects, prints, editions, one unique piece.')]
mm = ''.join(f'<div class="col g16"><img src="{d.m(k)}" alt="{a}" style="width:100%;height:380px;object-fit:cover"><p class="lab acc">{n}</p><h3 class="t t64">{t}</h3><p class="body mute">{s}</p><p class="small">{b}</p></div>' for k, a, n, t, s, b in mach)
d.add('machines', sec('machines', '', f'''<div class="col g24 in"><p class="lab acc">Any artist can take one · concept visuals</p><h2 class="t t120">Three machines</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{mm}</div>
{d.foot(6)}''', 'Photobooth: pull the curtain, sit down, your portrait comes out in the artist’s world; the artist brings 10 to 20 works and a print frame, no code, no game. Arcade: a cabinet in your colours, a 90-second game with your name on it; bring a game on our template, or the art and we pair you with a developer. Claw: a real crane machine, people fish for capsules full of your work; bring small objects, prints, a few editions and one unique piece.'))
wild = [('aff/at-shooting.jpg', 'Concept visual: a shooting gallery with painted cans and a screen', 'Shooting gallery', 'Cans and targets painted by you.'),
        ('aff/at-paintball.jpg', 'Concept visual: a player shooting paint at a printed artwork roll', 'Paintball roll', 'The splashes become a new piece.'),
        ('aff/at-punch.jpg', 'Concept visual: a punching bag in a wrapped booth with a column of score lights', 'The punch', 'Force and gesture set off the render.'),
        ('aff/at-mirror.jpg', 'Concept visual: a tall screen turning a silhouette into generative art', 'The mirror', 'Your algorithm follows the visitor.')]
ww = ''.join(f'<div class="col g12"><img src="{d.m(k)}" alt="{a}" style="width:100%;height:300px;object-fit:cover"><h3 class="t t48">{t}</h3><p class="body mute">{s}</p></div>' for k, a, t, s in wild)
d.add('wild', sec('wild', '', f'''<div class="col g24 in"><p class="lab acc">For those who want more</p><h2 class="t t120">The wild ones</h2><p class="lead">Same camera, payment and print as the first three. Bigger shows.</p></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:40px">{ww}</div>
{d.foot(7)}''', 'The wild ones, for artists and brands who want a bigger show: a shooting gallery with cans and targets painted by the artist, a screen showing the shot in their style; a paintball roll where the splashes on the printed work become a new digital piece; the punch, where force and gesture set off the render, with a strength board for the plaza; the mirror, no game, the artist’s algorithm follows you. Or bring your own machine: we plug it into the fair.'))
deal(d, 'split', ['10 to 20 works that define your style.', 'The art for your booth and your print frame.', 'Prizes: a small edition and a 1/1.'],
     [('The machine', 'Built, tested, and a wooden booth dressed in your colours.'), ('The tech', 'Contactless payment and colour printing.'), ('The crowd', 'The software, the staff and every visitor of NFC.')],
     'Who does what. You bring the world: 10 to 20 works that define your style, the art for your booth and your print frame, the prizes (a small edition and a 1/1), and for the arcade a game or its art. We bring the machine: built and tested, a wooden booth in your colours, contactless payment and colour printing, the software, the staff and the crowd. The ask is files, not hardware.', 8, label='Who does what')
pause_video(d, 'ways', VID('art-factory-rez-de-chaussee'), 'Art Fun Fair 2027', 'Three ways in.',
      'Three ways in: a shared machine for artists, your own stand for artists and galleries, and the whole fair for one brand.', 'The flour mill machines of the Art Factory at NFC Summit 2026', poster='px/factory-immersive.jpg')
value_offer(d, 'shared', 'For artists · 1 of 3', 'Shared attraction', 'The easy way in: your art inside a machine you share with other artists',
      [('1', 'machine', 'Your world on a machine shared with other artists'), ('50/50', 'plays', 'The revenue of your plays, shared with NFC'),
       ('3', 'days', 'Open all festival long. We run the machine'), ('50', 'places', 'You are an exhibited artist of NFC Summit 2027')],
      '€250', 'Per artist',
      'Shared attraction, €250 per artist, 50 places: your art on the machine and on the prints players win; you are an artist of NFC Summit 2027, in the official list; the revenue of your plays is shared 50/50 with NFC; open all festival long, we run the machine.')
value_offer(d, 'dedicated', 'For artists and galleries · 2 of 3', 'Your own ride', 'We bring the machine, you bring the game',
      [('2 m²', 'stand', 'A 1 × 2 m stand, walls printed with your art'), ('1', 'machine', 'A claw, an arcade or a photobooth, built on our base'),
       ('100%', 'of plays', 'The play revenue is yours'), ('100', 'prints', 'Included. Your best score wins a 1/1')],
      '€3,000', 'Bronze',
      'Dedicated attraction, €3,000, Bronze level: your own 1 × 2 m stand dressed in your universe, one machine built on our base, 100% of the play revenue, 100 prints included. Bronze perks: 6 three-day passes, 10 codes at −50% for your community, your logo on the website.')
value_offer(d, 'presenting', 'For brands · 3 of 3', 'Presenting partner', '“Art Fun Fair presented by you”. One brand only',
      [('1', 'brand', 'Category exclusivity across the festival'), ('All', 'signage', 'Your name on signage, agenda, Luma and posts'),
       ('10', 'minutes', 'On the main stage'), ('20', 'passes', 'Plus 8 VIP, 4 posts and a video, a dedicated email')],
      '€30,000', 'Platinum · 1 partner',
      'Presenting partner, €30,000, Platinum, one brand only: “Art Fun Fair presented by you” on signage, agenda, Luma and posts; category exclusivity across the festival; 10 minutes on the main stage; Platinum perks: 20 passes, 8 VIP, 4 posts and a video, a dedicated email. Bigger machines, like a shooting gallery or paintball, or an attraction built by an artist in your brand’s world: ask us.')
closing(d, 'close', 'Art Fun Fair · NFC Summit 2027', 'Build a ride', ['Early-bird prices until 31 December, excl. VAT. From 1 January, every price goes up by 25%.'],
      'Next step: tell John which way in you want. He confirms what is left and sends the contract.', contact='John Karp · john@nonfungibleconference.com · t.me/thejonnkarp')
SECTIONS = {"fair": {"description": "The fair: where it is and how it works.", "start": "cover"},
            "machines": {"description": "The machines and who does what.", "start": "rule"},
            "offers": {"description": "Three ways in, from €250 to €30,000.", "start": "ways"},
            "close": {"description": "Contact.", "start": "close"}}
