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
    params['shell'] = config.args.shell
    params['python_path'] = config.pyclips

    grapher = Grapher(params)
    print CTX
    if params['shell'] == True:
        grapher.InteractiveShellRun()

if __name__ == '__main__':
    main()