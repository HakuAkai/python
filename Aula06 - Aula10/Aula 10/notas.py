notas = []

for i in range(5):
    notas.append(float(input(f"Digite a {i + 1}º nota: ")))

soma = 0
for i in range(5):
    print("----------------------------------")
    numero = notas[i]
    soma = soma + numero
    print(f"Nota: {numero}", f"\tSoma: {soma}")
    

media = soma / 3.0

print("----------------------------------")
print(f"Sua média é: {media:.2f}")
print("----------------------------------")
