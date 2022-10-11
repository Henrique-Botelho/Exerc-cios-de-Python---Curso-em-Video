import random

n1 = input('Nome:')
n2 = input('Nome:')
n3 = input('Nome:')
n4 = input('Nome:')

Lista = [n1, n2, n3, n4]
random.shuffle(Lista)

print('='*60)
print('A ordem proposta é: \n {}'.format(Lista))

# Outra maneira de fazer
from random import shuffle

n1 = input('Nome:')
n2 = input('Nome:')
n3 = input('Nome:')
n4 = input('Nome:')

Lista = [n1, n2, n3, n4]
shuffle(Lista)

print('='*60)
print('A ordem proposta é:\n {}'.format(Lista))
