# Aprendemos que a função len() retorna o tamanho de uma string. Faça uma função
# chamada de tamString(s) que recebe uma string qualquer e retorna o tamanho de “s” sem
# usar a função len(). 

def TamString(S):
    return len(S)

palavra = input("Informe a palavra: ")
print(f"O tamanho é: {TamString(palavra)}")