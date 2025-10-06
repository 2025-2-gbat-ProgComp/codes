# Esse programa determina se há interseção entre segmentos de reta

inic1 = float (input ("Digite o inicio do seguimento 1:"))
fim1  = float (input ("Digite o final do seguimento 1:"))
inic2 = float (input ("Digite o inicio do seguimento 2:"))
fim2  =  float (input ("Digite o final do deguimento 2:"))

if inic1 <= inic2:
    if fim1<inic2:
        print ("if1: não tem interseção")
    else:
        print ("if1: Tem interseção")
else:
    if fim2<inic1:
        print ("if2: não tem interseção")
    else:
        print ("if2: Tem interseção")