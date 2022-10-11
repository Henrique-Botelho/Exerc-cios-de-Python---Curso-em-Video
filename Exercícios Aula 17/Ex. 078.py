maior = 0
menor = 0
cont = 0

numeros =[]


for p in range(0, 5):
    num = int(input(f'Digite um número para a posição {p}:'))
    numeros.append(num)

print('-='*20)

print(f'Você digitou os valores {numeros}')

for n in numeros:
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print(f'O menor número foi {menor} e está na[s] posição[ões] ', end=' ')
for l, u in enumerate(numeros):
    if u == menor:
        print(l, end=' ')


print(f'\nO maior número foi {maior} e está na[s] posição[ões] ', end=' ')
for l, u in enumerate(numeros):
    if u == maior:
        print(l, end=' ')