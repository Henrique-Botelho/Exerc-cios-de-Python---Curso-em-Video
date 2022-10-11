n = int(input('Digite um número inteiro:'))
print('[ 1 ] Para transformá-lo em \033[32mBINÁRIO\033[m')
print('[ 2 ] Para transformá-lo em \033[35mOCTAL\033[m')
print('[ 3 ] Para transformá-lo em \033[36mHEXADECIMAL\033[m')
b = int(input('Digite o número correspondente à base que deseja:'))
if b == 1:
    print('O número {} convertido em \033[32mbinário\033[m é {}.'.format(n, bin(n)))
elif b == 2:
    print('O número {} convertido em \033[35moctal\033[m é {}.'.format(n, oct(n)))
elif b == 3:
    print('O número {} convertido em \033[36mhexadecimal\033[m é {}.'.format(n, hex(n)))
else:
    print('\033[31mOpção inválida!\033[m')
