# (Sesión 4 fue playground_2.py)
text = "Esto es una prueba de una cadena"
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
print(text.count('a'))

# Método swapcase
print(text.swapcase())

# Método startswith
print(text.startswith("Esto  "))

# Método endswith
print(text.endswith("a\n"))

# Método replace
text.replace("cadena", "cadenas") # No se cambia la cadena original con los métodos :O
# print(text.replace("cadena", "cadenas"))
print(text)

texto_2 = "esto es una prueba"
print(texto_2.capitalize())
print(texto_2.title())
print(texto_2.isdigit()) #Devuelve falso

