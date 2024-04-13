# incluem qualquer tipo de dado

number = list(range(11))
print(number)

baby = ["baby", "penguin"]
print(baby)

bb = list("penguin")
print(bb)
print("-----")

# listas aninhadas = listas dentro de listas
animal = [
    ["b", "a", "b", "y"],
    ["p", "e", "n", "g"],
    ["u", "i", "n", "28"]
]

# índices 
print(animal[0])
print(animal[0][0])
print(animal[0][1])
print(animal[0][2])
print(animal[0][3])
print("-----")

animal = ["ba", "by","pen", "guin"]

# fatiamento
print(animal[:4])
print(animal[4:])
print(animal[0:4:2])
print(animal[::-1])
print("-----")

# iteração
for babe in animal:
    print(babe)

for indice, babe in enumerate(animal):
    print(f"{indice}: {babe}") #enumerate funcion
print("-----")

# compreenção
numbers = [1, 2, 3, 4, 5]
pares = []
impares = []

for num in numbers:
    if num % 2 == 0:
        pares.append(num)

for num in numbers:
    if num % 2 != 0:
        impares.append(num)

pares = [num for num in numbers if num % 2 == 0]
impares = [num for num in numbers if num % 2 != 0]

print(f"Numeros: {numbers}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print("-----")