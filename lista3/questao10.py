# Gere uma lista de 100 números inteiros de 1 até 100. Apenas usando as funções básicas
# (não use bibliotecas científicas tais como numpy, panda ou scipy). Calcule:
# a. Média
# b. Mediana (lembre-se, se o “n” é par ou ímpar)
# c. Variância
# d. Desvio Padrão

lista = [x for x in range(1, 101)]

def media(lista):
    soma = 0
    for i in lista:
        soma += i
        
    return soma / len(lista)

def mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[int(len(lista) / 2)] + lista[int(len(lista) / 2 - 1)]) / 2
    else:
        return lista[int(len(lista) / 2)]
    
def variancia(lista):
    m = media(lista)
    soma = 0
    for i in lista:
        soma += (i - m) ** 2
        
    return soma / len(lista)

def desvio_padrao(lista):
    return variancia(lista) ** 0.5

print(f'Média: {media(lista)}')
print(f'Mediana: {mediana(lista)}')
print(f'Variância: {variancia(lista)}')
print(f'Desvio Padrão: {desvio_padrao(lista)}')

