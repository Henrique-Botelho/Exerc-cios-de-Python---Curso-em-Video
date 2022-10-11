print('==== LOJAS BOTELHO ====')
p = float(input('Digite o valor do produto a a ser pago: R$'))
print('-=-'*20)

print('[ 1 ] Para pagamento a vista no dinheiro/cheque.')
print('[ 2 ] Para pagamento a vista no cartão.')
print('[ 3 ] Para pagamento em até \033[33m2x\033[m no cartão.')
print('[ 4 ] Para pagamento em \033[31m3x ou mais\033[m no cartão.')
print('-=-'*20)

n = int(input('Digite a opção de pagamento desejada:'))
print('-=-'*20)

if n == 1:
    print('O valor a ser pago é de R$\033[32m{:.2f}\033[m'.format(0.9*p))

elif n == 2:
    print('O valor a ser pago é de R$\033[32m{:.2f}\033[m'.format(0.95*p))

elif n == 3:
    print('O valor a ser pago é de R$\033[32m{:.2f}\033[m'.format(p))

elif n == 4:
    o = int(input('Em quantas parcelas?'))
    print('O valor total a ser pago é de R$\033[32m{:.2f}\033[m, sendo que cada parcela custará R$\033[33m{:.2f}\033[m'.format(1.2*p, (1.2*p)/o))
