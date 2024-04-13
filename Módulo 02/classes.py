numbers = [
    [28, 10, 2005],
    [19, 5, 2006]
]

numbers.clear() # limpa a lista
numbers.extend([28, 10]) # add à lista
numbers.append([2005]) # add elementos à lista 

numbers.extend([19, 5])
numbers.append([2006])


ani = numbers.copy() # copia a lista em outra lista
ani.extend([16, 5])
ani.append([2024])

print(f"ani ID: {id(ani)}, numbers ID: {id(numbers)}")
print(f"Aniversários 2024: {ani}\nAniversários 2023: {numbers}")
print("-----")

print("O número 5 aparece:", ani.count(5), "vezes") # conta quant. vezes um obj aparece
print("primeira vez que aparence é na posição: ", ani.index(5)) # 1º vez que o obj aparece
print("-----")

ani.pop() # remove o último item da lista
ani.pop(7) # remove o item desse índice
ani.remove(16) # remove o item indicado
ani.reverse() # mostra a lista ao contrario
print(ani)
print("-----")

alfa = ["ba", "by", "pen", "guin"]

alfa.sort() # deixa em ordem alfabetica
print(alfa)

alfa.sort(reverse=True)
print(alfa)

alfa.sort(key=lambda x: len(x))
print(alfa)

alfa.sort(key=lambda x: len(x), reverse=True)
print(alfa)

print(sorted(alfa, key=lambda x: len(x), reverse=True))

print(len(alfa))