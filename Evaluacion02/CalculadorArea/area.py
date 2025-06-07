baseRectangulo = float(input("Ingrese la base del rectángulo: "))
alturaRectangulo = float(input("Ingrese la altura del rectángulo: "))
if baseRectangulo <= 0 or alturaRectangulo <= 0:
    print("Base y altura deben ser mayores que cero.")
else:
    areaRectangulo = baseRectangulo * alturaRectangulo
    print(f"El área del rectángulo es {areaRectangulo}")