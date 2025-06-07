try:
    from rut import validar_rut
except ImportError:
    print("El archivo rut.py no se pudo importar.")
    
    def validar_rut(rut):
        print(f"No se pudo verificar el RUT: {rut}")
        return True 

class ClienteGimnasio:
   
    def __init__(self, nombreCompleto, rut, edad, peso, estatura, correoElectronico):
        self.nombreCompleto = str(nombreCompleto)
        self.rut = str(rut)
        self.edad = int(edad)
        self.peso = float(peso)
        self.estatura = float(estatura)
        self.correoElectronico = str(correoElectronico)

    # Getters
    def get_nombreCompleto(self):
        return self.nombreCompleto
    
    def get_rut(self):
        return self.rut
        
    def get_edad(self):
        return self.edad
        
    def get_peso(self):
        return self.peso
        
    def get_estatura(self):
        return self.estatura
        
    def get_correoElectronico(self):
        return self.correoElectronico
    
    # Setters 
    def set_nombreCompleto(self, ingreseNombre):
        self.nombreCompleto = ingreseNombre
    
    def set_rut(self, ingreseRut):
        self.rut = ingreseRut
    
    def set_edad(self, ingreseEdad):
        self.edad = ingreseEdad
    
    def set_peso(self, ingresePeso):
        self.peso = ingresePeso
    
    def set_estatura (self, ingreseEstatura):
        self.estatura = ingreseEstatura

    def set_correoElectronico(self, ingreseCorreo):
        self.correoElectronico = ingreseCorreo

    # Método Customer
    def calculadoraIMC(self):
        #Calculadora de IMC
        if self.estatura <= 0:
            return 0  
    
        imc = self.peso / (self.estatura ** 2)
        return round(imc, 2)

    def clasificarCondicion(self):
        #Clasifica la condición del cliente segun su IMC.
        imc = self.calculadoraIMC()
        if imc >= 30:
            return "Obesidad"
        elif imc >= 25:
            return "Sobrepeso"ads
        elif imc >= 18.5:
            return "Normal"
        elif imc > 0:
            return "Bajo peso"
        else:
            return "Datos no válidos"

def ingresar_y_validar_cliente():
    # Solicitar datos al usuario
    nombreCompleto = input("Nombre: ")
    rut = input("RUT: ")
    edad_str = input("Edad: ")
    peso_str = input("Peso (en kg, ej: 70.5): ")
    estatura_str = input("Estatura (en metros, Utilice formato 'A dos decimales'  EJEMPLO : 1.75): ")
    correo = input("Correo: ")
    
    # Validar RUT
    if not validar_rut(rut):
        print("\nError: El RUT ingresado es inválido.")
        return None
    
    # Formato y validación de datos 
    try:
        edad = int(edad_str)
        peso = float(peso_str)
        estatura = float(estatura_str)
        if edad <= 0 or peso <= 0 or estatura <= 0:
            print("\nError: Datos de condición física (edad, peso, estatura) deben ser mayores a cero.")
            return None
    except ValueError:
        print("\nError: Edad, peso y estatura deben ser valores numéricos.")
        return None

    # Creación del objeto cliente
    cliente = ClienteGimnasio(nombreCompleto, rut, edad, peso, estatura, correo)
    return cliente

def resumen(cliente, IMC, condicion, rut_es_valido_str, cumple_req_str):
    resumen_str = (
        "\n--- Resumen del Cliente ---\n"
        "-------------------------\n"
        f"a. Nombre: {cliente.get_nombreCompleto()}\n"
        f"   RUT: {cliente.get_rut()}\n"
        f"   Edad: {cliente.get_edad()} años\n"
        f"   Peso: {cliente.get_peso()} Kilogramos\n"
        f"   Correo: {cliente.get_correoElectronico()}\n"
        f"   Estatura: {cliente.get_estatura()} Metros\n"
        f"   Índice de Masa Corporal: {IMC}\n"
        f"   Condición física: {condicion}\n"
        f"d. Validación del RUT: {rut_es_valido_str}\n"
        f"   Cumple Requisitos: {cumple_req_str}\n"
        "-------------------------"
    )
    return resumen_str

# Input Registro de Cliente nuevo
if __name__ == "__main__":
    print("--- Registro de Nuevo Cliente de Gimnasio ---")
    
    # Llama a la función para ingresar y validar los datos del cliente.
    cliente_nuevo = ingresar_y_validar_cliente()

    #  Procede solo si el cliente fue creado exitosamente.
    if cliente_nuevo:
        #  métodos del objeto para obtener condicion fisica.
        IMC = cliente_nuevo.calculadoraIMC()
        condicion = cliente_nuevo.clasificarCondicion()
        
        # Resumen 
        rut_es_valido_str = "Válido"
        cumple_req_str = "Sí" if IMC >= 0 else "No (datos incorrectos)"
        informe_final = resumen(cliente_nuevo, IMC, condicion, rut_es_valido_str, cumple_req_str)
        print(informe_final)
    else:
        # Mensaje en caso de que la creación del cliente falle.
        print("\nPor favor, intente de nuevo.")
        
        
        
        #