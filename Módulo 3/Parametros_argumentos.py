# # Parametros y argumentos
# def sumar(parametro1 , parametro2):
#     """Función que suma dos parametros y los imprime en pantalla"""
#     print('Suma:', parametro1 +  parametro2)

# argumento1 = 5
# argumento2 = 7

# # Invocando a la función por medio de parametros variables
# #sumar(argumento1, argumento2)

# # Invocando a la función por medio de parametros de valor
# sumar('mundo!' , 'Hola')
# sumar('Hola ',  'mundo!')

# sumar('hola') # error por que se han declarado un parametro

#############################################################

# Parametros opcionales
def muestra_alumno(nombre, edad=18, sexo = 'F'):
    '''
    Es una función que muestra en pantalla el nombre, la edad y el sexo de un alumno
    Recibe tres parametros
    1.- Nombre
    2.- Edad = 18
    3.- sexo = 'F'
    '''
    print(f'Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}')

# Ejecución con parametro obligatorio
muestra_alumno('Maria')

# Ejecución utilizando el parametro obligario y un opcional
muestra_alumno('Maria', 22)

# Ejecución de función con el primer y ultimo parametro
muestra_alumno('Juan', sexo = 'M')