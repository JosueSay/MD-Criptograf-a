# Integrantes: Josué Say - 22801 | Mathew Córdero - 22982
# Funcionalidad: criptar y descencriptar mensajes utilizando el método RSA

from Operaciones import dameBloques, dameCodigoBloques, dameVectorCodigo

diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto a usar
modulo = len(diccionario) # modulo segun el alfabeto
cantidad_caracteres = 2 # cantidad de caracteres por bloque
cantidad_codigo = cantidad_caracteres*2


# Función para pedir datos para el cifrado RSA
def pedirDatosCifradoRSA():
    
    mensaje = input ("Ingrese el mensaje 'M': ")
    valor_p = input ("Ingrese el valor 'p': ")
    valor_q = input ("Ingrese el valor 'q': ")
    exponente = input ("Ingrese el exponente 'e': ")
    
    cifradoRSA(mensaje, int(valor_p), int(valor_q), int(exponente))
    

# Función para pedir datos para el descifrado RSA
def pedirDatosDescifradoRSA():
    mensaje = input ("Ingrese el mensaje 'C': ")
    exponente = input ("Ingrese dato 'e' de la llave pública: ")
    producto_n = input ("Ingrese dato 'n' de la llave pública: ")
    descifradoRSA(mensaje, exponente, producto_n)

# Función para el crigfrado RSA
def cifradoRSA(M, p, q, e):
    n = p*q # modulo a usar
    bloques = dameBloques(M, cantidad_caracteres) # bloques del mensaje M
    
    vector_codigo = dameVectorCodigo(bloques) # vector codigo segun el mensaje con bloques
    vector_codigo_nuevo = [dameFormatoNumero(vector_codigo[i]) + dameFormatoNumero(vector_codigo[i + 1]) for i in range(0, len(vector_codigo), cantidad_caracteres)] # vector codigo con el formato de cantidad de digitos reales
    
    codigo_encriptado = dameVectorOperado(vector_codigo_nuevo, e, n) # obtener el vector de codigo encriptado (con calculos)
    mensaje_respuesta = '-'.join(codigo_encriptado) # obtener el mensaje como respuesta de la codificacion
    print(bloques)
    print(vector_codigo)
    print("El mensaje encriptado es:",mensaje_respuesta)


# Función para agregar un cero a números menores que 10
def dameFormatoNumero(numero):
    if numero < 10:
        return f'0{numero}'
    else:
        return str(numero)

# Función para realizar calculo de cada codigo del vector
def dameVectorOperado(vector, e, n):
    _codigo_encriptado = []
    
    for i in vector:
        valor = int(i) ** e % n # operación del método RSA "pareja^e mod (n)"
        valor_formateado = '{:0{}}'.format(valor, cantidad_codigo) # formatear el valor a un valor de "cantidad_codigo"
        _codigo_encriptado.append(valor_formateado)

    return _codigo_encriptado


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

    if esCifrado == 1:
        pedirDatosCifradoRSA()
    else:
        pedirDatosDescifradoRSA()

cifradoRSA("SENDMONEY", 53, 61, 77)
    

    
    
    
    
    
    


