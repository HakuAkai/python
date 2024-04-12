num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(1, 13):
    if i % 3 == 0:
        num.remove(i)

print(num)