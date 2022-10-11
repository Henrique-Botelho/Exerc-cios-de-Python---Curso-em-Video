todos =list()
pessoa = list()
maior = menor = 0


while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(todos) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    
    todos.append(pessoa[:])
    pessoa.clear()

    resp = str(input('Quer continuar?[S/N]'))
    if resp in 'Nn':
        break

print('-='*30)
print(f'Ao todo foram {len(todos)} pessoa[s] cadastrada[s].')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in todos:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print(f'\nO menor peso foi {menor}kg. Peso de ', end='')
for m in todos:
    if m[1] == menor:
        print(f'{m[0]}', end=' ')