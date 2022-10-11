from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram:')
print(num)

org = sorted(num)

print(f'O maior valor sorteado foi {org[4]}')
print(f'O menor valor sorteado foi {org[0]}')
print('-='*30)

# Outra maneira de fazer

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os números sorteados foram:')
for c in numeros:
    print(c, end=' ')

print(f'\nO maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')
