# mant-stevenms123

Este proyecto esta creado con la finalidad de crear un nuevo repositorio y aplicar los pasos aprendidos durante el curso para el 
manejo de control de cambios.

### Pre requisitos:

El proyecto se puede descargar desde [github](https://github.com/) o desde la aplicación de GitHub Desktop. Para ejecutar el programa,
se necesita descargar la versión 3.7.2 de python desde [Python](https://www.python.org/downloads/); no obstante,
también funciona con versiones anteriores.

### Descargar el proyecto:

Para poder descargar el proyecto se puede realizar de 2 formar:

1. Para poder descargar y clonar el proyecto se debe de ingresar a este enlace [mant-stevenms123](https://github.com/stevenms123/mant-stevenms123) 
y luego dar clic en el boton de **clone or download**.

2. Ingresar a la aplicación github desktop dar clic a la opción File y luego a la opcion de clone repository, seguidamente ingresar el siguiente
enlace <https://github.com/stevenms123/mant-stevenms123>

### Ejecución del proyecto:

Cualquier archivo .py que se quiera correr, debe ejecutarse desde el IDLE de Python. Hay dos formas de abrirlo:

1. Desde el IDLE: File->Open y se escoge el archivo
2. Directamente desde el archivo se puede ejecutar al hacer clic en ctrl+F5


#### Generate Password:
Este proyecto cuenta con una función llamada generatePassword() dentro del archivo stevenms123.py, esta genera una 
contraseña aleatoria de entre 4 y 16 caracteres incluye minúsculas, mayúsculas, números y caracteres especiales.
Se importar el módulo string y se usa string.string.ascii_letters, string.digits y string.punctuation.

1. **string.string.ascii_letters**: Es una concatenación de constantes de cadena.
Resultado obtenido: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

2. **string.digits**: Es una cadena utilizada para generar los numeros del 0 al 9.
Resultado obtenido: 0123456789

3. **string.punctuation**: Esta opción contiene todos los caracteres de puntuación comunes.
