# Integrantes: Josué Say - 22801 | Mathew Córdero - 22982
# Funcionalidad: operaciones utilizadas por el método Vigénere y RSA

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto a usar
modulo = len(diccionario) # modulo segun el alfabeto

# Función para obtener bloques de la clave segun la llave
def dameBloques(_clave, _llave):
    _bloques_mensaje = [] # lista de bloques separada por bloques  
    bloques_completos = esBloquesCompletos(_clave, _llave) # determinar si la lista hay que agregar letras dummys o nos

    # realizar separación normal
    if bloques_completos:
        for i in range(0, len(_clave), _llave):
            bloque = _clave[i:i+_llave]
            _bloques_mensaje.append(bloque)
        
        #print("Los bloques son:", _bloques_mensaje)
        
    # agregar letras dummys al final
    else:
        for i in range(0, len(_clave), _llave):
            bloque = _clave[i:i+_llave]
            _bloques_mensaje.append(bloque)
        
        ultima_cadena = _bloques_mensaje[-1]
        letras_extras = _llave - len(ultima_cadena)
        
        while letras_extras > 0:
            _bloques_mensaje[-1] = _bloques_mensaje[-1] + "X"
            letras_extras -= 1  
        #print("Los bloques son:", _bloques_mensaje)

    return _bloques_mensaje

# Función para saber si hay que agregar letras dummys a la clave
def esBloquesCompletos(_clave, _llave):
    try:
        tamClave = len(_clave)
        division = tamClave / _llave

        if division.is_integer():
            return True
        else:
            return False

    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
        return False
    
# Función para operar el codigo de la llave con el codigo de los bloques
def dameCodigoBloques(_codigo_llave, _vector_codigo, _esCifrado):
    vector_suma = [] # vector resultante
    longitud_llave = len(_codigo_llave) # calcular la longitud de _codigo_llave para usarla en el módulo

    # realizar la operación para cifrado
    if _esCifrado:
        if longitud_llave > 0:
            # Iterar sobre vector_codigo y sumar modularmente con _codigo_llave
            for i, valor_codigo in enumerate(_vector_codigo):
                valor_sumando = _codigo_llave[i % longitud_llave]
                resultado_modular = (valor_codigo + valor_sumando) % modulo
                vector_suma.append(resultado_modular)
        else:
            print("Error: La longitud de _codigo_llave debe ser mayor que cero.")
    
    # realizar la operación para descifrado
    else:
        if longitud_llave > 0:
            # Iterar sobre vector_codigo y sumar modularmente con _codigo_llave
            for i, valor_codigo in enumerate(_vector_codigo):
                valor_sumando = _codigo_llave[i % longitud_llave]
                resultado_modular = (valor_codigo - valor_sumando) % modulo
                vector_suma.append(resultado_modular)
        else:
            print("Error: La longitud de _codigo_llave debe ser mayor que cero.")

    return vector_suma

# obtener el vector codigo de los bloques
def dameVectorCodigo(_bloques_mensaje):
    _vector_codigo = [] # almacenamiento del vector codigo
    
    # recorrer cada bloque
    for i in _bloques_mensaje:
        separacion = list(i)
        # recorrer cada caracter del bloque
        for j in separacion:
            _vector_codigo.append(diccionario.find(j))
            
    return _vector_codigo

