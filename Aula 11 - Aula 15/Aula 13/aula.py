x={
    "alunos": 40,
    "professor": "Antonio",
    "computadores": 43,
    "cadeiras": 43,
    "monitores": 43,
    "perifericos": {"computadores": 43, "monitores": 43}
}
 
x["sala_aula"] = 201
 
if "sala_aula" in x:
    print("Existe a chave 'sala_aula' no dicionario")
else:
    print("Não existe a chave 'sala_aula' no dicionario")
 
chaves = list(x.keys())
tamanho = len(chaves)

for i in range(tamanho):
    chave = chaves[i]
    print(chave)

x.keys()