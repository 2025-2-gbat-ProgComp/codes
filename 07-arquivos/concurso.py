fd = open('dadosResultadoConcurso.txt', 'r')

candidatos = []
for linha in fd:
	colunas = linha.split(';')
	
	nome = colunas[1]
	n1 = float(colunas[2].replace(',', '.'))
	n2 = float(colunas[3].replace(',', '.'))
	n3 = float(colunas[4].replace(',', '.'))
	subj = float(colunas[5].replace(',', '.'))
	media_obj = (n1 + n2 + n3) / 3
	total = media_obj + subj

	candidatos.append((nome, media_obj, subj))

print()
print(' - Resultados finais do concurso - \n')
	
maior_subj = max(candidatos, key=lambda x: x[2])
print(f'Maior nota subjetiva: {maior_subj[0]} - {maior_subj[2]}')

maior_obj = max(candidatos, key=lambda x: x[1])
print(f'Maior nota objetiva: {maior_obj[0]} - {maior_obj[1]}')

lista_aprovados = filter (lambda x : x[1] >= 6 and x[2] >= 20, candidatos)
print('Os aprovados são:')
for nome, obj, subj in lista_aprovados:
    print(f'{nome} - {obj + subj}')

print()

maiores_notas = sorted(candidatos, key=lambda x: x[1] + x[2], reverse=True)[:10]
print(f'Os dez primeiros colocados são:')
for nome, obj, subj in maiores_notas:
    print(f'{nome} - {obj + subj}')

nome_busca = input ("Nome a buscar: ").upper()
candidatos_nome = filter (lambda x : nome_busca in x[0], candidatos)
print(f'Candidatos com o nome {nome_busca}:')
for nome, obj, subj in candidatos_nome:
    print (f"{nome} - {obj} + {subj} = {obj+subj} ", end="-> ")
    aprovado = (obj >= 6) and (subj >= 20)
    if aprovado:
        print ("APROVADO")
    else:
        print ("REPROVADO")