cpf = int (input("Digite o CPF: "))

# Para CPF: ABCDEFGHIJK
dv2 = cpf % 10    # Extrai K
cpf = cpf // 10   # Torna o CPF = ABCDEFGHIJ
dv1 = cpf % 10    # Extrai J
cpf = cpf // 10   # Torna o CPF = ABCDEFGHI

erro = False
for dig in range(1, 3):
    soma  = 0
    index = 2
    cpf_base = cpf
    while cpf > 0:
        soma += (cpf % 10)*index
        cpf //= 10
        index += 1        
    cpf = cpf_base
    
    dv_calc = ((soma * 10) % 11) % 10
    if dig == 1:
        dv = dv1
    else:
        dv = dv2
    
    if dv_calc == dv:
        cpf = cpf * 10 + dv
    else:
        print ("Dígito verificador inválido. Esperado: ",
                 dv_calc, "encontrado", dv)
        erro = True

if erro == False:
    print ("CPF Válido.")