#Aquí creamos el menú de opciones para el usuario:
from turneoOdontologico import Paciente, Profesional, Turno, Clinica
from datetime import datetime

def menu():
    opcion = 0
    while opcion < 1 or opcion > 11:
        print("--")  
        print("\nBienvenido al sistema de turnos Dental Desk.")    
        print("1. Registrar un nuevo paciente")
        print("2. Registrar un nuevo profesional")
        print("3. Registrar un nuevo turno")
        print("4. Mostrar listado de pacientes")
        print("5. Mostrar paciente")
        print("6. Mostrar listado de profesionales")
        print("7. Mostrar profesional")
        print("8. Mostrar listado de turnos")
        print("9. Mostrar turno")
        print("10. Dar de baja un turno")
        print("11. Salir")
        print("--")
        opcion = int(input("Ingrese la opción deseada: "))
        
    return opcion

def run(turneoOdontologico):
    opcion = 0

    while opcion != 11:
        opcion = menu()
        
        if opcion == 1: #Registra nuevo paciente.
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
        
        elif opcion == 2: # Agrega el profesional a la lista de profesionales.
            nombre = input("Ingrese el nombre del profesional: ")
            apellido = input("Ingrese el apellido del profesional: ")
            dni = int(input("Ingrese el DNI del profesional: "))
            contacto = input("Ingrese el número de contacto del profesional: ")
            direccion = input("Ingrese la dirección del profesional: ")
            especialidad = input("Ingrese profesión: ")
            profesional = Profesional(dni, nombre, apellido, contacto, direccion,especialidad)
            if turneoOdontologico.contiene_profesional(profesional.dni):
                print("El profesional ya se encuentra registrado")
            else:
                turneoOdontologico.alta_nuevo_profesional(profesional)
                print("¡Profesional registrado con éxito!")
            input("Presione Enter para continuar...")    
        
        elif opcion == 3: #Registra un nuevo turno # Paciente y Profesional deben estar registrados.
            dni_paciente = int(input("Ingrese el DNI del paciente: "))
            if  turneoOdontologico.buscar_paciente(dni_paciente) == False: 
                print("El paciente no se encuentra registrado, es necesario registrar el cliente para asignar un turno.")
                break
            else: 
                dni_profesional = int(input("Ingrese el DNI del profesional: "))
                if not turneoOdontologico.contiene_profesional(dni_profesional):
                    print("El profesional no se encuentra registrado")
                    input("Presione Enter para continuar...")
                else:
                    fecha = input("Ingrese la fecha del turno en formato 'año,mes,dia,hora,min,seg': ")
                    anio, mes, dia, hora, minuto, segundo = fecha.split(",")
                    dato = datetime(int(anio), int(mes), int(dia), int(hora), int(minuto), int(segundo))
                    turno = Turno(paciente, profesional, dato)
                    if turneoOdontologico.contiene_turno(turno.dato):
                        print("El turno ya se encuentra registrado") 
                    else:
                        turneoOdontologico.registrar_turno(turno)
                        print("¡Turno registrado con éxito!")
                    input("Presione Enter para continuar...") 
        
        elif opcion == 4: #Mostrar lista de pacientes
            if turneoOdontologico.pacientes.longitud() == 0:
                print("No hay pacientes registrados")
            else:
                turneoOdontologico.mostrar_pacientes() 
            input("Presione Enter para continuar...") 
        
        elif opcion == 5: #Muestra paciente
            dni = int(input("Ingrese dni del paciente a buscar: "))
            resultado = turneoOdontologico.busqueda_individual_paciente(dni)
            if resultado is not None:
                print(resultado)
            else:
                print("El paciente no se encuentra registrado")
            input("Presione Enter para continuar")
                     
        elif opcion == 6: #Muestra lista de profesionales 
            if turneoOdontologico.profesionales.longitud() == 0:
                print("No hay profesionales registrados")
            else:
                turneoOdontologico.mostrar_profesionales() 
            input("Presione Enter para continuar...")
        
        elif opcion == 7: #Muestra profesional
            dni = int(input("Ingrese dni del profesional a buscar: "))
            resultado = turneoOdontologico.busqueda_individual_profesional(dni)
            if resultado is not None:
                print(resultado)
            else:
                print("El profesional no se encuentra registrado")
            input("Presione Enter para continuar")
            
        elif opcion == 8:  #Muestra lista de turnos  
            if turneoOdontologico.turnos.longitud() == 0:
                print("No hay turnos registrados")
            else:
                turneoOdontologico.mostrar_turnos()
            input("Presione Enter para continuar...") 
        
        elif opcion == 9: #Muestra turno
            fecha = input("Ingrese la fecha del turno que desea buscar en formato 'año,mes,dia,hora,min,seg': ")
            anio, mes, dia, hora, minuto, segundo = fecha.split(",")
            dato = datetime(int(anio), int(mes), int(dia), int(hora), int(minuto), int(segundo))
            resultado = turneoOdontologico.busqueda_individual_turno(dato) 
            if resultado is not None:
                print(resultado)
            else:
                print("El turno no se encuentra registrado")
            input("Presione Enter para continuar...")

        elif opcion == 10: #Da de baja un turno
            fechaelim = input("Ingrese la fecha del turno en formato 'año,mes,dia,hora,min,seg': ")
            anio, mes, dia, hora, minuto, segundo = fechaelim.split(",")
            dato = datetime(int(anio), int(mes), int(dia), int(hora), int(minuto), int(segundo))
            if not turneoOdontologico.contiene_turno(turno.dato): #TAREA: NO FUNCIONA
                print("El turno no se encuentra registrado")
            else:
                turneoOdontologico.eliminar_turno(turno) 
                print("Turno eliminado con éxito")
            input("Presione Enter para continuar...")
        
        elif opcion == 11: #Sale del programa
            print("Gracias por utilizar el sistema de turnos Dental Desk. Una buena salud oral es clave para el bienestar general.")
        else:
            print("Opción incorrecta. Por favor, ingrese una opción válida")
            
if __name__ == "__main__":
    turneoOdontologico = Clinica()
    run(turneoOdontologico)