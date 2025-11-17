num = int(input("Digite um numero: "))

qtde_impares = 0
soma_pares = 0
qtde_pares = 0
soma_total = 0

while num > 0:
    if num % 2 == 1:
        qtde_impares += 1
    else:
        soma_pares += num        
        qtde_pares += 1
    soma_total += num
         
    num = int(input("Digite um numero: "))

print (f"A qtde de ímpares é: {qtde_impares}")

if qtde_pares > 0:
    print ("A média dos pares é: ", soma_pares/qtde_pares)
else:
    print ("Nenhum par foi digitado. Média não calculada.")
    
if (qtde_pares + qtde_impares) > 0:
    print ("A média total é: ", soma_total/(qtde_pares+qtde_impares))
else:
    print ("Nenhum número positivo foi digitado. Média não calculada.")
