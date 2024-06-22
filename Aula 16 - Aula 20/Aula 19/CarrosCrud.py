carros = []
execucao = True

menu = """
    Como posso ajudar?

    [1] Cadastrar
    [2] Listar
    [3] Procurar
    [4] Sair

=> """

def cadastro( lista ):
    carro = {}

    carro["marca"] = input("Informe a marca do carro: ")
    carro["modelo"] = input("Informe o modelo do carro: ")
    carro["ano"] = input("Informe o ano do carro: ")
    carro["placa"] = input("Informe a placa do carro: ")
    
    lista.append( carro )

def lista( lista ):
    print(f"  {'Marca:'.ljust(20)} | {'Modelo:'.ljust(15)} | {'Ano:'.ljust(15)} | Placa:")
    for p in lista:
        print(f"> {p['marca'].ljust(20)} | {p['modelo'].ljust(15)} | {p['ano'].ljust(15)} | {p['placa']}")

def procurar( lista ):
    placa = input("Informe a placa do carro: ")
    for c in lista:
        if placa == c["placa"]:
            menu = """
    [A] Alterar
    [X] Excluir
    [R] Retornar ao menu
=> """
            escolha = input(menu).upper()
            print(escolha)
            if escolha == "A":
                c["marca"] = input("Informe a marca do carro: ")
                c["modelo"] = input("Informe o modelo do carro: ")
                c["ano"] = input("Informe o ano do carro: ")
                c["placa"] = input("Informe a placa do carro: ")
            elif escolha == "X":
                lista.remove(c)
            elif escolha == "R":
                print("Obrigado por usar nosso programa!!")
            else:
                print(" --- ERRO --- ")

while execucao:
    opcao = int(input(menu))
    if opcao == 1:
        cadastro( carros )
    elif opcao == 2:
        lista( carros )
    elif opcao == 3:
        procurar( carros )
    elif opcao == 4:
        print("Obrigado por usar nosso programa!!")
        execucao = False
    else:
        print(" --- ERRO --- ")
