num = int(input('Digite um número \npara saber seu fatorial:'))
cont = num
f = 1

print('O número {}! = '.format(num), end='')

while cont > 0:
    print('{}'.format(cont), end=' ')
    print('X' if cont > 1 else '=', end=' ')
    f *= cont
    cont -= 1
print(f)
