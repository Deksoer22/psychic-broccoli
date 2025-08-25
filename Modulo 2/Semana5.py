entrada = input("¡Hola! Introduce tu edad:")

if entrada.isnumeric():
    edad = int(entrada)
    if edad <= 0:
        print("WOOOWW!!!! que joven eres. pero, lo siento eso no es posible.")
    elif edad > 115:
        print("Vaya!!!!!! ¿Como le haces para vivir tanto? No te creo, mejor intenta de nuevo.")
    elif edad < 18:
        print("Eres menor de edad así que no puedes comprar los cigarros.")
    else:
        print("Eres mayor de edad. Aquí tienes tus cigarros.")
else:
    print("Dato incorrecto. Debes introducir un número.")