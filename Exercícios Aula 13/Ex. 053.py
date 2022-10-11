print('==== IDENTIFICADOR DE PALÍNDROMOS ====')
#Recebendo a frase, corrigindo os espaços e padronizando o que entra
frase = str(input('Escreva uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''


#O for também funciona para strings
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]


print('A frase lida de trás para frente fica {}'.format(inverso))
if inverso == junto:
    print('Essa frase É UM PALÍNDROMO.')
else:
    print('Essa frase NÃO É UM PALÍNDROMO.')

#Outra maneira de fazer sem usar o for
print('==== IDENTIFICADOR DE PALÍNDROMOS ====')
#Recebendo a frase, corrigindo os espaços e padronizando o que entra
frase = str(input('Escreva uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('A frase lida de trás para frente fica {}'.format(inverso))
if inverso == junto:
    print('Essa frase É UM PALÍNDROMO.')
else:
    print('Essa frase NÃO É UM PALÍNDROMO.')
