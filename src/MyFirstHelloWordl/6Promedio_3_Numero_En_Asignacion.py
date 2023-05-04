#Probando la precondición y poscondicion de Java y los operadores de asignación
valor = 0
contador = 0
valor +=5
contador += 1
valor +=3
contador += 1
valor +=5
contador += 1
# contador ++ #Esta línea da error, no hay precondicion o poscondicion
print(contador)
print(valor)
print(valor/contador)
