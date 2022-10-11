# Módulos
from datetime import date

# Declaração de variáveis
pessoa = dict()

# Entrada de dados da pessoa
pessoa['nome'] = str(input('Nome: '))

nasc = int(input('Ano de nascimento: '))

pessoa['idade'] = date.today().year - nasc

ctps = int(input('Carteira de Trabalho (0 se não possui): '))
if ctps != 0:
    pessoa['ctps'] = ctps
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 30) - nasc
    pessoa['salário'] = float(input('Salário: R$'))

print('-=-'*15)
for k, v in pessoa.items():
    print(f'- {k: <15} ---→ {v: >8}')