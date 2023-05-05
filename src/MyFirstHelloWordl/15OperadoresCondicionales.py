#Validacion de un numero para conocer en que rango se encuentra positivo-neutro-negativo

valor = input("Ingrese un valor numérico\n")
if valor.isdigit():
    if float(valor) > 0:
        print('El valor es positivo')
    elif float(valor) == 0:
        print('El valor es neutro')
    else:
        print('El valor es negativo')
else:
    print('Este valor contiene caracteres que no son números')
print('Fin del programa')
