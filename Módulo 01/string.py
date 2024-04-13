nome = "   THiaGo   "

print(nome.upper()) # sai em caps
print(nome.lower()) # sai em minusculo
print(nome.title()) # primeira letra maiuscula
nomet = (nome.title())

print(nomet.strip() + ".") # remove os esapçaos
print(nomet.lstrip() + ".") # remove os espaços à esquerda
print(nomet.rstrip() + ".") # remove os espaços à direita
nomec = (nomet.strip())

print(nomec.center(8, "☆")) # add caracteres e centraliza a string
print("☆".join(nomec)) # junta caracter com a string

#---------------------------------------------------

nome = "Thiago"
aparencia = "cabelo escuro e ondulado"
personalidade = "extrovertido e engraçado"

dados = {"nome": "Thiago", "aparencia": "Cabelo escuro e ondulado", "personalidade": "Extrovertido e engraçado"}


#método %
print("O %s tem %s e é %s." % (nome, aparencia, personalidade)) 


#método format
print("O {} tem {} e é {}.".format(nome, aparencia, personalidade))
print("O {1} tem {2} e é {3}.".format(nome, aparencia, personalidade))
print("O {nome} tem {aparencia} e é {personalidade}.".format(nome = nome, aparencia = aparencia, personalidade = personalidade))
print("O {nome} tem {aparencia} e é {personalidade}.".format(**dados))


#método f
print(f"O {nome} tem {aparencia} e é {personalidade}.")

PI = 3.14159

print(f"Valor de PI: {PI:10.2f}")
print(f"Valor de PI: {PI:1.2f}")
print(f"Valor de PI: {PI:.4f}")

#---------------------------------------------------

nome = "Thiago Henrique Condello de Jesus"

print(nome[:6])
print(nome[7:15])
print(nome[16:24])
print(nome[25:33])
print(nome[:])
print(nome[::-1])