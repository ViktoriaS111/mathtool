import sys
import cli
from calc.equation import prepare_solve
from calc.stats import stats
from calc.series import series
from calc.integrate import proverka_and_intgrt
from calc import arrays, sorting
import time

def read_massive(path):
    if path:
        with open(path, encoding="utf-8-sig") as f:
            mass = f.read()
    else:
        lines = []
        while True:
            try:
                line = input()
                if line == '':
                    break
            except EOFError:
                break
            if line.strip() == False:
                break
            lines.append(line)
        mass = ' '.join(lines)
    mass = mass.replace(',', ' ')
    mass = mass.split()
    try:
        val = [int(n) for n in mass]
    except ValueError:
        raise ValueError('в массиве есть не целые числа')
    arrays.check_val(val)
    return val

def write_massive(mass, path):
    res = ' '.join(str(n) for n in mass) + '\n'
    if path:           
        with open(path, 'w', encoding="utf-8") as f:
            f.write(res)
        print(f"Записано элементов: {len(mass)} в файл {path}")
    else:
        print(mass)

def mesure(name, oper, param):
    start = time.perf_counter()
    res = oper(*param)
    time_ = time.perf_counter() - start
    print(f'Время операции {name}: {time_:.6f} c.', file=sys.stderr)
    return res

def handle_fill(args):
    if not (1 <= args.count <= arrays.MAX_COUNT):
        raise ValueError('элементы вне диапазона')
    if not(arrays.MIN_VAL <= args.min <= args.max <= arrays.MAX_VAL):
        raise ValueError('границы вне диапазона или min > max')
    val = arrays.fill(args.count, args.min, args.max, args.seed)
    write_massive(val, args.output)
    return 0

def handle_sort(args):
    val = read_massive(args.input)
    meth = sorting.METHODS[args.method]
    descending = (args.order == 'desc')
    mesure(f'{args.method}', meth, [val, descending])
    write_massive(val, args.output)
    print('Массив успешно отсортирован')
    return 0

def handle_search(args):
    try: 
        abs(args.value) <= arrays.MAX_SEARCH
    except ValueError:
        raise('Искомое значение вне диапазона')
    val = read_massive(args.input)
    if not arrays.is_sorted_asc(val):
        raise ValueError('Массив не упорядочен')
    index = arrays.binary_search(val, args.value)
    if index is None:
        print(f'Значение {args.value} не найдено')
        return 1
    print(f'Значение {args.value} имеет элемент с индексом {index + 1}')
    return 0

def main(argv):
    parser = cli.set_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    
    operations = {
    "solve": prepare_solve,
    "stats": stats,
    "series": series,
    "integrate": proverka_and_intgrt,
    "fill": handle_fill,
    "sort": handle_sort,
    "search": handle_search
    }

    try:
        return operations[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1
    
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))