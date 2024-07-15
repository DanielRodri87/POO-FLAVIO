def check_num(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
            
    if count == 2:
        
        return 1
    else:
        return 0
    
def check_range(num_min, num_max):
    while num_min <= num_max:
        if check_num(num_min):
            print(num_min, end=' ')
        num_min += 1
 
while True:       
    try: 
        min_input = int(input("Informe o valor inicial do intervalo: "))
        max_input = int(input("Informe o valor final do intervalo: "))
        check_range(min_input, max_input)
        break

    except:
        print("Houve alguma entrada inválida, o que impossibilitou a operação")
