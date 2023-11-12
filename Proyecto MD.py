# Integrantes: Josué Say - 22801 | Mathew Córdero - 22982
# Funcionalidad: criptar y descencriptar mensajes utilizando el método RSA y Vigénere

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto a usar
modulo = len(diccionario) # modulo segun el alfabeto

# Función para descifrar mensajes usando el sistema Vigénere
def dameMensajeVigenere(_clave, _llave, _esCifrado):
    clave = _clave # clave del mensaje a descifrar
    llave = _llave # llave del mensaje a descifrar
    
    separacion_llave = list(llave) # separacion por caracteres de llave 
    codigo_llave = [diccionario.find(caracter) for caracter in separacion_llave] # codigo de los caracteres de separacion_llave

    bloques_mensaje = dameBloques(clave, llave) # mensaje a descifrar separado por bloques
    vector_codigo = [] # lista con el codigo de la clave
    
    # obtener el vector codigo de los bloques
    for i in bloques_mensaje:
        separacion = list(i)
        for j in separacion:
            vector_codigo.append(diccionario.find(j))
            
    vector_cifrado = dameCodigoBloques(codigo_llave, vector_codigo, _esCifrado) # lista con el codigo resultante de la operacion
    mensaje_respuesta = [diccionario[i] for i in vector_cifrado] # mensaje segun el vector_cifrado
    
    return mensaje_respuesta

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

# Función para obtener bloques de la clave segun la llave
def dameBloques(_clave, _llave):
    _bloques_mensaje = [] # lista de bloques separada por bloques  
    bloques_completos = esBloquesCompletos(_clave, _llave) # determinar si la lista hay que agregar letras dummys o nos

    # realizar separación normal
    if bloques_completos:
        for i in range(0, len(_clave), len(_llave)):
            bloque = _clave[i:i+len(_llave)]
            _bloques_mensaje.append(bloque)
        
        print("Los bloques son:", _bloques_mensaje)
        
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
        print("Los bloques son:", _bloques_mensaje)

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

# Función para pedir la información
def pedirInfo():
    while True:
        esCifrado = input("Ingresa la opción que deseas: \n1- Cifrado\n2- Descifrado\n")
        
        try:
            esCifrado = int(esCifrado)
        except ValueError:
            print("Error: Debes ingresar un número entero (1 o 2).")
            continue

        if esCifrado in [1, 2]:
            break
        else:
            print("Error: Debes ingresar 1 o 2.")

    clave = input("Ingresa el mensaje: ")
    llave = input("Ingresa la llave: ")

    if esCifrado == 1:
        mensaje = dameMensajeVigenere(clave, llave, True)
    else:
        mensaje = dameMensajeVigenere(clave, llave, False)

    cadena = ''.join(mensaje)
    print("El mensaje procesado es:", cadena)

# Llama a la función
pedirInfo()
