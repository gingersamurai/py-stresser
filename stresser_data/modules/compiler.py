import os

DLM = ("/" if os.name == 'posix' else '\\')

def clean():
    tests_path = f"stresser_data{DLM}tests"
    for test_file in os.listdir(tests_path):
        os.remove(f"{tests_path}{DLM}{test_file}")

    files_path = f"stresser_data{DLM}files"
    for file_file in os.listdir(files_path):
        os.remove(f"{files_path}{DLM}{file_file}")

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


    def launch(in_path: str = None, out_path: str = None):
        if in_path != None:
            in_path = '< ' + in_path
        else:
            in_path = ''
        if out_path != None:
            out_path = '> ' + out_path
        else:
            out_path = ''
        os.system(f"{launcher} {respath} {in_path} {out_path}")
        # print(f"{launcher} {respath} {in_path} {out_path}")
    
    return launch

     