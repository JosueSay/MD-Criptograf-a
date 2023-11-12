# Integrantes: Josué Say - 22801 | Mathew Córdero - 22982
# Funcionalidad: criptar y descencriptar mensajes utilizando Vigénere

from Operaciones import dameBloques, dameCodigoBloques, dameVectorCodigo

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto a usar
modulo = len(diccionario) # modulo segun el alfabeto

# Función para descifrar mensajes usando el sistema Vigénere
def dameMensajeVigenere(_clave, _llave, _esCifrado):
    clave = _clave # clave del mensaje a descifrar
    llave = _llave # llave del mensaje a descifrar
    
    separacion_llave = list(llave) # separacion por caracteres de llave 
    codigo_llave = [diccionario.find(caracter) for caracter in separacion_llave] # codigo de los caracteres de separacion_llave

    bloques_mensaje = dameBloques(clave, len(llave)) # mensaje a descifrar separado por bloques
    vector_codigo = dameVectorCodigo(bloques_mensaje) # lista con el codigo de la clave
    
    vector_cifrado = dameCodigoBloques(codigo_llave, vector_codigo, _esCifrado) # lista con el codigo resultante de la operacion
    mensaje_respuesta = [diccionario[i] for i in vector_cifrado] # mensaje segun el vector_cifrado
    
    return mensaje_respuesta

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
