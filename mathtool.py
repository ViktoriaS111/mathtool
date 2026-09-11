import sys
import math

note = "mathtool — решение уравнений вида A*x^2 + B*x + C = 0\nИспользование:\npython mathtool.py вывод справки\npython mathtool.py --help вывод справки\npython mathtool.py solve ввод коэффициентов c клавиатуры\npython mathtool.py solve -a 1 -b -3 -c 2 решение c заданными коэффициентами\nКоэффициенты A, B, C — целые числа, по модулю не превышающие 10000."

def tryy(x):
    try:
        x = int(x)
    except ValueError:
        print('ОШИБКА: коэффициент не является целым числом', file=sys.stderr)
        sys.exit(1)

if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print(note)
    sys.exit(0)
elif sys.argv[1] != 'solve':
    print('Неизвестная команда', file=sys.stderr)
    sys.exit(1)

if sys.argv[1] == 'solve' and len(sys.argv) == 2:
    A = input('Введите A:')
    B = input('Введите B:')
    C = input('Введите C:')
elif len(sys.argv) - 1 == 7:
    if sys.argv[2] != '-a' or sys.argv[4] != '-b' or sys.argv[6] != '-c':
        print('Неизвестный параметр', file=sys.stderr)
        sys.exit(1)
    A = sys.argv[3]
    B = sys.argv[5]
    C = sys.argv[7]
else:
    print('Неверный набор параметров', file=sys.stderr)
    sys.exit(1)

tryy(A)
tryy(B)
tryy(C)
A, B, C = int(A), int(B), int(C)

if abs(A) > 10_000 or abs(B) > 10_000 or abs(C) > 10_000:
    print('ОШИБКА: значение вне допустимого диапазона', file=sys.stderr)
    sys.exit(1)

def lineynoe(b, c):
    if b != 0:
        x = -c / b
        return f'x = {x:.3f}'

def kvadrat(a, b, c):
    D = b*b - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f'D = {D}', f'x1 = {x1:.3f}', f'x2 = {x2:.3f}' 
    elif D == 0:
        x = -b / (2 * a)
        return f'D = {D}', f'x = {x:.3f}'
    else:
        return f'D = {D}', 'Действительных корней нет'

if A == 0 and B != 0:
    print('Уравнение линейное', lineynoe(B, C))
elif A == 0 and B == 0:
    print('ОШИБКА: это не уравнение, неизвестное отсутствует')
    sys.exit(1)
else:
    print('Уравнение квадратное', kvadrat(A, B, C))  
