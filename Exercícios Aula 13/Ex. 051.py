print('='*29)
print('     10 TERMOS DE UMA PA')
print('='*29)

a1 = int(input('Digite o \033[32mprimeiro\033[m termo da sua PA:'))
r = int(input('Digite o valor da \033[31mrazão\033[m da sua PA:'))
print('='*29)

for c in range(0, 10):
    print(a1 + c*r, end='→')

print('ACABOU!')

#Outra maneira de fazer
print('='*50)

a1 = int(input('Digite o \033[32mprimeiro\033[m termo da sua PA:'))
r = int(input('Digite o valor da \033[31mrazão\033[m da sua PA:'))
dez = a1 + 9*r
print('='*29)

for l in range(a1, dez + r, r):
    print('{}'.format(l), end='→')

print('ACABOU!')
