import math

MAX_STEPS = 100000

def F_ratio(x):
    return x / (x + 1)

def F_root(x):
    return math.sqrt(x * x + 1)

table_func = {
    'ratio': (F_ratio, 'F(x) = x / (x + 1)', 0, 20, True),
    'root': (F_root, 'F(x) = sqrt(x^2 + 1)', -5, 5, False)
    }

def integrate(F, a, b, steps):
    dx = (b - a) / steps
    res = 0
    for i in range(0, steps):
        x = a + i * dx
        res += F(x) * dx
    return res

def proverka_and_intgrt(args):
    if math.isfinite(args.start) == False or math.isfinite(args.to) == False:
        raise ValueError('предел не является конечными числом')
    if args.start >= args.to:
        raise ValueError('начальный предел не меньше конечного')
    if not(1 <= args.steps <= MAX_STEPS):
        raise ValueError('количество шагов вне диапазона')
    
    fn, formula, low, high, limits = table_func[args.func]
    if limits:
        if not(low <= args.start and args.to <= high):
            raise ValueError('предел вне промежутка')
    else:
        if not(low < args.start and args.to < high):
            raise ValueError('предел вне промежутка')
        
    val = integrate(fn, args.start, args.to, args.steps)
    print(formula)
    print(f'значение интеграла: {val:.4f}')
    return 0