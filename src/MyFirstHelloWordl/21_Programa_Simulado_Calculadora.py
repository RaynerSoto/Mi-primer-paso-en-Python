'''
Contruir un programa que simule el funcionamiento de una calculadora, indicando la operación matemática
con una letra precedente
'''
print('Indique la operación Matemática especifica y luego ingrese los operando')
print('S/s para la suma')
print('R/r para la resta')
print('P/p o M/m para la multiplicación')
print('D/d para la división')
operacion = input().upper()
operando1 = input('Indique el primer operando\n')
operando2 = input('Indique el segundo operando\n')
if len(operacion) == 1:
    if operando1.isdigit():
        if operando2.isdigit():
            if operacion == 'S':
                print(float(operando1)+float(operando2))
            elif operacion == 'R':
                print(float(operando1)-float(operando2))
            elif operacion == 'M' or operacion == 'P':
                print(float(operando1)*float(operando2))
            elif operacion == 'D':
                print(float(operando1)/float(operando2))
            else:
                print('Se equivoco de operación')
        else:
            print('El segundo operando no es número')
    else:
        print('El primer operando no es número')
else:
    print('El operador contiene un solo caracter')

