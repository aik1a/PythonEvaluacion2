def numeroIngresado():
    numeroIngresado = (input(int("Ingrese un número: ")))
    if numeroIngresado > 0:
        print("El número es positivo.")
    elif numeroIngresado < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")