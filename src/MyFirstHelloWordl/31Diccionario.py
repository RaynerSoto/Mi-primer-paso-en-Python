#Diccionario
#Es una correpondecia clave-valor igual que el hash map
diccionario = {}
print(diccionario)

diccionario = {"azul":"blue",
               "rojo":"red",
               "verde":"green",
               "carmelita":"brown"
               }
print(diccionario)
print(diccionario["azul"]) #Imprimir un elemento de la clave "azul"
diccionario["amarillo"] = "yellow" #Añadir nuevos elementos al diccionario
print(diccionario)
diccionario["azul"] = "BLUE" #Modificar un elemento con la clave "azul"
print(diccionario)
del(diccionario["azul"]) #ELiminar un elemento con la clave "azul"
print(diccionario)
