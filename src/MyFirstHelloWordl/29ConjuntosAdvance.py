#Conjuntos Advance
# A la hora de comparar no importa el orden de los elementos
a = {1,2,3,0.1}
b = {2,3,1,9,1,3,4,5,6}
print(a == b) #Comparar dos conjuntos

c = a | b #Uniòn de dos conjuntos
print(c)

c = a & b #Intercepcion de dos conjuntos
print(c)

c = a - b #Elementos que están en A, pero no en B
d = b - a #Elementos que están en B, pero no en A
print(b)
print(c)

c = a | b #Elementos que están en A y B, pero sin contar su intercepción
print(c)

print(c.issubset(b)) #B es un subconjunto de C
print(c.issuperset(a)) #C es el superconjunto de A
print(a.isdisjoint(b)) # A y B tienen algún elemento en común