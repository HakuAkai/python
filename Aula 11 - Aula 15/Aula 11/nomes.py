nomes = []
x = int(input("Quantos nomes você gostaria de armazenar? "))

for i in range(0, x):
    nomes.append(input(f"Digite o {i + 1}º nome: "))

print(nomes[::-1])