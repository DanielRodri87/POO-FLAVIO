array = []
count = 0
while True:
    a = int(input("Digite o número: "))

    if a < 0:
        break

    if a == 0:
        array.insert(len(array) // 2, a)
    elif a % 2 == 0:
        array.append(a)
    else:
        array.insert(0, a)
    
print(array)