from datetime import date

print('O ano é bissexto ou não?')
print('-=-'*20)

ano = int(input('Digite o ano que deseja saber. Coloque 0 para saber do ano atual:'))

if ano == 0:
    ano = date.today().year

if ano %4 == 0 and ano %400 == 0:
    print('O ano de {} É BISSEXTO'.format(ano))

else:
    print('O ano de {} NÃO É bissexto'.format(ano))
