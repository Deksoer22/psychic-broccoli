# # Parametros de tipo tupla, *args

# # def promedio(*numeros):
# #     promedio = sum(numeros)/len(numeros)
# #     print('El promedio es:', promedio)

# # promedio(4)
# # promedio(4,5,6)
# # promedio(1,2,3,4,5,6,7,8,9)

# #
# def es_numero(titulo, *serie):
    
#     print(titulo)
#     for i in serie:
#         if type(i) == int or i.isdigit():
#             print(f'{i} es número')
#         else:
#             print(f'{i} no es número')

# # es_numero('Números', '1', '2', '3')
# # es_numero('Letras', 'a', 'b', 'c')

# #
# nombre = 'Mezcla'
# lista_varios = ['a', '2', 3, 'f', 5]
# es_numero(nombre, *lista_varios)

################################################################3

# Parametros tipo diccionario **kwargs
# **kaargs sirve 
def area(**dato): # **dato es un tipo de variable que recibe un diccionario
    '''Calcula el area de una figura geometrica y la imprime en la pantalla''' # docstring

    # Si el diccionario tiene una clave llamada "figura" evalúa el valor de clave
    if dato["figura"]=="Rectangulo":
        print(dato["base"]*dato["altura"]) # Si el valor de la clave es "Rectangulo" imprime el valor de la base multiplicandolo por el valor de la altura 
    elif dato["figura"]=="Triangulo":
        print(dato["base"]*dato["altura"]/2) # Si el valor de la clave es "Triangulo" imprime el valor de la clave "base" multiplicado por la altura y despues dividide por 2
    elif dato["figura"]=="Circulo": 
        print(3.141593*dato["radio"]**2) # si el valor de la calve es "Circulo" imprime  el valor de la clave "radio" al cuadrado multiplicado por 3.141593
    else:
        print("Figura desconocida") # Si el valor de la clave no es ninguna de la anteriores, imprime "Figura desconocida"

area(figura = 'Triangulo', base = 10, altura = 5)
area(figura = 'Circulo', radio = 10, color = 'rojo')
area(figura = 'Dodecagono', lado = 10)