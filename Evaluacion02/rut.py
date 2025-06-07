#Herramienta creada por el usuario / programador mapachito dev en Github 

from itertools import cycle

def verificar_formato(rut_str):
    """
    Verifica que la cadena del RUT contenga solo los caracteres permitidos.
    Esta función espera un string ya limpio (sin puntos ni guion).
    """
    if not rut_str:
        return False
    
    cuerpo = rut_str[:-1]
    dv = rut_str[-1]

    # El cuerpo (antes del guion) debe contener solo dígitos
    if not cuerpo.isdigit():
        return False
    
    # El dígito verificador debe ser un número (0-9) o la letra 'K'
    if not (dv.isdigit() or dv == 'K'):
        return False
        
    return True

def validar_rut(rut):
    """
    Valida un RUT chileno, primero verificando el formato y luego el dígito verificador.
    Retorna True si es válido, False en caso contrario.
    """
    if not isinstance(rut, str):
        return False

    # Limpiar el RUT de espacios, puntos y guiones, y convertir a mayúsculas
    rut_limpio = rut.strip().upper().replace(".", "").replace("-", "")

    # 1. Se verifica el formato (solo números y K) antes de continuar
    if not verificar_formato(rut_limpio):
        return False

    rut_aux = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]

    # 2. Cálculo del dígito verificador
    try:
        revertido = map(int, reversed(rut_aux))
        factors = cycle(range(2, 8))
        suma = sum(d * f for d, f in zip(revertido, factors))
        residuo = suma % 11
    except ValueError:
        # Esto no debería ocurrir si verificar_formato funciona, pero es una protección
        return False

    # 3. Comparar con el dígito verificador esperado
    dv_calculado = 11 - residuo
    
    if dv_calculado == 11:
        dv_esperado = '0'
    elif dv_calculado == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(dv_calculado)

    return dv_ingresado == dv_esperado

def main():
    """
    Función principal para probar la validación desde la consola.
    Proporciona mensajes de error específicos para formato o dígito verificador incorrecto.
    """
    rut_usuario = input("Ingrese un RUT para validar: ")

    # Se realiza una verificación de formato previa para poder dar un mensaje específico
    rut_limpio_para_test = rut_usuario.strip().upper().replace(".", "").replace("-", "")
    
    if not verificar_formato(rut_limpio_para_test):
        print("\nFormato inválido.")
        print("El RUT debe contener solo números (0-9) y terminar con un número o la letra 'K'.")
        print("Los puntos y el guion son opcionales.")
    elif validar_rut(rut_usuario):
        print("\nEl RUT ingresado es VÁLIDO.")
    else:
        # Si el formato es correcto pero la validación falla, es por el dígito verificador.
        print("\nEl RUT tiene un formato correcto, pero el dígito verificador es INVÁLIDO.")

if __name__ == "__main__":
    main()