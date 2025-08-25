# Probando ámbitos

titulo = 'Probando ámbitos'
suma = 10.5

def sumar():
    suma = 2 + 2
    #titulo = titulo + 'mundo' #error
    print(titulo)
    print('Suma en ámbito local:', suma, id(suma))

print('Antes de llamar a la función')
print('Suma en ámbito global:', suma,id(suma))
sumar()
print('Despues de llamar a la función sumar')
print('Suma en el ámbito global:', suma, id(suma))
