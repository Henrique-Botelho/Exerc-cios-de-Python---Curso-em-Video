# Declaração de variáveis
lista = []
listap = []
listai = []

while True:
    # Entrada de dados
    num = int(input('Digite um número: '))

    # Dados alocados de acordo com o seu tipo
    lista.append(num)
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)
    
    # Entrada de dados relacionada à estrutura de repetição
    esc = input('Você quer continuar? [s/n]').lower()
    while esc not in 'sn':
        esc = input('Você quer continuar? [s/n]').lower()
    if esc == 'n':
        break

# Saída de dados
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {listap}')
print(f'A lista de números ímpares é {listai}')