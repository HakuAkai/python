exec = True

while exec == True:
    aluno_nome = input("Nome do aluno: ")
    aluno_n1 = float(input("Primeira nota do aluno: "))
    aluno_n2 = float(input("Segunda nota do aluno: "))
    aluno_n3 = float(input("Terceira nota do aluno: "))

    aluno_mf = (aluno_n1 + aluno_n2 + aluno_n3) / 3.0

    print("------------------------------------------------------------------")
    print("Nome           Nota01         Nota02         Nota03         Média")
    print(f"{aluno_nome:<15}{aluno_n1:<15}{aluno_n2:<15}{aluno_n3:<15}{aluno_mf:<15.1f}")
    print("------------------------------------------------------------------")

    x = input("Deseja executar novamente? S/N ").lower()
    if x == "n":
        break