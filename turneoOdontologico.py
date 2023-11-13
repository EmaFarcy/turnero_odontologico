from abb import ArbolBinarioBusqueda

class Persona: #Creo la clase Persona.
    def __init__(self, dni, nombre, apellido, contacto, direccion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.contacto = contacto
        self.direccion = direccion
    
    def __lt__(self, other): # x<y llama x.__lt__(y) 
        return self.dni<other.dni
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.dni<=other.dni
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.dni==other.dni
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.dni!=other.dni
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.dni>other.dni
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.dni>=other.dni
    
    def __str__(self): # Método __str__ para mostrar los datos de la persona.
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}- Contacto: {self.contacto} - Dirección: {self.direccion}" \
            .format(self.nombre, self.apellido, self.dni, self.contacto, self.direccion) #Retorno los datos de la persona.
    
    

class Paciente(Persona): #Creo la clase Paciente. #utilizo el arbol binario de busqueda (ABB)
    def __init__(self, dni, nombre, apellido, contacto, direccion):
        super().__init__(dni, nombre, apellido, contacto, direccion)

    def __str__(self):
        return f"Paciente: {self.nombre} - Apellido: {self.apellido} - Contacto: {self.contacto} - Dirección: {self.direccion} " \
            .format(self.nombre, self.apellido, self.contacto, self.direccion)
class Profesional(Persona): #Creo la clase Profesional.
    def __init__(self, dni, nombre, apellido, contacto, direccion, especialidad):
        super().__init__(dni, nombre, apellido, contacto, direccion)#Profesional es una subclase que hereda de Persona. Utilizo el super() para heredar los atributos de la clase padre.
        self.especialidad = especialidad

    def __str__(self):
        return f"Nombre del profesional: {self.nombre} - Apellido: {self.apellido} - Especialidad: {self.especialidad} - " \
            .format(self.nombre, self.apellido, self.especialidad)



class Turno: #Creo la clase Turno.
    def __init__(self, paciente, profesional, dato):
        self.paciente = paciente
        self.profesional = profesional
        self.dato = dato
        
    
    def __str__(self):
        return f"Paciente: {self.paciente} - Profesional: {self.profesional} - Fecha y hora: {self.dato} - " \
            .format(self.paciente, self.profesional, self.dato)
        
    def __lt__(self, other):
            return self.fecha<other.fecha
        
    def __le__(self, other):
            return self.fecha<=other.fecha
        
    def __eq__(self, other):
            return self.fecha==other.fecha
        
    def __ne__(self, other):
            return self.fecha!=other.fecha
        
    def __gt__(self, other):
            return self.fecha>other.fecha
        
    def __ge__(self, other):
            return self.fecha>=other.fecha

class Clinica:
    def __init__(self):
        self.pacientes = ArbolBinarioBusqueda()
        self.profesionales = ArbolBinarioBusqueda()
        self.turnos = ArbolBinarioBusqueda()
        self.lista_pacientes = []
        self.lista_profesionales = []
        self.lista_turnos = []
    
    def contiene_paciente(self, dni): #Verifico si el paciente ya se encuentra registrado.
        return dni in self.pacientes
    
    def buscar_paciente(self,dnipaciente):
        self.pacientes.__contains__(dnipaciente)

    def busqueda_individual(self,dnipaciente):
        self.pacientes.__getitem__(dnipaciente) 
    
    def alta_nuevo_paciente(self, paciente): #Agrego un nuevo paciente a la lista de pacientes.
        self.pacientes.agregar(paciente.dni, paciente) #paciente.dni es la clave y paciente es el valor asociado a la clave.
        
    def mostrar_pacientes(self):
        self.pacientes.inorden()   
   
    def contiene_profesional(self, dni): #Verifico si el profesional ya se encuentra registrado.
        return dni in self.profesionales
    
    def alta_nuevo_profesional(self, profesional): #Agrego un nuevo profesional a la lista de profesionales.
        self.profesionales.agregar(profesional.dni, profesional)

    def buscar_profesional(self,dniprofesional):
        self.pacientes.__contains__(dniprofesional)

    def busqueda_individual_profesional(self,dniprofesional):
         self.profesionales.__getitem__(self,dniprofesional)

    def  mostrar_profesionales(self):
        self.profesionales.inorden()
    
    def contiene_turno(self, fecha): #Verifico si el turno ya se encuentra registrado.
        return fecha in self.turnos
    
    def registrar_turno(self, turno): #Agrego un nuevo turno a la lista de turnos.
        self.turnos.agregar(turno.dato, turno) #TAREA: Comparar fecha y hora.
    
    def mostrar_turnos(self):
        self.turnos.inorden()

    def busqueda_individual_turno(self,dato):
         self.profesionales.__getitem__(self,dato)
    
    def eliminar_turno(self, turno): #Elimino un turno de la lista de turnos.
        self.turnos.eliminar(turno.dato) #TAREA: Comparar fecha y hora.


def seleccionar_especialidad(self): #Selecciono la especialidad odontológica.
        print("Seleccione la especialidad odontológica:")
        print("1. Ortodoncia - Dr. Carlos Martínez")
        print("2. Odontopediatría - Dra. Ana Gómez")
        print("3. Endodoncia - Dr. Jorge Pérez")
        print("4. Periodoncia - Dra. Laura Rodríguez")
        opcion = int(input("Ingrese su opción: "))

        especialidades = { #Creo un diccionario con las especialidades odontológicas y los profesionales asignados a cada una.
            1: ("Ortodoncia", "Dr. Carlos Martínez"),
            2: ("Odontopediatría", "Dra. Ana Gómez"),
            3: ("Endodoncia", "Dr. Jorge Pérez"),
            4: ("Periodoncia", "Dra. Laura Rodríguez")
        }

        especialidad, especialista = especialidades.get(opcion, (None, None)) #Obtengo la especialidad y el especialista asignado a la especialidad seleccionada.
        if especialidad:
            print(f"Ha seleccionado {especialidad}. El especialista asignado es {especialista}.")
        else:
            print("Opción no válida.")