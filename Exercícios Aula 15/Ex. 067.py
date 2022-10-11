while True:
    num = int(input('Qual número você deseja saber a tabuada?'))
    if num <= 0:
        break
    print('='*20)
    for c in range(1,11):
        res = num*c
        print(num, 'X', c, f' = {res}')
    print('='*20)
print('Obrigado por usar esse programa!')