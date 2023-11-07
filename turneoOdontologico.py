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

# Crear pacientes:
juan = Paciente("12345678", "Juan", "Pérez", "+123456789", "Calle 123")
maria = Paciente("87654321", "María", "González", "+987654321", "Avenida 456")

# Agregar pacientes a la lista:
juan.agregar_paciente(juan)
juan.agregar_paciente(maria)

# Mostrar lista de pacientes:
print("Lista de pacientes:")
juan.mostrar_pacientes()

# Crear profesionales:
dr_rodriguez = Profesional("55554444", "Dr. Carlos", "Rodríguez", "+55554444", "Clínica Central")
dra_fernandez = Profesional("66667777", "Dra. Laura", "Fernández", "+66667777", "Clínica Central")

# Agregar profesionales a la lista:
dr_rodriguez.agregar_profesional(dr_rodriguez)
dr_rodriguez.agregar_profesional(dra_fernandez)

# Mostrar lista de profesionales:
print("\nLista de profesionales:")
dr_rodriguez.mostrar_profesionales()

# Crear turnos:
turno1 = Turno(juan, dr_rodriguez, "10/11/2023", "10:00 AM")
turno2 = Turno(maria, dra_fernandez, "11/11/2023", "11:00 AM")

# Agregar turnos a la lista:
turno1.agregar_turno(turno1)
turno1.agregar_turno(turno2)

# Mostrar lista de turnos:
print("\nLista de turnos:")
turno1.mostrar_turnos()

# Contar turnos registrados:
print(f"\nTotal de turnos registrados: {turno1.contar_turnos()}")