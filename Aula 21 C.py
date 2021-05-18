def funcao():
    n1 = 4 #escopo local, vai chamar o N1 local
    print(f'N1 dentro vale {n1}')

#Programa Principal
n1 = 2 #escopo global, vai chamar o N1 global.
funcao()
print(f'N1 fora vale {n1}')