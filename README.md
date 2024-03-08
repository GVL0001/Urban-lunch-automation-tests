# Pruebas Automatizadas para la Creación de Kits de Usuario

Este proyecto contiene un conjunto de pruebas automatizadas para verificar la funcionalidad de creación de kits de usuario en una aplicación web. Las pruebas se enfocan en validar los diferentes casos de uso relacionados con el parámetro "name" al crear un nuevo kit.

## Descripción

El objetivo principal de este proyecto es asegurar la calidad del proceso de creación de kits de usuario, validando diferentes escenarios y condiciones relacionadas con el nombre del kit. Las pruebas cubren casos positivos, donde se espera una creación exitosa, y casos negativos, donde se esperan errores debido a entradas no válidas.

La documentación utilizada como referencia para las especificaciones de la funcionalidad es **apiDoc**.

## Tecnologías y Técnicas Utilizadas

- **Lenguaje de Programación**: Python
- **Framework de Pruebas**: pytest
- **Librería de Solicitudes HTTP**: requests
- **Enfoque de Pruebas**: Pruebas Unitarias

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `configuration.py`: Contiene las constantes de configuración, como la URL del servicio y las rutas de las API.
- `data.py`: Almacena los datos de prueba, como los encabezados y los cuerpos de solicitud.
- `sender_stand_request.py`: Contiene las funciones para enviar solicitudes HTTP a la API.
- `create_kit_name_kit_test.py`: Incluye las funciones de prueba y las aserciones para validar los casos de prueba.
- `README.md`: Este archivo, que proporciona información general sobre el proyecto.
- `.gitignore`: Archivo de configuración para excluir archivos y directorios innecesarios del control de versiones.

## Ejecución de las Pruebas

Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes de Python:

- **pytest**
- **requests**

## Mis redes

- **LinkedIn:** [Gustavo Ángel Vargas Leal](https://www.linkedin.com/in/gustavo-angel-vargas-leal/)
- **GitHub:** [GVL0001](https://github.com/GVL0001)
