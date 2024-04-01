def recursive_factorial(factorial):
    if factorial == 0:
        return 1
    
    return factorial * recursive_factorial(factorial-1)


def arrangement(n, p):
    return  recursive_factorial(n)/(recursive_factorial(n-p))

def combination(n, r):
    return recursive_factorial(n) / (recursive_factorial(r) * recursive_factorial(n - r))
    
    
while True:
    try: 
        menu = int(input("Escolha a opção:\n1 - Arranjo\n2 - Combinação\n3 - Sair\n-> "))
        
        if menu == 1:
            print("Arranjo: ")
            n_input = int(input("Informe o valor de n: "))
            p_input = int(input("Informe o valor de p: "))
            print(arrangement(n_input, p_input))
           
            
        elif menu == 2:
            print("Combinação: ")
            n_input = int(input("Informe o valor de n: "))
            r_input = int(input("Informe o valor de r: "))
            print(combination(n_input, r_input))

        elif menu == 3:
            print("saindo...")
            break
        else:
            print("Valor inválido, digite novamente")
    except:
        print("Houve alguma entrada inválida, o que impossibilitou o cálculo")

    