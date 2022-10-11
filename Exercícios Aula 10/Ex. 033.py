n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
n3 = float(input('Digite mais um número:'))

if n1<n2 and n1<n3:

    print('O menor número é {}'.format(n1))

    if n2<n3:
        print('O maior número é {}'.format(n3))
    else:
        print('O maior número é {}'.format(n2))

if n2<n1 and n2<n3:

    print('O menor número é {}'.format(n2))

    if n1<n3:
        print('O maior número é {}'.format(n3))
    else:
        print('O maior número é {}'.format(n1))

if n3<n1 and n3<n2:

    print('O menor número é {}'.format(n3))

    if n1<n2:
        print('O maior número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n1))
