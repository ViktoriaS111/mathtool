import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000

DIGITS = math.ceil(-math.log10(MAX_EPS))

def sign(n):
    if n % 2 == 0:
        return -1
    else:
        return 1

def addend_sqplus(n):
    return sign(n) / (n * n + 1)

def addend_third(n):
    return sign(n) / (3 * n)

FORMULAS = {
    'sqplus': (addend_sqplus, 'S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ...'),
    'third': (addend_third, 'S = 1/3 - 1/6 + 1/9 - 1/12 + ...')
    }

def sum_term(add, count):
    res = 0
    for n in range(1, count + 1):
        res += add(n)
    return res

def sum_eps(add, eps):
    res = 0
    n = 0
    while True:
        n += 1
        znach = add(n)
        res += znach
        if abs(znach) < eps:
            return res, n
        if n >= MAX_ITERATIONS:
            raise ValueError('точность не достигнута')

def series(args):
    if args.eps is not None:
        if not(math.isfinite(args.eps) and 0 < args.eps <= MAX_EPS):
            raise ValueError('точность вне диапазона')
    if args.terms is not None:
        if not(1 <= args.terms <= MAX_TERMS):
            raise ValueError('количество слагаемых вне диапазона')

    term, formula = FORMULAS[args.func]
    print(formula)

    if args.terms is not None:
        result = sum_term(term, args.terms)
        n = args.terms
    else:
        result, n = sum_eps(term, args.eps)

    print(f"слагаемых: {n}")
    print(f"сумма ряда: {result:.{DIGITS}f}")
    return 0