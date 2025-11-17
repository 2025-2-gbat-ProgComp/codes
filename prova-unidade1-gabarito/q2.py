num = 1
ndivs = 0

while ndivs < 5:
    num = num + 1
    if (num % 13 == 0) and (num % 7 == 0):
        ndivs += 1
    
print ("O quinto divisor é: ", num)