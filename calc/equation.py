import math

def solve(a, b, c):
    d = b * b - 4 * a * c
    roots = []
    if a == 0:
        x = -c / b
        d = None
        roots.append(x)
        return 'линейное', d, roots
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        roots.append(x1)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        roots.append(x2)
        return 'квадратное', d, roots
    elif d == 0:
        x = -b / (2 * a)
        roots.append(x)
        return 'квадратное', d, roots
    else:
        return 'квадратное', d, roots

def check_int(x):
    try: return int(x)
    except ValueError: raise ValueError('коэффициент не является целым числом')

def proverka(x):
    MAX_VALUE = 10000
    if abs(x) > MAX_VALUE:
        raise ValueError('коэффициент вне допустимого диапазона')
    return x

def prepare_solve(args):
    MAX_VALUE = 10000
    if args.a is None and args.b is None and args.c is None:
        A, B, C = proverka(check_int(input('Введите A: '))), proverka(check_int(input('Введите B: '))), proverka(check_int(input('Введите C: ')))
    elif args.a is not None and args.b is not None and args.c is not None:
        A, B, C = args.a, args.b, args.c
    else: raise ValueError('указаны не все коэффициенты')
    res = solve(A, B, C)
    print(res)
    