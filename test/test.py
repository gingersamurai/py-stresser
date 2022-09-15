import os

pref = '/home/gingersamurai/coding/projects/py-stresser/test/tests'
os.chdir(pref)

cnt = len(os.listdir('.'))

for now_case in os.listdir('.'):
    os.chdir(f'{pref}/{now_case}')

    with open('args') as f:
        args = f.read()

    print(F"{'_'*20}[{now_case}] START TESTING{'_'*20}\n\n\n")
    os.system(f'stresser {args}')
    print(F"\n\n\n{'_'*20}[{now_case}] FINISH TESTING{'_'*20}\n\n\n")

print(f"DONE {cnt} testcases")
