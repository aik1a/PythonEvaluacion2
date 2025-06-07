def calcular_pares(inicio, fin):
    contador = 0
    if inicio > fin:
        return 0
        
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            contador += 1
    return contador


if __name__ == '__main__':
        numero_inicio = int(input("Ingrese el número inicial: "))
        numero_fin = int(input("Ingrese el número final: "))
        
        cantidad_pares = calcular_pares(numero_inicio, numero_fin)
        
        print(f"Hay {cantidad_pares} números pares entre {numero_inicio} y {numero_fin}.")
