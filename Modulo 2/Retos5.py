print("Hola, Bienvenido a la calculadora de años transcurridos.")

año_actual = input("Introduce el año actual: ")
año_2 = input("Introduce otro año para calcular los años transcurridos: ")

if año_actual.isnumeric() and año_2.isnumeric():
    año_actual = int(año_actual)
    año_2 = int(año_2)
    
    if año_actual == año_2:
        print("Ambos años son iguales, no ha pasado ningún año.")
    elif año_actual > año_2:
        print(f"Han pasado {año_actual - año_2} años desde {año_2} hasta {año_actual}. ")
    elif año_actual < año_2:
        print(f"Faltan {año_2 - año_actual} años para llegar a {año_2} desde {año_actual}. ")
else:
    print("Dato incorrecto. Debes ingresar solo números.")




