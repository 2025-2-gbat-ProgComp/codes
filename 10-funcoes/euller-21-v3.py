def soma_divisores (num):
    soma_div_num = 0
    for div in range (1, num//2+1):
        if num % div == 0:
            soma_div_num += div
    return soma_div_num

def amigos (a, b):
    if soma_divisores(a) == b and soma_divisores(b) == a:
        return True
    else:
        return False
    
for a in range(1, 10000):   
    for b in range (a+1, 10000):
        if amigos(a, b):
            print (a, b)