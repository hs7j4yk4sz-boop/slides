"""Add or refresh a media file for the website, made light for the web.

    python3 src/tools/optimize_media.py <source file> <media key>

The media key is the path the deck specs use, e.g. 'photos-2026/scene-speaker.jpg'
or 'dragons-2027/dragon-parties.png'. The result lands in media/<key>:
  - videos (.mp4, .mov): H.264, no sound, 1920 px wide at most, CRF 27, fast start (8 to 12 s loops)
  - PNG over 300 KB (dragons, drawings): WebP quality 88 with transparency, saved as media/<key without .png>.webp;
    the decks keep using the .png key, the build finds the .webp
  - JPEG: 1920 px wide at most, quality 84
  - anything else: copied as is
Never re-grade a photo here: 2026 photos and videos are already graded in the file,
and artworks (Polygon1993, PHANTASM cards) are never graded at all.
"""
import os, shutil, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEDIA = os.path.join(ROOT, 'media')


def optimize(src, key):
    dst = os.path.join(MEDIA, key)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    ext = os.path.splitext(key)[1].lower()
    if ext in ('.mp4', '.mov'):
        dst = os.path.splitext(dst)[0] + '.mp4'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-an', '-vf', "scale='min(1920,iw)':-2",
                        '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27', '-pix_fmt', 'yuv420p',
                        '-movflags', '+faststart', dst], check=True)
    elif ext == '.png' and os.path.getsize(src) > 300_000:
        dst = os.path.splitext(dst)[0] + '.webp'
        Image.open(src).save(dst, 'WEBP', quality=88, method=6)
    elif ext in ('.jpg', '.jpeg'):
        im = Image.open(src)
        if im.width > 1920:
            im = im.resize((1920, round(im.height * 1920 / im.width)), Image.LANCZOS)
        im.convert('RGB').save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
        if os.path.getsize(dst) > os.path.getsize(src) and im.width <= 1920:
            shutil.copyfile(src, dst)   # never make a file heavier than its source
    else:
        shutil.copyfile(src, dst)
    return dst


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    out = optimize(sys.argv[1], sys.argv[2])
    print(f'{out}  {os.path.getsize(out) / 1e6:.2f} MB')
