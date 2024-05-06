while True:
    fatorial = int(input("Digite o valor para fatorial"))
    r = 1

    if (fatorial < 0):
        break
    
    while fatorial > 0:
        r *= fatorial
        fatorial -= 1
        
    print(r)