# NFC Summit 2027 — les decks de l'équipe

Le site interne où l'équipe NFC retrouve, présente et partage les cinq decks 2027 :

| Deck | Pour qui | Slides |
|---|---|---|
| General Presentation | Tout le monde : partenaires, presse, sponsors, speakers | 23 |
| CryptoStamp Corner | Postes et émetteurs de timbres numériques | 9 |
| NFC Artist Cards — Kawaii × PHANTASM | Artistes invités à dessiner une carte | 11 |
| NFC Collection Cards | Collections NFT et PFP | 14 |
| NFC Street Activations — On The Wall | Sponsors, galeries, plateformes, communautés | 29 |

Chaque deck se présente en plein écran dans le navigateur (flèches, **F** plein écran, **N** notes, **G** toutes les slides, glisser sur téléphone), se télécharge en PDF, et a son propre lien à envoyer.

## Mise en ligne

Le site est statique : la page d'accueil est `index.html` à la racine, chaque deck est dans `decks/<nom>/`.
Si le repo est déjà relié à Vercel (c'était le cas pour le deck v7), chaque `git push` sur `main` remet le site à jour tout seul.
Sinon, une seule fois sur [vercel.com](https://vercel.com) : **Add New → Project**, importer `slides`, Framework **Other**, pas de commande de build, dossier de sortie : la racine. **Deploy**.

Le site n'est pas référencé par Google (`noindex`), mais toute personne qui a le lien peut l'ouvrir, et **le repo est public** : tout ce qui est commité ici est lisible sur GitHub. Pour un mot de passe sur le site, il faut l'option *Deployment Protection* de Vercel (plan Pro).

## Modifier un deck avec Claude Code

Dans le dossier du repo, lancer `claude`, puis par exemple :

```
/update-deck Street Activations : remplace "Your wall is waiting." par "Pick your wall."
/update-deck GP : ajoute une slide pause avec le dragon Parties avant "Every night, everywhere."
```

Claude modifie la source du deck, reconstruit le site et les PDF, vérifie les slides touchées, puis pousse : Vercel publie dans la minute.
Tout est expliqué pour Claude dans `CLAUDE.md` (organisation du repo, règles du design system).

Sans Claude Code :

```bash
pip3 install playwright pillow && python3 -m playwright install chromium   # la première fois
python3 src/build_site.py && python3 src/render.py
git add -A && git commit -m "…" && git push
```

## Les originaux sur claude.ai

Les cinq decks existent aussi en version modifiable sur claude.ai (compte de John), reliés au design system NFC Summit 2027. Ce repo ne les met pas à jour : pour reporter un changement là-bas, le demander à Claude dans le projet « Nfc 27 ».

## L'ancien deck Street Activations v7 (septembre 2026)

Les fichiers déjà présents à la racine avant le site (`NFC Street Activations.dc.html`, les `.mp4`, `compressed/`, `uploads/`, `_ds/`, `assets/dragons/`, `deck-stage.js`, `image-slot.js`, `support.js`) forment l'ancien deck v7. Il reste en ligne à son adresse (`/NFC Street Activations.dc.html`) ; seule la racine du site montre désormais la page d'équipe. Ne pas déplacer ces fichiers : ses vidéos sont chargées depuis `raw.githubusercontent.com/hs7j4yk4sz-boop/slides/main/…`. La version à jour du deck est `decks/street-activations/`.
