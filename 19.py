def f(s, s2, p):
    if s + s2 >= 65 or p > 3:return p == 3
    d = [f(s + 1, s2, p + 1), f(s * 3, s2, p + 1), f(s, s2 + 1, p + 1), f(s, s2 * 3, p + 1)]
    if p % 2 == 1:
        return any(d)
    if p % 2 == 0:
        return any(d)
for s in range(1, 59):
    if f(6, s, 1):
        print(s)
        break