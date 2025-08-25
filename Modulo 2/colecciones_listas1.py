#Listas
# mix = [0, 1.0,"dos", 3+4j] 

# for i in mix : 
#     print(f"{i:6} - Tipo: {type(i)}") # Imprime cada elemento y su tipo

#
# print(len(mix))  # Imprime la longitud de la lista

#
# sin_dos = mix[:2] + mix[3:]  # Elimina el elemento "dos"
# print(mix, sin_dos)  # Imprime la lista original y la modificada

#
# duplicado = mix * 2  # Duplica la lista
# print(duplicado)  # Imprime la lista duplicada

############################

cuadrados = [0, 1, 4, 9, 16, 25]
# for i in range(len(cuadrados)):
#     print(f"{i} **2 = {cuadrados[i]}") # imprime el indice y el resultado de elevar al cuadrado

#
# for i in range(len(cuadrados)):
    # cuadrados[i] = cuadrados[i] * i # Modifica cada elemento de la lista multiplicándolo por su índice
    # print(f"Ahora están al cubo{cuadrados[i]}")  # Imprime el nuevo valor de cada elemento

#
# cuadrados.append(7 ** 3) # Añade el cubo de 7 al final de la lista
# print(cuadrados)

#
# cuadrados.insert(6, 6 ** 3) # Inserta el cubo de 6 en la posición 6
# print(cuadrados)

#
cuadrados.extend([27, 1000, -1])  # Añade varios elementos al final de la lista
print(cuadrados)

#
cuadrados.extend(range(-1, -4, -1))  # Añade una secuencia de números negativos al final de la lista
print(cuadrados)

#
# del cuadrados[9:]  # Elimina todos los elementos desde el índice 9 en adelante
# print(cuadrados)

#
# cuadrados.remove(27)# Elimina el primer elemento que sea igual a 27
# print(cuadrados)

#
# valor_removido = cuadrados.pop(2)  # Elimina y devuelve el elemento en la posición 2
# print(cuadrados)
# print(f"El valor eliminado es: {valor_removido}")  # Imprime el valor eliminado

#
cuadrados.clear()  # Elimina todos los elementos de la lista
print(cuadrados)