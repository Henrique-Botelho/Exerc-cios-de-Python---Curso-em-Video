imp = list()
par = list()
todos = list()

todos.append(par)
todos.append(imp)

for n in range(1, 8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        par.append(num)

    if num % 2 == 1:
        imp.append(num)
    
par.sort()
imp.sort()

print('-='*30)
print(f'Os valores pares digitados foram {todos[0]}')
print(f'Os valores impares digitados foram {todos[1]}')