import math

MAX_VALUE = 10000
MAX_COUNT = 20 

def add_to_nmbrs(args):
    chisla = []
    if args.input:
        with open(args.input, encoding='utf-8') as handle:
            for x in handle.read().split():
                chisla.append(x)
    else:
        while True:
            try:
                s = input()
            except EOFError:
                break
            for x in s.split():
                chisla.append(x)

    if len(chisla) > MAX_COUNT:
        raise ValueError('чисел больше 20')
    
    numbers = []
    for x in chisla:
        try: x = float(x)
        except ValueError: raise ValueError(f'{x} не является числом')
        numbers.append(x)
    if len(numbers) == 0:
        raise ValueError('список пуст')
    return numbers
    
def chek_nmbrs(x):
    if math.isfinite(x) == False:
        raise ValueError('значение не является конечным')
    if abs(x) > MAX_VALUE:
        raise ValueError('значение вне допустимого диапазона')

def summ(n):
    res = 0
    for x in n:
        res += x
    return res

def mid(n):
    if not n:
        return None
    return summ(n) / len(n)

def min_nmb(n):
    res = n[0]
    for x in n:
        if x < res:
            res = x
    return res

def max_nmb(n):
    res = n[0]
    for x in n:
        if x > res:
            res = x
    return res
    
def pos_nmbrs(n):
    res = 0
    for x in n:
        if x > 0:
            res += 1
    return res

def neg_nmbrs(n):
    res = 0
    for x in n:
        if x < 0:
            res += 1
    return res

def summ_sqrt(n):
    res = 0
    for x in n:
        res += x ** 2
    return res

def mid_sqrt(n):
    return math.sqrt(summ_sqrt(n) / len(n))

def summ_sqrt_dev(n):
    if not n:
        return None
    mid_val = mid(n)
    res = 0
    for x in n:
        res += (x - mid_val) ** 2
    return res

def disp(n):
    return summ_sqrt_dev(n) / len(n)

def sko(n):
    return math.sqrt(disp(n))

def stand_dev(n):
    if len(n) < 2:
        return None
    return math.sqrt(summ_sqrt_dev(n) / (len(n) - 1))

def stats(args):
    values = add_to_nmbrs(args)
    for n in values:
        chek_nmbrs(n)

    indicators_table = [
        ('Количество', len, 'd'),
        ('Сумма', sum, '.3f'),
        ('Среднее арифметическое', mid, '.3f'),
        ('Сумма квадратов', summ_sqrt, '.3f'),
        ('Среднее квадратическое', mid_sqrt, '.3f'),
        ('Дисперсия', disp, '.3f'),
        ('СКО', sko, '.3f'),
        ('Станд. отклонение', stand_dev, '.3f'),
        ('Наименьшее', min_nmb, '.3f'),
        ('Наибольшее', max_nmb, '.3f'),
        ('Положительных', pos_nmbrs, 'd'),
        ('Отрицательных', neg_nmbrs, 'd'),
    ]

    for label, function, form in indicators_table:
        val = function(values)
        if val is None:
            output = 'не существует'
        else:
            output = f'{val:{form}}'
        print(f'{label}:{output}')
    return 0