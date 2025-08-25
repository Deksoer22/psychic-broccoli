# tiempos = {
#     'Hamilton': '1:49.8',
#     'Bottas': '1:56.4',
#     'Perez': '1:53.8',
#     'Verstappen': '1:52.6',
# } # Diccionario con tiempos de vuelta

# print(tiempos.items())# Imprime los elementos del diccionario

# print(tiempos.keys())# Imprime las claves del diccionario

# print(tiempos.values())# Imprime los valores del diccionario

# print(tiempos.get('Hamilton'))# Imprime el valor de la clave Hamilton

# print(tiempos.get('hamilton', 'No encontrado')) # Imprime 'No encontrado' si la clave no existe

######################################################
#Convertir tupla a diccionario

tiempos = dict(
    Hamilton= '1:49.8',
    Bottas= '1:56.4',
    Perez= '1:53.8',
    Verstappen= '1:52.6',
)

print(tiempos)