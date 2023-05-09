#Generador de nombres para tarjetas del gremio para bots de Monster Hunter Rise
import random

primer_nombre = {
    1:'El señor',
    2:'El rey',
    3:'El enviado',
    4:'El campeón',
    5:'El único',
    6:'La pieza',
    7:'El más grande',
    8:'Ninja',
    9:'Samurai',
    10:'Muerto'
}
segunda_parte ={
    1:'De',
    2:'Del'
}
tercer_nombre={
    1:'La casa',
    2:'El bosque',
    3:'La vida',
    4:'Los más grandes',
    5:'El tanque'
}
valor = random.randint(1,10)
cadena = primer_nombre[valor]
cadena += ' '
valor = random.randint(1,2)
cadena += segunda_parte[valor]
cadena += ' '
valor = random.randint(1,5)
cadena += tercer_nombre[valor]
print(cadena)