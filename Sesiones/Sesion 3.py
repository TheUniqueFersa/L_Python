
#ALGUNOS APUNTES
# -----------------------------------------------------------------
#Sobre Operadores lógicos
def imprimirSeparador(char, manera):
    if manera == 1:
        #La manera antigua:
        for i in range(1,25):
            print(char,end='')
    else:
        #La nueva manera >:)
        print(char*25)
    
def pruebasApuntes():
    rangInf = 100
    rangSup = 1000
    print('not True and True =>', not (True and True))
    print('not True and False =>', not (True and False))
    print('not False and True =>', not (False and True))
    print('not False and False =>', not (False and False))

    entrada = input("Ingrese un número: ")
    entrada = int(entrada) #Cast hecho posteriormente sobre la misma variable
    print(not(entrada>rangInf and entrada <=rangSup)) #Invierte el valor en sí, osea si es verdadero, lo voltea a false y viceversa
    #Se puede entender como que si devuelve true, entonces es falso; caso contrario en que devuelva falso, es verdadero, porque es not.
    imprimirSeparador('XD', 2)#Intercambiar entre 1 y 2 y ver las diferencias
# -----------------------------------------------------------------

# EJERCICIOS
# -----------------------------------------------------------------
pruebasApuntes()