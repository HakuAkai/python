def somar_lista():
    soma = 0 
    for num in lista:
        soma = soma + num
    return soma

lista = [1, 2, 3, 4, 5]
menu = """

[1] Soma
[2] Média
[3] Sair

=> """

opcao = input(menu).upper()[0]

if opcao == "1" :
    somar_lista()
    print(f"Soma: {somar_lista()}")
elif opcao == "2":
    somar_lista()
    media = somar_lista() / len(lista)
    print(f"Média: {media}")
elif opcao == "3":
    print("Até breve!")
else: 
    print("erro")