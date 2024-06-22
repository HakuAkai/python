contatos = []
execucao = True

menu = """
    Como posso ajudar?

    [1] Cadastrar
    [2] Listar
    [3] Procurar
    [4] Backup em um arquivo
    [5] Restaurar um arquivo
    [6] Sair

=> """

def cadastro( lista ):
    dados = {}

    dados["nome"] = input("Informe o nome: ")
    dados["telefone"] = input("Informe o telefone: ")
    dados["email"] = input("Informe o email: ")
    dados["peso"] = float(input("Informe o peso: "))
    
    lista.append( dados )

def lista( lista ):
    print(f"  {'Nome:'.ljust(20)} | {'Telefone:'.ljust(15)} | {'Email:'.ljust(15)} | Peso:")
    for c in lista:
        print(f"> {c['nome'].ljust(20)} | {c['telefone'].ljust(15)} | {c['email'].ljust(15)} | {c['peso']}")

def procurar( lista ):
    email = input("Qual email está cadastrado? ")
    for e in lista:
        if email == e["email"]:
            menu = """
    [A] Alterar
    [X] Excluir
    [R] Retornar ao menu
=> """
            escolha = input(menu).upper()
            print(escolha)
            if escolha == "A":
                e["nome"] = input("Informe o nome: ")
                e["telefone"] = input("Informe o telefone: ")
                e["email"] = input("Informe o email: ")
                e["peso"] = float(input("Informe o peso: "))
            elif escolha == "X":
                lista.remove(e)
            elif escolha == "R":
                print("Obrigado por usar nosso programa!!")
            else:
                print(" --- ERRO --- ")

def backup( lista ):
    arq = open("Aula 16 - Aula 20\Aula 19\contatos.csv", "a+", encoding="utf-8")

    for e in lista:
        arq.write(f"{e['nome']} ; {e['telefone']} ; {e['email']} ; {e['peso']}\n")

    arq.close()

def restaurar( lista ):
    arq = open("Aula 16 - Aula 20\Aula 19\contatos.csv", "r", encoding="utf-8")

    lista = []
    x = "-"

    while x != "":
        x = arq.readline()
        x = x.replace("\n", "")
        if x != "":
            dados = x.split(";")
            dicio = {
                "nome" : dados[0].strip(" "),
                "telefone" : dados[1].strip(" "),
                "email" : dados[2].strip(" "),
                "peso" : dados[3].strip(" ")
            }
            lista.append(dicio)

    print(f"  {'Nome:'.ljust(20)} | {'Telefone:'.ljust(15)} | {'Email:'.ljust(15)} | Peso:")
    for e in lista:
        print(f"> {e['nome'].ljust(20)} | {e['telefone'].ljust(15)} | {e['email'].ljust(15)} | {e['peso']}")

    arq.close()

while execucao:
    opcao = int(input(menu))
    if opcao == 1:
        cadastro( contatos )
    elif opcao == 2:
        lista( contatos )
    elif opcao == 3:
        procurar( contatos )
    elif opcao == 4:
        backup( contatos )
    elif opcao == 5:
        restaurar( contatos )
    elif opcao == 6:
        print("Obrigado por usar nosso programa!!")
        execucao = False
    else:
        print(" --- ERRO --- ")