#Da la bienvenida y solicita las coordenadas al usuario
coordenadas = []

cantidad = int(input("¿Cuantos puntos deseas ingresar? "))# pregunta cuantos puntos quieres localizar

for i in range(cantidad):
    print(f"\nPunto {i + 1}: ")
    eje_x = float(input("Ingrese el valor del eje x: "))
    eje_y = float(input("Ingrese el valor del eje y: "))

#Guarda las coordenadas en la lista      
    coordenadas.append((eje_x, eje_y))

#Va validando las coordenadas dependiendo los valores ingresados, para así darde el cuadrante
    if eje_x == 0 or eje_y == 0:
        print("Error:Las coordenadas no deben ser cero. ")
    elif eje_x > 0 and eje_y > 0 :
        print("El punto se encuentra en el cuadrante I. ")
    elif eje_x < 0 and eje_y > 0 :
        print("El punto se encuentra en el cuadrante II. " )
    elif eje_x < 0 and eje_y < 0 :
        print("El punto se encuentra en el cuadrante III. ")
    elif eje_x > 0 and eje_y <0 :
        print("El punto se encuentra en el cuadrante IV ")

#muestra los datos ingresados 
print("\nCoordenadas ingresadas:")
for i,(x, y) in enumerate(coordenadas, start=1):
    print(f"Punto {i}: ({x}, {y})")





