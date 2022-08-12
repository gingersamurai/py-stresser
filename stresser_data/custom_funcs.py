"""
файл в котором пользователь может 
написать свои кастомные функции
для генерации и проверки
"""

# декоратор для корректной работы функций для генерации
from stresser_data.modules.generator import gen_decorator

import random


# пример функции для генерации
# функция генерирует набор чисел
@gen_decorator
def my_gen():
    res = ""

    n = random.randint(1, 10)
    res += f'{n}\n'
    for i in range(n):
        x = random.randint(1, 10)
        res += f'{x} '

    return res
