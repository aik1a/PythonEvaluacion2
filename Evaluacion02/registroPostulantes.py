# Se intenta importar la función desde el archivo rut.py
try:
    from rut import validar_rut
except ImportError:
    print("El archivo rut.py no se pudo importar ")
    # por si la importación falla 
    def validar_rut(rut):
        print("Usando validador de RUT de respaldo: no se pudo verificar el RUT.")
        return False

class Postulante:
    def __init__(self, nombreCompleto, Rut, edad, correoElectronico, aniosExperiencia, pretensionSalarial, conocimientoPy):
        self.nombreCompleto = nombreCompleto
        self.Rut = Rut
        self.edad = edad
        self.correoElectronico = correoElectronico
        self.aniosExperiencia = aniosExperiencia
        self.pretensionSalarial = pretensionSalarial
        self.conocimientoPy = conocimientoPy

    # Getters
    def get_nombreCompleto(self):
        return self.nombreCompleto

    def get_rut(self):
        return self.Rut

    def get_edad(self):
        return self.edad

    def get_correoElectronico(self):
        return self.correoElectronico

    def get_aniosExperiencia(self):
        return self.aniosExperiencia

    def get_conocimientoPy(self):
        return self.conocimientoPy

    def get_pretensionSalarial(self):
        return self.pretensionSalarial

    # Setters
    def set_nombreCompleto(self, ingreseNombre):
        self.nombreCompleto = ingreseNombre

    def set_rut(self, ingreseRut):
        self.Rut = ingreseRut

    def set_edad(self, ingreseEdad):
        self.edad = ingreseEdad

    def set_correoElectronico(self, ingreseCorreo):
        self.correoElectronico = ingreseCorreo

    def set_aniosExperiencia(self, ingreseAniosExp):
        self.aniosExperiencia = ingreseAniosExp

    def set_pretensionSalarial(self, ingresePretensionSalarial):
        self.pretensionSalarial = ingresePretensionSalarial

    def set_conocimientoPy(self, tienePy):
        self.conocimientoPy = True if tienePy == "si" else False
        

    # Método Customer 
    def cumpleRequisitos(self):
        # Verifica Experiencia 
        if not isinstance(self.aniosExperiencia, (int, float)) or self.aniosExperiencia < 2:
            return False

        # Verifica si es mayor de edad 
        if not isinstance(self.edad, int) or self.edad < 18:
            return False

        # Verifica conocimientos en Python
        if not isinstance(self.conocimientoPy, str) or "si" not in self.conocimientoPy.lower():
            return False
            
        return True

    
    def esRutValido(self):
        
        if not (self.Rut, str) or not self.Rut:
            return False
        
        return validar_rut(self.Rut)

    # print __str__ para mostrar la información del postulante
    def __str__(self):
        rut_es_valido_str = "Sí" if self.esRutValido() else "No"
        cumple_req_str = "Sí" if self.cumpleRequisitos() else "No"
        
      #formato salario
        pretension_formateada = f"${self.pretensionSalarial:}".replace(",", ".")

        resumen = (
            f"Resumen del Postulante:\n"
            f"-------------------------\n"
            f"a. Nombre: {self.get_nombreCompleto()}\n"
            f"   RUT: {self.get_rut()}\n"
            f"   Edad: {self.get_edad()} años\n"
            f"   Correo: {self.get_correoElectronico()}\n"
            f"b. Años de Experiencia: {self.get_aniosExperiencia()}\n"
            f"   Posee Conocimientos en Python: {self.get_conocimientoPy().capitalize()}\n"
            f"c. Pretensión Salarial: {pretension_formateada}\n"
            f"d. Validación del RUT: {rut_es_valido_str}\n"
            f"   Cumple Requisitos: {cumple_req_str}\n"
            f"-------------------------"
        )
        return resumen

# Ejemplo de Uso
if __name__ == "__main__":
    # Postulante para Prueba
    postulante = Postulante(
        nombreCompleto="Aikia Riveros",
        Rut="20882980k",  
        edad=23,
        correoElectronico="aikia100@mail.com",
        aniosExperiencia=4,
        pretensionSalarial=1200000,
        conocimientoPy="si"  
    )
    # EN ESTE CASO DE EJEMPLO QUE COLOQUE POR DEFECTO Deberia arrojar error de rut solamente ;) debido a digito verificador incorrecto
    print(postulante)
    