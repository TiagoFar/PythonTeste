estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # com Copy! eu mudo os valores na COPIA, e não no PRINCIPAL! Precisa fazer uma cópia com 'copy' ao invés do '[:]' fatiamento
for e in brasil:
    print(e) # para cada estado no Brasil eu mostro estado.
for e in brasil:
    for k, v in e.items(): # mostra tudo
        print(f'O campo {k} tem valor {v}') # mostrando formatado
for e in brasil:
    for v in e.values(): # mostra só os valores, por isso não tem o 'K'
        print(f'{v}', end=' ')
    print()






