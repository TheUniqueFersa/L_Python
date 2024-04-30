# Estructuras básicas (if-elif-else, for, while) vistas en otras sesiones
# TERNARIO:
edad = int(input("Ingresa tu edad: "))
mensaje = "Eres mayor de edad" if edad > 18 else "Eres un bebé"
print(mensaje)

# import (todo el módulo)
"""
import playground_1
playground_1.tipo(range(5), "troll")
"""
# Solo importamos la función
from playground_1 import tipo
tipo(["Non", 1, 5.42, True], "Queso")



