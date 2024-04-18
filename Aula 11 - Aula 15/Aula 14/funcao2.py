lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [10, 20, 30, 40, 50, 60]

def somar_lista():
    soma = 0
    for numero in lista1:
        soma = soma + numero
    return soma

def somar_lista2():
    soma = 0
    for numero in lista2:
        soma = soma + numero
    return soma

exec = True
while exec == True:
    menu = """

    [1] Soma
    [2] Média
    [3] Sair

    => """

    opcao = input(menu).upper()[0]

    if opcao == "1" :
        somar_lista2()
        print(f"Soma: {somar_lista2()}")
    elif opcao == "2":
        somar_lista()
        media = somar_lista() / len(lista1)
        print(f"Média: {media}")
    elif opcao == "3":
        print("Até breve!")
        exec = False
    else: 
        print("-------------- ERRO --------------")
        exec = False