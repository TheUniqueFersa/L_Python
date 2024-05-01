# (Sesión 4 fue playground_2.py)
text = "Esto es uña prueba de una cadena"
print('Float' in text) # Regresa False
print('cadena' in text) # Regresa True

if("cadena" in text):
    print("Hay una cadena")
else:
    print("Hay otra cosa")

# size
size = len(text)
print(size)

# Métodos upper y lower
print(text)
print("En minúsculas: {}".format(text.lower()))
print(f"En mayúsculas: {text.upper()}")

# Método count
print(text.count(' cadena\0')) # Regresa 0 a menos que se ponga explícitamente dicho caracter: text = "Esto es uña prueba de una cadena\0" o text = "Esto es uña prueba de una cadena\n"
print(text.count(' cadena')) # Regresa 1

# Método swapcase
print(text.swapcase())

# Método startswith
print(text.startswith("Esto  "))

# Método endswith
print(text.endswith("a\n"))

# Método replace
text.replace("a", "AÑA") # No se cambia la cadena original con los métodos :O
print(text.replace("a", "oo"))
print(text)

texto_2 = "esto es una prueba"
print(texto_2.capitalize())
print(texto_2.title())
print(texto_2.isdigit()) #Devuelve falso


print("0".isdigit()) #Devuelve True
print("11209103192e+12".isdigit()) #Devuelve falso
print("-1120910319212".isnumeric()) # Devolveré False, porque no puede identificar números negativos
print("0.0".isdigit()) #Devuelve falso