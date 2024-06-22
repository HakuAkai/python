numeros = [34, 67, 12, 9, 52, 13, 126, 42, 1, -128, -54, 87]
soma = 0
grupo = 0

for num in numeros:
    soma = soma + num

for num in numeros:
    num *= num

print(f"""
    A soma dos numeros é: {soma}
    O produto dos numeros é: {num}

    Grupos de números: 
    > Grupo 01: {numeros[0:3]}
    > Grupo 02: {numeros[3:6]}
    > Grupo 03: {numeros[6:9]}
    > Grupo 01: {numeros[9:12]}
""")

print("""
    Soma dos grupos de números:
""")

for n in numeros[0:3]:
    grupo = grupo + n
print(f"    > Grupo 01 é: {grupo}")

grupo = 0
for n in numeros[3:6]:
    grupo = grupo + n
print(f"    > Grupo 02 é: {grupo}")

grupo = 0
for n in numeros[6:9]:
    grupo = grupo + n
print(f"    > Grupo 03 é: {grupo}")

grupo = 0
for n in numeros[9:12]:
    grupo = grupo + n
print(f"    > Grupo 04 é: {grupo}\n")

y = 0
for x in numeros:
    if x > y:
        y = x
print(f"    O maior número da lista é: {y}")

w = 0
for x in numeros:
    if x > w and x != y:
        w = x
print(f"    O segundo maior número da lista é: {w}")

y = 0
for x in numeros:
    if x < y:
        y = x
print(f"    O menor número da lista é: {y}")

w = 0
for x in numeros:
    if x < w and x != y:
        w = x
print(f"    O segundo menor número da lista é: {w}")