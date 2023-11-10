from abb import ArbolBinarioBusqueda

class Persona: #Creo la clase Persona.
    def __init__(self, dni, nombre, apellido, contacto, direccion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.contacto = contacto
        self.direccion = direccion
    
    def __str__(self): # Método __str__ para mostrar los datos de la persona.
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"
    

class Paciente(Persona): #Creo la clase Paciente.
    def __init__(self, dni, nombre, apellido, contacto, direccion, obra_social):
        super().__init__(dni, nombre, apellido, contacto, direccion)
        self.obra_social = obra_social


class Profesional(Persona): #Creo la clase Profesional.
    def __init__(self, dni, nombre, apellido, contacto, direccion):
        super().__init__(dni, nombre, apellido, contacto, direccion) #Profesional es una subclase que hereda de Persona. Utilizo el super() para heredar los atributos de la clase padre.


class Turno: #Creo la clase Turno.
    def __init__(self, paciente, profesional, fecha, hora):
        self.paciente = paciente
        self.profesional = profesional
        self.fecha = fecha
        self.hora = hora


class Clinica:
    self.lista_pacientes = ArbolBinarioBusqueda()
    self.lista_profesionales = ArbolBinarioBusqueda()
    self.lista_turnos = ArbolBinarioBusqueda()

    def alta_paciente(self):
            pass

    def alta_profesional(self):
            pass

    def alta_turno(self):
            pass

    def ver_paciente(self):
            pass

    def ver_profesional(self):
            pass

    def ver_turno(self):
            pass

    def baja_paciente(self):
            pass

    def baja_profesional(self):
            pass

    def baja_turno(self):
            pass

'''
class Clinica:
        lista_pacientes = ArbolBinarioBusqueda()
		lista_profesionales = ArbolBinarioBusqueda()
        lista_turnos = ArbolBinarioBusqueda()

	def mostrar_turno_paciente(contar turnos asignados a un paciente):

	def mostrar_turno_profesional (conteo de cuantos turnos tiene un profeesional).
	
	def mostar_turnosdeldia

	def (buscar turno)
	
	def (alta de pacientes, profesional,turnos)

	def (baja de pacientes,profesional,turnos)

	def(modificar pacientes,profesional,turnos)

    def(probando git)
'''