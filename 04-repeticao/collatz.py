maior = -1
for n in range (1, 100000):
    tam = 0
    while n > 1:
        tam += 1
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    tam += 1
    if tam > maior:
        maior = tam
print ("A squencia de maior tamanhor tem ", maior)