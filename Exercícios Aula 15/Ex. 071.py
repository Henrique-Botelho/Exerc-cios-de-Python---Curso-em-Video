cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

print('='*25)
print('       BANCO CEV')
print('='*25)

num = float(input('Qual valor você quer sacar? R$'))
while True:
    if num -50 < 0:
        break
    num -= 50
    cont1 += 1
while True:
    if num - 20 < 0:
        break
    num -= 20
    cont2 += 1
while True:
    if num - 10 < 0:
        break
    num -= 10
    cont3 += 1
while True:
    if num - 1 < 0:
        break
    num -= 1
    cont4 += 1
if cont1!= 0:
    print(f'Total de {cont1} cédulas de R$50')

elif cont2 != 0:
    print(f'Total de {cont2} cédulas de R$20')

elif cont3 != 0:
    print(f'Total de {cont3} cédulas de R$10')

elif cont4 != 0:
    print(f'Total de {cont4} cédulas de R$1')
