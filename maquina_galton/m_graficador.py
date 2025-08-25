import matplotlib.pyplot as plt 

def grafica_de_resultados(contenedores):
    """
    Función que grafica los resultados utlizando matplotlib, y muestra la distribucion de las canicas en los contenedores.
    """

    plt.bar(range(len(contenedores)), contenedores, color = "purple") # grafica de barras
    plt.xlabel("Contenedores (veces que la canica fue a la derecha)") # eje x
    plt.ylabel("Cantidad de canicas") # eje y
    plt.title("Maquina de Galton - Distribuidor de canicas")
    plt.grid(True, linestyle = "--", alpha = 0.5)
    plt.show()