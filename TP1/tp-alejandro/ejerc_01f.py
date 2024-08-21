"""f. Un portal web requiere un formulario de alta de usuario donde se ingrese,
 mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python,
una función contrasena_valida(contrasena) que devuelva True en caso de superar
las siguientes validaciones sobre la contraseña proporcionada por el usuario:
i. Longitud entre 6 y 20 caracteres.
ii. Debe contener al menos un número.
iii. Debe contener al menos dos mayúsculas.
iv. Debe contener al menos un carácter especial.
v. No puede contener espacios.
La salida esperada es la siguiente:
abc.123 es válida: False
Abc.123 es válida: False
AbC.123 es válida: True
AbC.1 23 es válida: False
ÁbC.123 es válida: False"""
import re

def contrasena_valida(contrasena):
    # Verifica la longitud
    if len(contrasena) < 6 or len(contrasena) > 20:
        return False
    
    # Verifica que exita al menos un número
    if not re.search(r'\d', contrasena):
        return False
    
    # Verifica que exita al menos dos mayúsculas
    if len(re.findall(r'[A-Z]', contrasena)) < 2:
        return False
    
    # Verifica que exista al menos un carácter especial
    if not re.search(r'[$&+,:;=?@#|<>.^*()%!-]', contrasena):
        return False
    
    # Verifica que no contenga espacios
    if ' ' in contrasena:
        return False
    
    return True

# Pruebas
print("abc.123 es válida:", contrasena_valida("abc.123"))
print("Abc.123 es válida:", contrasena_valida("Abc.123"))
print("AbC.123 es válida:", contrasena_valida("AbC.123"))
print("AbC.1 23 es válida:", contrasena_valida("AbC.1 23"))
print("ÁbC.123 es válida:", contrasena_valida("ÁbC.123"))