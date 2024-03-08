import sender_stand_request
import data


# Crea un nuevo diccionario user_body a partir del diccionario user_body de data.py
def get_user_body(first_name):
    user_body = data.user_body.copy()
    user_body["firstName"] = first_name
    return user_body


# Crea un nuevo usuario utilizando la función post_new_user y devuelve el token de autenticación de la respuesta
def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]


# Crea un nuevo diccionario del cuerpo de kit con el campo name ingresado.
def get_kit_body(name):
    kit_body = {"name": name}
    return kit_body


# Función para las pruebas positivas: envía una solicitud POST para crear un nuevo kit de usuario y verifica que el código de respuesta sea 201 y que el campo name en la respuesta coincida con el valor en el kit_body
def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_user_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Función para las pruebas negativas: envía una solicitud POST para crear un nuevo kit de usuario y verifica que el código de respuesta sea 400
def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_user_kit(kit_body, auth_token)
    assert response.status_code == 400


# PARA PROBAR LOS TEST CASES AUTOMATIZADOS: INGRESA EL COMANDO "Pytest" en la terminal

# №1 El número permitido de caracteres (1)
# Resultado esperado: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
def test_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)


# №2 El número permitido de caracteres (511)
# Resultado esperado: Código de respuesta: 201; El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
def test_create_kit_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body, auth_token)


# №3 El número de caracteres es menor que la cantidad permitida (0)
# Resultado esperado: Código de respuesta: 400
def test_create_kit_0_letter_in_name_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)


# №4 El número de caracteres es mayor que la cantidad permitida (512)
# Resultado esperado: Código de respuesta: 400
def test_create_kit_512_letter_in_name_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body, auth_token)


# №5 Se permiten caracteres especiales
# Resultado esperado: Código de respuesta: 201; El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
def test_create_kit_special_caracter_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("№%@',")
    positive_assert(kit_body, auth_token)


# №6 Se permiten espacios
# Resultado esperado: Código de respuesta: 201; El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
def test_create_kit_with_spaces_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("A aaa")
    positive_assert(kit_body, auth_token)


# №7 Se permiten números
# Resultado esperado: Código de respuesta: 201; El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
def test_create_kit_numbers_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body("123")
    positive_assert(kit_body, auth_token)


# №8 El parámetro no se pasa en la solicitud
# Resultado esperado: Código de respuesta: 400
def test_create_kit_no_parameter_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = {} #Se ingresa un diccionario vac[io
    negative_assert_code_400(kit_body, auth_token)


# №9 Se ha pasado un tipo de parámetro diferente (número)
# Resultado esperado: Código de respuesta: 400
def test_create_kit_type_number_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = get_kit_body(123)
    negative_assert_code_400(auth_token, kit_body)
