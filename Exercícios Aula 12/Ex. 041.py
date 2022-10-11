from datetime import date

nasc = int(input('Digite o seu ano de nascimento:'))

ano = int(date.today().year) - nasc

if ano <= 9:
    print('Esse atleta é MIRIM.')

elif ano <= 14 and ano > 9:
    print('Esse atleta é INFANTIL.')

elif ano > 14 and ano <= 19:
    print('Esse atleta é JUNIOR.')

elif ano > 19 and ano <= 25:
    print('Esse atleta é SENIOR.')

elif ano > 25:
    print('Esse atleta é MASTER.')
