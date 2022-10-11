# Módulo usado
from time import sleep

# Declaração de variáveis
pessoa = []
todos = []
medias = []

while True:
    # Coleta de dados
    pessoa.append(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    # Adicionando dados às listas
    medias.append((nota1+nota2)/2)
    pessoa.append(nota1)
    pessoa.append(nota2)
    todos.append(pessoa[:])
    pessoa.clear()

    # Break da estrutura de repetição
    esc = str(input('Quer continuar?[s/n] '))
    if esc in 'Nn':
        break

# Cabeçalho da tabela
print('='*25)   
print(f'{"No.": <5}{"Nome": <15}{"Média": >3}')
print('-'*25)

# Cada linha da tabela
for pos, ele in enumerate(todos):
    print(f'{pos: <5}{ele[0]: <15}{medias[pos]: >4}')

# Estrutura de repetição de requerimento das notas de cada aluno
while True:
    print('-'*40)
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    while aluno < 0 or 999 > aluno >= len(todos):
        aluno = int(input('INVALIDO!\nMostrar notas de qual aluno? [999 interrompe] '))
    if aluno == 999:
        break

    print(f'Notas de {todos[aluno][0]}: {todos[aluno][1]} e {todos[aluno][2]}')


# Finalizaçao
print('FINALIZANDO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print(f'{"<<< VOLTE SEMPRE >>>": ^40}')