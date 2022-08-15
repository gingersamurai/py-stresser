import os
import sys

# очищение файлов
def clean(files = False, tests = False):
    if tests:
        tests_path = f"stresser_data{os.sep}tests"
        for test_file in os.listdir(tests_path):
            os.remove(f"{tests_path}{os.sep}{test_file}")
    if files:
        files_path = f"stresser_data{os.sep}files"
        for file_file in os.listdir(files_path):
            os.remove(f"{files_path}{os.sep}{file_file}")
    if files and tests:
        os.rmdir(f"stresser_data{os.sep}tests")
        os.rmdir(f"stresser_data{os.sep}files")
        os.rmdir("stresser_data")

# компиляция файла и возвращение функции запуска
def get_launcher(path: str, type: str, flags: str = ""):
    exst = path[path.find('.'):]
    respath = f"stresser_data{os.sep}files{os.sep}{type}"
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
        os.system(f"{command} {path} {flags} {respath}")
    elif exst == '.c':
        launcher = ''
        if os.name == 'posix':
            respath += '.out'
        else:
            respath == '.exe'
        os.system(f"gcc {path} {flags} -o {respath}")
    elif exst == '.cpp':
        launcher = ''
        if os.name == 'posix':
            respath += '.out'
        else:
            respath == '.exe'
        os.system(f"g++ {path} {flags} -o {respath}")


    def launch(in_path: str = None, out_path: str = None, flags = ""):
        if in_path != None:
            in_path = '< ' + in_path
        else:
            in_path = ''
        if out_path != None:
            out_path = '> ' + out_path
        else:
            out_path = ''
        os.system(f"{launcher} {respath} {flags} {in_path} {out_path}")
    
    return launch

