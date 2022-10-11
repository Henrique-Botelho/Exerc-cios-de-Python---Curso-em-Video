n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
m = (n1 + n2)/2

if m < 5:
    print('Você foi \033[31mREPROVADO\033[m! Sua média foi de {:.2f}'.format(m))

elif m >= 5 and m <= 6.9:
    print('Você está de \033[33mRECUPERAÇÃO\033[m! Sua média foi de {:.2f}'.format(m))

elif m >= 7:
    print('Você está \033[32mAPROVADO\033[m! Sua média foi de {:.2f}'.format(m))
