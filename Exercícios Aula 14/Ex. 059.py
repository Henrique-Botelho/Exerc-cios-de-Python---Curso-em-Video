num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
print('-=-'*30)

print('[ 1 ] Somar os dois \n[ 2 ] Multiplicar os dois \n[ 3 ] Qual o maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa')
print('-=-'*30)

esc  = int(input('Selecione uma opção:'))

while esc != 5:

    if esc == 1:
        print('A soma dos dois números é {}'.format(num1 + num2))
    
    elif esc == 2:
        print('O produto dos dois números é {}'.format(num1*num2))
    
    elif esc == 3:
        if num1 > num2:
            print('O número {} é maior.'.format(num1))
        elif num2 > num1:
            print('O número {} é maior.'.format(num2))
        elif num1 == num2:
            print('Os dois são iguais.')
            
    if esc == 4:
        print('-=-'*30)
        num1 = float(input('Digite um número:'))
        num2 = float(input('Digite outro número:'))


    print('-=-'*30)
    esc  = int(input('Selecione uma opção:'))


print('Obrigado por usar este programa!')