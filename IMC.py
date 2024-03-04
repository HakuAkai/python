Altura = int(input("Digite sua altura: "))
Peso = int(input("Digite seu peso: "))

print(Altura, Peso)

IMC = (Altura * Altura) / Peso

print(IMC)

if IMC > 25:
    print("Sobrepreso ou mais")
else:
    print("Peso normal para baixo") 


