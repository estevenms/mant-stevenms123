import random
import string
"""Función que genera contraseña aleatoria de entre 4 y 16 caracteres
que incluyen minúsculas, mayúsculas, números y caracteres especiales """
def generatePassword():
    password = string.ascii_letters + string.digits + string.punctuation
    """ Retorna un cantraseña aleatoria de la lista de letras, números
    y caracteres con un tamaña entre 4 y 16 caracteres """
    return ''.join(random.choice(password) for i in range(random.randint(4,16)))
print ("Generando contraseña aleatoria ...")
print ("Contraseña aleatoria:", generatePassword() )


