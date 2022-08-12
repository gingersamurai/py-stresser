"""
конфиг, в котором задаются настройки тестера
"""






from stresser_data.modules import *
from stresser_data import custom_funcs







# путь до тестируемого файла
SOLUTION_PATH = "solution.py"

# путь до тестирующего файла
DUMMY_PATH = "dummy.py"

# какую функцию использовать для генерации тестов
GEN_TEST = generator.base_gen

# какую функцию использовать для проверки выходных данных
CHECK_TEST = checker.base_check

# количество тестов 
TEST_CNT = 100

# сохранять ли тесты
SAVE_TESTS = False