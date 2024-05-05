# ----------------------------------------------------------------------
# Apuntes - ejemplos
# --------
def apuntes():

    # INDEXING
    texto = "A ella le gusta lenguaje C, es decir, ella es perfecta"
    print(texto[0]) # Como en C :ooo
    print(texto[1]) # Es espacio

    #print(texto[999]) # IndexError: string index out of range

    print(texto[-1]) # Esto si es válido, lo que hace es ir de regreso
    print(texto[len(texto)-1]) #Línea que hace lo mismo que la de arriba 
    '''(Nótese que dentro del índice) se resta 1, porque len() regresa el tamaño, y, así como los arreglos 
    el índice máximo para cualquier arreglo es el numero n (tamaño) - 1
    '''

    # -------
    # SLICING
    print(texto[0:5]) #Desde la posición 0 hasta la 5, sin contar el límite superior
    print(texto[10:17])

    print(texto[:10]) # Desde el principio ([0]) hasta n, sin contar n
    print(texto[5:]) # Desde el numero n hasta el final

    print(texto[20: -1]) #Desde la posición 20, hasta la última posición, pero sin contarla, en este caso -1 es equivalente a la última posición

    # jumps
    print(texto[2:6:1]) #Mandar un tercer valor representa la cantidad de caracteres en los que irá saltando
    print(texto[2:12:2]) #Mandar un tercer valor representa la cantidad de caracteres en los que irá saltando
    print(texto[2:24:4]) #Mandar un tercer valor representa la cantidad de caracteres en los que irá saltando
    print(texto[::2]) # Aunque rara sintaxis, es totalmente válida

    cadena = "cadena"
    print(cadena[1::2]) #Empieza en el índice 1, dando saltos de 2 en 2 hasta el final
    cadena = "cadena 23sis"
    print(cadena[1::3]) #Empieza en el índice 1, dando saltos de 3 en 3 hasta el final

# ----------------------------------------------------------------------
# Ejercicios
#apuntes()

