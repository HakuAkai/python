# funções são blocos de código

# def = identificador da função
def exibir_mensagem1():
    print("Hi :)")

def exibir_mensagem2(nome):
    print(f"Hi {nome} :)")

def exibir_mensagem3(nome="Thiago"):
    print(f"Hi {nome} :)")

'''
# chamando a função:
exibir_mensagem1()
exibir_mensagem2(nome="Thiago")
exibir_mensagem3()
'''

# ----------------------------------------

def calc_total(numeros):
    return sum(numeros)

def ante_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

'''
print(calc_total([6, 28, 19, 12]))
print(ante_sucessor(28))
'''

# ----------------------------------------

def idades(ano, mes):
    if mes <= 4:
        idade = 2024 - ano
    else:
        idade = (2024 - 1) - ano
    return idade

'''
print(idades(ano=2005, mes=10))
'''

# ----------------------------------------

# Args = *valor, Kwargs = **valor
# Args ⇾ Tupla, Kwargs ⇾ Dicio

def banco(nome, *conteudo, **informacoes):
    texto = "\n".join(conteudo)
    dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in informacoes.items()])
    mensagem = f"Olá {nome}, somos do banco xxx.\n\n{texto}\n\n{dados}"
    print(mensagem)

banco("Thiago", "Sua compra foi realizada com sucesso!", valor="1.800,00", cartao="Debito")