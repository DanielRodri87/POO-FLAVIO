# Crie uma função que imprima o conteúdo de uma Lista. Por exemplo, se o array for [1, “a”,
# 2.5, True], então será impresso em cada linha os valores: 1, “a”, 2.5 e True. Construa uma
# solução que trate a possibilidade que um elemento da lista também possa ser uma lista, por
# exemplo: [0,[1,2],3], neste caso a saída do programa em cada linha será: 0,1,2,3. Sua
# solução está tratando desta possibilidade: [0,1,[2,[3,4]],5] ?

lista = [0,1,[2,[3,4]],5]

for x in range(4):
    if x == 2:
        for y in range(2):
            if y == 1:
                for k in range(2):
                    print(lista[x][y][k], end=" ")
            else:
                print(lista[x][y], end=" ")
    else:
        print(lista[x], end=" ")
        
        
