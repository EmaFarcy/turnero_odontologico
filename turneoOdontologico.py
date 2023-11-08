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
    lista_pacientes = []
    
    def agregar_paciente(self, paciente): #Agrego un paciente a la lista de pacientes.
        Paciente.lista_pacientes.append(paciente)
    
    def mostrar_pacientes(self): #Muestro la lista de pacientes.
        for paciente in self.lista_pacientes:
            print(paciente)


class Profesional(Persona): #Creo la clase Profesional.
    def __init__(self, dni, nombre, apellido, contacto, direccion):
        super().__init__(dni, nombre, apellido, contacto, direccion) #Profesional es una subclase que hereda de Persona. Utilizo el super() para heredar los atributos de la clase padre.
        self.lista_profesionales = []
    
    def agregar_profesional(self, profesional): #Agrego un profesional a la lista de profesionales.
        self.lista_profesionales.append(profesional)

    def mostrar_profesionales(self):
        for profesional in self.lista_profesionales: #Recorro la lista de profesionales y muestro cada uno.
            print(profesional)


class Turno: #Creo la clase Turno.
    def __init__(self, paciente, profesional, fecha, hora):
        self.paciente = paciente
        self.profesional = profesional
        self.fecha = fecha
        self.hora = hora
        self.lista_turnos = []

    def agregar_turno(self, turno): #Agrego un turno a la lista de turnos.
        self.lista_turnos.append(turno)

    def contar_turnos(self):
        return len(self.lista_turnos) #Retorno la cantidad de turnos registrados.

    def mostrar_turnos(self):
        for turno in self.lista_turnos: #Recorro la lista de turnos y muestro cada uno.
            print(f"Paciente: {turno.paciente} - Profesional: {turno.profesional} - Fecha: {turno.fecha} - Hora: {turno.hora}") 


'''
class Clinica:
        pacientes (ABB)
		profesionales (ABB)
		lista turnos (ABB)

	def mostrar_turno_paciente(contar turnos asignados a un paciente):

	def mostrar_turno_profesional (conteo de cuantos turnos tiene un profeesional).
	
	def mostar_turnosdeldia

	def (buscar turno)
	
	def (alta de pacientes, profesional,turnos)

	def (baja de pacientes,profesional,turnos)

	def(modificar pacientes,profesional,turnos)
'''