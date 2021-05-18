n = int(input('Digite um número: '))
n2 = int(input('Digite outro número:'))
s = n+n2
m = (n+n2)/2
di = n//n2
e = n**n2
r1 = n**(1/2)
r2 = n2**(1/2)
mod = (n+n2)%2
print('A soma de {} e {} é {}'.format(n,n2,s))
print('A média entre {} e {} é {}'.format(n,n2,m),'\n A divisão inteira de {} e {} é {}'.format(n,n2,di))
print('A exponenciação entre {} e {} é {:.4f}'.format(n,n2,e), end ='...')
print('A raiz quadrada de {} e de {} são respectivamente {},{}'.format(n,n2,r1,r2))
print('O módulo de {} com {} é {}'.format(n,n2,mod))








