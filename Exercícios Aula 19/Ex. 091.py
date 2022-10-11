# Módulos
from operator import itemgetter
from random import randint
from time import sleep

# Declaração de variáveis
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}

ranking = dict()

# Apresentação dos jogadores e os valores sorteados
print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# Processamento
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)

# Ranking na dos vencedores
print('-=-'*15)
print('  == RANKING DOS JOGADORES ==  ')
for i, j in enumerate(ranking):
    print(f'{i + 1}º lugar: {j[0]} com {j[1]} pontos')
    sleep(1)