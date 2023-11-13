### Prueba 2
C = "0981 0461"
p2 = 43
q2 = 59
e2 = 13
caracteres2 = 2
digitos2 = caracteres2*2

def descifradoRSA(C, p, q, e, cantidad_caracteres, cantidad_codigo):
    mensaje = C.split()
    n = p*q
    phi = (p-1)*(q-1)
    
    # e*d ≡ 1 (mod phi) → d*e + phi*k = 1
    mcd, d, k = algoritmoEuclidesExtendido(e, phi)
    resultado = [] # codigo en numeros
    
    for i in mensaje:
        valor = exponenciacionModular(int(i), d, phi)
        resultado.append(valor)
    
    codigo_encriptado = [str(numero) for numero in resultado] # codigo en cadenas
    codigo_encriptado_numeros = [numero for cadena in codigo_encriptado for numero in separarVectorCodigo(cadena, cantidad_caracteres)] # codigo con los valores separados
      
    
    

    
    
# Función para obtener el valor de "d" de la llave privada
def algoritmoEuclidesExtendido(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        mcd, x, y = algoritmoEuclidesExtendido(b, a % b)
        return (mcd, y, x - (a // b) * y)

# Función para determinar la exponenciacion modular de un valor de la encriptación
def exponenciacionModular(b, e, m):
    if e == 0:
        return 1
    elif e % 2 == 0:  # Si e es par
        temp = exponenciacionModular(b, e // 2, m)
        return (temp * temp) % m
    else:  # Si e es impar
        temp = exponenciacionModular(b, (e - 1) // 2, m)
        return (b * temp * temp) % m

# Función para dividir cada cadena en pares de dígitos y convertir a números
def separarVectorCodigo(cadena, cantidad_caracteres):
    return [int(cadena[i:i+cantidad_caracteres]) for i in range(0, len(cadena), cantidad_caracteres)]

# Descifrado
descifradoRSA(C, p2, q2, e2, caracteres2, digitos2)

    
    

