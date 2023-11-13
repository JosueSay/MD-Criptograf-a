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

# Función para el cifrado de mensajes usando RSA
def cifradoRSA(M, e, n, cantidad_caracteres, cantidad_codigo):
    bloques = dameBloques(M, cantidad_caracteres) # bloques del mensaje M
    
    vector_codigo = dameVectorCodigo(bloques) # vector codigo segun el mensaje con bloques
    vector_codigo_nuevo = [dameFormatoNumero(vector_codigo[i]) + dameFormatoNumero(vector_codigo[i + 1]) for i in range(0, len(vector_codigo), cantidad_caracteres)] # vector codigo con el formato de cantidad de digitos reales
    
    codigo_encriptado = dameVectorOperado(vector_codigo_nuevo, e, n, cantidad_codigo) # obtener el vector de codigo encriptado (con calculos)
    mensaje_respuesta = '-'.join(codigo_encriptado) # obtener el mensaje como respuesta de la codificacion
    
    print("\033[1m===============================\033[0m")
    print("\033[1m||Encriptar con el método RSA||\033[0m")
    print("\033[1m===============================\033[0m")
    print("El mensaje ingresado es:",M)
    print(f"Su llave pública es: ({e}, {n})")
    print("La separación por bloques es:",bloques)
    print("El vector codigo es:",vector_codigo_nuevo)
    print("El mensaje encriptado es:",mensaje_respuesta)

# Función para el descifrado de mensajes usando RSA
def descifradoRSA(C, p, q, e, cantidad_caracteres, cantidad_codigo):
    mensaje = C.split()
    n = p*q
    phi = (p-1)*(q-1)
    # e*d ≡ 1 (mod phi) → d*e + phi*k = 1
    mcd, d, k = algoritmoEuclidesExtendido(e, phi)
    
    codigo_descencriptado = dameVectorOperado(mensaje, d, n, cantidad_codigo) # obtener el vector de codigo encriptado (con calculos)
    codigo_pares = [numero for cadena in codigo_descencriptado for numero in separarVectorCodigo(cadena, cantidad_caracteres)] # convertir el codigo_descencriptado en pares
    codigo_completo = [diccionario[i] for i in codigo_pares] # mensaje segun el codigo_pares
    mensaje_respuesta = ''.join(codigo_completo)
    
    
    print("\033[1m===================================\033[0m")
    print("\033[1m||Descencriptar con el método RSA||\033[0m")
    print("\033[1m===================================\033[0m")
    print("El mensaje ingresado es:",C)
    print(f"Su llave privada es: {d}")
    print("El vector codigo descencriptado es:",codigo_pares)
    print("El mensaje descencriptado es:",mensaje_respuesta)
    
# Función para agregar un cero a números menores que 10
def dameFormatoNumero(numero):
    if numero < 10:
        return f'0{numero}'
    else:
        return str(numero)

# Función para realizar el cálculo de exponenciación modular de cada código de un vector de forma recursiva
def dameVectorOperado(vector, e, n, cantidad_codigo):
    _codigo_encriptado = []

    def exponenciacionModular(b, e, m):
        if e == 0:
            return 1
        elif e % 2 == 0:  # Si e es par
            temp = exponenciacionModular(b, e // 2, m)
            return (temp * temp) % m
        else:  # Si e es impar
            temp = exponenciacionModular(b, (e - 1) // 2, m)
            return (b * temp * temp) % m

    for i in vector:
        valor = exponenciacionModular(int(i), e, n)
        valor_formateado = '{:0{}}'.format(valor, cantidad_codigo)
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

# Función para obtener el valor de "d" de la llave privada
def algoritmoEuclidesExtendido(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        mcd, x, y = algoritmoEuclidesExtendido(b, a % b)
        return (mcd, y, x - (a // b) * y)

# Función para dividir cada cadena en pares de dígitos y convertir a números
def separarVectorCodigo(cadena, cantidad_caracteres):
    return [int(cadena[i:i+cantidad_caracteres]) for i in range(0, len(cadena), cantidad_caracteres)]


#### PRUEBAS:
# Cifrado
cifradoRSA(M, e1, n1, caracteres1, digitos1)
#cifradoRSA("SENDMONEY", 77, 3233, 2,4)

# Descifrado
descifradoRSA(C, p2, q2, e2, caracteres2, digitos2)


