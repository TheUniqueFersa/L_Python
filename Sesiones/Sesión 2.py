from math import trunc
def tolerarFlotante(x, y):
    tolerance = 0.0001
    condicion = abs(x - y) < tolerance
    # Ejemplo de ternario:
    z=0
    total = 0
    if condicion:
        entero = trunc(x)
        z = x - entero
        z *= (10**4)
        print(entero, z, type(entero), type(z))
        total = entero + (z/(10**4))
        print(total)
        h = x
        print(id(h), id(x), id(y))
        y = (total)
        print(y)
        print(id(y))
    return (True if (condicion) else False, y) #Obviamente esta linea es innecesaria o repetitiva, pero lo hice par aprobar el ternario
x = 3.3
print(x)
y = 1.1 + 2.2 #Es igual a 
print(y)
print(x==y) # 3.3 no es igual a 3.300000000000003
# ¿Cómo resolvemos este problema?

y_str = format(y, ".2g")
print(f"y_str : {y_str}, {type(y_str)}")
print(y_str == str(x))
print(x == float(y_str))

tolerance = 0.0001
print(abs(x - y) < tolerance) #Devuelve true si el numero en cuestión es menor a 'tolerance', osea nuestro número de tolerancia
print(x==y)

print(tolerarFlotante(x, y)) #Tupla
y = tolerarFlotante(x, y)[1]
print(x,y)
print(x==y)