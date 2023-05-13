promedio = 0
iterator = 0
parador = True
while parador == True:
    i = input('Ingresa la nota: ')
    if i.isdigit() and float(i) in range(2,6):
        promedio += float(i)
        iterator += 1
    else:
        print('Nota no promediable')
        parador = False
print(f'El promedio sería {(promedio/iterator)}.')