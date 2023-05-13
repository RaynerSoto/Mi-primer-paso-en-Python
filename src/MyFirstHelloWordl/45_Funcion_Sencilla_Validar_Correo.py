def validacion_correo(valor):
    correcto = 0
    contador = 0
    if len(valor) != 0:
        cadena = list(valor)
        for i in cadena:
            if i == '@' and correcto == 0:
                correcto = 1
            elif i == '.' and correcto == 1:
                correcto = 2
            elif i == '.' and correcto == 0:
                correcto = -1
        if correcto == 2:
            return True
        else:
            return False