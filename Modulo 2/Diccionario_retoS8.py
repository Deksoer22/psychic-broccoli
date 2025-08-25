#Diccionario ingles y portugues
diccionario_colores = {
    'negro': {'en': 'black', 'port': 'preto'},
    'blanco' : {'en': 'white', 'port': 'branco'},
    'azul': {'en': 'blue', 'port': 'azul'},
    'rojo': {'en': 'red', 'port': 'Vermelho'},
    'verde': {'en': 'green', 'port': 'verde'},
    'amarillo': {'en': 'yellow', 'port': 'amarelo'},
    'morado': {'en': 'purple', 'port': 'roxo'},
    'naranja': {'en': 'orange', 'port': 'laranja'},
    'rosa': {'en': 'pink', 'port': 'rosa'},
    'gris': {'en': 'gray', 'port': 'cinza'},
    'dorado' : {'en': 'gold', 'port': 'dourado'},
    'violeta': {'en':'violet', 'port': 'violeta'},
    'plata': {'en': 'silver', 'port': 'prateado'},
    
}

print('🎨\n Traductor de colores (Inglés y portugués)')
frase = input('Escribe una frase con un color en español: ').lower()
idioma = input('¿Quieres la traducción en inglés o portugués? (escribe "en" o "port"): ').lower()

#Buscar el color dentro de la frace
color_detectado = None
for color in diccionario_colores:
    if color in frase:
        color_detectado = color
        break

if color_detectado:
    if idioma in diccionario_colores[color_detectado]:
        traduccion = diccionario_colores[color_detectado][idioma]
        frase_traducida = frase.replace(color_detectado, traduccion)
        print(f"Frase original: '{frase}'")
        print(f"Frase traducida: '{frase_traducida}'")
        
    else:
        print('Idioma no valido. Por favor, escribe "en" o "port". ')
else: 
    print(f"Lo siento, no reconozco un color en la frase: '{frase}'. Intenta con otro")



