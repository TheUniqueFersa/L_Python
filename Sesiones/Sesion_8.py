# -----------------------------------------------
# Apuntes
#---------
# Listas
numeros = [1,2,3,4]
print("La lista {} es de la clase {}".format(numeros, type(numeros)))
lista = [2, 31.43, True, "soy cadena", 'c', ["otra lista", False, range(2,1)]]
print(f"Las listas pueden contener distintos tipos de datos\nComo la lista: {lista}")

#  Cadenas son inmutables
cadena = "si"
#cadena[0] = 'n' #Arroja un TypeError: 'str' object does not support item assignment

# Las listas si son mutables (Actualiza valores de la lista)
lista[3] = "ahora soy cadenan't" # Note que las comillas dobles se ponen por la presencia de ''
print(lista)

# Indexing
print(lista[:3]) # Imprime desde 0 hasta 3 excluyendo el 3

# Esto tiene sentido cuando recordamos los id's de las variables
print(type(lista[:3]), f"Original: {id(lista)}, sliced: {id(lista[:3])}")
print(lista[:3][2], id(lista[:3]))
lista[:3][2] = False
print(lista[:3][2], id(lista[:3]))

lista2 = lista[:3]
#lista2[2] = False
print(f"La lista original: {lista}\nid orig: {id(lista)}, id del elemento 2: {id(lista[2])}")
print(f"{lista[:3][2]}, {lista2[2]}; \nEl id sliced list: {id(lista[:3])} Id pasado: {id(lista2)}, id del elemento 2: {id(lista2[2])}")

# La mutabilidad de la lista:
# lista[:0] = "no"
# print(lista)
# -----------------------------------------------
# Ejercicios

