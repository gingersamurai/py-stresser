import os

DLM = ("/" if os.name == 'posix' else '\\')


def compile(path: str, type: str):
    """
    compile file in path and return launch function \\
    ### params: 
    + path: 
    + type: 'solution' if solution 'dummy' if dummy
    """
    exst = path[path.find('.'):]
    respath = f"stresser_data{DLM}files{DLM}{type}"
    launcher: str
    if exst == '.py':
        respath += ".py"
        command: str
        if os.name == 'posix':
            launcher = 'python3'
            command = 'cp'
        else:
            launcher = 'python'
            command = 'copy'
        os.system(f"{command} {path} {respath}")
    elif exst == '.c':
        launcher = ''
        if os.name == 'posix':
            respath += '.out'
        else:
            respath == '.exe'
        os.system(f"gcc {path} -o {respath}")
    elif exst == '.cpp':
        launcher = ''
        if os.name == 'posix':
            respath += '.out'
        else:
            respath == '.exe'
        os.system(f"g++ {path} -o {respath}")


    def launch(in_path: str, out_path: str):
        os.system(f"{launcher} {respath} < {in_path} > {out_path}")
    
    return launch
        