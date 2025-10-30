cpf = int (input("Digite o CPF: "))

dv2 = cpf % 10
cpf = cpf // 10
dv1 = cpf % 10
cpf = cpf // 10
cpf_base = cpf

soma  = 0
index = 2
while cpf > 0:
    soma += (cpf % 10)*index
    cpf //= 10
    index += 1        

dv_calc = ((soma * 10) % 11) % 10
if dv_calc == dv1:
    cpf = cpf_base * 10 + dv1
    
    soma  = 0
    index = 2
    while cpf > 0:
        soma += (cpf % 10)*index
        cpf //= 10
        index += 1        

    dv_calc = ((soma * 10) % 11) % 10
    if dv_calc == dv2:
        print ("CPF válido ...")
    else:
        print ("Dígito verificador 2 inválido. Esperado: ",
                dv_calc, "encontrado", dv2)
else:
    print ("Dígito verificador 1 inválido. Esperado: ",
            dv_calc, "encontrado", dv1)
