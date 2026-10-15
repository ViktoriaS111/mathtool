import math

MAX_VALUE = 10000

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

def check_koeff(x):
    try: int(x)
    except ValueError: raise ValueError('коэффициент не является целым числом')
    if abs(int(x)) > MAX_VALUE:
            raise ValueError(f'коэффициент {x} вне допустимого диапазона')
    return int(x)

def prepare_solve(args):
    if args.a is None and args.b is None and args.c is None:
        A, B, C = check_koeff(input('Введите A: ')), check_koeff(input('Введите B: ')), check_koeff(input('Введите C: '))
    elif args.a is not None and args.b is not None and args.c is not None:
        A, B, C = check_koeff(args.a), check_koeff(args.b), check_koeff(args.c)
    else: raise ValueError('указаны не все коэффициенты')
    if A == 0 and B == 0:
        raise ValueError('это не уравнение, неизвестное отсутствует')

    kind, d, roots = solve(A, B, C)
    print(f'Тип уравнения: {kind}')
    if d is not None:
        print(f'Дискриминант: {d}')
    if len(roots) == 1:
        print(f'x = {roots[0]:.3f}')
    if len(roots) == 2:
        print(f'x1 = {roots[0]:.3f}, x2 = {roots[1]:.3f}')
    if len(roots) == 0:
        print('Действительных корней нет')
    return 0
    