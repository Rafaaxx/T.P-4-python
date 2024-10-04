# Verificar existencia de un elemento

def verifyExists(tupla, palabra):
    if palabra in tupla:
        print(palabra + ' encontrado en la tupla')
    else:
        print(palabra + ' no existe en la tupla')


colores = ("rojo", "verde", "azul", "amarillo")
verifyExists(colores, "morado")
verifyExists(colores, "azul")