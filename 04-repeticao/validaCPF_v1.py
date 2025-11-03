cpf = int (input("Digite o CPF: "))

# Para CPF: ABCDEFGHIJK
dv2 = cpf % 10    # Extrai K
cpf = cpf // 10   # Torna o CPF = ABCDEFGHIJ
cpf_10 = cpf      # Guarda o CPF com 10 digitos
dv1 = cpf % 10    # Extrai J
cpf = cpf // 10   # Torna o CPF = ABCDEFGHI

# Calcula um digito verificador
soma  = 0
index = 2
while cpf > 0:
    soma += (cpf % 10)*index
    cpf //= 10
    index += 1        

dv_calc = ((soma * 10) % 11) % 10

if dv_calc == dv1:
    cpf = cpf_10
    
    # Calcula um digito verificador
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
                dv_calc, "informado", dv2)
else:
    print ("Dígito verificador 1 inválido. Esperado: ",
            dv_calc, "informado", dv1)
