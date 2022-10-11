def maior(* num):
    m = max(num)
    t = len(num)

    print('-=-'*15)
    print('Analisando os valores passados . . .')
    for c in num:
        print(c, end=' ')
    print(f'Foram informados {t} valores ao todo.')
    print(f'O maior número foi {m}')


maior(5, 4, 9, 0)
maior(4, 3)
maior(0)
maior(2, 1, 8, 6)