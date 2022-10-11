h = float(input('Digite a altura da sua parede:'))
l = float(input('Digite a largura da sua parede:'))
a = h*l
t = a/2
print('-'*60)

print('A parede de dimensões {} X {} possui {} m² de área e necessita de {} litros de tinta para ser pintada.'.format(h, l, a, t))
