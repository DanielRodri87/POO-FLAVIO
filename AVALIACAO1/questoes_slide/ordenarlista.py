total = []
while True:
    
    n = int(input("Informe um número: "))
    if n < 0:
        break
    else:
        total.append(n)
        
total.sort()

total = list(filter(lambda x: x % 2 == 0 and x != 0, total)) + list(filter(lambda x: x==0, total))  + list(filter(lambda x: x % 2 != 0, total))
    
    
print(total)