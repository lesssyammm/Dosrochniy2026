s = open("C:\\Users\\olesy\\Downloads\\24_28765.txt").readline()
s = s.split("BC")
mx = 0
for i in range(len(s)):
    a = s[i:i+181]
    st = "BC".join(a)
    mx = max(len(st) + 2, mx)
print(mx)
