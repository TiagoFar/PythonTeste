lista = []
listapar = []
listaimpar = []
resp = ' '
lista.append(int(input('Digite um número: ')))
while True:
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'S':
        lista.append(int(input('Digite um número: ')))
    if resp == 'N':
        break
for i, v in enumerate(lista): #aqui em cada posição eu mostro o que está na lista, um a um...
    if v % 2 == 0:
        listapar.append(v)
    else:
        if v % 2 == 1:
            listaimpar.append(v)
print(f'A lista completa é: {lista}')
print(f'Os valores pares são: {listapar}')
print(f'Os valores ímpares são: {listaimpar}')








