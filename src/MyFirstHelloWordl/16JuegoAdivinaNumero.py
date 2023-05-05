import random

numero_adivinado = random.randint(1,10)
print('Estoy pensando en un número del 1-10. Adivinalo')
valor = input()
if valor.isdigit() and 1<=int(valor)<=10:
    if(int(valor) == numero_adivinado):
        print('Adivinaste el número, bien hecho')
    else:
        print(f'El número que estaba pensando era:{numero_adivinado}')
else:
    print('No has ingresado un número o un número no valido')
