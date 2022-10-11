soma = 0
maior = 0
contagem = 0

for pessoa in range(1, 5):
    print('---- {}ª PESSOA -----'.format(pessoa))
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    soma += idade
    if pessoa == 1:
        maior = idade

    if idade < 20 and sexo == 'F':
        contagem += 1

    else:
        if idade > maior and sexo == 'M':
            maisv = nome
            age = idade

print('A média de idade entre essas pessoas é {}.'.format(soma/4))
print('O homem mais velho se chama {} e possui {} anos.'.format(maisv, age))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contagem))
