from functools import wraps
import random


def gen_decorator(func):
    
    @wraps(func)
    def inner(seed: int = None, *args, **kwargs):
        if seed != None:
            random.seed(seed)
        return func(*args, **kwargs)
    
    return inner


@gen_decorator
def base_gen() -> str:
    "генерирует случайный тест"
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    res = f"{a} {b}"
    return res

