import math #  << importa todas as funcionalidades
# from math import sqrt << vai importar só a raiz quadrada e não irá precisa mais a "math" para chamar a raiz!
n = int(input('Digite um número: '))
raiz = math.sqrt(n) # aqui não precisa chamar a raiz se ela foi importada com o "from math import sqrt".
print('A raiz quadrada de {} é {}.'.format(n,raiz))
print('A raiz quadrada de {} arredondado pra cima é {}.'.format(n, math.ceil(raiz)))
print('A raiz quadrada de {} arredondada pra baixo é {}.'.format(n, math.floor(raiz)))
print('A raiz quadrada de {} é {:.2f} com formatação de 2 casas'.format(n, raiz))