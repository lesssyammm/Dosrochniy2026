f = open("C:\\Users\\olesy\\Downloads\\17_28762(1).txt").readlines()
a = [int(x) for x in f]
mn = min([x for x in a if x % 23 == 0])
b = []
for i in range(len(a) - 1):
    x, y = a[i:i + 2]
    if x % mn == 0 or y % mn == 0:
        b.append(x + y)
print(len(b), max(b))