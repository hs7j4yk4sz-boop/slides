import sys; sys.path.insert(0, '.')
from fpbuild import build, SECTIONS
# The FAIR PLAY season deck for every other season partner. The slides live in fpbuild.py, shared with fp.py.
d = build('fps', 'sponsor')
