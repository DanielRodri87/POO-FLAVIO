num = "0"
nome = str(input())
num.type(int)
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

if lado1 > lado2+lado3 or lado2 > lado3+lado1 or lado3 > lado1+lado2:
    print("não é possivel formar um trigando")
elif lado1 == lado2 and lado2 == lado3:
    print("equilatero")
elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1:
    print("isoceles")
else:
    print("escaleno")