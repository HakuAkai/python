menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor informado é invalido")


    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque ultrapassou o limite")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques atingido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor inválido")

    elif opcao == "3":
        print("\n ------------------- Extrato ------------------- ")
        print("Não houve movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------- Extrato ------------------- ")

    elif opcao == "4":
        break

    else:
        print("Operaçao inválida")