n = int(input("Nhap n= "))
a = []
b = []
c = []
c.append(a)


def reset():
    global b
    b = []
    for i in range(n * 2 + 1):
        b.append(0)


for i in range(n * 2 + 1):
    if i == n:
        a.append(1)
    else:
        a.append(0)
    b.append(0)


def pascal_triangle(para_1, para_2, n):
    j = 1
    global a
    global k
    for i in range(n * 2 - 1):
        e = para_1[i] + para_1[i + 2]
        if e != 0 and e != 1:
            para_2[j] = e + 1
        else:
            para_2[j] = e
        j += 1
    a = para_2
    reset()
    c.append(a)


for i in range(n - 1):
    pascal_triangle(a, b, n)
length = len(c)
c = list(reversed(c))
for i in range(n * 2):
    for j in range(length):
        if c[j][i] == 0:
            print(" ", end=" ")
        else:
            print(c[j][i], end=" ")
    print()
