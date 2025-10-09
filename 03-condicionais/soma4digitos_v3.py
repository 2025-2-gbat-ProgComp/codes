# Este programa soma os digitos de números positivos 
# de até 4 dígitos
try:
    num = int (input("Digite um numero: "))
    if 0 <= num < 10000:
        soma = 0
        
        soma = soma + num % 10
        num = num // 10
        soma = soma + num % 10
        num = num // 10
        soma = soma + num % 10
        num = num // 10
        soma = soma + num % 10
        num = num // 10
        
        print ("A soma dos dígitos é: ", soma)
    else:
        print ("Número fora dos limites (4 dígitos)")
except ValueError:
    print ("Número com formato inválido!!!")