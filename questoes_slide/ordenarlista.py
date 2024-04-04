array = []
count = 0
while True:
    a = int(input("Digite o número: "))
    
    if a == 0:
        array.insert(len(array) // 2, a)
    elif a > 0:
        if a % 2 == 0:
            array.insert(0, a)
        else:
            array.append(a)
    else:
        break
print(array)