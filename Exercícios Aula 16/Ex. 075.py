soma = 0

numeros = (int(input('Digite um número:')), int(input('Digite outro número:')), int(input('Digite mais um número:')), int(input('Digite o último número:')))

print(f'Você digitou os valores {numeros}')
print('-='*20)
print(f'O valor 9 apareceu {numeros.count(9)} vez[es].')
if 3 in numeros:    
    print(f'O primeiro valor 3 aparece na {numeros.index(3) + 1}ª posição.')
else:
    print('Nenhum valor 3 dentre os digitados.')
for n in numeros:
    if  n % 2 == 0:
        soma += 1
    
print(f'Ao todo são {soma} números pares.')