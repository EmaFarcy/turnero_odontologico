#Aquí creamos el menú de opciones para el usuario:
from turneoOdontologico import Paciente, Profesional, Turno, Clinica

def menu():
    opcion = 0
    while opcion < 1 or opcion > 9:
        print("--")  
        print("\nBienvenido al sistema de turnos de la Clínica Odontológica")
        print("1. Registrar un nuevo paciente")
        print("2. Registrar un nuevo profesional")
        print("3. Registrar un nuevo turno")
        print("4. Mostrar listado de pacientes")
        print("5. Mostrar listado de profesionales")
        print("6. Mostrar listado de turnos")
        print("7. Dar de baja un turno")
        print("8. Seleccionar una especialidad")
        print("9. Salir")
        print("--")
        opcion = int(input("Ingrese la opción deseada: "))
    return opcion

def run(turneoOdontologico):
    opcion = 0
    while opcion != 9:
        opcion = menu()
        if opcion == 1: #Acá tengo que agregar el paciente a la lista de pacientes.
            nombre = input("Ingrese el nombre del paciente: ")
            apellido = input("Ingrese el apellido del paciente: ")
            dni = int(input("Ingrese el DNI del paciente: "))
            contacto = input("Ingrese el número de contacto del paciente: ")
            direccion = input("Ingrese la dirección del paciente: ")
            paciente = Paciente(dni, nombre, apellido, contacto, direccion)
            if turneoOdontologico.contiene_paciente(paciente.dni):
                print("El paciente ya se encuentra registrado")
            else:
                turneoOdontologico.alta_nuevo_paciente(paciente)
                print("¡Paciente registrado con éxito!")
            input("Presione Enter para continuar...")
            
        elif opcion == 2: #Acá tengo que agregar el profesional a la lista de profesionales.
            nombre = input("Ingrese el nombre del profesional: ")
            apellido = input("Ingrese el apellido del profesional: ")
            dni = int(input("Ingrese el DNI del profesional: "))
            contacto = input("Ingrese el número de contacto del profesional: ")
            direccion = input("Ingrese la dirección del profesional: ")
            profesional = Profesional(dni, nombre, apellido, contacto, direccion)
            if turneoOdontologico.contiene_profesional(profesional.dni):
                print("El profesional ya se encuentra registrado")
            else:
                turneoOdontologico.alta_nuevo_profesional(profesional)
                print("¡Profesional registrado con éxito!")
            input("Presione Enter para continuar...")    
        
        elif opcion == 3: #Se registra un nuevo turno #TAREA: COMPROBAR QUE PROFESIONAL Y PACIENTE ESTÉN REGISTRADOS.
                          #TAREA: Que se pueda registar un nuevo turno en la misma fecha pero en diferente hora.
            dni_paciente = int(input("Ingrese el DNI del paciente: "))
            paciente = turneoOdontologico.contiene_paciente(dni_paciente)
            if paciente is None:
                print("El paciente no se encuentra registrado")
            else: 
                dni_profesional = int(input("Ingrese el DNI del profesional: "))
                profesional = turneoOdontologico.contiene_profesional(dni_profesional)
                if profesional is None:
                    print("El profesional no se encuentra registrado")
                    input("Presione Enter para continuar...")
                else:
                    fecha = input("Ingrese la fecha del turno: ")
                    hora = input("Ingrese la hora del turno: ")
                    turno = Turno(paciente, profesional, fecha, hora)
                    if turneoOdontologico.contiene_turno(turno.fecha):
                        print("El turno ya se encuentra registrado") #Tarea: VER SI FUNCIONA
                    else:
                        turneoOdontologico.registrar_turno(turno)
                        print("¡Turno registrado con éxito!")
                    input("Presione Enter para continuar...") 
        
        elif opcion == 4: #Mostrar lista de pacientes
            turneoOdontologico.pacientes.inorden() #Tarea: lLAMAR AL MÉTODO mostrar_pacientes
            input("Presione Enter para continuar...")            
        elif opcion == 5: #Mostrar lista de profesionales
            turneoOdontologico.profesionales.inorden() #Tarea: Llamar al método mostrar_profesionales
            input("Presione Enter para continuar...")
        elif opcion == 6: #Mostrar lista de turnos
            turneoOdontologico.mostrar_turnos() #Tarea: Agregar que muestre fecha, hora, paciente y profesional
            input("Presione Enter para continuar...")        
        elif opcion == 7: #Dar de baja un turno
            fecha = input("Ingrese la fecha del turno a dar de baja: ")
            turno = turneoOdontologico.contiene_turno(fecha)
            if turno == None: ## Tarea: Tira ERROR!!!
                print("El turno no se encuentra registrado")
            else:
                turneoOdontologico.turnos.eliminar(fecha)
                print("Turno eliminado con éxito")
            input("Presione Enter para continuar...")    
                
        
        
        elif opcion == 8:
            turneoOdontologico.seleccionar_especialidad()
            input("Presione Enter para continuar...")
        elif opcion == 9:
            print("Gracias por utilizar el sistema de turnos de la Clínica Odontológica")
        else: #Tarea: FIJARSE LA INDENTACIÓN
            print("Opción incorrecta. Por favor, ingrese una opción válida")
            
if __name__ == "__main__":
    turneoOdontologico = Clinica()
    run(turneoOdontologico)


    
    
