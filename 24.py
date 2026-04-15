# f = open("c:\\Users\\olesy\\Downloads\\24(22).txt").readline()
# mx = 0
# num = ""
# for x in f:
#     if x in "1234567890":
#         num += x
#         if x in "24680":
#             mx = max(mx, int(num))
#     else:
#         num = ""
# print(mx)

#11
# s = open("c:\\Users\\olesy\\Downloads\\24(23).txt").readline()
# s = s.replace("AB", "1")
# s = s.replace("CB", "1")
# s = s.replace("A", ".")
# s = s.replace("B", ".")
# s = s.replace("C", ".")
# a = s.split(".")
# print(len(max(a, key = len)))


# k = 0
# mx = 0
# i = 0
# while i < len(s) - 1:
#     if (s[i] == "A" or s[i] == "C") and s[i + 1] == "B":
#         k += 1
#         i += 1
#     else:
#         mx = max(k, mx)
#         k = 0
#     i += 1
# mx = max(k, mx)
# print(mx)

# s = open("c:\\Users\\olesy\\Downloads\\24(23).txt").readline()
# s = s.replace("AB", "1")
# s = s.replace("CB", "2")
# s = s.replace("A", ".")
# s = s.replace("B", ".")
# s = s.replace("C", ".")
# a = s.split(".")

# print(len(max(a, key=len)))

#12
# s = open("c:\\Users\\olesy\\Downloads\\24(24).txt").readline()
# mx = 0
# k = 1
# for i in range(len(s) - 1):
#     if (s[i] in "ABC") and (s[i + 1] in "ABC"):
#         mx = max(mx, k)
#         k = 1
#     else:
#         k += 1
# mx = max(mx, k)
# print(mx)

# for c1 in "ABC":
#     for c2 in "ABC":
#         s = s.replace(f"{c1}{c2}", "1")
# s = s.replace("AA", "1")
# s = s.replace("BB", "1")
# s = s.replace("CC", "1")
# s = s.replace("AC", "1")
# s = s.replace("CA", "1")
# s = s.replace("AB", "1")
# s = s.replace("BA", "1")
# s = s.replace("BC", "1")
# s = s.replace("CB", "1")
# a = s.split("1")
# print(len(max(a, key= len)) + 1)

#4
# s = open("c:\\Users\\olesy\\Downloads\\24(26).txt").readline()
# k = 0
# mx = 0
# for i in range(len(s)):
#     if s[i].isdigit():
#         k += 1
#     else:
#         mx = max(mx, k)
#         k = 0
# print(mx)

#14
# s = open("c:\\Users\\olesy\\Downloads\\24(29).txt").readline()
# s = s.replace("A1", "*")
# s = s.replace("B1", "*")
# s = s.replace("A2", "*")
# s = s.replace("B2", "*")
# s = s.replace("A", ".")
# s = s.replace("B", ".")
# s = s.replace("2", ".")
# s = s.replace("1", ".")
# a = s.split(".")
# print(len(max(a, key=len)))

#15
# s = open("c:\\Users\\olesy\\Downloads\\24(28).txt").readline()
# for x in "LISENOK":
#     s = s.replace(x, ".")
# a = s.split(".")
# print(len(max(a, key=len)))

#16
# s = open("c:\\Users\\olesy\\Downloads\\24(30).txt").readline()
# k = 1
# mx = 0
# for i in range(len(s) - 1):
#     if s[i] == "A" and s[i + 1] == "B":
#         mx = max(k, mx)
#         k = 1
#     else:
#         k += 1
# mx = max(mx, k)
# print(mx)



#ДИНАМИЧЕСКИМ ЧЕРЕЗ ПРЕФИКС СУММ
#2

# s = open("C:\\Users\\olesy\\Downloads\\ECjxYCSUU(1).txt").readline()
# p = [0 for _ in range(len(s) + 1)]
# c = 0
# for i in range(len(s)):
#     if s[i] == ".":
#         c += 1
#     if (s[i] == 'Y' or c == 6):
#         p[i + 1] = 0
#         c = 0
#     else:
#         p[i + 1] = p[i] + 1

# print(max(p))

# p = [0]
# for x in range(len(s)):
#     if s[x] == ".":
#         p.append(p[-1] + 1)
#     elif s[x] == "Y":
#         p.append(0)
#     else:
#         p.append(p[-1])
# mx = 0
# K = {}
# for i in range(len(p) - 1):
#     l = p[i]
#     r = p[i + 1]
#     K[l] = i
#     if r - 5 in K:
#         d = (i + 1) - K[r - 5]
#         mx = max(mx, d)
# print(mx)
#3
s = open("C:\\Users\\olesy\\Downloads\\huzooBIjx.txt").readline()
k = set()
alf = "0123456789ABCDEF"
ln = 0
mn = 10**1000
st = 0
for i in range(len(s)):
    if s[i] in alf:
        k.add(s[i])
        st += 1
    if st != 0:
        ln += 1
    if len(k) == 16:
        mn = min(mn, ln)
        ln = 0
        k = set()
        st = 0
print(mn)
# p = [0]
# for x in range(len(s)):
#     if s[x] == ".":
#         p.append(p[-1] + 1)
#     elif s[x] == "Y":
#         p.append(0)
#     else:
#         p.append(p[-1])
# mn = 10**1000
# K = {}
# for i in range(len(p) - 1):
#     l = p[i]
#     r = p[i + 1]
#     K[l] = i
#     if r - 5 in K:
#         d = (i + 1) - K[r - 5]
#         mn = max(mn, d)
# print(mn)