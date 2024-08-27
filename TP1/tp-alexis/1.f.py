"""
1.f. Un portal web requiere un formulario de alta de usuario donde se ingrese, mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python, una función contrasena_valida(contrasena) que devuelva True en caso de superar las siguientes validaciones sobre la contraseña proporcionada por el usuario:
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
  ÁbC.123 es válida: False
Para la búsqueda de caracteres de cierto tipo (mayúsculas, acentos, espacios y otros) debe hacerse uso de la librería re:
- https://docs.python.org/es/3/library/re.html
- https://relopezbriega.github.io/blog/2015/07/19/expresiones-regularescon-python/
- Para buscar caracteres especiales, puede utilizarse la siguiente expresión
[$&+,:;=?@#|<>.^*()%!-]
"""
import re

patronLongitud = re.compile(r'^.{6,20}$')
patroNumero = re.compile(r'.*\d+.*')
patronMayusculas = re.compile(r'^(.*[A-Z].*){2,}$')
patronEspacios = re.compile(r'^\S*$')
patronCaracteresEspeciales = re.compile(r'.*[$&+,:;=?@#|<>.^*()%!-].*')

def contrasena_valida(contrasena):
  if not patronLongitud.match(contrasena):
    print("La contraseña tiene que tener entre 6 a 20 caracteres")
    return False;
  if not patroNumero.match(contrasena):
    print("La contraseña debe tener al menos un número")
    return False;
  if not patronMayusculas.match(contrasena):
    print("La contraseña debe tener al menos dos mayúsculas")
    return False;
  if not patronEspacios.match(contrasena):
    print("La contraseña no puede contener espacios")
    return False;
  if not patronCaracteresEspeciales.match(contrasena):
    print("La contraseña debe tener al menos un caractér especial")
    return False;

  print(f"{contrasena} es válida")
  return True;

contrasena_valida("abc.123")
contrasena_valida("Abc.123")
contrasena_valida("AbC.123")
contrasena_valida("abc.123$")
contrasena_valida("AbC.1 23")
contrasena_valida("ÁbC.123")