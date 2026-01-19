for num in range(1, 10000):
    soma_div_num = 0
    for div in range (1, num//2+1):
        if num % div == 0:
            soma_div_num += div
                
    soma_soma_div_num = 0
    for div in range (1, soma_div_num//2+1):
        if soma_div_num % div == 0:
            soma_soma_div_num += div
    
    if num < soma_div_num and num == soma_soma_div_num:
        print (num, soma_div_num)