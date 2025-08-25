def captura_alumnos(numero = 3):
    '''
    Registra alumnos y dos calificaciones
    Recibe como parámetro la cantidad de alumnos a registrar
    si no se especifica el número de alumnos, se registrarán 3
    ''' 
    lista_alumnos = []
    for i in range(numero):
        nombre = input(f'{i + 1}.- Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificación de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificación de {nombre}: '))
        lista_alumnos.append([nombre, calificacion1, calificacion2])
        promedio(nombre,calificacion1, calificacion2)
    print('Las calificaciones de los alumnos son:', lista_alumnos)

def promedio(nombre,calificacion1,calificacion2):
    '''
    Calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    Recibe como parámetros el nombre y dos calificaciones del alumno 
    '''
    promedio = (calificacion1 + calificacion2) /2
    print(f'el promedio de {nombre} es: {promedio}')

numero_alumnos = input('¿Cuántos alumnos deseas registrar?')

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()

