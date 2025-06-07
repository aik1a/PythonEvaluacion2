def multiplicar(base, altura):
    return base * altura
if __name__ == '__main__':
    base_rectangulo = float(input("Ingrese la base del rectángulo: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
    
    if base_rectangulo <= 0 or altura_rectangulo <= 0:
        print("Base y altura deben ser mayores que cero.")
    else:
        area = multiplicar(base_rectangulo, altura_rectangulo)
        print(f"El área del rectángulo es {area}")