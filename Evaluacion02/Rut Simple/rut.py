rutIngresado = input("Ingrese su RUT sin dígito verificador (8 digitos): ")
if len(rutIngresado) == 8 and rutIngresado.isdigit():
    print("RUT valido")
else:
    print("RUT invalido")