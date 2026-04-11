def f(n):
    b = set()
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d % 10 == 7 and d != 7:
                b.add(d)
            if n // d % 10 == 7 and n // d != 7:
                b.add(n // d)
    return sorted(b)
k = 0
for n in range(700_001, 710_000):
    if len(f(n)) > 0:
        print(n, f(n)[0])
        k += 1
        if k == 5:break