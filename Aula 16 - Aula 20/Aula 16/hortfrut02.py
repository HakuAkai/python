def menu_inicial():
    menu = """
    * Sistema de Gestão - Hortifruti * 

    Menu Principal:

    [1] Cadastrar um produto
    [2] Listar os produtos
    [3] Gravar
    [4] Sair

=> """
    print(menu)

def solicita_opcao():
    opcao = int(input("Escolha uma opção: "))
    print(f"Você escolheu a opção {opcao}")
    return opcao

def cadastro_prod( lista_produto ):
    produto = {}
    produto["nome"] = input("Informe o nome do produto: ")
    produto["cor"] = input("Informe a cor do produto: ")
    produto["preco"] = float(input("Informe o preço do produto: "))
    produto["un_medida"] = input("Informe a unidade de medida do produto: ")
    lista_produto.append( produto )

def listar_prod( lista_produto ):
    print(f"  {'Nome:'.ljust(20)} | {'Cor:'.ljust(15)} | Valor:")
    for p in lista_produto:
        print(f"> {p['nome'].ljust(20)} | {p['cor'].ljust(15)} | {p['preco']}/{p['un_medida']}")

def gravar_arquivo( lista_produto ):
    arql = open("Aula 16 - Aula 20\Aula 16\hortifruit02.csv", "w", encoding="utf-8")
    arql.write(f"{lista_produto}")

def invalida():
    print("Opção Inválida!!")

lista = []
executando = True

while executando:
    menu_inicial()
    escolha = solicita_opcao()
    if escolha == 1:
        cadastro_prod( lista )
    elif escolha == 2:
        listar_prod( lista )
    elif escolha == 3:
        gravar_arquivo( lista )
    elif escolha == 4:
        print("Obrigado por usar nosso sistema!!")
        executando = False
    else:
        invalida()