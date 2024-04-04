print("Programa usando laços")

linhas = int(input("Quantas linhas?"))
colunas = int(input("Quantas colunas?"))

for l in range(0, linhas):
  for c in range(0, colunas):
    print(c + 1, end="")
  print("")