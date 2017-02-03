##
##  Configure Grapher command line
##

_DESC="""Grapher - Graph Database"""
_EPILOG="""Build and experiment with persistant Graph data structures"""

class PyConfig:
    def __init__(self):
        self.parser.add_argument("--pyclips", type=str, default=".",
                                 help="Semi-colon separated list of the directories containing PYCLIPS libraries")
        self.ready -= 1
    def process(self):
        self.pyclips = []
        for d in self.args.pyclips.split(";"):
            if not check_directory(d):
                print "Directory %s can not be accessed for a PYCLIPS modules" % d
                self.ready += 1
            elif not check_file_read("%s/init_pyclips.py" % d):
                print "Directory %s is invalid for a PYCLIPS" % d
                self.ready += 1
            else:
                self.pyclips.append(d)
class RunConfig:
    def __init__(self):
        self.parser.add_argument('model', metavar='N', type=str, nargs='*', help='Name of the query facts and procedures')
        self.ready -= 1
    def process(self):
        if len(self.args.model) == 0:
            print "You did not specified facts or models"
            self.ready += 1

class ClipsConfig:
    def __init__(self):
        self.parser.add_argument("-c", "--config", type=str, default="/etc/grapher",
                                 help="Path to the config (bootstrap) directory")
        self.parser.add_argument("--trace", "-t", action="store_true")
        self.ready -= 1
    def process(self):
        if not check_directory(self.args.config):
            print "Bootstrap directory %s is not accessible"%self.args.config
            self.ready += 1
        self.bootstrap_file = "%s/bootstrap.clp"%self.args.config
        self.initial_facts = "%s/initial.fact"%self.args.config
        if not check_file_read(self.bootstrap_file):
            print "Bootstrap file %s is not accessible"%self.bootstrap_file
            self.ready += 1
        if not check_file_read(self.initial_facts):
            print "Initial facts file %s is not accessible"%self.initial_facts
            self.ready += 1


class GrapherConfig(PyConfig, RunConfig,ClipsConfig):
    def __init__(self):
        import argparse
        self.parser = argparse.ArgumentParser(prog='grapher_cmd', description=_DESC, epilog=_EPILOG)
        self.ready = 3
        PyConfig.__init__(self)
        ClipsConfig.__init__(self)
        RunConfig.__init__(self)
        if self.ready != 0:
            print "Argument parsing and checking is unsatisfactory. Exit."
            sys.exit(99)
        self.parse_args()
        PyConfig.process(self)
        ClipsConfig.process(self)
        RunConfig.process(self)
        if self.ready != 0:
            print "Argument processing is unsatisfactory. Exit."
            sys.exit(97)
    def parse_args(self):
        self.args = self.parser.parse_args()
        print self.args
    def shutdown(self):
        pass

