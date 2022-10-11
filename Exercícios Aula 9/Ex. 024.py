c = str(input('Digite o nome de uma cidade:').strip())

v = c.capitalize()

print('A cidade começa ou não com o nome Santo? {}'.format(v[:5] == 'Santo'))


# Outra maneira de fazer

cid = str(input('Digite o nome de uma cidade:')).strip()

print('Começa com a palavra Santo? {}'.format(cid[:5].capitalize() == 'Santo'))
