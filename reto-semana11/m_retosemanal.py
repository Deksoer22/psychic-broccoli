

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

def crear_varias_listas():
    """
    Función para crear multiples listas (la cantidad que el usuario quiera crear).
    """
    listas = []
    cantidad_listas = int(input("¿Cuantas listas deseas crear? "))
    for i in range(cantidad_listas):
        nombre_lista = f"Lista {i+1}"
        lista = crear_lista(nombre_lista)
        listas.append(lista)
    return listas


def eliminar_elementos_repetidos(listas):
    """
    función para eliminar de cada lista los elementos que están en las otras listas.
    """

    listas_filtradas = []
    for i in range(len(listas)):
        lista_actual = listas[i]
        elementos_para_eliminar =[]
        for j in range(i + 1, len(listas)):
            elementos_para_eliminar.extend(listas[j])
            elementos_para_eliminar = [elemento.lower() for elemento in elementos_para_eliminar]

        nueva_lista = [elemento for elemento in lista_actual if elemento.lower() not in elementos_para_eliminar]
        listas_filtradas.append(nueva_lista)
    return listas_filtradas
    
def imprimir_listas(listas, mensaje):
    print(f"\n {mensaje}")
    for i, lista in enumerate(listas):
        print(f"Lista {i + 1}: {lista}")
    




