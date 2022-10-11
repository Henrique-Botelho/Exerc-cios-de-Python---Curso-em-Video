# Declaração de variáveis
jogador = dict()
partida = list()
soma = 0

# Entrada de dados do jogador
jogador['nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(1, (partidas + 1 )):
    gol = int(input(f'Quantos gols ele fez na {c}ª partida?'))
    partida.append(gol)
    soma += gol

jogador['gols'] = partida

jogador['total'] = soma

# Saída de dados

# Primeira maneira
print('-=-'*15)
print(jogador)

# Segunda maneira
print('-=-'*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

# Terceira maneira
print('-=-'*15)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas: ')

for pos, g in enumerate(partida):
    print(f'    Na {pos + 1}ª ele fez {g} gols;')

print(f'Foi um total de {jogador["total"]} gols.')