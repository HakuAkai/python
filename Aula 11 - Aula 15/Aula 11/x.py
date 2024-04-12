x = 10
a = x * 2
b = x - x


for i in range(0, x):
    print(" " * (b + 1) + "*" + (" " * (a - 2)) + "*")
    a -= 2
    b += 1

for i in range(0, x):
    print(" " * (b - 1) + "*" + (" " * (a + 2)) + "*")
    a += 2
    b -= 1
