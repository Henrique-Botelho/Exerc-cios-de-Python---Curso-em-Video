nasc = int(input('Informe o ano de seu nascimento:'))
if 2022 - nasc < 18:
    print('Ainda faltam {} anos para você se alistar.'.format(2022 - nasc))
elif 2022 - nasc == 18:
    print('Você deve se alistar imediatamente!')
elif 2022 - nasc > 18:
    print('Você deveria ter se alistado há {} anos atrás!'.format(2022 - (nasc+18)))
