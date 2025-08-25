# vocales = ('a', 'e', 'i', 'o', 'u')

# print (vocales[2])

# #vocales[2] = 'I'  # Esto generará un error porque las tuplas son inmutables

# print (vocales[:3] + vocales[2:]) #[:3] toma los primeros 3 elementos, [2:] toma desde el tercer elemento hasta el final

# print (vocales.index('o')) # Devuelve el índice del primer elemento encontrado

# lista_vocales = list(vocales)  # Convertir la tupla a una lista
# #list sirve para convertir una tupla a una lista

# lista_vocales[2] = 'I' # Ahora podemos modificar la lista

# print (lista_vocales)# Imprime la lista modificada

# tupla_vocales = tuple(lista_vocales) # convierte la lista de nuevo a una tupla

# tupla_vocales[2] = 'I' # Esto generará un error porque las tuplas son inmutables

##################################

#Conjuntos (un conjunto no posee un orden ni un índice)

####
# vocales = ['a', 'e', 'i', 'o', 'u', 'a']
# print (vocales)

# vocales = list(set(vocales))  # Convertir la lista a un conjunto para eliminar duplicados

# print (vocales) # convierte el conjunto de nuevo a una lista sin un orden específico

####
# vocales1 = {'a', 'e', 'i', 'o', 'u', 'a'}

# vocales2 = {'e', 'i', 'o'}

# print(vocales2.issubset(vocales1)) #.issubset() verifica si todos los elementos de vocales2 están en vocales1

####
vocales1 = {'a', 'e', 'i', 'o', 'u'}
vocales2 = {'A', 'E', 'I', 'O', 'U'}

print(vocales1 - vocales2)  # Diferencia entre conjuntos, elementos en vocales1 que no están en vocales2

print(vocales1 | vocales2) # Unión de conjuntos, todos los elementos de ambos conjuntos

print(vocales1 & vocales2)  # Intersección de conjuntos, elementos comunes en ambos conjuntos

print(vocales1 ^ vocales2) # Diferencia simétrica, elementos que están en uno u otro conjunto, pero no en ambos