num = int(input("Digite um nuúmro: "))
i = 1

        #range(iniciação, termino, incremento)
for i in range(1, 11, 1):
    res = num * i
    print(f"{num} x {i:>2} = {res:>2}")