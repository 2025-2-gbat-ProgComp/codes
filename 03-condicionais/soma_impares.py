num1 = int(input("Numero1: "))
num2 = int(input("Numero2: "))
num3 = int(input("Numero3: "))
num4 = int(input("Numero4: "))


soma = 0
if num1 % 2 == 1:
    soma = soma + num1      
    
if num2 % 2 == 1:
    soma = soma + num2
    
if num3 % 2 == 1:
    soma = soma + num3
    
if num4 % 2 == 1:
    soma = soma + num4
    
print ("A soma dos ímpares é: ", soma)