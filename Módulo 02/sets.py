# set = conjuntos que não possuem objs repetidos
# não suporta indexação

values = {"bola", "quadrado", "retangulo"}
for value in values:
    print(value)
print("-----")

for indice, value in enumerate(values):
    print(f"{indice}: {value}")
print("-----")

total = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = {1, 2, 3, 4, 5}
b = {2, 4, 6, 8, 10}
c = {1, 3, 5, 7, 9}

print(a.union(b)) # une dois conjuntos
print(a.intersection(b)) # busca objs que ambos possuem
print(a.difference(b)) # busca objs que apenas o conjunto inicial possui
print(a.symmetric_difference(b)) # diferença entre os dois
print("-----")

print(f"O conjunto c pertence ao total: {c.issubset(total)}") # se pertence ao conjunto
print(f"Tem pertencentes c no total: {c.issuperset(total)}") # se tem pertencentes ao conjunto
print(f"Possuem objetos em comum: {c.isdisjoint(total)}") # se possuem objs compartilhados
print("-----")

total.add(11)
print(f"O valor 11 está no conjunto: {11 in total}\n{total}\n")

total.discard(11)
print(f"O valor 11 está no conjunto: {11 in total}\n{total}\n")

total.clear()
print(total)
