from m_retosemanal import crear_varias_listas, eliminar_elementos_repetidos, imprimir_listas

def ejecutar_proceso():
    listas_originales = crear_varias_listas()
    imprimir_listas(listas_originales, "Listas originales: ")

    listas_filtradas = eliminar_elementos_repetidos(listas_originales)
    imprimir_listas(listas_filtradas, "Listas después de eliminar elementos repetidos: ")

if __name__ == "__main__":
    ejecutar_proceso()