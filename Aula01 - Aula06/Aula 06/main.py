executar = True
while executar == True:
  nome = input("Por favor, digite seu nome: ")
  print("Bom dia, ", nome)
  res = input("Deseja executar novamente? (s/n) ")
  if res == "s" :
    executar = True
  else :
    executar = False
