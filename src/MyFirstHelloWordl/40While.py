#Ciclos while
#caculo de promedio de valores

promedio = 0
contador = 0 #Contador o iterador
valor = '0'
print('Si se ingresa un caracter no númerico, se procederá a calcular. Debe ingresar al menos uno')
while (valor.isdigit() or ( len(valor)>1 and valor[0] == '-' and valor[1:].isdigit())):
    valor = input('Promedio de valores\n')
    if(valor.isdigit()):
        promedio += float(valor)
        contador+=1
    elif valor[0] == '-' and valor[1:].isdigit():
        promedio += float(valor)
        contador+=1
if contador == 0:
    print(f'El promedio es {promedio}')
else:
    print(f'El promedio es {promedio / contador}')