#Ingresar los Asserts
from turneoOdontologico import Persona, Paciente, Profesional, Turno, Clinica
from datetime import datetime

def test_persona_comparacion(): #Testeo la comparación entre dos personas.
    persona1=Persona(29475561, "Juan", "Pérez", "123456789", "Calle 123")
    persona2=Persona(33504912, "Ana", "González", "123456789", "Calle 456")
    assert persona1<persona2 #Testeo el menor
    assert persona2>persona1 #Testeo el mayor

def test_persona_str(): #Testeo el método str de la clase Persona.
    persona= Persona(12345678, "Juan", "Pérez", "123456789", "Calle 123") #Creo una persona.
    assert str(persona) == "Juan Pérez - DNI: 12345678- Contacto: 123456789 - Dirección: Calle 123" #Testeo el método str.

def test_creacion_paciente(): #Testeo la creación de un paciente.
    paciente= Paciente(12345678, "Marcos", "Juarez", "123456789", "Calle 123") #Creo un paciente.
    assert paciente.dni == 12345678 #Testeo los atributos del paciente.
    assert paciente.nombre == "Marcos" 
    assert paciente.apellido == "Juarez"
    assert paciente.contacto == "123456789"
    assert paciente.direccion == "Calle 123"

def test_creacion_profesional(): #Testeo la creación de un profesional.
    profesional= Profesional(23456789, "Ana", "Sanchez", "4562899", "Avenida Siempre Viva 742", "Odontología General")
    assert profesional.dni == 23456789
    assert profesional.nombre == "Ana"
    assert profesional.apellido == "Sanchez"
    assert profesional.especialidad == "Odontología General"
    assert profesional.direccion == "Avenida Siempre Viva 742"

def test_creacion_turno(): #Testeo la creación de un turno.
    paciente= Paciente(12345678, "Marcos", "Juarez", "123456789", "Calle 123")
    profesional = Profesional(23456789, "Roberto", "Sanchez", "4562899", "Calle 123", "Odontólogo")
    fecha_turno= datetime(2021, 11, 10, 10, 0, 0)
    turno= Turno(paciente, profesional, fecha_turno)
    assert turno.paciente == paciente
    assert turno.profesional == profesional
    assert turno.dato == fecha_turno

def test_busqueda_turno(): #Testeo la creación de un turno.
    paciente= Paciente(12345678, "Marcos", "Juarez", "123456789", "Calle 123")
    profesional = Profesional(23456789, "Roberto", "Sanchez", "4562899", "Calle 123", "Odontólogo")
    fecha_turno= datetime(2021, 11, 10, 10, 0, 0)
    turno= Turno(paciente, profesional, fecha_turno)
    clinica = Clinica()
    clinica.alta_nuevo_paciente(paciente)
    clinica.alta_nuevo_profesional(profesional)
    clinica.registrar_turno(turno)
    turno2 = clinica.busqueda_individual_turno(fecha_turno)
    assert turno == turno2

def run_tests(): #Ejecuto los tests.
    test_persona_comparacion()
    test_persona_str()
    test_creacion_paciente()
    test_creacion_profesional()
    test_creacion_turno()
    test_busqueda_turno()

if __name__ == "__main__": #Ejecuto la función run_tests().
    run_tests()