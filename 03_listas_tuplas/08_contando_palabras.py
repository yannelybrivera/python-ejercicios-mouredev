
def contador_palabras(frase):
    contador= {}
    for palabra in frase.split(" "):
        if palabra in contador:
            contador[palabra] = contador[palabra] + 1
        else: 
            contador[palabra] = 1
    print(contador)
    
contador_palabras("yannely blas yannely blass")
