emoji_diccionario = {'feliz': '😊', 'amo':'😍', 'risa': '😂', 'sonrisa': '😊', 'llorar': '😭', 'beso': '😘', \
                     'aplauso': '👏', 'reir': '😁', 'fuego': '🔥', 'roto': '💔', 'pensando': '🤔',\
                     'maravilloso': '🤩', 'aburrido': '🥱', 'güiño': '😉', 'ok': '👌', 'abrazo': '🤗',\
                     'cool': '😎', 'enojado': '😠', 'python': '🐍'}

frase = input('Escriba una frace: ')
frase = frase.lower()
palabras = frase.split()

respuesta = ''

for palabra in palabras: 
    if palabra in emoji_diccionario:
        respuesta = respuesta + emoji_diccionario[palabra] + " "
    else:
        respuesta = respuesta + palabra + " "

print(respuesta)
