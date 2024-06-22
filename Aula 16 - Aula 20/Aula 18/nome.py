def gravar():
    arq02 = open("Aula 16 - Aula 20/Aula 18/nomes-idades.csv", "a+", encoding="utf-8")

    n = int(input("Quantos nomes você quer adicionar? "))

    for i in range(n):
        nome = input("Informe o nome: ")
        idade = input("Informe a idade: ")
        telefone = input("Informe o telefone: ")
        arq02.write(f"{nome.ljust(10)} ; {idade.ljust(10)} ; {telefone}\n")
        print("-------------------------")

    arq02.close()

def ler():
    arq03 = open("Aula 16 - Aula 20/Aula 18/nomes-idades.csv", "r", encoding="utf-8")

    lista = []
    linha = "-"

    while linha != "":
        linha = arq03.readline()
        linha = linha.replace("\n", "")
        if linha != "":
            dados = linha.split(";")
            dicio = {
                "Nome" : dados[0].strip(" "),
                "Idade" : int(dados[1].strip(" ")),
                "Telefone" : dados[2].strip(" ")
            }
            lista.append(dicio)

    print("Linhas: ", lista)

    arq03.close()

menu = """
    - MENU -

    Escolha uma opção:
    [1] Gravar dados
    [2] Ler dados
    [3] Sair

"""

opcao = int(input(menu))

if opcao == 1:
    gravar()
elif opcao == 2:
    ler()
elif opcao == 3:
    print("Obrigado por usar nosso serviço!!")
else:
    print("Opção inválida!!")

