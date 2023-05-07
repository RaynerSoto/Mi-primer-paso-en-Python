listado = [[1,2,3,4],90,[4,8,9]]
print(listado)
print(listado[0][1]) #Imprimir elemento de una lista anidada en otras palabras arreglo bidimensional
listado = ['Rayner','Poty']
print(listado[0][0],'\n') #Busqueda en una sublista un elemento específico

listado = [1,2,3]
listado2 = [4,5,6]
print(listado+listado2,'\n') #Concatenar 2 listas

listado.append(listado2)
print(listado)

listado.extend([6,7,8]) #Añadir a una lista elementos elemetos
print(listado,'\n') #Concatenar 2 listas

print(1 in listado,'\n') #Buscar un elemento en la lista

listado.insert(0,4) #Insertar un elemento en una posición exacta de la lista. 0 es la posicion y 4 el valor
print(listado,'\n')

print(listado.index(1)) #Buscando el índice de un elemento en la lista
print(listado.count(2),'\n') #Contando cuantos veces aparece un elemento en la lista

valor = listado.pop() #Obtiene el último elemento de la lista y lo elimina
print(valor)
print(listado,'\n')

valor = listado.pop(1) #Obtiene el elemento con índice 1 de la lista y lo elimina
print(valor)
print(listado,'\n')

listado.remove(3) #Remueve un elemento de la lista
print(listado,'\n')

print(listado.reverse()) #Voltear la lista al reverso

listado = [1,2,3]*2
print(listado,'\n') #Repetir una lista una x cantidad de veces

listado = [2,3,4,5,77,1,45,23,98,23]
listado.sort()
print(listado) #Ordenar ascendentemente
listado.sort(reverse=True)
print(listado,'\n') #Ordenar descendentemente

listado.clear() #Eliminar toda la lista
print(listado)