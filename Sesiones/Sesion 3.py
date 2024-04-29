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
#pruebasApuntes()
# 1. Hacer un programa que identifique entre pares y nones

def evenOrOdd(x):
    if entrada == 0:
        print("Soy cero")
    elif entrada % 2 == 0:
        print("El número {} es par".format(entrada))
    else:
        print("El número {} es impar".format(entrada))
def ejercicio1():
    entrada = ""
    #while entrada.__class__ != type(1) and entrada != -1:
    entrada = input("Ingresa un numero: ")
    print(entrada.__class__, type(1))
    while entrada != "Ya estuvo": 
        #print(entrada.__class__) #Prueba
        """
        if entrada.__class__ == type(1):
            entrada = int(entrada)
            evenOrOdd(entrada)
        else:
            print("Dato inválido. ")
        """
        entrada = int(entrada)
        evenOrOdd(entrada)
        entrada = input("Ingresa un numero entero: ")
    print("Ya me salí")
#ejercicio1()
# -----------------------------------------------------------------
#Ejercicio 2. 
def ejercicio2():
    user_option = input('rock, paper, scissors => ')
    computer_option = 'scissors'
    if user_option == computer_option:
        print('Draw!')
    elif user_option=='rock':
        if computer_option=='scissors':
            print("Rock beats scissors")
            print("User won!")
        else:
            print("Paper beats rock")
            print("Computer won!")
    elif user_option=='paper':
        if computer_option=='rock':
            print("Paper beats rock\nUser won!")
        else:
            print("Scissors beat paper\nComputer won!")
    elif user_option=='scissors':
        if computer_option =='paper':
            print("Scissors beat paper\nUser won!")
        else:
            print("Rock beats scissors\nComputer won!")
    """
    entrada = input("Ingresa un numero: ")
    while entrada != "Ya estuvo": 
        entrada = int(entrada)
        entrada = input("Ingresa un numero entero: ")
    print("Ya me salí")
    """

ejercicio2()

