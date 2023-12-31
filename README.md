#  API Rest para la gestión de Tareas

La API REST para la Gestión de Tareas es un proyecto diseñado para aprender cómo crear una API REST siguiendo las mejores prácticas y entender cómo establecer relaciones entre las tablas de una base de datos. Esta aplicación utiliza FastAPI como framework para el desarrollo del backend y SQLAlchemy como ORM (Object-Relational Mapping) para interactuar con la base de datos MySQL.

### Clonar e instalar las Dependencias:

```cmd
git clone https://github.com/ErickSiguache/Task-List-API
pip install
```

### Entorno virtual

```cmd
Ruta > virtualenv -p python3 venv
Ruta > venv\Scripts\activate
```

### Creacion del proyecto

Comandos usados para la creación del proyecto:

```cmd
Ruta (venv)> pip install fastapi
Ruta (venv)> pip install "uvicorn[standard]"

Ruta (venv)> uvicorn main:app --reload
```

#### Dependencias usadas en el proyecto:

* SQLAlchemy: Biblioteca de Python que facilita la comunicación entre aplicaciones Python y bases de datos relacionales: https://www.sqlalchemy.org

```cmd
Ruta (venv)> pip install sqlalchemy
```

* PyMySQL: Es una biblioteca de Python que proporciona una interfaz para trabajar con bases de datos MySQL: https://pypi.org/project/pymysql/

```cmd
Ruta (venv)> pip install pymysql
```

* Python DotENV: Es una biblioteca de Python que permite cargar variables de entorno desde un archivo llamado ".env": https://pypi.org/project/python-dotenv/

```cmd
Ruta (venv)> pip install python-dotenv
```

Por último, se genera un archivo requirements.txt que contiene una lista de todas las bibliotecas (paquetes) que están instaladas actualmente en tu entorno de Python virtual.

```cmd
Ruta (venv)> pip freeze
Ruta (venv)> pip freeze > requirements.txt
```

### Vista de la aplicación

* [Documentación del módulo de categorías](https://github.com/ErickSiguache/Task-List-API/blob/main/documentation/crud-categories.md)
* [Documentación del módulo de tareas](https://github.com/ErickSiguache/Task-List-API/blob/main/documentation/crud-tasks.md)