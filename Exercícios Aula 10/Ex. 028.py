from random import randint
from time import sleep

n = randint(0,5)

print('Vou pensar em um número inteiro entre 0 e 5. \nTente adivinhar:')
print('-=-'*30)

num = int(input('Em qual número eu pensei?'))
print('-=-'*30)

print('Calculando...')
sleep(3)

if num == n:
    print('PARABÉNS, VOCÊ ACERTOU! \nEu pensei no número {}'.format(num))

else:
    print('ERRADO! Eu pensei no número {}'.format(n))

# Outra maneira de fazer condicional

'''l = randint(0,5)

print('Vou pensar em um número inteiro entre 0 e 5. \nTente adivinhar:')

glu = int(input('Em qual número eu pensei?'))

print('PARABÉNS, VOCÊ ACERTOU! \nEu pensei no número {}'.format(glu) if glu == l else 'ERRADO! Eu pensei no número {}'.format(l))'''
