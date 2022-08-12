"""
Основной скрипт для запуска тестов.
настраивается с помощью config.py
"""





import os
from stresser_data.config import *
from stresser_data.modules import *

if not os.path.exists(f"stresser_data{DLM}files"):
    os.mkdir(f"stresser_data{DLM}files")
if not os.path.exists(f"stresser_data{DLM}tests"):
    os.mkdir(f"stresser_data{DLM}tests")

clean(tests=True, files=True)

launch_solution = compile(SOLUTION_PATH, "solution")
launch_dummy = compile(DUMMY_PATH, "dummy")

for test_num in range(1, TEST_CNT):
    
    test_path = f"stresser_data{DLM}tests{DLM}{test_num}_in_.txt"
    dummy_out_path = f"stresser_data{DLM}tests{DLM}{test_num}_dummy_out_.txt"
    solution_out_path = f"stresser_data{DLM}tests{DLM}{test_num}_solution_out_.txt"
    
    test_now = open(test_path, "a")
    test_now.write(GEN_TEST(test_num))
    test_now.close()

    launch_dummy(test_path, dummy_out_path)
    launch_solution(test_path, solution_out_path)

    f_dummy_out = open(dummy_out_path, "r")
    dummy_out = f_dummy_out.read()
    f_dummy_out.close()

    f_solution_out = open(solution_out_path, "r")
    solution_out = f_solution_out.read()
    f_solution_out.close()
    
    if not SAVE_TESTS:
        clean(tests=True)

    if CHECK_TEST(dummy_out, solution_out) == True:
        print(f"test {test_num} OK")
    else:
        print(
            f"""
        test {test_num} WA
        ------------------------------
        INPUT:
        {GEN_TEST(test_num)}
        --------------------
        RIGHT:
        {dummy_out}
        --------------------
        WRONG:
        {solution_out}
        ------------------------------
            """
        )
        break

clean(files=True)
