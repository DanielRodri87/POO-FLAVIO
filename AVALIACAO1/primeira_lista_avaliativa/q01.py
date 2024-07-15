def square_area(side):
    return side * side

def triangle_area(base, height):
    return (base * height) / 2

def circle_area(radius):
    return 3.14 * radius * radius
    

while True:
    try:
        print("Você deseja calcular área de:\n1 - Quadrado\n2 - Triângulo\n3 - Circulo\n4 - Sair")
        menu = int(input())
        if menu == 1:
            print("Quadrado: ")
            side_input = float(input("Informe o tamanho dos lados: (em cm) "))
            output = square_area(side_input)
        elif menu == 2:
            print("Triângulo: ")
            base_input = float(input("Informe o tamanho da base do triângulo: (em cm) "))
            height_input = float(input("Informe a altura do triângulo: (em cm) "))
            output = triangle_area(base_input, height_input)
        elif menu == 3:
            print("Circulo: ")
            radius_input = float(input("Informe o tamanho do raio: (em cm) "))
            output = circle_area(radius_input)
        elif menu == 4:
            print("saindo...")
            break
        else:
            print("Valor inválido, digite novamente")
            
        print(f"A área é: {output} centimetros")
    except:
        print("Output não pode ser calculado devido a opção inválida de entrada\n\n")