def validar_rut(rutIngresado):

    if len(rutIngresado) == 8 and rutIngresado.isdigit():
        return True
    else:
        return False
if __name__ == '__main__':
    rut_ingresado = input("Ingrese su RUT sin digito verificador (8 digitos): ")
    
    if validar_rut(rut_ingresado):
        print("RUT valido")
    else:
        print("RUT invalido")