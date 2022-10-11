
from time import sleep

for b in range(10, -1, -1):
    print(b)
    sleep(1)
print('BUM! TADA! POW! FELIZ ANO NOVO!')

#Outra forma
n = 11
for c in range(10, -1, -1):
    n += -1
    print(n)
    sleep(1)

print('BUM! TADA! POW! FELIZ ANO NOVO!')
