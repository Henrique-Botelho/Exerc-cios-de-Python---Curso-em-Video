print('-='*25)
print('CALCULANDO OS 10 PRIMEIROS TERMOS DE UMA PA')
print('-='*25)

n = 0

a1 = float(input('Digite o primeiro termo dessa PA:'))
r = float(input('Digite a razão dessa PA:'))

while n <= 9:
    n += 1
    an = a1 + (n-1)*r
    print(an, end='')
    print(' → ' if n <= 9 else '', end='')