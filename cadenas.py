# texto_variado = "palabra 123 +*- #$%$"
# print(type(texto_variado)) 

# #Podemos utlilizar comillas triples para que  el texto se muestre como la cadena que hemos escrito
# print("""
# Funcionamiento de \
# programas: (opciones)
#   -1 para accerder a opciones 
#     -2 para salir
# """)

######################################################

#Substring e indexado

# texto = "Python"

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) #Error no pudemos acceder a un rango que no existe
# print(texto[-7]) #Error no pudemos acceder a un rango que no existe

# letra = texto[0]
# print(letra)

# texto[0] = "p" # Error no podemos modificar una cadena

# letra = "p"
# print(letra)

# texto_compuesto = letra + texto[1] # Concatenación de cadenas
# print(texto_compuesto)

##########################################################

#slicing o substringing
# texto = "Python"

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])
# print(texto[2:2])

#########################################################
#cadenas y formatos

# texto = "Hola Mundo! Buenas noches"
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print(texto.swapcase())
# texto = texto.upper()
# print(texto)

# print("{} + {} = {}".format(2, 3, 2+3))
# print("{} + {} = {}".format("hola", "mundo", "hola mundo"))
# print("{:.3f} + {:.4f} = {}".format(2, 3, 2+3))
# print("{1} + {0} = {2}".format(2, 3, 2+3)) 
# print("{2} + {0} = {1}".format("hola", "mundo", "hola mundo"))
# print("{:d} = {:b} = {:o} = {:x}".format(15, 15, 15, 15))