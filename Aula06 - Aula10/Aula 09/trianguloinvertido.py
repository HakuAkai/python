a = int(input("Quantos linhas tem o triangulo? "))

for i in range(0, a):
    print(" " * (a - i) + "*" * (i + 1))