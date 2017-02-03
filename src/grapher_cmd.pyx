##
## Main module for the Grapher command line tool
##
include "Grapher.pyx"

def main():
    global CTX
    params = {}
    config = GrapherConfig()
    params['config'] = config
    params['models'] = config.args.model
    params['bootstrap'] = config.bootstrap_file
    params['initial_facts'] = config.initial_facts
    grapher = Grapher(params)
    print CTX

if __name__ == '__main__':
    main()