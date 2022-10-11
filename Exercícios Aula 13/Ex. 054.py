from datetime import date
contagem1 = 0
contagem2 = 0

for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(pessoa)))

    if int(date.today().year) - ano >= 18:
        contagem1 += 1
    else:
        contagem2 += 1

print('Dessas pessoas, \033[32m{}\033[m são maiores de idade e \033[31m{}\033[m são menores de idade.'.format(contagem1, contagem2))
