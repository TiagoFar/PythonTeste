from time import sleep
def contador(*num): # desempacotar, vou jogar qualquer valor de contador dentro de num!
    print(f'Foram digitados os valores {num} e temos ao total {len(num)} valores')

contador(2, 4, 6)
sleep(1)
contador(10, 20, 30, 40, 50)
sleep(1)
contador(3, 2)
sleep(1)
print('Fim')