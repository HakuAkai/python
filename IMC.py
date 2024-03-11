Altura = float(input("Digite sua altura: "))
Peso = float(input("Digite seu peso: "))

print(Altura, Peso)

IMC = Peso / (Altura**2) 

print(IMC)

if IMC > 25:
    print("Sobrepreso ou mais")
elif IMC < 18.5:
    print("Abaixo do peso ou menor")
else:
    print("Peso normal") 


