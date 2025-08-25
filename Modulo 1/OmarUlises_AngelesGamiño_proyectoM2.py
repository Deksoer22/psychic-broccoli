#Programa para solicitar una palabra 
print("\n Bienvendio")

#Lista para guardar las palabras ingresadas
palabras_ingresadas = []

while True:
    palabra = input("ingrese una palabra entre 4 y 8 letras: ").strip()
    numero_de_letras = len(palabra)

#Guarda la palabra ingresada
    palabras_ingresadas.append(palabra)

#Aqui valida la longitud de la palabra
    if 4 <= numero_de_letras <= 8:
        print(f"La palabra '{palabra}' es correcta. Tiene {numero_de_letras} letras. ")
        break
    if numero_de_letras < 4:
        print(f"Hacen falta letras. '{palabra}' solo tiene {numero_de_letras} letras. ")
    else:
        print(f"Sobran letras. '{palabra}' tiene {numero_de_letras} letras. ")

#Muestra la palabra escrita con el cuadrante al que pertenece 
    print("\n Palabra que ingresaste: ")
    for i, palabras in enumerate(palabras_ingresadas, start=1):
        print(f"{i}. {palabra}")

################################################################################################################

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