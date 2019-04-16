# Instalación local

## Virtual environment

Para evitar conflictos con las paquetes instalados globalmente y en el home del usuario activo es recomendable el uso de un virtual environment. Para ello hay dos opciones:
* [virtualenv](https://virtualenv.pypa.io/en/stable/): Recomiendo esta por que añadí un settings.json al repositorio para que vscode (los que lo usen) detecte la presencia de un entorno `env` en la carpeta del proyecto y que este autocomplete las librerías y paquetes del proyecto.
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/): La ventaja de esta sobre la anterior es que tienes un directorio en tu computadora que tiene todos los entornos virtuales creados y te permite activarlos desde cualquier directorio sin saber la ruta exacta poniendole un nombre que los identifique.

Independientemente de la herramienta que escojan es importante que la versión de python con la que creen el entorno sea la 3. Para hacer eso solo tienen que pasarle un flag adicional al comando. Ejemplo:

```bash
virtualenv env --python=$(which python3)
```

Para instalar las dependencias del proyecto primero se debe activar el entorno virtual

```bash
# en el caso de que usemos virtualenv
source env/bin/activate
# en el caso que usemos virtualenvwrapper
workon nombre-entorno
```

Y luego se instalan los paquetes con pip

```bash
pip install -r requirements.txt
```

**Importante**: En el .gitignore del repositorio esta añadido env, .env, venv, .venv, entre otros. Si creas un entorno virtual con un nombre que git no ignore por favor **no lo commitees**.

## Base de datos
Como RDBMS vamos a utilizar PostgreSQL. Los datos para la conexión local son los siguientes:

```bash
NAME: eia
USER: eia
PASSWORD: eiae123
HOST: localhost
PORT: 5432
```

En [este](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) enlace pueden ver como crear la base de datos con los datos especificados, sin embargo, correr el script [installdb.sh](./installdb.sh) debería crear la base de datos de una vez si estamos en linux (no aseguro en windows por que nunca lo he intentado).

Importante: El script [installdb.sh](./installdb.sh) asume que tienes instalado postgresql. Pueden usar el script para borrar la bd y crearla sin problemas.

Para verificar que todo funciona, activamos nuestro entorno virtual y ejecutamos:

```bash
python manage.py migrate # hay que estar en la carpeta del proyecto
```

Este comando replica el esquema presente en las carpetas migrations en la base de datos local. Para mas info: migrations (no hace falta hacer makemigrations, solo migrate).

## Selenium

Selenium es un framework para probar interfaces de usuario en el navegador. Cuando corres los tests, selenium abre un navegador con el que no puedes interactuar y ves como todo va ocurriendo automáticamente. Posee implementaciones en varios lenguajes, entre estos, python.

Para instalar selenium se tienen que hacer tres cosas:

1. Instalarlo de requirements.txt
2. Instalar firefox
3. Instalar geckodriver

En el repositorio hay un script llamado [installgeckodriver.sh](./installgeckodriver.sh) que hace lo que indica su nombre.

Si necesitan información sobre selenium (como usarlo, ejemplos) pueden visitar las siguientes referencias:
* [Documentación](https://selenium-python.readthedocs.io/index.html) del driver de selenium para python
* [german1608/sip-software](https://github.com/german1608/sip-software)
