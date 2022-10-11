p = float(input('Digite o valor do produto em questão: R$'))
d = p*0.95
print('-'*60)

print('O preço do produto é R${:.2f} e o seu novo valor com um desconto de 5% é R${:.2f}.'.format(p, d))
