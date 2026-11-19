import sys; sys.path.insert(0, '.')
from nfclib import *
d = Deck('fp', 'FAIR PLAY — the AI fun fair')

cover(d, 'cover', 'aff/fair-drone.jpg', 'A season in Lisbon · February — October 2027', 'FAIR PLAY',
      'The AI fun fair, built by artists. You play with AI to see how it decides.', 'Concept visual · the fair at sunset',
      'FAIR PLAY is a fairground where every ride is an artwork and every ride runs on AI. It opens at NFC Summit in Lisbon, 27 to 29 May 2027, travels across the city during the summer and ends during Devcon week in October. This deck presents the idea, the rides, the season and what a founding partner brings and gets.',
      'Concept visual: FAIR PLAY at sunset, seen from above, its stalls wrapped in artwork')
vstatement(d, 'fear', VID('place-totem-et-mur'), 'Most people have never seen AI decide.', 'They read about it. They have never played with it.',
      'The starting point: AI already decides a lot for us, and the public debate is stuck between fear and hype. Museums show the critical side. Nobody shows the side where people put their hands on it.',
      'The central plaza of NFC Summit 2026: a digital art totem in front of the pixel portraits of the Wall')
vstatement(d, 'fair', VID('mur-crane-pixel'), 'So artists built a fairground.', 'Every ride is an artwork. Every ride runs on AI.',
      'A fairground is the best setting there is to talk about decisions: you try your luck, you trust a fortune-teller, you aim, you bet, you follow the crowd. Each classic ride becomes a question asked to AI, and the visitor answers by playing.',
      'A giant pixel skull painted on a facade at the Unicorn Factory, filmed by drone')
rows = ''.join(f'<div class="row g32 rule" style="padding:28px 0;align-items:baseline"><h3 class="t t64" style="width:330px;flex:none">{t}</h3><p class="body">{s}</p></div>' for t, s in [
      ('Fair', 'The fairground: rides, lights, prizes and a crowd.'),
      ('Fairness', 'How a machine decides, and whether it decides well.'),
      ('Play', 'You learn it with your hands, in one minute.')])
statement_light(d, 'name', 'The name', '<span style="display:block;line-height:1">Two words,<br>three ideas</span>', rows,
      'Three meanings in two words. Fair: the fairground. Fairness: the word AI research uses for whether an algorithm treats everyone equally. Play: the promise. The show is AI-positive: it does not denounce, it lets people practise.', 4)
pause_dragon(d, 'rule', 'art-fun-fair', 'The rule', 'Everyone leaves<br>with art.',
      'You always pay for an artwork, never for a chance. Every play gives a print. The target score gives an edition. The best score of the day takes the 1/1.', side='right', h=980)
mach = [('aff/at-photobooth.jpg', 'Concept visual: an artist photobooth, a wooden cabin wrapped in artwork', '01', 'Photobooth', 'Your portrait, remade by the artist’s model.', 'Ten booths, ten artists.'),
        ('aff/at-arcade.jpg', 'Concept visual: an arcade cabinet wrapped in an artist’s work', '02', 'Arcade', 'A 90-second game. Your score generates your artwork.', 'Ten cabinets, ten artists.'),
        ('aff/at-claw.jpg', 'Concept visual: a claw machine full of capsules, wrapped in an artist’s work', '03', 'Claw', 'A real claw. You fish for capsules full of art.', 'Ten machines, ten artists.')]
mm = ''.join(f'<div class="col g16"><img src="{d.m(k)}" alt="{a}" style="width:100%;height:380px;object-fit:cover"><p class="lab acc">{n}</p><h3 class="t t64">{t}</h3><p class="body mute">{s}</p><p class="small">{b}</p></div>' for k, a, n, t, s, b in mach)
d.add('machines', sec('machines', '', f'''<div class="col g24 in"><p class="lab acc">The heart of the fair · concept visuals</p><h2 class="t t120">Three machines, thirty artists</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(3, 1fr);column-gap:48px">{mm}</div>
{d.foot(6)}''', 'The crowd comes for three simple machines, each made in series, one artist per machine: about ten photobooths, ten arcade cabinets, ten claws. Same hardware, thirty different worlds. Photobooth: your portrait comes out in the artist’s world. Arcade: a short game, and your score decides the artwork you get, generated on the spot. Claw: capsules full of prints, objects, editions and one unique piece.'))
rows = ''.join(f'<div class="row g32 rule" style="padding:24px 0;align-items:baseline"><p class="lab acc">{n}</p><div class="col g8"><h3 class="t t48">{t}</h3><p class="small">{s}</p></div></div>' for n, t, s in [
      ('01', 'Pay', 'Tap a card or a phone. No app, no account.'), ('02', 'Play', 'Sixty to ninety seconds. A camera watches you.'),
      ('03', 'Generate', 'AI turns your face and your score into a piece in the artist’s world.'), ('04', 'Win', 'Everyone gets a print. Beat the target for an edition.')])
