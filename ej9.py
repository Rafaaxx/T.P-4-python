#Contar palabras en un texto

def countWords(string):
    contador = {}
    obj = string.split(' ')
    for palabra in obj:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    print(contador)

texto = "manzana naranja manzana pera pera pera naranja manzana"

countWords(texto)