print('DIGITE APENAS NÚMEROS INTEIROS:')
print('-=-'*20)

h = 0
p = 0
for c in range(1, 7):
    c = int(input('Digite um número:'))
    if c%2 == 0:
        h += 1
        p += c
print('A soma de todos os {} números pares dentre os escolhidos é: {}.'.format(h, p))
