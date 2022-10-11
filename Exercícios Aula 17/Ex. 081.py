# Declaração de variáveis
from audioop import reverse


lista = []
cont = 0

# Estrutura de repetição para a entrada de dados
while True:
    num = int(input('Digite um valor: '))
    cont += 1
    lista.append(num)
    esc = input('Você quer continuar? [S/N]').upper()
    while esc not in 'SN':
        esc = input('Você quer continuar? [S/N]').upper()        
    if esc == 'N':
        break

# Saída dos dados requisitados
    # A quantidade de números digitados
print(f'Você digitou {cont} número[s].')

    # Os números em ordem decrescente
lista.sort(reverse=True)
print(f'Os números digitados em ordem decrescente são {lista}')

    # Se o número 5 faz parte ou não da lista
if 5 in lista:
    print('O valor 5 faz parte da lista!')
elif 5 not in lista:
    print('O valor 5 não faz parte da lista!')