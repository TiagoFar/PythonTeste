valores = [] # list() << é outra opção
valores.append(2)
valores.append(4)
valores.append(6)
for c, v in enumerate(valores): #na posiçao 'C', o valor é 'V'
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

