'''
Actualización del ejercico 18
Ahora he añadido una validación más exacta, si han probado los códigos que he desarrollado verán que
los números negativos tienen errores ya que el isdigit detecta el '-' como un caracter no valido

Este es el único ejercicio que voy a cambiar, ya que se entiende que en todos los demás es igual

Este cambio lo mantendre vigente en los demás ejercicios

Este ejercicio será modificado en un futuro
'''
numero = input('Ingrese el valor numèrico\n')
if len(numero) >= 1 and numero.isdigit():
    if (int(numero) % 2 == 0):
        print('Nùmero Par')
    else:
        print('Impar')
elif len(numero) > 1 and numero[0] == '-' and numero[1:].isdigit():
    if (int(numero) % 2 == 0):
        print('Nùmero Par')
    else:
        print('Impar')
else:
    print('Error caracter no válido')