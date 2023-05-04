#Convertir una cadena a un entero
print(int('10'))

#Convertir una cadena a un float
print(float('10.2'))

#Convertir de un valor numerico a una cadena
print(str(10))

#Convertir un valor entero a binario
print(bin(19))

#Convertir un valor entero a hexadecimal
print(hex(10))

#Convetir un binario a un entero
print(int('0b10011',2))

#Convertir de un hexadecimal a binario
print(int(0xa))

#Una cadena de caracteres compuesta por numeros
valor = '12'
print(valor.isdigit()) #Función que devuelve si una cadena son todos números

#Una cadena compuesta compuesta por caracteres alfabéticos
valor = 'AVASCVcsasdg'
print(valor.isalpha()) #Función que devuelve si una cadena son todos letras

#Valor absoluto de un número
valor = 12.123414213
print(abs(valor))

#Redondeo de los valores
valor = 7.9
print(round(valor)) #Funcion para redondear los valores

#Cantidad de caracteres de una cadena
valor = 'Rayner'
print(len(valor))