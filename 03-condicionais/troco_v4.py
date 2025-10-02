# Este programa calcula o troco de uma conta.
# Ele foi feito por Galileu Batista em set/2025.
 
valor_conta = int(input("Qual o valor da conta: "))
valor_pago  = int(input("Qual o valor de pagamento: "))
if valor_pago > valor_conta:
    troco = valor_pago - valor_conta
    print ("O valor do troco é: ", troco)

    ced200 = troco // 200
    if ced200 > 0:
        print ("Devolva ", ced200, "cédulas de 200.")
        troco = troco - 200*ced200

    ced100 = troco // 100
    if ced100 > 0:
        print ("Devolva ", ced100, "cédulas de 100.")
        troco = troco - 100*ced100

    ced50 = troco // 50
    if ced50 > 0:
        print ("Devolva ", ced50, "cédulas de 50.")
        troco = troco - 50*ced50

    ced20 = troco // 20
    if ced20 > 0:
        print ("Devolva ", ced20, "cédulas de 20.")
        troco = troco - 20*ced20

    ced10 = troco // 10
    if ced10 > 0:
        print ("Devolva ", ced10, "cédulas de 10.")
        troco = troco - 10*ced10

    ced5 = troco // 5
    if ced5 > 0:
        print ("Devolva ", ced5, "cédulas de 5.")
        troco = troco - 5*ced5

    ced2 = troco // 2
    if ced2 > 0:
        print ("Devolva ", ced2, "cédulas de 2.")

    moedas1 = troco - 2*ced2
    if moedas1 > 0:
        print ("Devolva ", moedas1, "moedas de 1.")
else:
    if valor_conta == valor_pago:
        print ("Sem troco. Obrigado.")
    else:
        print ("Pagamento insuficiente")