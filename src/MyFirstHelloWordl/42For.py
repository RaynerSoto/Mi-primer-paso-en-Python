promedio =0
contador =0
notas = [5,5,2,4,4,5]
for i in notas:
    promedio += i
    contador +=1
print(f'BB tiene un promedio de {promedio/contador}')
#La funcion range asigna valores menores al limite superior
for i in range(0,len(notas)):
    print(i)

diccionario = {"azul":"blue",
               "rojo":"red",
               "verde":"green",
               "carmelita":"brown"
               }
for i in diccionario:
    print(i)
for i in diccionario:
    print(diccionario[i])
for clave,valor in diccionario.items():
    print(f'Clave {clave} -> Valor {valor}')

valor = 'Rayner'
for i in valor:
    print(i)
for i in valor: #Imprimir sin dejar espacio ni saltos de línea
    print(i,end='.')