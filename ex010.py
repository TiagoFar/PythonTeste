n1 = float(input('Digite sua 1a nota: '))
n2 = float(input('Digite sua 2a nota: '))
m = (n1 + n2) / 2
print('Sua primeira nota foi {}, a segunda foi {} e sua '
      'Média foi {}.'.format(n1, n2, m))
if m >= 7.0:
    print('Parabéns, você é foda!')
else:
    print('Não desista, continue estudando!')