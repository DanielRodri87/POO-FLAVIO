
def iterative_factorial(factorial):
    r = 1

    while factorial > 0:
        r *= factorial
        factorial -= 1
        
    print(r)

def recursive_factorial(factorial):
    if factorial == 0:
        return 1
    
    return factorial * recursive_factorial(factorial-1)


while True:
    try: 
        menu = int(input("Escolha a opção:\n1 - Iterativo\n2 - Recursivo\n3 - Sair\n-> "))
        
        if menu == 1:
            factoria_input = int(input("Informe o valor para ser calculado: "))
            print("Iterativo: ")
            iterative_factorial(factoria_input)
            
        elif menu == 2:
            factoria_input = int(input("Informe o valor para ser calculado: "))
            print("Recursivo: ")
            output = recursive_factorial(factoria_input)
            print(output)

        elif menu == 3:
            print("saindo...")
            break
        else:
            print("Valor inválido, digite novamente")
    except:
        print("Houve alguma entrada inválida, o que impossibilitou o cálculo do fatorial")

    