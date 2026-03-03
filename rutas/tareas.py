from fastapi import APIRouter

from DB.datos import getConnection
from Repositorios.RepositorioTareas import RepositorioTareas
from schemas.DataClasses import Tarea
from schemas.Tarea_Schema import Crear_Tarea

router = APIRouter(prefix="/tareas", tags=["Tareas"])


@router.post("/")
def crear_tarea(payload: Crear_Tarea):
    tarea = Tarea(
        nombre=payload.nombre,
        urgencia=payload.urgencia,
        descripcion=payload.descripcion,
    )

    with getConnection() as connection:
        repositorio_tareas = RepositorioTareas(connection)
        tarea_id = repositorio_tareas.CrearTarea(tarea)

    return {"id": tarea_id, "nombre": payload.nombre}


@router.get("/persona/{persona_id}")
def obtener_tareas_de_persona(persona_id: int):
    with getConnection() as connection:
        repositorio_tareas = RepositorioTareas(connection)
        tareas = repositorio_tareas.ObtenerTareas(persona_id)

    return {"persona_id": persona_id, "tareas": tareas}
