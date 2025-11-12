texto = input ("Texto a cifrar: ")
senha = input ("Qual o alfabeto da cifragem: ").lower()
pos = 0

if len(senha) > 0:
    cifrado = ""
    for letra in texto:
        dist_a = ord(senha[pos]) - ord('a') 
        pos = (pos + 1) % len(senha)

        if 'a' <= letra <= 'z':
            letra = chr(ord(letra) + dist_a)
            if letra > 'z':
                letra = chr(ord('a') + (ord(letra) - ord('z') - 1)) 
        elif 'A' <= letra <= 'Z':
            letra = chr(ord(letra) + dist_a)
            if letra > 'Z':
                letra = chr(ord('A') + (ord(letra) - ord('Z') - 1)) 
        cifrado = cifrado + letra
        
    print (cifrado)
else:
    print ("Alfabeto nao informado!")