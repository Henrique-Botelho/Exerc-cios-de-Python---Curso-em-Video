from time import sleep
from random import choice

print('Suas opções:')
print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')
eu = int(input('Sua escolha:'))

if eu == 1:
    es = 'Pedra'
elif eu == 2:
    es = 'Papel'
elif eu == 3:
    es = 'Tesoura'

print('-=-'*10)

print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ!')

lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)

print('-=-'*10)

print('O computador jogou {}'.format(pc))
print('Você jogou {}'.format(es))

print('-=-'*10)

if es == 'Pedra':
    if pc == 'Pedra':
        print('\033[33mEMPATE!\033[m')
    elif pc == 'Papel':
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif pc == 'Tesoura':
        print('\033[32mVOCÊ GANHOU!\033[m')

elif es == 'Papel':
    if pc == 'Pedra':
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif pc == 'Papel':
        print('\033[33mEMPATE!\033[m')
    elif pc == 'Tesoura':
        print('\033[31mVOCÊ PERDEU!\033[m')

elif es == 'Tesoura':
    if pc == 'Pedra':
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif pc == 'Papel':
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif pc == 'Tesoura':
        print('\033[33mEMPATE!\033[m')
