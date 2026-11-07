import argparse
from calc.series import FORMULAS
from calc.arrays import MIN_VAL, MAX_VAL
from calc.sorting import METHODS

def set_parser():
    parser = argparse.ArgumentParser(prog="mathtool", description='расчёты над уравнениями и числовыми последовательностями', allow_abbrev=False)
    commands = parser.add_subparsers(dest="command")

    #solve
    solve = commands.add_parser("solve", help='решает квадратные и линейные уравнения', allow_abbrev=False)
    solve.add_argument("-a", type=int, help='коэффициент A: целое, по модулю не более 10000')
    solve.add_argument("-b", type=int, help='коэффициент B: целое, по модулю не более 10000')
    solve.add_argument("-c", type=int, help='коэффициент C: целое, по модулю не более 10000')

    #stats
    stats = commands.add_parser("stats", help='показатели последовательности', allow_abbrev=False)
    stats.add_argument('--input', help='имя файла, из которого читаются числа')

    #series
    series = commands.add_parser("series", help='сумма ряда', allow_abbrev=False)
    series.add_argument('--func', choices=sorted(FORMULAS), type=str, required=True, help='какой ряд суммировать')
    group = series.add_mutually_exclusive_group(required=True)
    group.add_argument('--terms', type=int, help='сколько слагаемых')
    group.add_argument('--eps', type=float, help='до какой величины слагаемого считать')

    #integrate
    integrate = commands.add_parser("integrate", help='численное интегрирование', allow_abbrev=False)
    integrate.add_argument('--func', required=True, help='какую функцию интегрировать')
    integrate.add_argument('--from', type=float, required=True, help='нижний предел интегрирования', dest="start")
    integrate.add_argument('--to', type=float, required=True, help='верхний предел интегрирования')
    integrate.add_argument('--steps', type=int, required=True, help='на сколько прямоугольников делится отрезок')

    #fill
    fill = commands.add_parser("fill", help='генерация списка', allow_abbrev=False)
    fill.add_argument('-c', '--count', type=int, required=True, help='количество элементов, от 1 до 1_000_000')
    fill.add_argument('--min', type=int, default=MIN_VAL, help='нижняя граница значений, -100 <= min <= max')
    fill.add_argument('--max', type=int, default=MAX_VAL, help='верхняя граница значений, min <= max <= 100')
    fill.add_argument('--seed', type=int, help='начальное значение генератора, целое число')
    fill.add_argument('-o', '--output', help='файл для созданного массива')

    #sort
    sort = commands.add_parser("sort", help='сортировка массива', allow_abbrev=False)
    sort.add_argument('-m', '--method', required=True, help='bubble, selection, insertion или counting', choices=METHODS)
    sort.add_argument('--order', choices=['asc', 'desc'], default='asc', help='asc — по возрастанию, desc — по убыванию')
    sort.add_argument('-i', '--input', help='файл с исходным массивом')
    sort.add_argument('-o', '--output', help='файл для отсортированного массива')

    #search
    search = commands.add_parser("search", help='двоичный поиск', allow_abbrev=False)
    search.add_argument('-v', '--value', type=int, required=True, help='искомое целое число, модуль не больше 1000')
    search.add_argument('-i', '--input', help='файл с массивом по возрастанию')

    return parser