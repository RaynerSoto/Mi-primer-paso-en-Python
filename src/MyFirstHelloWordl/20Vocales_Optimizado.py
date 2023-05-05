silaba = input('Ingrese la cadena\n').upper()
if(len(silaba) == 1) and silaba.isalpha():
    if silaba == 'A' or silaba == 'E' or silaba == 'I' or silaba == 'O' or silaba == 'U':
        print('Es una vocal')
    else:
        print('Es una consonante')
else:
    print('Debe tener un solo valor en la cadena o no es una cadena valida')