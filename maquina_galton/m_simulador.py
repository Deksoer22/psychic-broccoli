import random

def simulador_canicas(cantidad_canicas=3000, niveles=12):
    """Función que simula el recorrido de las canicas en la maquina de Galton.
    """
    contenedores = [0] * (niveles + 1)

    for _ in range(cantidad_canicas): # Simula cada canica 
        derecha = 0
        for _ in range(niveles):
            if random.choice(["izquierda", "derecha"]) == "derecha": 
                derecha += 1 # cuenta las veces que la canica va a la derecha
        contenedores[derecha] += 1 
    return contenedores

    