def calcularArea(polygon):
    if polygon["tipo"] == "T":
        base = polygon["base"]
        altura = polygon["altura"]
        return (base* altura)/2
    elif polygon["tipo"] == "C":
        lado = polygon["lado"]
        return lado**2
    elif polygon["tipo"] == "R":
        base = polygon["base"]
        altura = polygon["altura"] 
        return base * altura

print("Area del triangulo: ", calcularArea({ "tipo": "T", "base": 5, "altura": 3 }))
print("Area del cuadrado: ", calcularArea({ "tipo": "C", "lado": 4 }))
print("Area del rectangulo: ", calcularArea({ "tipo": "R", "base": 6, "altura": 2 }))