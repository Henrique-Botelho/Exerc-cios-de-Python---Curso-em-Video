from random import randint

cont = 0

print('='*30)
print('JOGO DO PAR OU ÍMPAR')
print('='*30)

while True:
    comp = randint(0, 10)

    num = int(input('Digite um número inteiro de 0 a 10: '))
    while num not in range(0, 10):
        num = int(input('Digite um número inteiro de 0 a 10: '))

    esc = str(input('Par[P] ou Ímpar[I]?')).strip().upper()
    while esc not in 'PI':
            esc = str(input('Par[P] ou Ímpar[I]?')).strip().upper()
    print('='*20)
    
    soma = comp + num

    if soma%2 == 0:
        if esc == 'P':
            print(f'O computador escolheu {comp} e você {num}. A soma é {soma}. Você ganhou! \nJogue mais uma vez!')
            print('='*20)
            cont += 1
        else:
            print(f'O computador escolheu {comp} e você {num}. A soma é {soma}. Você perdeu! \nReinicie o programa!')
            print('='*20)
            print(f'Você venceu {cont} rodada[s].')
            break

    elif soma%2 != 0:
        if esc == 'I':
            print(f'O computador escolheu {comp} e você {num}. A soma é {soma}. Você ganhou! \nJogue mais uma vez!')
            print('='*20)
            cont += 1
        else:
            print(f'O computador escolheu {comp} e você {num}. A soma é {soma}. Você perdeu! \nReinicie o programa!')
            print('='*20)
            print(f'Você venceu {cont} rodada[s].')
            break