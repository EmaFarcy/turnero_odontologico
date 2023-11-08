#Aquí creamos el menú de opciones para el usuario:
from turneoOdontologico import Clinica

def menu():
    while opcion < 1 or opcion > 8:  
        print("\nBienvenido al sistema de turnos de la Clínica Odontológica")
        print("1. Registrar un nuevo paciente")
        print("2. Registrar un nuevo profesional")
        print("3. Registrar un nuevo turno")
        print("4. Mostrar listado de pacientes")
        print("5. Mostrar listado de profesionales")
        print("6. Mostrar listado de turnos")
        print("7. Dar de baja un turno")
        print("8. Salir")
        opcion = int(input("Ingrese la opción deseada: "))
        return opcion
    
