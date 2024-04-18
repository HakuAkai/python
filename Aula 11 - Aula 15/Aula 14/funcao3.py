def area_triangulo(b, a):
    area = b * a / 2
    return area

def area_retangulo(b, a):
    area = b * a
    return area

exec = True
while exec == True:
    menu = """

    Qual o tipo de objeto?

    [1] Triangulo
    [2] Retangulo 
    [3] Sair

    => """

    opcao = input(menu)[0] 

    if opcao == "1":
        base = float(input("Informe a base: "))
        altura = float(input("Informe a altura: "))
        area_triangulo(base, altura)
        print(f"Area é igual à {area_triangulo(base, altura)}")
    elif opcao == "2":
        base = float(input("Informe a base: "))
        altura = float(input("Informe a altura: "))
        area_retangulo(base, altura)
        print(f"Area é igual à {area_retangulo(base, altura)}")
    elif opcao == "3":
        print("Até breve!")
        exec = False
    else:
        print("-------------- ERRO --------------")
        exec = False
