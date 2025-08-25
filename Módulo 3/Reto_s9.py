def letras_vecinas(letra):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    letra_mayuscula = letra.isupper()
    letra_minuscula = letra.lower()

    if letra_minuscula in alfabeto:
        indice = alfabeto.index(letra_minuscula)
        anterior = alfabeto[indice - 1] if indice > 0 else 'No existe letra anterior'
        siguiente = alfabeto[indice + 1] if indice < len(alfabeto) - 1 else 'No existe letra siguiente'

        if letra_mayuscula:
            anterior = anterior.upper() if 'No existe' not in anterior else anterior
            siguiente = siguiente.upper() if 'No existe' not in siguiente else siguiente
            letra = letra.upper()

        
        print(f'Letra ingresada: {letra}')    
        print(f'Orden las letras: {anterior},{letra}, {siguiente}')
    else:
        print('El caracter ingresado no es una letra del alfabeto')

while True:
    entrada = input('Escriba una letra del alfabeto (ejemplo: ñ) o escriba "salir" para terminar el programa: ')
    if entrada.lower() == "salir":
        print('Adios, programa terminado. ')
        break
    elif len(entrada) == 1:
        letras_vecinas(entrada)
    else:
        print('Por favor, solo ingrese una letra del alfabeto. ')

