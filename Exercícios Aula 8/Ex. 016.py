# Dessa maneira a biblioteca math não precisa ser usada
n2 = float(input('Digite um número real qualquer:'))
print('A parte real do número {} é {}.'.format(n2, int(n2)))

print('='*60)

import math

n = float(input('Digite qualquer número real:'))

print('A parte inteira do número {} é {}.'.format(n, math.trunc(n)))


print('='*60)
# Uma outra maneira de fazer é:

from math import trunc

n = float(input('Digite qualquer número real:'))

print('A parte inteira do número {} é {}.'.format(n, trunc(n)))
