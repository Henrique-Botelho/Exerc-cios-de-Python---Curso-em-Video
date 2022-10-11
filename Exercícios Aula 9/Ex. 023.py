n = int(input('Digite um número inteiro:'))

u = n//1 %10
d = n//10 %10
c = n//100 %10
m = n//1000 %10

print('Analisando o número {}:'.format(n))
print('Unidade(s): {}'.format(u))
print('Dezena(s): {}'.format(d))
print('Centena(s): {}'.format(c))
print('Milhar(es): {}'.format(m))
