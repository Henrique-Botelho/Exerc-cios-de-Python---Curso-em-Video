v = float(input('Digite o valor do imóvel:'))
s = float(input('Digite o valor do salário do comprador:'))
a = float(input('Em quantos anos pretende pagar a casa?'))

if v/(12*a) > 0.3*s:
    print('\033[31mEMPRÉSTIMO NEGADO!\033[m')
    print('O valor da prestação seria de R${:.2f}'.format(v/(12*a)))
else:
    print('\033[32mEMPRÉSTIMO APROVADO!\033[m')
    print('O valor da prestação é de R${:.2f}'.format(v/(12*a)))
