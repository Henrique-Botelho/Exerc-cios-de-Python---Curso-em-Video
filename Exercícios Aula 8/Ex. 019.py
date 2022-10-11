import random

n1 = input('Digite o nome de um(a) aluno(a):')
n2 = input('Digite o nome de um(a) aluno(a):')
n3 = input('Digite o nome de um (a) aluno(a):')
n4 = input('Digite o nome de um (a) aluno(a):')

Lista = [n1, n2, n3, n4]

es = random.choice(Lista)

print('='*60)
print('O escolhido foi {}.'.format(es))

# Outra maneira de fazer
from random import choice

n1 = input('Digite o nome de um (a) aluno(a):')
n2 = input('Digite o nome de um (a) aluno(a):')
n3 = input('Digite o nome de um (a) aluno(a):')
n4 = input('Digite o nome de um (a) aluno(a):')

Lista = [n1, n2, n3, n4]

es = choice(Lista)

print('='*60)
print('O escolhido foi {}.'.format(es))
