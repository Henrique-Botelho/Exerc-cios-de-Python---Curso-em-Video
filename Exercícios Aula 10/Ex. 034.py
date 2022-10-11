sal = float(input('Digite o valor do seu salário:'))

if sal <= 1250:

    print('Com o aumento, seu salário passa a ser de R${:.2f}'.format(1.15*sal))

else:

    print('Com o aumento, seu salário passa a ser de R${:.2f}'.format(1.1*sal))