statement_light(d, 'how', 'How every machine works', '<span style="display:block;line-height:1">One minute,<br>one artwork</span>', rows,
      'Same four beats on every machine. Pay: tap a card or a phone. Play: sixty to ninety seconds, filmed. Generate: the partner’s model turns the player’s photo and performance into a piece in the artist’s style; on the shooting stands, the piece mixes the score and a capture taken at the moment of the shot. Win: everyone gets a print, the target score gives an edition, the best score of the day a 1/1.', 7,
      sentence='You pay for an artwork, never for a chance.')
pause_video(d, 'signature', VID('art-factory-rez-de-chaussee'), 'Beyond the machines', 'Eight rides<br>that ask a question.',
      'Next to the machines that make the crowd, eight signature rides. Each one takes a fairground classic and turns it into a question about how AI decides.', 'The flour mill machines of the Art Factory at NFC Summit 2026', poster='px/factory-immersive.jpg')
def rides(sid, label, title, items, n, note):
    cells = ''.join(f'<div class="col g16 rule-d" style="padding-top:28px"><p class="lab mute">{a}</p><h3 class="t t64">{t}</h3><p class="lab acc">{q}</p><p class="body mute">{b}</p></div>' for a, t, q, b in items)
    d.add(sid, sec(sid, '', f'''<div class="col g24 in"><p class="lab acc">{label}</p><h2 class="t t120">{title}</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:48px">{cells}</div>
{d.foot(n)}''', note))
rides('rides-a', 'Signature rides · 1 to 4', 'Play the question', [
      ('01', 'The Oracle', 'Why do we trust a voice?', 'Three fortune-tellers: one finds your match, one tells your future, one shows what the web says about you.'),
      ('02', 'The Wheel of Odds', 'Chance or prediction?', 'The AI calls where the wheel will stop. You bet with it or against it, in points.'),
      ('03', 'The Two-Hand Claw', 'When do you delegate?', 'You steer, the AI steers, or the crowd votes. Three modes, three scores on the board.'),
      ('04', 'The Hall of Doubles', 'What am I to a model?', 'Every mirror remakes you differently. You choose the double you keep.')], 9,
      'The Oracle comes in three characters: a slightly scary fortune-teller who asks you questions and names your best match; one who tells your future from nothing; and one who, with your consent, shows what the public web says about you from your name alone, on a private screen. The Wheel of Odds: the model announces its prediction before each spin; bets are in points, never money. The Two-Hand Claw: the same claw, driven by you, by the AI or by the crowd. The Hall of Doubles: a corridor of mirrors, each one a different model’s idea of you.')
rides('rides-b', 'Signature rides · 5 to 8', 'Four more', [
      ('05', 'The Train of Layers', 'What happens inside?', 'A dark ride through a model, from the raw image to the decision.'),
      ('06', 'The Agents’ Arena', 'What is a fair rule?', 'AI agents compete under different rules. The crowd rewrites them between rounds.'),
      ('07', 'The Robot Portraitist', 'Who is the author?', 'You sit. A robot looks at you and draws. You leave with the drawing.'),
      ('08', 'The Dance Mirror', 'Who leads, who follows?', 'An artist’s choreography to copy. The mirror scores your moves and prints them.')], 10,
      'The Train of Layers is the big walk-through piece, built in a shipping container. The Agents’ Arena is still being designed: the principle is agents with different rules, and a public that changes the rules. The Robot Portraitist: a drawing robot on the path of the fair. The Dance Mirror: a choreography to reproduce, made with an artist; the picture of your movement is the prize.')
wild = [('aff/at-shooting.jpg', 'Concept visual: a shooting gallery with painted cans and a screen', 'Shooting gallery', 'Your shot and a photo of the moment become one piece.'),
        ('aff/at-paintball.jpg', 'Concept visual: a player shooting paint at a printed artwork roll', 'Paintball roll', 'The splashes become a new work.'),
        ('aff/at-punch.jpg', 'Concept visual: a punching bag in a wrapped booth with a column of score lights', 'The punch', 'Your strike sets off the render.')]
