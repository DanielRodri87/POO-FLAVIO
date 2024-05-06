# Vimos em sala de aula o método find e index que retornam a posição de um caractere
# dentro de uma string. Por exemplo: “Teste”.find(“T”), a saída será 0. Implemente sua solução
# de procurar um caractere em uma string sem utilizar os métodos find ou o index.

def find_escrito(s, c):
    count = 0
    encontrado = 0
    for i in s:
        if i == c:
            encontrado = 1
            break
        count += 1

    
    if encontrado == 1:
        return count
    
    else:
        return -1
        

entrada = input("Informe um texto: ")
car = input("Informe o caractere para a pesquisa ")
saida = find_escrito(entrada, car)
if saida >= 0:
    print(saida)
else:
    print("Caractere não encontrado")

