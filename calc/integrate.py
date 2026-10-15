import math

MAX_STEPS = 100000

def F_ratio(x):
    return x / (x + 1)

def F_root(x):
    return (x * x + 1)

table_func = {'ratio': (F_ratio, 'F(x) = x / (x + 1)', 0, 20, True),
              'root': (F_root, 'F(x) = sqrt(x^2 + 1)', -5, 5, False)}

def integrate(F, a, b, steps):
    dx = (b - a) / steps
    res = 0
    for i in range(0, steps - 1):
        x = a + i * dx
        res += F(x) * dx
    return res

def proverka_intgr(args):
    if math.isfinite(args.a) == False or math.isfinite(args.b):
        raise ValueError('предел не является конечными числом')
    if args.a >= args.b:
        raise ValueError('начальный предел не меньше конечного')
    if not(1 <= args.speps < MAX_STEPS):
        raise ValueError('шагов вне диапазона')