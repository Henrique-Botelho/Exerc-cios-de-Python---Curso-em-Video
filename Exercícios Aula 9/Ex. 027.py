nome = str(input('Digite seu nome completo:')).strip()

l = nome.split()

print('Seu primeiro nome é', l[0])
print('Seu último nome é', l[len(l) -1])
