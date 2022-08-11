from stresser_data.modules.generator import gen_decorator
import random

@gen_decorator
def my_gen():
    res = ""

    n = random.randint(1, 10)
    n = 5
    res += f'{n}\n'
    for i in range(n):
        x = random.randint(1, 10)
        res += f'{x} '

    return res






if __name__ == '__main__':
    print("START testing custom_funcs.py:")
    print(my_gen())
    print("FINISH testing custom_funcs.py:")