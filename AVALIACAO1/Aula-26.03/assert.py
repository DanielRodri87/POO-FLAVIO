try: 
    a = input("Digite o primeiro valor: ")
    a = int(a)

    try:
        assert isinstance(a, int)
    except: 
        while True:
            try:
                a = int(input("Digite um novo valor: "))
                break
            except:
                print("Digite um inteiro")
                continue
except:
    while True:
        try:
            a = int(input("Digite um novo valor: "))
            break
        except:
            print("Digite um inteiro")
            continue
        
print(a)