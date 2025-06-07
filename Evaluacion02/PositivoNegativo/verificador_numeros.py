def verificar_numeros(numero):

    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"
    
if __name__ == '__main__':

        numero_ingresado = int(input("Ingrese un número: "))
        
        resultado = verificar_numeros(numero_ingresado)
        
        print(f"El número es {resultado}.")