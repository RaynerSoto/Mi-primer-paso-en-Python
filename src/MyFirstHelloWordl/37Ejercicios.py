#Eliminar los elementos repetidos de una lista

listado = [9,8,9,7,5]
listado.sort()
print(listado)
conjunto = set(listado)
print(conjunto)
listado = list(conjunto)
print(listado)