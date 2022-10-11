# Declaração de variáveis
pessoas = list()
pessoa = dict()
soma = 0
cont1 = 0
cont2 = 0

while True:
    # Coleta de dados
    pessoa['nome'] = str(input('Nome: '))

    sexo = str(input('Sexo (F/M): ')).upper()[0]
    while sexo not in 'FM':
        print('Caracter INVÁLIDO!')
        sexo = str(input('Sexo (F/M): ')).upper()[0]


    idade = float(input('Idade: '))

    soma += idade

    # Guardo os dados em um dicionário, depois copio este para uma lista e limpo o dicionário para receber outros dados
    pessoa['idade'] = idade
    pessoa['sexo'] = sexo
    pessoas.append(pessoa.copy())
    pessoa.clear()

    # Interrompendo a repetição
    esc = str(input('Quer continuar?(S/N) ')).upper()[0]
    while esc not in 'SN':
        print('Caracter INVÁLIDO!')
        esc = str(input('Quer continuar?(S/N) ')).upper()[0]
    if esc in 'N':
        break

# Criação de uma variável 'media' para apresentar a média das idades
media = soma/len(pessoas)

# Saída dos dados solicitados
print('-=-'*15)
print(f'A) Foram cadastradas {len(pessoas)} pessoas.')

print(f'B) A média das idades é {media:.1f}')

print('C) Mulheres registradas: ', end='')
for pes in pessoas:
    if pes['sexo'] == 'F':
        print(pes['nome'], end=', ')
        cont1 += 1
if cont1 == 0:
    print('nenhuma')

print()
print('D) Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'     {k} → {v}', end=' ')
        print()
        cont2 += 1
if cont2 == 0:
    print('nenhuma')