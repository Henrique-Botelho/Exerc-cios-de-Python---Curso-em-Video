#Primeira maneira
n1 = float(input('Digite um número:'))
n2 = float(input('Digite mais um número:'))

print('A soma dos números é \033[1;33m{}\033[m'.format(n1+n2))

#Segunda maneira
n3 = float(input('Digite um número:'))
n4 = float(input('Digite outro número:'))
s = n3 + n4

print('A soma dos números é \033[33;44m{}\033[m'.format(s))
