a = 1
b = [0, 1, 2]

# if ternário
print("A = 1") if a == 1 else print("A ≠ 1")

a += 1

# if aninhado
if a == 1:
    print("A = 1")
elif a == 2:
    print("A = 2")
else:
    print("A ≠ 1 ou 2")

# for
for num in b:
    print(num) 

# for range
for num in range(0, 3):
    print(num)


