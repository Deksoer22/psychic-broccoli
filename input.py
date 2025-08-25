nombre = input(' ¿Cómo te llamas? ') # ¿Como te llamas? (omar)
print('Hola ' + nombre) # Hola omar
edad = input(' ¿cuantos años tienes? ') # ¿Cuantos años tienes? (28)
print(type(edad)) # class string
print(f' {nombre} tiene {edad} años') # Omar tiene 27 años 

# Programa que pide dos numeros al usuario
numero1 = int(input(' introduce un numero por favor: '))
numero2 = int(input('introduce otro numero por favor: '))
numero3 = numero1 + numero2

print(f'El resultado de la suma es {numero3}')
