from time import sleep

cores = {'sem cor':'\033[m', 'vermelho':'\033[1;31m', 'verde': '\033[1;32m'}

v = float(input('Digite a velocidade do carro (em Km/h):'))
print('-=-'*30)

print('ANALISANDO...')
sleep(3)
print('-=-'*8)

if v > 80:

    print('{}VOCÊ FOI MULTADO!{}'.format(cores['vermelho'], cores['sem cor']))
    print('-=-'*8)

    print('Terá que pagar {}R${:.2f}{}'.format(cores['vermelho'], (v-80)*7, cores['sem cor']))

else:

    print('{}Tudo certo{}, você está dentro do limite de velocidade!'.format(cores['verde'], cores['sem cor']))
