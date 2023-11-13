# Integrantes: Josué Say - 22801 | Mathew Córdero - 22982
# Funcionalidad: criptar y descencriptar mensajes utilizando el método RSA

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto a usar
modulo = len(diccionario) # modulo segun el alfabeto

### Prueba 1
M = "STOP"
e1 = 13
n1 = 2537
caracteres1 = 2
digitos1 = caracteres1*2

### Prueba 2
C = "0981 0461"
p2 = 43
q2 = 59
e2 = 13
caracteres2 = 2
digitos2 = caracteres2*2

# Función para el crigfrado RSA
def cifradoRSA(M, e, n, cantidad_caracteres, cantidad_codigo):
    bloques = dameBloques(M, cantidad_caracteres) # bloques del mensaje M
    
    vector_codigo = dameVectorCodigo(bloques) # vector codigo segun el mensaje con bloques
    vector_codigo_nuevo = [dameFormatoNumero(vector_codigo[i]) + dameFormatoNumero(vector_codigo[i + 1]) for i in range(0, len(vector_codigo), cantidad_caracteres)] # vector codigo con el formato de cantidad de digitos reales
    
    codigo_encriptado = dameVectorOperado(vector_codigo_nuevo, e, n, cantidad_codigo) # obtener el vector de codigo encriptado (con calculos)
    mensaje_respuesta = '-'.join(codigo_encriptado) # obtener el mensaje como respuesta de la codificacion
    
    print("El mensaje encriptado es:",mensaje_respuesta)

def descifradoRSA(C, p, q, e, cantidad_caracteres, cantidad_codigo):
    mensaje = C.split()
    n = p*q
    
# Función para agregar un cero a números menores que 10
def dameFormatoNumero(numero):
    if numero < 10:
        return f'0{numero}'
    else:
        return str(numero)

# Función para realizar calculo de cada codigo del vector
def dameVectorOperado(vector, e, n, cantidad_codigo):
    _codigo_encriptado = []
    
    for i in vector:
        valor = int(i) ** e % n # operación del método RSA "pareja^e mod (n)"
        valor_formateado = '{:0{}}'.format(valor, cantidad_codigo) # formatear el valor a un valor de "cantidad_codigo"
        _codigo_encriptado.append(valor_formateado)

    return _codigo_encriptado

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





cifradoRSA(mensaje, int(valor_e), int(valor_n), int(cantidad_caracteres), cantidad_codigo)
descifradoRSA(mensaje, int(valor_p), int(valor_q), int(valor_e), int(cantidad_caracteres), cantidad_codigo)


