lista = []
executando = True

# funções:
def gravar_lista():
    produto = {}
    produto["nome"] = input("Digite o nome do produto: ")
    produto["cor"] = input("Digite a cor do produto: ")
    produto["preco"] = float(input("Digite o preço do produto: "))
    produto["uni_medida"] = input("Digite a unidade de medida: ")
    lista.append(produto)


def exibir_produto(produto):
    info = f"""
    Produto: {produto['nome']}
    Cor: {produto['cor']}
    Preço: {produto['preco']} por {produto['uni_medida']}
    """
    print(info)

def mostrar_lista():
    for p in lista:
        exibir_produto(p)

def pesquisar_lista(nome):
    for p in lista:
        if nome == p["nome"]:
            return p
    return None


def sair():
    print("Obrigado por usar nosso sistema!")


while executando:
    menu = """

    SISTEMA PARA HORT-FRUT

    [1] Adicionar um novo produto
    [2] Listar todos os profutos
    [3] Pesquisar por um produto específico
    [4] Sair

    =>  """

    opcao = input(menu)

    if opcao == "1":
        gravar_lista()
    elif opcao == "2":
        mostrar_lista()
    elif opcao == "3":
        n1 = input("Informe o nome do produto: ")
        produto = pesquisar_lista(n1)
        if produto is not None:
            exibir_produto(produto)
    elif opcao == "4":
        sair()
        executando = False
    else:
        print("-------------- ERRO --------------")
        executando = False
