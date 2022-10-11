print('Calcule seu Índice de Massa Corpórea')
print('-=-'*20)

peso = float(input('Quanto você está pesando?(kg)'))
altura = float(input('Qual é a sua altura?(m)'))
imc = peso/(altura**2)

print('-=-'*20)
print('O IMC dessa pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO.')

elif imc >= 18.5 and imc < 25:
    print('Você está com um PESO IDEAL.')

elif imc >= 25 and imc <30:
    print('Você está com SOBREPESO.')

elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE.')

elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA.')
