from calc.arrays import MAX_VAL, MIN_VAL

def out_of_order(a, b, descending):
    if descending:
        return a < b
    else:
        return a > b
                            
def bubble(massive, descending = False):
    n = len(massive)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if out_of_order(massive[j], massive[j + 1], descending):
                massive[j], massive[j + 1] = massive[j + 1], massive[j]
                swapped = True
        if swapped == False:
                break

def selection(massive, descending = False):
     n = len(massive)
     for i in range(0, n - 1):
        best = i
        for j in range(i + 1, n):
            if out_of_order(massive[best], massive[j], descending):
                best = j
        massive[i], massive[best] = massive[best], massive[i]

def insertion(massive, descending = False):
    n = len(massive)
    for i in range(1, n):
        current = massive[i]
        j = i
        while j > 0 and out_of_order(massive[j - 1], current, descending):
            massive[j] = massive[j - 1]
            j = j - 1
        massive[j] = current

def counting(massive, descending = False):
    counters = [0 for i in range(MAX_VAL - MIN_VAL + 1)]
    for i in massive:
        counters[i - MIN_VAL] += 1
    k = 0
    if descending:
        numbers = range(0, len(counters))
    else:
        numbers = range(0, len(counters), -1)
    for n in numbers:
        for _ in range(counters[n]):
            massive[k] = n + MIN_VAL
            k = k + 1

METHODS = {
    'bubble': bubble,
    'selection': selection,
    'insertion': insertion,
    'counting': counting
}