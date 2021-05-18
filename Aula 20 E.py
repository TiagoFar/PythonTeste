def soma(*valores): # desempacotar, somar varios valores
    s = 0
    for num in valores:
        s += num
    print(f'A soma de {valores} é igual a {s}')
soma(1, 2, 4)
soma11(2, 3)