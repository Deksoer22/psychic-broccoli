# contraseña
intentos = 0 
contraseña_valida = False
max_intentos = 3

while intentos < max_intentos:
    print(f"\nIntento {intentos + 1} de {max_intentos}")
    contraseña = input("Ingrese una contraseña: ")

    if not contraseña or not contraseña[0].isdigit():
        print("La contraseña debe comenzar con un número. ")
        intentos += 1
        continue

    repetir = input("Ingrese la contraseña nuevamente: ")
    
    if contraseña == repetir:
        print("Contraseña correcta")
        contraseña_valida = True 
        break

    else:
        print("La contraseña no coincide. intentalo de nuevo. ")
        intentos += 1

if not contraseña_valida:
    print("\nHas agotado tus 3 intentos. Intenta mas tarde .")
else:
    print("Acceso concedido. ")

    