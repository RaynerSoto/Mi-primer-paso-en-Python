silaba = input('Ingrese la cadena\n')
if(len(silaba) == 1) and silaba.isalpha():
    if silaba.upper() == 'A' or silaba.upper() == 'E' or silaba.upper() == 'I' or silaba.upper() == 'O' or silaba.upper() == 'U':
        print('Es una vocal')
    else:
        print('Es una consonante')
else:
    print('Debe tener un solo valor en la cadena o no es una cadena valida')