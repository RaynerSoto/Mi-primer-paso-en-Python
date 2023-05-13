#Conjuntos
#Los conjuntos son datos desordenados únicos
#Los conjuntos funcionan igual que los conjuntos matematicos
conjuntos = set() #Indicación para crear un conjunto vacío
conjuntos = {1,2,3,4,5,'Nombre',1} #NO PUEDE HABER OTRO TIPO DE COLECCIONES DENTRO DE LOS CONJUNTOS
print(conjuntos) #Para los conjuntos existen valores único, no existe valores duplicados
conjuntos.add(34) #Añadir elemento
conjuntos.add('Adios')
conjuntos.add(True)
conjuntos.add(22)
conjuntos.add(23.3)
conjuntos.add(9.0)
conjuntos.add(9.4)
conjuntos.add(9.3)
conjuntos.add(0.1)
print(conjuntos) #Los conjuntos añaden elementos en posiciones aleatorias
conjuntos.discard(True)
print(1 in conjuntos)
print(conjuntos)
conjuntos.clear() #Eliminar toda la lista}
print(conjuntos)

