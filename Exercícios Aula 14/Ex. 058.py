import time
import random

dif = 0
cont = 1

print('Sou se computador...')
time.sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
time.sleep(2)
print('Será que você é capaz de advinhar ?')
time.sleep(2)

num = int(input('Digite o número e tente a sorte:'))
esc = random.randint(1, 10)

while num != esc:
    if num < esc:
        dif = esc- num
        num = int(input('É um número maior. Tente novamente:'))
    if num > esc:
        dif = num - esc
        num = int(input('É um número menor. Tente novamente:'))
    cont += 1

if cont <= 3:
    print('PARABÉNS! Você acertou na {}ª tentativa! O número é {}.'.format(cont, esc))

if 3 < cont <= 5:
    print('BOA! Você acertou na {}ª tentativa. O número é {}.'.format(cont, esc))

if cont > 5:
    print('Você acetou na {}ª tentativa. O número é {}. A sorte não está com você.'.format(cont, esc))