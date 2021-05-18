valores = []
for cont in range(0, 5): # conta de 0 a 5 (range = conta = alcance)
    valores.append(int(input('Digite um número: ')))
for pos, val in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {val}!')