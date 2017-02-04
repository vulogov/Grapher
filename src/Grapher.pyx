import sys
try:
    import sys
    import imp
    import types
    import os
    import clips
    import posixpath
except ImportError, msg:
    print "One or mode required modules not found"
    sys.exit(10)

global CTX

include "grapher_clips.py"
include "grapher_lib.py"
include "grapher_config.py"
include "grapher_clips_shell.py"
include "grapher_module.py"