##
##
##


class PYLOADER:
    def __init__(self, python_path=[]):
        self.python_path = []
        self.mods = {}
        print "PPA", python_path
        for d in list(python_path):
            if check_directory(d):
                self.python_path.append(d)
        self.reload_mods()
    def module_loaded(self, mod, fun):
        pass
    def mod_exec(self, _mod):
        if type(_mod) == types.StringType:
            ## Passing the name
            _mod = self.find_the_mod(_mod)
            if _mod == None:
                return []
        elif type(_mod) == types.ModuleType:
            _mod = _mod
        else:
            return []
        out = []
        for f in dir(_mod):
            if type(getattr(_mod, f)) != types.FunctionType:
                continue
            out.append(f)
        return out
    def find_the_mod(self, mod_name):
        for p in self.mods.keys():
            if self.mods[p].has_key(mod_name):
                return self.mods[p][mod_name]
        return None
    def reload_mods(self, path=None):
        if not path:
            _path = self.python_path
        else:
            _path = path
        print "PATH",_path
        for p in _path:
            if not self.mods.has_key(p):
                self.mods[p] = {}
            dir = get_dir_content(p)
            for m in dir:
                file, full_path, mod = m
                modname, ext = mod
                if ext not in [".py",] or self.find_the_mod(modname) != None:
                    continue
                try:
                    _mod = imp.load_source(modname, full_path)
                except KeyboardInterrupt:
                    continue
                self.mods[p][modname] = _mod
                f_list = self.mod_exec(_mod)
                for f in f_list:
                    self.module_loaded(modname, f)
        for p in self.mods.keys():
            if p not in self.python_path:
                del self.mods[p]

class CLPEXEC:
    def load(self, **args):
        return self._load(self.env.Load, self.env.Eval, args)
    def execute(self, **args):
        return self._load(self.env.BatchStar, self.env.Eval, args)
    def bootstrap_dir(self, path):
        for f, fpath, fmod in get_dir_content(path):
            try:
                print fpath
                clips.Load(fpath)
            except KeyboardInterrupt:
                raise ValueError, "Error in bootstrapping from %s"%fpath
    def bootstrap_facts(self, initial_facts_dir):
        if not initial_facts_dir:
            return
        for f, fpath, fmod in get_dir_content(initial_facts_dir):
            try:
                clips.LoadFacts(fpath)
            except:
                raise ValueError, "Error in loading facts from %s"%fpath

class LOADER:
    def _load(self, lf_file, lf_string, args):
        if args.has_key("file") and lf_file:
            if not check_module(args["file"]):
                raise IOError, "File %s not found or not accessible"%args["file"]
            return apply(lf_file, (args["file"],))
        elif args.has_key("data") and len(args["data"]) and lf_string:
            return apply(lf_string, (args["data"],))
        else:
            raise ValueError, "Loader requested to load not from file, nether from string"

class ENV(CLPEXEC,LOADER):
    def __init__(self, **argv):
        self.argv = argv
        self.env = clips.Environment()
        self.clear()
        self.current()
    def clear(self):
        self.env.Clear()
        self.env.Reset()
    def current(self):
        self.env.SetCurrent()

class CLP(ENV,PYLOADER):
    def __init__(self, ctx, arg={}, **kw):
        import posixpath
        self.python_path = []
        self.bootstrap_file = None
        self.model = None
        self.initial_facts = None
        self.initial_facts_dir=None
        self.CTX = ctx


        for k in arg.keys():
            kw[k] = arg[k]
        if kw.has_key("bootstrap") and check_file_read(kw["bootstrap"]):
            self.bootstrap_file = kw["bootstrap"]
        if kw.has_key("initial_facts") and check_file_read(kw["initial_facts"]):
            self.initial_facts = kw["initial_facts"]
        if kw.has_key("python_path"):
            self.python_path = kw["python_path"]
        if kw.has_key("models"):
            self.models = kw["models"]
        else:
            self.models = []
        ENV.__init__(self)
        PYLOADER.__init__(self, self.python_path)
        ## Reload CLIPS modules
        print "MODS",self.mods
        for dir in self.mods.keys():
            for mod in self.mods[dir].keys():
                self.load_module(mod)
        self.ReloadModels()
    def ReloadModels(self):
        if self.bootstrap_file != None:
            ## We do have a bootstrap
            try:
                clips.Load(self.bootstrap_file)
            except KeyboardInterrupt:
                raise ValueError, "Can not load bootstrap.clp"
            clp_base = posixpath.dirname(self.bootstrap_file)+"/bootstrap"
            if check_directory(clp_base):
                self.bootstrap_dir(clp_base)
            other_base = os.environ["HOME"]+".grapher/bootstrap"
            if check_directory(other_base):
                self.bootstrap_dir(other_base)
        ## Load models
        for m in self.models:
            if not check_file_read(m):
                raise ValueError, "Can not open %s"%m
            p = m.split(".")[-1].lower()
            if p == "clp":
                ## This is the Rule
                clips.Load(m)
            if p == "fact":
                ## This is a Fact
                clips.LoadFacts(m)
            else:
                raise ValueError, "I do not know what to do with %s"%m
    ## First, let's detect if it is a Fact or Rule
    def Run(self):
        import traceback
        clips.Run()
        out = clips.StdoutStream.Read()
        ret = ""
        if type(out) == type(""):
            ret = out
        err = clips.ErrorStream.Read()
        if type(err) == type(""):
            ret += err
            ret += traceback.format_exc()
        return ret
    def printFacts(self):
        for f in clips.FactList():
            print f.PPForm()
    def getTrace(self):
        return clips.TraceStream.Read()
    def load_module(self, name):
        import fnmatch
        mod = self.find_the_mod(name)
        mod.CTX = self.CTX
        mod.m_globals = globals()
        if mod == None:
            raise ValueError
        c = 0
        for e in dir(mod):
            if fnmatch.fnmatch(e, "*_clips"):
                fun_name = rchop(e,"_clips")
                #print "!!!",fun_name,e,mod,fun_name,dir(mod)
                try:
                    fun = getattr(mod, fun_name)
                except KeyboardInterrupt:
                    continue
                print "!!!",fun
                clips.RegisterPythonFunction(fun)
                clips.Build(getattr(mod, e))
                c += 1
        return c
    def globalCLEAR(self):
        clips.Reset()
        clips.Clear()
    def shutdown(self):
        self.globalCLEAR()


