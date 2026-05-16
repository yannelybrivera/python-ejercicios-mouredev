def invertir():
    palabra = str(input("Escriba: "))
    revertido = ""
    for letra in palabra:
        revertido = letra + revertido
    print(revertido)
invertir()