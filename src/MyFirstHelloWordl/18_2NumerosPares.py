#Hacer un programa que pida 2 números y se de cuenta cual de ellos es par, o si ambos lo son

numero1 = input('Introduzca el primer número:\n')
numero2 = input('Introduzca el segundo número\n')
if numero1.isdigit() and numero2.isdigit():
    if int(numero1) % 2 == 0 and int(numero2) % 2 ==0:
        print('Ambos números son pares')
    elif int(numero1) % 2 == 0:
        print(f'El valor {numero1} es par')
    elif int(numero2) % 2 == 0:
        print(f'El valor {numero2} es par')
    else:
        print('Ambos números son impares')
else:
    print('Alguna de las numeros contiene parámetros erroneos')