ww = ''.join(f'<div class="col g12"><img src="{d.m(k)}" alt="{a}" style="width:100%;height:300px;object-fit:cover"><h3 class="t t48">{t}</h3><p class="body mute">{s}</p></div>' for k, a, t, s in wild)
more = ''.join(f'<p class="t t48 rule" style="padding:18px 0">{x}</p>' for x in ['Knock-down', 'Darts', 'Duck pond', 'Pixel wall', 'Scratch wall'])
d.add('classics', sec('classics', '', f'''<div class="col g24 in"><p class="lab acc">And the classics, remade by artists · concept visuals</p><h2 class="t t120">The whole fairground</h2></div>
<div class="in2" style="display:grid;grid-template-columns:repeat(4, 1fr);column-gap:40px;align-items:end">{ww}<div class="col">{more}</div></div>
{d.foot(11)}''', 'The rest of the fairground uses the same camera, payment and print as the three machines. Shooting gallery and knock-down: the artwork mixes the player’s performance and a capture taken at the moment of the shot. Paintball roll: the splashes on a printed roll become a new digital piece. The punch: force and gesture set off the render. Also darts, a duck pond, a pixel wall that the crowd fills over three days, and a scratch wall where a portrait appears under your hands.'))
pause_dragon(d, 'season', 'ringmaster-hero', 'February — October 2027', 'One season.<br>One city.',
      'A pause before the calendar. FAIR PLAY is not a three-day stand: it is a season in Lisbon.', side='right', h=980)
timeline(d, 'calendar', 'The season', 'From the jams to Devcon week', [
      ('February', 'Online art jams: anyone can prototype a ride'),
      ('March — May', 'Residencies: the artists build with the partner’s tools'),
      ('27 — 29 May', 'Premiere at NFC Summit, Unicorn Factory, Lisbon'),
      ('June — September', 'The fair travels across Lisbon'),
      ('October', 'Finale during Devcon week, in Lisbon')],
      'February: four online art jams, open to everyone, one theme each; the best prototypes win a residency. March to May: eight to twelve projects built with the partner’s tools and engineers. 27 to 29 May: the fair opens on the central plaza of NFC Summit. Summer: it travels across Lisbon. October: the finale, during the week Devcon brings the Ethereum ecosystem to Lisbon. Web Summit follows in November, in the same city.', 13,
      line='One partnership, four audiences: digital art, Lisbon, Ethereum, tech.')
figures(d, 'crowd', PH('place-centrale-visiteuses'), 'NFC Summit 2026 · final report', 'The crowd is already there',
      [('2,740', 'Visitors in 2026'), ('79', 'Countries'), ('200+', 'Artists exhibited'), ('150+', 'Speakers'),
       ('1,000', 'Artists in the NFC network'), ('6M+', 'Organic impressions')],
      'NFC Summit is in its sixth edition. In 2026: 2,740 visitors from 79 countries, more than 200 artists exhibited, more than 150 speakers, 6M+ organic impressions. Around 1,000 artists in the network, many already fluent with AI.',
      'Visitors on the central plaza of the Unicorn Factory, NFC Summit 2026', 14, 'Source: NFC Summit 2026 final report')
deal(d, 'partner', ['Your models inside the rides.', 'Your team in the residencies.', 'Your name on the season.'],
     [('The artists', 'A curated line-up from the NFC network, paid and credited.'), ('The fair', 'Machines, booths, staff, payment and printing.'), ('The audiences', 'Digital art in May, Lisbon all summer, Ethereum in October.')],
     'For one founding partner. Your part: your models generate the artworks inside the rides, your engineers and artists take part in the residencies and the onboarding sessions, your name signs the season. Our part: the artists, the production of the fair, and the audiences. Nothing is used to train a model without the written agreement of the artist.', 15, label='For a founding partner')
world(d, 'curated', PH('hall-galeries'), 'Independent', 'Curated, not sponsored.', 'A curator chooses the artists. The partner never does. That is why artists say yes.',
      'FAIR PLAY is an exhibition, with a curator who chooses the artists and writes the intention. The partner does not choose the artists and does not review the works. This independence is what makes the project credible for artists and for the press.',
      'A hall of galleries at NFC Summit 2026', 16)
closing(d, 'close', 'FAIR PLAY · Lisbon 2027', 'Build a ride', ['A 20-minute call, then a proposal made for your team.'],
      'Next step: a 20-minute call with John, then a proposal.', contact='John Karp · john@nonfungibleconference.com · t.me/thejonnkarp')
SECTIONS = {"idea": {"description": "Why a fairground about AI, and the name.", "start": "cover"},
            "rides": {"description": "The three machines, the eight signature rides and the classics.", "start": "rule"},
            "season": {"description": "The calendar, the audience and what a founding partner brings and gets.", "start": "season"},
            "close": {"description": "Contact.", "start": "close"}}
