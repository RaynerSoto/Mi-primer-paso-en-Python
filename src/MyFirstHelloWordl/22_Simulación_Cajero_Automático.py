#Cajero automático con un saldo inicial de 1000
saldo = 1000
print('Ingrese la operación deseada:')
print('1-Ingresar dinero a la cuenta')
print('2-Retirar dinero de la cuenta')
print('3-Mostrar dinero disponible')
print('Otro-Salir')
opcion = input()
if opcion.isdigit():
    if opcion == '1':
        valor = input('Ingrese la cantidad deseada para ingresar\n')
        if valor.isdigit():
            if float(valor) > 0:
                saldo += float(valor)
            else:
                print('No se puede ingresar un número negativo')
        else:
            print('Caracteres erróneos en el valor')
    elif opcion == '2':
        valor = input('Ingrese la cantidad deseada a retirar\n')
        if valor.isdigit():
            if float(valor) > 0:
                if saldo >= float(valor):
                    saldo -= float(valor)
                else:
                    print('No tiene esa cantidad de dinero')
            else:
                print('No se puede ingresar un número negativo')
        else:
            print('Caracteres erróneos en el valor')
    elif opcion == '3':
        print(f'El saldo disponible es: {saldo}')
    else:
        print('Adiós')
    if opcion != '3':
        print(f'El saldo disponible es: {saldo}')