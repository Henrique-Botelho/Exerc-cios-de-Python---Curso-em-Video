n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
if n1 > n2:
    print('O número {} é \033[32mmaior\033[m que o {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é \033[32mmaior\033[m que o {}'.format(n2, n1))
else:
    print('Os números são \033[31miguais\033[m!'.format(n1, n2))
