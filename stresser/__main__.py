import os
from stresser.modules import *

my_config = parse_input()

SOLUTION_PATH = my_config['SOLUTION_PATH']
DUMMY_PATH = my_config['DUMMY_PATH']
GENERATOR_PATH = my_config['GENERATOR_PATH']
NTESTS = my_config['NTESTS']
SAVE_TESTS = my_config['SAVE_TESTS']
CHECKER_TYPE = my_config['CHECKER_TYPE']

if not os.path.exists('stresser_data'):
    os.mkdir('stresser_data')
if not os.path.exists(f"stresser_data{os.sep}files"):
    os.mkdir(f"stresser_data{os.sep}files")
if not os.path.exists(f"stresser_data{os.sep}tests"):
    os.mkdir(f"stresser_data{os.sep}tests")
clean(tests=True)
clean(files=True)


launch_solution = get_launcher(SOLUTION_PATH, "solution")
launch_dummy = get_launcher(DUMMY_PATH, "dummy")
launch_generator = get_launcher(GENERATOR_PATH, "generator")

cur_checker = None
if CHECKER_TYPE == 'base':
    cur_checker = base_check
elif CHECKER_TYPE == 'base_with_format':
    cur_checker = base_with_format_check


for test_num in range(1, NTESTS + 1):
    if not SAVE_TESTS:
        clean(tests=True)
    test_path = f"stresser_data{os.sep}tests{os.sep}{test_num}_in.txt"
    dummy_out_path = f"stresser_data{os.sep}tests{os.sep}{test_num}_out_dummy.txt"
    solution_out_path = f"stresser_data{os.sep}tests{os.sep}{test_num}_out_solution.txt"

    launch_generator(out_path=test_path, flags=str(test_num))
    launch_dummy(test_path, dummy_out_path)
    launch_solution(test_path, solution_out_path)

    f_dummy_out = open(dummy_out_path, "r")
    dummy_out = f_dummy_out.read()
    f_dummy_out.close()

    f_solution_out = open(solution_out_path, "r")
    solution_out = f_solution_out.read()
    f_solution_out.close()

    

    if cur_checker(dummy_out, solution_out):
        print(f"test {test_num} OK")
    else:
        target_test = open(test_path)
        print(
            f"""
test {test_num} WA
------------------------------
INPUT:
{target_test.read()}
--------------------
RIGHT:
{dummy_out}
--------------------
WRONG:
{solution_out}
------------------------------
    """
        )
        target_test.close()
        break

if not SAVE_TESTS:
    clean(files=True, tests=True)