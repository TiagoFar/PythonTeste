a = [1,2,3,4]
# b = a #É UMA LIGACAO! igualei e criei uma ligação entre elas!
b = a[:] # é uma CÓPIA! [:] pego todos os valores da lista!
b[2] = 8 # com esse comando eu troco o valor 2 por 8 nas DUAS LISTAS!
print(f'Lista A: {a}')
print(f'Lista B: {b}')