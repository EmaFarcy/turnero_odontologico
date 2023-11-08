from turneoOdontologico import Paciente, Profesional, Turno

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