
def soma_divisores (num):
    soma_div_num = 0
    for div in range (1, num//2+1):
        if num % div == 0:
            soma_div_num += div
    return soma_div_num



for num in range(1, 10000):   
    a = soma_divisores(num)
    b = soma_divisores(a)

    if num < a and num == b:
        print (num, a)