def somar(a=0, b=0, c=0): # podem ser todos parametros opcionais, se não tiver valor de c, ele será igual a zero!
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(3, 2)
somar(3)
somar()
#soma(b=4, c=2) posso designar os valores e o 'a' vai ser zero.