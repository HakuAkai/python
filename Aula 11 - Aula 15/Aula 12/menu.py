menu = """

[1] Cadastrar nova bicicleta
[2] Cadastro de usuário
[3] Calcular seguro
[4] Sair

=> """

opcao = input(menu)

if opcao == "1":
    print("Cadastro de nova bicicleta")
elif opcao == "2":
    print("Cadastro de usuário")
elif opcao == "3":
    print("Calculo do seguro")
elif opcao == "4":
    print("Saindo")
else:
    print("erro")