# Sem utilizar o módulo math
ca = float(input('Digite o valor de um cateto:'))
co = float(input('Digite o valor de outro cateto:'))
h = ((ca**2) + (co**2))**(1/2)

print('A hipotenusa desse triângulo retângulo vale {}.'.format(h))
print('='*60)

# Essa maneira utilizada o módulo math
import math

c1 = float(input('Valor de um cateto:'))
c2 = float(input('Valor de outro cateto:'))

print('A hipotenusa desse triângulo retângulo é {}.'.format(math.hypot(c1, c2)))
print('='*60)

# Outra maneira de fazer
from math import hypot
c1 = float(input('Valor de um cateto:'))
c2 = float(input('Valor do outro cateto:'))
print('A hipotenusa desse triângulo retângulo é {}.'.format(hypot(c1, c2)))
