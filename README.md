# Gestor de Tareas

Una aplicación de gestión de tareas desarrollada en Python que permite crear tareas, registrar personas y asignar tareas a usuarios usando una base de datos SQLite.

## Características

- Crear y almacenar tareas con nombre, urgencia y descripción
- Registrar personas (usuarios)
- Asociar tareas a uno o varios usuarios
- Consultar las tareas asignadas a una persona
- Eliminar y completar tareas (funcionalidad en desarrollo)

## Estructura del proyecto

```
Gestor-de-Tareas/
├── main.py                          # Punto de entrada de la aplicación
├── DataClasses.py                   # Clases de datos (Tarea)
├── datos.py                         # Configuración e inicialización de la base de datos
├── tareas.db                        # Base de datos SQLite (generada automáticamente)
└── Repositorios/
    ├── RepositorioTareas.py         # Operaciones CRUD para tareas
    ├── RepositorioPersona.py        # Operaciones CRUD para personas
    └── RepositorioUsuarioTarea.py   # Gestión de asociaciones tarea-usuario
```

## Requisitos

- Python 3.7 o superior
- No se requieren dependencias externas (usa `sqlite3` de la biblioteca estándar de Python)

## Instalación y uso

1. Clona el repositorio:

   ```bash
   git clone https://github.com/V2garcia120/Gestor-de-Tareas.git
   cd Gestor-de-Tareas
   ```

2. Ejecuta la aplicación:

   ```bash
   python main.py
   ```

   Al ejecutarse, la aplicación inicializará la base de datos automáticamente, creará una tarea de ejemplo, registrará una persona y la asociará a dicha tarea.

## Modelo de datos

### Tarea

| Campo       | Tipo    | Descripción                        |
|-------------|---------|------------------------------------|
| id          | INTEGER | Identificador único (autoincremental) |
| nombre      | TEXT    | Nombre de la tarea                 |
| urgencia    | TEXT    | Nivel de urgencia de la tarea      |
| descripcion | TEXT    | Descripción detallada de la tarea  |
| completada  | INTEGER | Estado de la tarea (0 = pendiente, 1 = completada) |

### Persona

| Campo  | Tipo    | Descripción                        |
|--------|---------|------------------------------------|
| id     | INTEGER | Identificador único (autoincremental) |
| nombre | TEXT    | Nombre de la persona               |

### AsignacionTarea

| Campo     | Tipo    | Descripción                        |
|-----------|---------|------------------------------------|
| idTarea   | INTEGER | Referencia a la tabla Tarea        |
| idPersona | INTEGER | Referencia a la tabla Persona      |

## Repositorios

### RepositorioTareas

- `CrearTarea(tarea)` – Inserta una nueva tarea y devuelve su ID.
- `ObtenerTareas(idPersona)` – Devuelve todas las tareas asignadas a una persona.
- `EliminarTarea()` – Elimina una tarea (en desarrollo).
- `CompletarTarea()` – Marca una tarea como completada (en desarrollo).

### RepositorioPersona

- `CrearPersona(nombre)` – Registra una nueva persona y devuelve su ID.
- `BuscarPersona(nombre)` – Busca una persona por nombre y devuelve su ID.
- `EliminarPersona()` – Elimina una persona (en desarrollo).

### RepositorioUsuarioTarea

- `Asociar_Tareas_Usuarios(tarea_id, usuario_ids)` – Asocia una tarea a uno o varios usuarios.
