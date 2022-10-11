frase = str(input('Digite uma frase:')).strip().lower()

print('Quantidade de letras A:', frase.count('a'))

print('A primeira letra A aparece na posição', frase.find('a') + 1)

print('A última letra A aparece na poisção', frase.rfind('a') + 1)
