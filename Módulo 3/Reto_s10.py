# ● Que permita crear dos listas de distintas longitudes.
# ● Que la longitud y los elementos de cada lista sean especificados por el usuario.
# ● Que imprima las listas indicando que son las listas originales.
# ● Que elimine de la primera lista los nombres de la segunda.
# ● Que imprima la primera lista indicando que se han eliminado los elementos que estaban también en la segunda.
# ● utliza por lo menos dos funciones 

def crear_lista(nombre_lista):
    """
    Función para crear una lista con elementos especificados por el usuario.
    """
    longitud = int(input(f"¿Cuantos elementos tendrá la {nombre_lista}? "))
    lista = []
    for i in range(longitud):
        elemento = input(f"Ingrese el elemento {i+1} para la {nombre_lista}: ")
        lista.append(elemento)
    return lista

def eliminar_elementos(lista1, lista2):
    """
    Función para eliminar de la primera lista los elementos que están en la segunda lista.
    """
    nueva_lista = []
    lista2_minuscula = [elemento.lower() for elemento in lista2]

    for elemento in lista1:
        if elemento.lower() not in lista2_minuscula:
            nueva_lista.append(elemento)
    return nueva_lista
    
# Crear las listas
lista1 = crear_lista("Primera lista")
lista2 = crear_lista("Segunda lista")

# Imprimir las listas originales
print("\n Listas originales: ")
print("Primera lista: ", lista1)
print("Segunda lista: ", lista2)

# Eliminar elementos de la primera lista que están en la segunda
lista_filtrada = eliminar_elementos(lista1, lista2)

# Imprimir la primera lista después de eliminar los elementos
print("\n Primera lista después de eliminar los elementos que también estaban en la segunda: ")
print(lista_filtrada)

        

