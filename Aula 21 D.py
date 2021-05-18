def teste(b):
    global a # nao crie uma variavel a, utilize o 'a' global
    a = 8 # aqui estou adicionando a variavel A dentro do escopo local
    b += 4 # 5 + 4 = 9
    c = 2
    print(f'Var A dentro vale {a}')
    print(f'Var B dentro vale {b}')
    print(f'Var C dentro vale {c}')

a = 5
teste(a)
print(f'Var A fora vale {a}') # aqui eu digo que é para manter a variavel
                                # A do escopo global "global a", a=5 vira a=8!!!