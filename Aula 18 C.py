galera = []
dados = []
totmaior = totmenor = 0 # só posso fazer desse jeito para variáveis simples e NÃO PARA LISTAS!
for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite a sua idade: ')))
    galera.append(dados[:]) # [:] faz uma cópia
    dados.clear()
print(galera)
print('*'*20)
for p in galera:
    if p[1] >= 21: # p1 é a IDADE!!!
        print(f'{p[0]} é maior de idade.') # p[0] é o NOME!!!
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maior de idade e {totmenor} menor de idade')

