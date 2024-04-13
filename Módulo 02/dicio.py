# Dicionários = conjuntos não ordenados
# chave:valor
# chave imutavel

noivos = dict(noivo="thigasz") # add chave e valor
noivos["noiva"] = "h4ku" # add chave e valor

print(f"\n(o °Д °;)o| Os noivos são o {noivos['noivo']} e a {noivos['noiva']}. |")

noivos["noiva"] = "haku"
print(f"\n(o゜▽ ゜)o| Os noivos são o {noivos['noivo']} e a {noivos['noiva']}. |")

print("\n-----")

info = {
    "01": {"nome": {"nome": "Filipe", "sobrenome": "Silva"}, "idade": 18},
    "02": {"nome": {"nome": "Augusto", "sobrenome": "Silva"}, "idade": 38},
}

info.update({"03": {"nome": {"nome": "Iris", "sobrenome": "Silva"}, "idade": 39}})

for chave in info:
    print(chave, info[chave])
print("-----")

for chave, valor in info.items():
	print(chave, valor)
print("-----")

print(info.keys())
print("-----")

print(info.get("nome", {"nome": "Filipe", "sobrenome": "Silva"}))
print("-----")

print(info.values())
print("-----")

del info["01"]
print(info)
print("-----")

info.clear()
print(info)