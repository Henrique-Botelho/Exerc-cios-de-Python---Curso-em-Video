n = int(input('Digite um número inteiro:'))
contar1 = 0

for c in range(1, n+1):
    if n%c == 0: #Divisores
        print('\033[32m{}\033[m'.format(c), end=' ')
        contar1 += 1
    else: #Não divisores
        print('\033[31m{}\033[m'.format(c), end=' ')

print('\nO número {} possui {} divisores iteiros.'.format(n, contar1))

if contar1 == 2:
    print('O núemro {} é PRIMO.'.format(n))

else:
    print('O número {} não é PRIMO.'.format(n))
