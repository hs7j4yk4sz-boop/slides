import sys; sys.path.insert(0, '.')
from fpbuild import build, SECTIONS
# The FAIR PLAY season deck for AI labs. The slides live in fpbuild.py, shared with fps.py.
d = build('fp', 'ai')
