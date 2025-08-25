

lista = []

capacidad_maxima = 10

while True :
    if len(lista) >= capacidad_maxima:
        print("La lista esta llena. no se pueden agregar mas alumnos.")
        break

    opcion = input("Agregar alumno (1) o terminar (2): ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        calificacion1 = int(input(f"ingrese la primera calificación de {nombre}: "))
        calificacion2 = int(input(f"Ingrese la segunda calificación de {nombre}: "))
        calificacion3 = int(input(f"Ingrese la tercera calificación de {nombre}: "))
        alumno = [nombre, calificacion1, calificacion2, calificacion3]
        lista.append(alumno)
        print(f"{nombre} ha sido agregado correctamente. Total de alumnos: {len(lista)} ")
        
    elif opcion == "2":
        print(f"El programa a terminado con {len(lista)} alumnos. ")
        break
    
    else: 
        print("Se a ingresado una opcion invalida. ")
        continue

#Muestra la lista final
print("\n Lista de alumnos registrada: ")

for alumno in lista:
    print(f"Nombre: {alumno[0]} | Calificaciones: {alumno[1]}, {alumno[2]}, {alumno[3]}")
