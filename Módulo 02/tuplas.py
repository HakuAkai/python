# tuplas são imutaveis

add = ("lindo", "cheiroso", "gostoso",)
add1 = tuple("perfeito")
add2 = tuple([1, 2, 3])

print(add[0:3])
print(add1[0:])
print(add2[0])

print(f"Count: {add2.count(1)} | Index: {add2.index(1)}")


add3 = (
    ("lindo", "cheiroso", "gostoso"),
    ("perfeito", 1, 2, 3),
)

print(add3[0][0], add3[0][1], add3[0][2], add3[1][0])
print(add3[1][1], add3[1][2], add3[1][3])

