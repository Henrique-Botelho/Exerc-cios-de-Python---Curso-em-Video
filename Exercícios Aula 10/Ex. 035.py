print('-=-'*30)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*30)

l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo segmento:'))
l3 = float(input('Terceiro segmento:'))

if (l1 + l2) <= l3 or (l2 + l3) <= l1 or (l2 + l3) <= l1:

    print('Não é possível fazer um triângulo com esses segmentos.')

else:

    print('É possivel fazer um triângulo com esses segmentos.')
