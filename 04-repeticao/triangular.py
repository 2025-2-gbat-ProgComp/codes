triang = 0
for n in range (1, 101):
    triang += n
    print ("triangular(",n, ") =", triang, end=": ")
    for div in range(1, triang+1):
        if triang % div == 0:
            print (div, end=" ")
    print ()