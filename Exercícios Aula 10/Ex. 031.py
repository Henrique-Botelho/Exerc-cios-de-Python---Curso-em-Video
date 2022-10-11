x = float(input('Qual será a distância (em Km) percorrida na viagem?'))

if x <= 200:

    print('O preço da viagem será de R${:.2f}'.format(0.5*x))

else:

    print('O preço da viagm será de R${:.2f}'.format(0.45*x))
