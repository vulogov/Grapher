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
        pass

class Grapher(GrapherDBDriver, GrapherLogger):
    def __init__(self, params={}, **kw):
        global CTX
        for k in kw.keys():
            params[k] = kw[k]
        self.args = params
        GrapherLogger.__init__(self)
        GrapherDBDriver.__init__(self)
        CTX = self
        print self.args