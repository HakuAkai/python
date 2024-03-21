executar = True
while executar == True:
    nome = input("Digite seu nome: ")
    print("Bom dia, ", nome)

    print("Deseja continuar? (S/N)")
    continuar = input()

    if continuar == "N":
        executar = False