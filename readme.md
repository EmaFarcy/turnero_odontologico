# Título del Proyecto

Dental Desk es un software de gestión de registros enfocado en administrar un listado de turnos, pacientes y profesionales
para un centro de consultorios odontológicos.

### Pre-requisitos 📋

Qué cosas necesitas para instalar el software y cómo instalarlas:

. Python 3.8 o superior.
. Gestor de paquetes pip (generalmente incluido con Python).
. Git para clonar el proyecto.
. (Opcional) Entorno virtual para Python como venv.

# En sistemas basados en Debian/Ubuntu

Para instalar Python y pip:
sudo apt-get install python3 python3-pip

### Instalación 🔧

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu computadora local para propósitos de desarrollo y pruebas:

1. Clona el repositorio:

git clone https://github.com/EmaFarcy/turnero_odontologico

2. Navega al directorio del proyecto:

cd directorio-del-proyecto

3. ¡Ya esta listo para usar!

## Ejecutando las pruebas

Para ejecutar las pruebas, puedes usar el siguiente comando:
python -m unittest discover

### Análisis pruebas end-to-end 🔩

1- Registro de un Nuevo Paciente: La prueba comienza simulando la entrada de datos para un nuevo paciente, incluyendo detalles como nombre, apellido, DNI, contacto y dirección y verifica que el paciente se registre correctamente en el sistema.

2- Agendar un Turno: A continuación, la prueba simula la programación de un turno para el paciente recién registrado, seleccionando un profesional disponible y una fecha y hora específicas. La prueba verifica que el turno se asigne correctamente y se refleje en la base de datos.

3- Cancelar un Turno: La prueba continúa con la simulación de la cancelación de un turno, asegurándose de que se actualice el estado del turno en el sistema y se liberen los recursos correspondientes.

### Pruebas de Estilo de Codificación###

Las pruebas de estilo de codificación en nuestro proyecto garantizan que todo el código siga un conjunto uniforme de reglas de estilo y buenas prácticas. Esto es importante no solo para mantener la coherencia en la base de código, sino también para facilitar la colaboración entre desarrolladores y mejorar la mantenibilidad del software.
Utilizamos herramientas como flake8 y pylint para realizar estas pruebas. Estas herramientas ayudan a identificar problemas comunes como errores de sintaxis, malas prácticas, desviaciones de las convenciones de estilo, y otros problemas que podrían afectar la calidad y la legibilidad del código.

## Despliegue 📦

Para desplegar este proyecto en un entorno de producción, sigue los siguientes pasos:

Configuración del Entorno:

Asegúrate de que el entorno de producción tiene Python instalado y configurado.
Si tu aplicación depende de bases de datos o servicios externos, asegúrate de que estén accesibles desde el entorno de producción.
Clonar el Repositorio:

Clona el repositorio en el entorno de producción: git clone https://github.com/EmaFarcy/turnero_odontologico

## Construido con 🛠️

. Python - Lenguaje de programación utilizado.
. Git - Sistema de control de versiones.
. Flake8/Pylint - Herramientas para el análisis de estilo de código.

## Versionado 📌

Para todas las versiones disponibles, los tags del repositorio son los siguientes: https://github.com/EmaFarcy/turnero_odontologico/tags . Este proyecto utiliza Semantic Versioning: https://semver.org/

El versionado se realiza a través de Git.

## Autores ✒️

- **Emanuel Farcy** - _Delegado de equipo - Desarrollador_ - [EmaFarcy](https://github.com/EmaFarcy)
- **Enzo Medina** - _Desarrollador_ - [EnzoMedina] [https://github.com/proger2]
- **Raúl Scavuzzo** - _Desarrollador_ - [rascavuzzo1990](https://github.com/rascavuzzo1990)

## Licencia 📄

Este proyecto está bajo la Creative Commons Atribución- CompartirIgual(CC BY-SA) - mira el archivo LICENSE.md para detalles.

## Expresiones de Gratitud 🎁

Nos gustaría expresar nuestro agradecimiento a:
. Matías Bordone por su orientación y valiosos consejos a lo largo del desarollo de este proyecto y de la cursada de la materia Programación 2 de la carrera de Desarrollo de Software del Instituto Técnico Superior Córdoba.
. Nico: por sus clases de consultas y seguimiento de nuestro proyecto.
. Nuestros compañeros/as de curso por sus feedbacks.

## Este proyecto no sería lo mismo sin su ayuda y apoyo. 🙌
