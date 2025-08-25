# las pilas son estructuras de datos que siguen el principio LIFO (Last In, First Out)
pila = [3, 6, 7]

while len(pila) >= 3 : # mientras la pila tenga al menos 3 elementos
    if pila[-1] % 3 : # si el último elemento no es múltiplo de 3
        extraido = pila.pop() # extrae el último elemento
        pila.append(extraido + 1) # añade el elemento incrementado en 1 al final de la pila
        print(pila) # imprime el estado actual de la pila
    else:
        print("Todos los elementos de la pila son múltiplos de 3") 
        break # si el último elemento es múltiplo de 3, imprime un mensaje y sale del bucle
