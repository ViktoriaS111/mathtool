import random

MAX_COUNT = 1_000_000
MIN_VAL = -100
MAX_VAL = 100
MAX_SEARCH = 1000

def fill(count, low = MIN_VAL, high = MAX_VAL, seed = None):
    random.seed(seed)
    res = []
    for i in range(count):
        res.append(random.randint(low, high))
    return res

def check_val(values):
    if len(values) == 0:
        raise ValueError('массив пуст')
    if len(values) > MAX_COUNT:
        raise ValueError('количество элементов превышвет {MAX_COUNT}')
    for v in values:
            if (MIN_VAL <= v <= MAX_VAL) == False:
                raise ValueError('элемент {n} вне допустимого диапазона')
    