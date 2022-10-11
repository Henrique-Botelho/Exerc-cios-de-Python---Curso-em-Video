import math

alfa = float(input('Digite o valor de um ângulo qualquer em graus:'))

s = math.sin(math.radians(alfa))
c = math.cos(math.radians(alfa))
t = math.tan(math.radians(alfa))
print('-'*60)

print('Valor do seno: {:.2f} \nValor do cosseno: {:.2f} \nValor da tangente: {:.2f}'.format(s, c, t))

print('='*60)

# Outra maneira de fazer
from math import sin, cos, tan, radians

beta = float(input('Escreva o ângulo que deseja:'))

s = sin(radians(beta))
c = cos(radians(beta))
t = tan(radians(beta))
print('-'*60)
print('Valor do seno {:.2f} \nValor do cosseno {:.2f} \nValor da tangente {:.2f}'.format(s, c, t))
