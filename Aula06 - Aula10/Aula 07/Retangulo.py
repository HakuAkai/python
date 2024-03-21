calcular = True

while calcular == True:
    base = float(input("Informe o tamanho da base: (cm²) "))
    altura = float(input("Informe o tamanho da altura: (cm²) "))

    area = base * altura

    print(f"O tamanho da área é: {area} cm²")

    x = input("Gostaria calcular novamente? (S/N) ")
    if x == "N":
        break
