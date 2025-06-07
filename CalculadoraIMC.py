#Calculadora de IMC (Índice de Masa Corporal)
print("""         Calculadora de IMC         """) #(Calculadora de IMC)
print("Bienvenidos. Este programa le ayudara a conoces su IMC y conocer su clasificacion.") #Saludo al usuario

#Solicitar datos al usuario 
nombre = input("Por favor, ingrese su nombre: ")
apellido1 = input("Por favor, ingrese su apellido paterno: ")
apellido2 = input("Por favor, ingrese su apellido materno: ")
edad = int(input("Por favor, ingrese su edad: "))
print(f"{nombre}. vamos a calcular su IMC.")#Saludo al usuario solo con su nombre

#Solicitar peso y altura
peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("por favor, ingrese su altura en metros (ejemplo: 1.75): "))

if peso <= 0 or peso <= 0:
    print("\n Error: Los valores de peso y altura deben ser mayores a cero. ")

#Formula para calcular el IMC

imc = peso/(altura **2)

#Determinacion de clasificacion del IMC
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "sobrepeso"
else:
    categoria = "Obesidad"

    #Mostrar resultados solicitados
print("""   RESULTADOS   """)
print(f"Nombre: {nombre} {apellido1} {apellido2}")
print(f"tu edad es: {edad} años")
print(f"Tu peso es: {peso} kg")
print(f"Tu altura es: {altura} m")
print(f"Tu IMC es: {imc:.2f}")
print(f"Tu categoria es: {categoria}")
print("Recuerda que el IMC es una referencia y no reemplaza la evaluación médica profesional.")
print("Gracias por usar la calculadora de IMC. Que tenga un exelente día.")#Agradecimiento al usiario y despedida
input()