## Instalacion
Instalen pipenv
```
pip install pipenv
```

luego para iniciar el entorno virtual ejecuten:

```
pipenv shell
```

y se crea una consola con los modulos que necesita el proyecto para correr


Luego tienes que ejecutar
```sh
pipenv install
```
dentro de la carpeta donde se encuentra el archivo Pipfile.lock

o bien ejecutar
```sh
pipenv install -r requirements.txt
```

si no funciona reemplaza por un ``` pip ```

## MySQL

El proyecto usa como base de datos MySQL, dentro del proyecto en settings.py esta de esta forma:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Motor de la base de datos
        'NAME': 'deshuesadero_pruebas', # Nombre base de datos
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS':
            {'charset': 'utf8mb4',
             'autocommit': True, },
    }
}
```

## Errores al cargar base de datos

Antes de hacer las migraciones, comenta los formularios que estan en las carpetas
- [deshuezadero\account\forms.py](https://github.com/fate-9x/deshuezadero/blob/master/deshuezadero/account/forms.py)
- [deshuezadero\store\forms.py](https://github.com/fate-9x/deshuezadero/blob/master/deshuezadero/store/forms.py)

y ejecuta 
```sh
python manage.py makemigrations appDeshuezadero
```
```sh
python manage.py migrate
```

y ya puedes descomentar los formularios.