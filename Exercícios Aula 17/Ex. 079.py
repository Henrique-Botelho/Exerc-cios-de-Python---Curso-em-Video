numeros = []


while True:
    num = int(input('Digite um número: '))
    while num in numeros:
        num = int(input('Esse número já está na lista. Digite outro número: '))
    
    numeros.append(num)
    print('Número adicionado com sucesso!')

    perg = input('Você que continuar?[s/n] ')
    print('-='*30)
    while perg not in 'SsNn':
        perg = input('Você que continuar?[s/n] ')
        print('-='*30)
        
    if perg in 'nN':
        break

numeros.sort()
print('-=-'*20)
print(f'Você digitou os valores {numeros}')
