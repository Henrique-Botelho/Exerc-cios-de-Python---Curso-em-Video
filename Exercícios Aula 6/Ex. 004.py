c = input('Digite qualquer coisa:')
print('O tipo primitivo desse elemento é', '\033[7m', type(c), '\033[m')
#Usando a função "type", se não estiver especificado o tipo primitivo da variável no input, ela será sempre string
cores = {'sem cor':'\033[m', 'branco':'\033[30m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m', 'magenta':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m'}


d = input('Digite qualquer coisa:')
print('{}É um número?{}'.format(cores['branco'], cores['sem cor']), d.isnumeric())
print('{}É alfabético?{}'.format(cores['vermelho'], cores['sem cor']), d.isalpha())
print('{}É alfanumérico?{}'.format(cores['verde'], cores['sem cor']), d.isalnum())
print('{}Tem espaços?{}'.format(cores['amarelo'], cores['sem cor']), d.isspace())
print('{}Está em caixa alta?{}'.format(cores['azul'], cores['sem cor']), d.isupper())
print('{}Está em minúsculas?{}'.format(cores['magenta'], cores['sem cor']), d.islower())
print('{}Está capitalizada?{}'.format(cores['ciano'], cores['sem cor']), d.istitle())
#Usando dessa forma, analisamos os métodos de uma string
