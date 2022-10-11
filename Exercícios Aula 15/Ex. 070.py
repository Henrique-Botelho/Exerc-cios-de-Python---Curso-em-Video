menor = 0
soma = 0
cont = 0
cont2 =0
nomenor = 0

print('='*20)
print(' LOJA SUPER BARATO')
print('='*20)

while True:
    nome = input('Nome do produto:')
    pre = float(input('Preço: R$'))
    cont += 1
    soma += pre

    if pre > 1000:
        cont2 += 1

    if cont == 1:
        menor = pre
        nomenor = nome

    else:
        if pre < menor:
            menor = pre
            nomenor = nome

    pros = str(input('Quer continuar?[S/N]')).strip().upper()
    while pros not in 'SN':
        pros = str(input('Quer continuar?[S/N]')).strip().upper()
    
    if pros == 'N':
        break

print(f'O total da compra foi de R${soma:.2f}')
print(f'{cont2} produtos custam mais do que R$1000.00')
print(f'O produto mais barato é {nomenor} e custa R${menor:.2f}')
