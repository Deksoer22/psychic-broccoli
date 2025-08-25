# vocales = ["a", "e", "i", "o", "u"] # Lista de vocales

# vocales[1:4] = ["E", "I", "O"]

# print(vocales)

# #
# print(vocales, len(vocales))

# #
# vocales[1:4] = []# Elimina las vocales "e", "i", "o"

# print(vocales, len(vocales))

# #
# vocales[1:2] = ["e", "i", "o", "u"]
# print(vocales, len(vocales))# Imprime la lista de vocales y su longitud

# #
# vocales.extend(['i', 'i']) # Añade dos 'i' al final de la lista
# print(vocales, len(vocales))

# #
# print(vocales.index('i')) # Encuentra el índice de la primera 'i'

# #
# print(vocales.count('i'))# Cuenta cuántas veces aparece 'i' en la lista

# #
# print(vocales.index('i', 6))# Encuentra el índice de la primera 'i' a partir del índice 6

# #
# vocales.reverse() # Invierte el orden de los elementos en la lista
# print(vocales, len(vocales)) # Imprime la lista invertida y su longitud

# #
# vocales.sort() # Ordena la lista alfabéticamente
# print(vocales, len(vocales)) # Imprime la lista ordenada y su longitud

########################################

# carros = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"] # Lista de marcas de carros

# carros.sort(key=len)# Ordena la lista de carros por la longitud de cada marca

# print(carros)

# ##################
# listas = [[0,1], [2, 3, 4], [5,6]] 

# print(listas[0], listas[1:3]) 

# #
# print(listas[2] [1]) # Imprime el segundo elemento de la tercera lista

###########################

vocales1 = ['a', 'e', 'i', 'o', 'u'] # Lista de vocales

vocales2 = vocales1 # Asigna la misma referencia de lista a vocales2

print(vocales1, vocales2) # Imprime ambas listas

print(id(vocales1), id(vocales2)) # Imprime las direcciones de memoria de ambas listas

vocales3 = vocales1.copy() # Crea una copia de vocales1 en vocales3

print(vocales1, vocales3) # Imprime ambas listas

print(id(vocales1), id(vocales3)) # Imprime las direcciones de memoria de ambas listas

print(id(vocales1[2])) # Imprime la dirección de memoria del tercer elemento de vocales1

print(id(vocales1[2]), id(vocales2[2])) # Imprime las direcciones de memoria del tercer elemento de vocales1 y vocales2)

print(id(vocales1[2]), id(vocales3[2])) # Imprime las direcciones de memoria del tercer elemento de vocales1 y vocales3

del vocales1[2]

print(vocales2, vocales3) # Imprime vocales2 y vocales3 después de eliminar el tercer elemento de vocales1

print(id(vocales1[2]), id(vocales3[3])) # Imprime las direcciones de memoria del tercer elemento de vocales1 y el cuarto elemento de vocales3