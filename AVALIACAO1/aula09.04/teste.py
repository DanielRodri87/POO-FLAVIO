var = int(input("Valor: "))

primos = [y for y in range(1, var+1) if var % y == 0]
print(primos)
if len(primos) == 2:
    print("é primo")
else:
    print("nao é primo")