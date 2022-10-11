c = float(input('Escreva a temperatura em celsius que deseja converter:'))
f = (9*c/5) + 32
k = c + 273
print('='*60)

print('A temperatura {:.2f}°C corresponde a: \n{:.2f} °Fahrenheit \n{} Kelvin'.format(c, f, k))
