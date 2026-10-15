import argparse

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
    series.add_argument('--func', type=str, required=True, help='какой ряд суммировать')
    group = series.add_mutually_exclusive_group(required=True)
    group.add_argument('--terms', type=int, help='сколько слагаемых')
    group.add_argument('--eps', type=float, help='до какой величины слагаемого считать')

    #integrate
    integrate = commands.add_parser("integrate", help='численное интегрирование', allow_abbrev=False)
    integrate.add_argument('--func', required=True, help='какую функцию интегрировать')
    integrate.add_argument('--from', type=float, required=True, help='нижний предел интегрирования', dest="start")
    integrate.add_argument('--to', type=float, required=True, help='верхний предел интегрирования')
    integrate.add_argument('--steps', type=str, required=True, help='на сколько прямоугольников делится отрезок')

    return parser