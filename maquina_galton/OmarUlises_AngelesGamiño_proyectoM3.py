# modulo galton(galton_app.py)
from m_simulador import simulador_canicas
from m_graficador import grafica_de_resultados

cantidad_canicas=3000
niveles=12

contenedores = simulador_canicas(cantidad_canicas, niveles)
grafica_de_resultados(contenedores)

## Pruebas de la simulación
print(f"Contenedores: {contenedores}")
print(f"Total de canicas simuladas: {sum(contenedores)}")