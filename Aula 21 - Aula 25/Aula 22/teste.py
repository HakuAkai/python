def somar ( n1, n2 ):
    s = n1 + n2
    print(f"Soma: {s}")
    return s

def dividir ( n1, n2 ):
    r = n1 / n2
    print(f"Divisão: {r}")
    return r

numero01 = int(input("Informe o número: "))
numero02 = int(input("Informe o número: "))
soma = somar( numero01, numero02 )
resultado = dividir( numero01, numero02 )