#Conococer si un número es par o impar
numero = input('Ingrese el valor numèrico\n')
if(numero.isdigit()):
    if(int(numero)%2 == 0):
        print('Nùmero Par')
    else:
        print('Impar')
else:
    print('Esto no es un nùmero')