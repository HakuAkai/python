tempo = 12
medidas = []

for i in range(tempo):
    medidas.append(float(input(f"Digite o crescimento da {i + 1}º mês: ")))

print("------------------------------------")

soma = 0
for i in range(tempo):
    soma = soma + medidas[i]
    print(f"Crescimento {i+1}º mês: {soma}")

media = soma / 10.0

print("------------------------------------")
print(f"A média de crescimento é: {media:.2f}")
print("------------------------------------")
