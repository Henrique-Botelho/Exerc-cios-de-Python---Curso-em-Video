# Declaração de variáveis
pessoa = dict()

# Entrada de dados
pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))

if pessoa['media'] >= 7:
    pessoa['situação'] = 'Aprovado'

elif 5 <= pessoa['media'] < 7:
    pessoa['situação'] = 'Recuperação'

else:
    pessoa['situação'] = 'Reprovado'

# Saída de dados
print('='*30)

for k, v in pessoa.items():
    print(f' → {k.capitalize()} é igual a {v}')