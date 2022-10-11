nome = str(input('Digite o seu nome completo:')).strip()

clean = nome.title()

print('O seu nome tem Silva? {}'.format('Silva' in clean))


# Outra maneira de fazer

nome = str(input('Digite seu nome completo:')).strip()

print('O seu nome tem Silva? {}'.format('Silva' in nome.title()))
