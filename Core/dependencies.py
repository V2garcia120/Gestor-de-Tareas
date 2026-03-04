from collections.abc import Generator
from sqlite3 import Connection

from fastapi import Depends

from DB.datos import getConnection
from Repositorios.RepositorioPersona import RepositorioPersona
from Repositorios.RepositorioTareas import RepositorioTareas
from Repositorios.RepositorioUsuarioTarea import RepositorioUsuarioTarea
from Servicios.Asignaciones.ServicioAsignaciones import ServicioAsignaciones
from Servicios.Personas.ServicioPersonas import ServicioPersonas
from Servicios.Tareas.ServicioTareas import ServicioTareas


def get_db_connection() -> Generator[Connection, None, None]:
    connection = getConnection()
    try:
        yield connection
    finally:
        connection.close()


def get_repositorio_tareas(
    connection: Connection = Depends(get_db_connection),
) -> RepositorioTareas:
    return RepositorioTareas(connection)


def get_repositorio_personas(
    connection: Connection = Depends(get_db_connection),
) -> RepositorioPersona:
    return RepositorioPersona(connection)


def get_repositorio_asignaciones(
    connection: Connection = Depends(get_db_connection),
) -> RepositorioUsuarioTarea:
    return RepositorioUsuarioTarea(connection)


def get_servicio_tareas(
    repositorio_tareas: RepositorioTareas = Depends(get_repositorio_tareas),
) -> ServicioTareas:
    return ServicioTareas(repositorio_tareas)


def get_servicio_personas(
    repositorio_personas: RepositorioPersona = Depends(get_repositorio_personas),
) -> ServicioPersonas:
    return ServicioPersonas(repositorio_personas)


def get_servicio_asignaciones(
    repositorio_asignaciones: RepositorioUsuarioTarea = Depends(get_repositorio_asignaciones),
) -> ServicioAsignaciones:
    return ServicioAsignaciones(repositorio_asignaciones)