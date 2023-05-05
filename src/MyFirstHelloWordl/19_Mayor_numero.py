#El mayor de los números positivos
numero = input('Ingrese el número\n')
numero1 = input('Ingrese el segundo número\n')
numero2 = input('Ingrese el tercer número\n')
if numero.isdigit() and numero1.isdigit() and numero2.isdigit() :
    if float(numero)<float(numero1):
        numero,numero1 = numero1,numero
    if float(numero)<float(numero2):
        numero,numero2 = numero2,numero
    print(f'El mayor número es:{numero}')
else:
    print('Esta es una cadena no valida')