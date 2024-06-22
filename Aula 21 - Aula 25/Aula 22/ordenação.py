from random import randrange, sample

cartas = sample(range(0, 50), 10)
print(f"\nDesordenada: {cartas}")

for j in range(len(cartas)):
    for i in range(0, len(cartas) - 1):
        if cartas[i] > cartas[i + 1]:
            ajuda = cartas[i]
            cartas[i] = cartas[i + 1]
            cartas[i + 1] = ajuda

print(f"Ordenada: {cartas}\n")