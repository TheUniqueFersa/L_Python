# ----------------------------------------------------------------------
# Apuntes - ejemplos
# --------
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

# -------------
# SLICING
print(texto[0:5]) #Desde la posición 0 hasta la 5, sin contar el límite superior
print(texto[10:16])


print(texto[:10])
print(texto[5:])



# ----------------------------------------------------------------------
# Ejercicios
