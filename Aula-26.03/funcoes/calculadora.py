def soma(num1, num2=0):
    print(num1+num2)

def subtracao(num1, num2=0):
    print(num1-num2)

def multiplicacao(num1, num2=1):
    print(num1*num2)

def divisao(num1, num2=1):
    try:
        num1/num2
    except:
        print("Divisão por 0")
while True:   
    def main():
        print("CALCULADORA DO DANIEL\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
        x = int(input("Digite o valor 1: "))
        y = int(input("Digite o valor 2: "))
        menu = int(input("Escolha a opção: "))
        if menu == 1:
            soma(x, y)
        elif menu == 2:
            subtracao(x, y)
        elif menu == 3:
            multiplicacao(x, y)
        else:
            divisao(x, y)

    if __name__ == '__main__':
        main()