##
##
##
import sys
__author__  =  'Vladimir Ulogov'
__version__ = 'v0.1.0'

import clips
import sys

system_exit_clips="(deffunction system_exit (?c) (python-call system_exit ?c))"
boo_clips="(deffunction boo (?c) (python-call boo ?c))"

def system_exit(_ex):
    global CTX
    print CTX.shutdown()
def boo(c):
    global CTX
    print repr(c),int(c),sys.exit,globals().keys()
    print CTX.boo()
    return int(c)

if __name__ == '__main__':
    _exit(11)