
numeroInicio = int(input("Ingrese el número inicial: "))
numeroFin = int(input("Ingrese el número final: "))
contadorNumerosPares = 0
for numeroActual in range(numeroInicio, numeroFin + 1):
    if numeroActual % 2 == 0:
        contadorNumerosPares += 1
print(f"Hay {contadorNumerosPares} números pares entre {numeroInicio} y {numeroFin}.")