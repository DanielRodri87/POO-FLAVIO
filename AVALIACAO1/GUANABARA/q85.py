lista = [[], [], []]
for i in range(3):
    for j in range(3):
        lista[i].append(int(input(f"Digite o valor de {i}|{j}: ")))

for i in range(3):
    for j in range(3):
        print(lista[i][j], end=" ")
    print()