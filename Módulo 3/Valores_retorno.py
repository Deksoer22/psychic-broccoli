# Valores de retorno sentencia return

# def promedio (*numeros):
#     return sum(numeros) / len(numeros)

# x = promedio(4,5,6)
# print(x)

#
# def area(**dato): # **dato es un tipo de variable que recibe un diccionario
#     '''Calcula el area de una figura geometrica y la imprime en la pantalla''' # docstring

#     # Si el diccionario tiene una clave llamada "figura" evalúa el valor de clave
#     if dato["figura"]=="Rectangulo":
#         return(dato["base"]*dato["altura"]) # Si el valor de la clave es "Rectangulo" imprime el valor de la base multiplicandolo por el valor de la altura 
#     elif dato["figura"]=="Triangulo":
#         return(dato["base"]*dato["altura"]/2) # Si el valor de la clave es "Triangulo" imprime el valor de la clave "base" multiplicado por la altura y despues dividide por 2
#     elif dato["figura"]=="Circulo": 
#         return(3.141593*dato["radio"]**2) # si el valor de la calve es "Circulo" imprime  el valor de la clave "radio" al cuadrado multiplicado por 3.141593
#     else:
#         print("Figura desconocida") # Si el valor de la clave no es ninguna de la anteriores, imprime "Figura desconocida"

# triangulo=area(figura = 'Triangulo', base = 10, altura = 8)
# print(f'El area del triangulo es:{triangulo}')
# circulo=area(figura = 'Circulo', radio = 10, color = 'rojo')
# print(f'El area del circulo es:{circulo}')
# dodecagono=area(figura = 'Dodecagono', lado = 10)
# print(f'El area del dodecagono es:{dodecagono}')

#######################################

# Recursividad de funcciones en python

# def factorial(numero, intentos = 0):
#     if numero == 0:
#         return 1
#     else:
#         intentos += 1
#         print(intentos)
#         return numero * factorial(numero - 1, intentos)
    
# # print('El factorial de 0 es (0!):', factorial(0))
# # print('El factorial de 1 es (1!):', factorial(1))
# # print('El factorial de 3 es (3!):', factorial(3))
# print('El factorial de -1 es (-1!):', factorial(-1))

################################################
# Funciones lambda o funciones anónimas

# suma = lambda x, y : x + y 
# print(suma('Hola ', 'mundo!'))
# print(suma(2, 5))

#
# lista_numeros = [1, 0, -2]
# lista_numeros = sorted(lista_numeros, key = lambda n: abs(n))
# print(lista_numeros)

###################################################
# Función zip

paises = ['Kenia', 'Francia', 'México', 'Japón']
capitales = ['Nairobi', 'París', 'Ciudad de México', 'Tokio']
poblacion = [54, 66, 130]

for i in zip(paises, capitales, poblacion):
    print(i)