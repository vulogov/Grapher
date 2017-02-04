##
##
##


class GrapherLogger:
    def __init__(self):
        pass
class GrapherDBDriver:
    def __init__(self):
        pass
class GrapherClips:
    def __init__(self):
        self.clp = CLP(self, self.args)

class Grapher(GrapherDBDriver, GrapherLogger, GrapherClips, GrapherClipsShell):
    def __init__(self, params={}, **kw):
        global CTX
        for k in kw.keys():
            params[k] = kw[k]
        self.args = params
        GrapherLogger.__init__(self)
        GrapherDBDriver.__init__(self)
        GrapherClips.__init__(self)
        GrapherClipsShell.__init__(self)
        CTX = self
        self.CTX = self
        print self.args
    def shutdown(self):
        print "Shutdown called",sys.exit
        sys.exit(0)