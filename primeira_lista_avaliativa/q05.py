def decimal_binary(decimal):
    if decimal == 0:
        return [0]
    
    binary_list = []
    while decimal > 0:
        rest = decimal % 2
        binary_list.insert(0, rest)
        decimal = decimal // 2
    
    return binary_list

def read_list(list_input):
    for i in range(len(list_input)):
        print(list_input[i], end=' ')
   
while True:      
    try:
        decimal = int(input("Digite um número decimal: "))
        read_list(decimal_binary(decimal))
        break
    except:
        print("Houve algum erro com a entrada, tente novamente")
