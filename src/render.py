"""Thumbnails, covers and PDFs for every deck of the website.

    python3 src/render.py                       # all decks
    python3 src/render.py street-activations    # one deck

Run after build_site.py. Needs Playwright for Python with Chromium
(pip install playwright pillow && python3 -m playwright install chromium) and an internet
connection for the Google fonts (Anton, Space Grotesk).
Writes, per deck: decks/<slug>/thumbs/NN.jpg (480 x 270), decks/<slug>/cover.jpg (1280 x 720)
and decks/<slug>/<slug>.pdf (one 1920 x 1080 page per slide, from 1920 x 1080 captures).
"""
import io, json, os, sys
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def render(page, slug):
    folder = os.path.join(ROOT, 'decks', slug)
    page.goto('file://' + os.path.join(folder, 'index.html') + '?print')
    page.wait_for_load_state('load')
    page.evaluate('document.fonts.ready.then(() => true)')
    # only the slides' own images: the overview thumbnails are lazy and may not exist yet
    page.evaluate('''Promise.all([...document.querySelectorAll('#deck img')].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))''')
    page.wait_for_timeout(400)
    os.makedirs(os.path.join(folder, 'thumbs'), exist_ok=True)
    pages = []
    for i, sec in enumerate(page.query_selector_all('#deck > section'), 1):
        im = Image.open(io.BytesIO(sec.screenshot(type='png'))).convert('RGB')
        im.resize((480, 270), Image.LANCZOS).save(os.path.join(folder, 'thumbs', f'{i:02d}.jpg'), 'JPEG', quality=80, optimize=True)
        if i == 1:
            im.resize((1280, 720), Image.LANCZOS).save(os.path.join(folder, 'cover.jpg'), 'JPEG', quality=84, optimize=True)
        pages.append(im)
    pdf = os.path.join(folder, slug + '.pdf')
    # captured pages keep the look exactly (videos show their still frame); JPEG keeps the file light enough to email
    buf = []
    for im in pages:
        b = io.BytesIO(); im.save(b, 'JPEG', quality=82, optimize=True); buf.append(Image.open(b))
    buf[0].save(pdf, 'PDF', save_all=True, append_images=buf[1:], resolution=144)
    print(f'decks/{slug}/  {len(pages)} slides  PDF {os.path.getsize(pdf) / 1e6:.1f} MB')


def main():
    decks = json.load(open(os.path.join(ROOT, 'decks', 'decks.json')))
    only = set(sys.argv[1:])
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        for dk in decks:
            if not only or dk['slug'] in only:
                render(page, dk['slug'])
        browser.close()


if __name__ == '__main__':
    main()
