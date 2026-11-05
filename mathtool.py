import sys
import cli
from calc.equation import prepare_solve
from calc.stats import stats
from calc.series import series
from calc.integrate import proverka_and_intgrt
from calc import arrays

def read_massive(path):
    if path:
        with open(path, encoding="utf-8-sig") as f:
            mass = f.read()
    else:
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == False:
                break
            lines.append(line)
        mass = ' '.join(lines)
    mass.replace(',', ' ')
    mass = mass.split()
    try:
        mass = [int(n) for n in mass]
    except ValueError:
        raise ValueError('в массиве есть не целые числа')
    arrays.check_val(mass)
    return mass

def write_massive(mass, path):
    res = ' '.join(str(n) for n in mass) + '\n'            
    with open(path, 'w', encoding="utf-8") as f:
        f.write(res)
    return res

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
    }

    try:
        return operations[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1
    
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))