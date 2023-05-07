#Aprendiendo listas
#Una lista puede almacenar distintos tipos de datos
#Las listas son tanto arreglos unidimensionales como bidimensionales, según el caso
listado = [] #Creación de lista vacía
listado = [1,2,3,4] #Creacion de un listado con valores
listado = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
print(listado) #Imprimir toda la lista
print(listado[0]) #Imprimir un elemento de la lista de adelante hacia detras
print(listado[-1]) #Imprimir un elemento de la lista de detrás hacia delante
print(listado[0:5]) #Imprimir sublistas
print(listado[1:]) #Sublista que empieza en el elemento 1 hasta el final
print(listado[:4]) #Sublista que termina en el elemento 4-1
print(len(listado)) #Cantidad de elementos de la lista