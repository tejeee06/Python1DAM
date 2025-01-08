def invertirCadena(cadena):

    pila = []

    for i in cadena:

        pila.append(i)
    
    cadenaInvertida = ""

    while len(pila) > 0:

        cadenaInvertida += pila.pop()

    return cadenaInvertida

cadena = "Python"
print(invertirCadena(cadena))