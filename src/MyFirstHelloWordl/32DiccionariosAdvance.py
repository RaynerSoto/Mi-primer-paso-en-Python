#Voy a crear un diccionario con nombre-apellido y una especie de categría
agenda = {
    "Rayner":{"Apellido":"Soto Martinez","edad":22,"categoría":"Estudiante de ingeniería"},
    "Lion":{"Apellido":"S. Kennedy","edad":31,"categoría":"+RacconCity Survivor"},
    "Lionel":{"Apellido":"Messi","edad":35,"categoría":"Campeón del Mundo"}
}

print(agenda["Lion"]["Apellido"])
print(agenda.get("LA",'Este valor no lo tengo asignado')) #Método para extraer valores de un diccionario y validar la existencia de errores
print('Rayner' in agenda) #Busqueda en los diccionarios
print(agenda.keys()) #Imprimir solamente las claves del diccionario
print(agenda.values()) #Imprimir los valores de las claves
print(agenda) #Imprimir todos los valores
print(len(agenda)) #Cuantos elementos hay en la agenda
print(agenda.clear()) #Eliminar todos los valores del diccionario