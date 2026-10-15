import sys
import cli
from calc.equation import prepare_solve
from calc.stats import stats
from calc.series import series
from calc.integrate import proverka_and_intgrt

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