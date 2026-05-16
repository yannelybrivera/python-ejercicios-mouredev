def binario(decimal):
    modulo = (decimal % 2)
    residuo = 0
    resultado = ""
    while decimal > 0:
        residuo = decimal % 2
        decimal = decimal // 2
        resultado = str(residuo) + resultado
    print(resultado)

binario(2) 