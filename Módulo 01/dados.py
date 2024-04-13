print(int(9.99))
print(int("999"))
print(float("9.99"))
print(float("999"))

numero = 999
numero_str = str(numero)
print(type(numero))
print(type(numero_str))

print(99 / 9)
print(99 // 9)

#-------------------------------------------------

nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
idade = input("Informe o ano de nascimento: ")
idade_int = int(idade)
ANO = 2023

print("O nome dele é", nome, sobrenome, "e ele tem ", ANO - idade_int, "anos")