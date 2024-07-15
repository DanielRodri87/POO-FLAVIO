a = int(input("Digite um número: "))
b = type(a)
try: 
    if b != int:
        print("Numero invalido")
    else:
        print(a)
except:
    print("Numero invalido")
