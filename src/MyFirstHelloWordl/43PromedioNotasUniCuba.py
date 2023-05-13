promedio = 0
for iterador in range(0,11):
    i = input('Ingresa la nota: ')
    if i.isdigit() and float(i) in range(2,6):
        promedio += float(i)
    else:
        print('Nota no promediable')
print(f'El promedio sería {promedio/iterador}')