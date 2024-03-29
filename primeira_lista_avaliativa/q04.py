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
            print(num_min)
        num_min += 1
        
    
check_range(1, 14)