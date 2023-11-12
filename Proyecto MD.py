# Integrantes: Josué Say - 22801 | Mathew Córdero - 22982
# Funcionalidad: criptar y descencriptar mensajes utilizando el método RSA y Vigénere

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto a usar
modulo = len(diccionario) # modulo segun el alfabeto


# Función para descifrar mensajes usando el sistema Vigénere
def dameMensajeVigenere(_clave, _llave):
    clave = _clave # clave del mensaje a descifrar
    llave = _llave # llave del mensaje a descifrar
    
    separacion_llave = list(llave) # separacion por caracteres de llave 
    codigo_llave = [diccionario.find(caracter) for caracter in separacion_llave] # codigo de los caracteres de separacion_llave

    bloques_mensaje = dameBloques(clave, llave) # mensaje a descifrar separado por bloques
    vector_codigo = []
    vector_cifrado = []

    # obtener el vector codigo de los bloques
    for i in bloques_mensaje:
        separacion = list(i)
        for j in separacion:
            vector_codigo.append(diccionario.find(j))
            
           


# Función para operar el codigo de la llave con el codigo de los bloques
def dameCodigoBloques(_codigo_llave, _vector_codigo):
   
    _vector_cifrado = []
   # Calcular la longitud de vector_sumando para usarla en el módulo
    longitud_sumando = len(_codigo_llave)

    # Iterar sobre vector_codigo y sumar modularmente con vector_sumando
    for i, valor_codigo in enumerate(_vector_codigo):
        valor_sumando = _codigo_llave[i % longitud_sumando]
        resultado_modular = (valor_codigo + valor_sumando) % modulo
        _vector_cifrado.append(resultado_modular) 
    
    return _vector_cifrado

# Función para obtener bloques de la clave segun la llave
def dameBloques(_clave, _llave):
    
    _bloques_mensaje = []
    
    bloques_completos = esBloquesCompletos(_clave, _llave) # determinar si la lista hay que agregar letras dummys o nos

    # realizar separación normal
    if bloques_completos:
        for i in range(0, len(_clave), len(_llave)):
            bloque = _clave[i:i+len(_llave)]
            _bloques_mensaje.append(bloque)
        
        print(_bloques_mensaje)
        
    # agregar letras dummys al final
    else:
        for i in range(0, len(_clave), len(_llave)):
            bloque = _clave[i:i+len(_llave)]
            _bloques_mensaje.append(bloque)
        
        ultima_cadena = _bloques_mensaje[-1]
        letras_extras = len(_llave) - len(ultima_cadena)
        
        while letras_extras > 0:
            _bloques_mensaje[-1] = _bloques_mensaje[-1] + "X"
            letras_extras -= 1  
        print(_bloques_mensaje)

    return _bloques_mensaje

# Función para saber si hay que agregar letras dummys a la clave
def esBloquesCompletos(_clave, _llave):
    try:
        tamClave = len(_clave)
        tamLlave = len(_llave)
        division = tamClave / tamLlave

        if division.is_integer():
            return True
        else:
            return False

    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
        return False




    
    













