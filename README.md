# Pruebas Automatizadas para la Creación de Kits de Usuario

Este proyecto contiene pruebas automatizadas para la funcionalidad de creación de usuarios y creación de kits de usuarios en una aplicación web.

## Descripción

Este proyecto busca asegurar la calidad de los procesos para que todo funcione como debería al momento de que el usuario introduzca los datos necesarios. Las pruebas cubren casos positivos, donde se espera una creación exitosa, y casos negativos, donde se esperan errores debido a entradas no válidas.

La documentación utilizada como referencia para las especificaciones de la funcionalidad es **apiDoc**.

## Tecnologías y Técnicas Utilizadas

- **Lenguaje de Programación**: Python
- **Framework de Pruebas**: pytest
- **Librería de Solicitudes HTTP**: requests

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `configuration.py`: Contiene las constantes de configuración, como la URL del servicio y las rutas de las API.
- `data.py`: Almacena los datos de prueba, como los encabezados y los cuerpos de solicitud.
- `sender_stand_request.py`: Contiene las funciones para enviar solicitudes HTTP a la API.
- `create_kit_name_kit_test.py`: Incluye las funciones de prueba y las aserciones para validar los casos de prueba.
- `README.md`: Este archivo, que proporciona información general sobre el proyecto.
- `.gitignore`: Archivo de configuración para excluir archivos y directorios innecesarios del control de versiones.

## Listas de comprobación

### Creación de Usuarios

| ID | Descripción | Resultado esperado |
|----|--------------|---------------------|
| №1 | El parámetro "firstName" contiene dos caracteres | El código de respuesta y el estado: 201 Created; El parámetro "authToken" contiene un token generado recientemente; La tabla "Users" contiene valores pasados |
| №2 | El parámetro "firstName" contiene quince caracteres | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №3 | El parámetro "firstName" contiene solo un caracter | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №4 | El parámetro "firstName" contiene dieciseis caracteres | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №5 | El parámetro "firstName" contiene dieciseis caracteres | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №6 | El parámetro "firstName" contiene caracteres especiales | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №7 | El parámetro "firstName" contiene un string de números | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №8 | La solicitud no contiene el parámetro "firstName" | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №9 | El parámetro "firstName" contiene un string vacío | El código de respuesta y el estado: 400 Bad Request; {"code": 400, "message": El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"} |
| №10 | El tipo del parámetro "firstName" es un número | El código de respuesta y el estado: 400 Bad Request |

### Creación de Kits de Usuarios

| ID | Descripción | Resultado esperado |
|----|--------------|---------------------|
| №1 | El número permitido de caracteres (1) | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| №2 | El número permitido de caracteres (511) | Código de respuesta: 201; El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| №3 | El número de caracteres es menor que la cantidad permitida (0) | Código de respuesta: 400 |
| №4 | El número de caracteres es mayor que la cantidad permitida (512) | Código de respuesta: 400 |
| №5 | Se permiten caracteres especiales | Código de respuesta: 201; El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| №6 | Se permiten espacios | Código de respuesta: 201; El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| №7 | Se permiten números | Código de respuesta: 201; El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| №8 | El parámetro no se pasa en la solicitud | Código de respuesta: 400 |
| №9 | Se ha pasado un tipo de parámetro diferente (número) | Código de respuesta: 400 |

## Ejecución de las Pruebas

Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes de Python:

- **pytest**
- **requests**

Para ejecutar las pruebas, usa la terminal y ejecuta el comando "pytest" seguido del nombre del archivo que contiene las pruebas.  

**Pruebas para la creación de usuario**: pytest create_user_test.py  

**Pruebas para la creación de un kit de usuario**: pytest create_kit_name_kit_test.py

## Mis redes

- **LinkedIn:** [Gustavo Ángel Vargas Leal](https://www.linkedin.com/in/gustavo-angel-vargas-leal/)
- **GitHub:** [GVL0001](https://github.com/GVL0001)
