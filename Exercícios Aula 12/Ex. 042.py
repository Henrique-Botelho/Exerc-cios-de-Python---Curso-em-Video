print('-=-'*20)
print('ANALISADOR DE TRIÂNGULOS 2.0')
print('-=-'*20)

l1 = float(input('Digite o primeiro segmento:'))
l2 = float(input('Digite  o segundo segmento:'))
l3 = float(input('Digite o terceiro segmento:'))


if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print('Com esses segmentos não é possível fazer um triângulo.')

else:
    if l1 == l2 == l3:
        print('Esses segmentos formam um triângulo EQUILÁTERO')

    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('Esses segmentos formam um triângulo ISÓCELES')

    elif l1 != l2 != l3:
        print('Esses segmentos formam um triângulo ESCALENO')
