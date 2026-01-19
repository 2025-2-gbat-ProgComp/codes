fd = open("0067_triangle.txt", "r")
triangulo = []
for linha in fd:
    triangulo.append([int(e) for e in linha.split()])
fd.close()

for lin in range(1, len(triangulo)):
    triangulo[lin][0] += triangulo[lin-1][0]
    for col in range(1, len(triangulo[lin]) - 1):
        triangulo[lin][col] += max (
            triangulo[lin-1][col-1],
            triangulo[lin-1][col]             
        )
    triangulo[lin][-1] += triangulo[lin-1][-1]

print (f"O maior caminho custa {max(triangulo[-1])}")
