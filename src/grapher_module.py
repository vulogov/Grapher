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
        self.clp = CLP(self.args)

class Grapher(GrapherDBDriver, GrapherLogger, GrapherClips):
    def __init__(self, params={}, **kw):
        global CTX
        for k in kw.keys():
            params[k] = kw[k]
        self.args = params
        GrapherLogger.__init__(self)
        GrapherDBDriver.__init__(self)
        GrapherClips.__init__(self)
        CTX = self
        print self.args