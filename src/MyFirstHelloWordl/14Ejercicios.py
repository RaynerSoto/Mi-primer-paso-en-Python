#Devolución del 15% de la compra total
valor = float(input('Ingrese el valor de la compra total\n'))
print(f'El cliente deberá pagar: {(valor-((valor*15)/100)):.2f}') #Dos cifras después de la coma