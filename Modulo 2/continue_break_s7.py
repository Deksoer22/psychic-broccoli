#La sentencia continue omite una sola interacíon de la repetición de un ciclo.
# uso de la sentencia continue en un ciclo for

# for numero in range(1, 11): # iteramos del 1 al 10
#     if numero % 2 == 1:# si el número es impar
#      continue # saltamos a la siguiente iteración
#     print(f'{numero} es un número par')

    # uso de la sentencia continue en un ciclo while

# numero = 0  # inicializamos la variable numero
# while numero < 11: # iteramos del 0 al 10
#     numero += 1 # incrementamos el numero en 1
#     if numero % 2 == 0: # si el número es par
#      continue # saltamos a la siguiente iteración
#     print(f'{numero} es un número impar') # imprimimos el número impar

######################################

# uso de la sentencia break

# numero = int(input('Ingrese un digito:'))
# limite_inferior = 0 # inicializamos la variable limite_inferior
# limite_superior = 10 # inicializamos la variable limite_superior
# buscado = 5 # inicializamos la variable buscado     
# intentos = 0 # inicializamos la variable intentos

# while True: # iteramos indefinitamente
#     intentos += 1 # incrementamos los intentos en 1
#     if numero == buscado: # si el número es igual al buscado
#         print(f'El numero {numero} fue encontrado en {intentos} intentos') # imprimimos el número encontrado y los intentos
#         break # salimos del ciclo
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2 # actualizamos el buscado 
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print('Fin del programa')

##################################

#Uso de la sentencia exit


# numero = int(input('Ingrese un digito:'))
# limite_inferior = 0 # inicializamos la variable limite_inferior
# limite_superior = 10 # inicializamos la variable limite_superior
# buscado = 5 # inicializamos la variable buscado     
# intentos = 0 # inicializamos la variable intentos

# while True: # iteramos indefinitamente
#     intentos += 1 # incrementamos los intentos en 1
#     if numero == buscado: # si el número es igual al buscado
#         print(f'El numero {numero} fue encontrado en {intentos} intentos') # imprimimos el número encontrado y los intentos
#         exit() # salimos del ciclo
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2 # actualizamos el buscado 
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print('Fin del programa')
# print('Impresión despues de la sentencia break ')
# print('Impresión despues de la sentencia exit()')

intentos = 0
while True :
  intentos += 2
  print(f"Intentos{intentos}")
  if  intentos == 20 :
    print("Fin del programa")
    exit()
   
    