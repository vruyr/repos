import sys
assert sys.version_info[:2] in [(3, 6), (3, 7), (3, 8)]
from . import cli as _cli
