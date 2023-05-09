# De dos listas obtener datos
listado1 = [1,3,4,5,6,7,'BB','Poty']
listado2 = [4,5,1,2,3,4,'BB','Poty']

listado_respuesta1 = list(set(listado1)|set(listado2)) #Unión de los elementos
listado_respuesta2 = list(set(listado1)-set(listado2)) #Elementos de la lista 1 que no están en 2
listado_respuesta3 = list(set(listado2)-set(listado1)) #Elementos de la lista 2 que no están en 1
listado_respuesta4 = list(set(listado1) & set(listado2)) #Intercepción de las listas
print(listado_respuesta1)
print(listado_respuesta2)
print(listado_respuesta3)
print(listado_respuesta4)