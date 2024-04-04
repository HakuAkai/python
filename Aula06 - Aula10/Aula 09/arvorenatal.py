a = int(input("Quantos galhos tem a árvore? "))

for i in range(0, a):
    print(" " * (a - i -1) + "*" * (2 * i + 1))

for i in range(3):
    print(" " * (a -2) + "||")


