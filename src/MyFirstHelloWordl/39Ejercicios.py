personajes = []
LordOfRings = {
    'Personaje 1':{
        'Nombre': 'Aragon',
        'Clase' : 'Guerrero',
        'Raza' : 'Dúnadan del Norte'
    },
    'Personaje 2':{
        'Nombre': 'Gandalf',
        'Clase': 'Mago',
        'Raza': 'Istar'
    },
    'Personaje 3':{
        'Nombre': 'Legolas',
        'Clase': 'Arquero',
        'Raza': 'Elfo Sindar'
    }
}
Diccionario = LordOfRings.get('Personaje 1')
diccionario_list = [Diccionario.get('Nombre'),Diccionario.get('Clase'),Diccionario.get('Raza')]
personajes.append(diccionario_list)
Diccionario = LordOfRings.get('Personaje 2')
diccionario_list = [Diccionario.get('Nombre'),Diccionario.get('Clase'),Diccionario.get('Raza')]
personajes.append(diccionario_list)
Diccionario = LordOfRings.get('Personaje 3')
diccionario_list = [Diccionario.get('Nombre'),Diccionario.get('Clase'),Diccionario.get('Raza')]
personajes.append(diccionario_list)
print(personajes)

