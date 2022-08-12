"""
Основной скрипт для запуска тестов.
настраивается с помощью config.py
"""





# для работы с ОС
import os

# конфиг
from stresser_data.config import *

# доп модули
from stresser_data.modules import *

# в stresser_data создаем папку tests с тестами
# и files с испольяемыми файлами решений
if not os.path.exists(f"stresser_data{DLM}files"):
    os.mkdir(f"stresser_data{DLM}files")
if not os.path.exists(f"stresser_data{DLM}tests"):
    os.mkdir(f"stresser_data{DLM}tests")

# очищаем папки от старых данных
clean(tests=True, files=True)

# копмилируем решения
launch_solution = compile(SOLUTION_PATH, "solution")
launch_dummy = compile(DUMMY_PATH, "dummy")

# в цикле перебираем тесты и запускаем
for test_num in range(1, TEST_CNT):
    
    # прописываем пути для тестов
    test_path = f"stresser_data{DLM}tests{DLM}{test_num}_in_.txt"
    dummy_out_path = f"stresser_data{DLM}tests{DLM}{test_num}_dummy_out_.txt"
    solution_out_path = f"stresser_data{DLM}tests{DLM}{test_num}_solution_out_.txt"
    
    #создаем файл и записываем в него сгенерирорванный тест
    test_now = open(test_path, "a")
    test_now.write(GEN_TEST(test_num))
    test_now.close()

    # запускаем наши решения, на вход даем тест
    # выходные данные сохраняем в отдельных файлах
    launch_dummy(test_path, dummy_out_path)
    launch_solution(test_path, solution_out_path)

    # считываем выходные данные
    f_dummy_out = open(dummy_out_path, "r")
    dummy_out = f_dummy_out.read()
    f_dummy_out.close()

    f_solution_out = open(solution_out_path, "r")
    solution_out = f_solution_out.read()
    f_solution_out.close()
    
    # если пользователь не просит сохранять тесты, удаляем
    if not SAVE_TESTS:
        clean(tests=True)

    # проверяем с помощью чекера
    if CHECK_TEST(dummy_out, solution_out) == True:
        print(f"test {test_num} OK")
    else:
        print(f"test {test_num} WA")
        print("-" * 30)
        print("INPUT:")
        print(GEN_TEST(test_num))
        print("-" * 20)
        print("RIGHT:")
        print(dummy_out)
        print("-" * 20)
        print("WRONG:")
        print(solution_out)
        print("-" * 30)
        break

clean(files=True)
