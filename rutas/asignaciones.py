from fastapi import APIRouter

from DB.datos import getConnection
from Repositorios.RepositorioUsuarioTarea import RepositorioUsuarioTarea
from schemas.Asignacion_Schema import Asignar_Tarea

router = APIRouter(prefix="/asignaciones", tags=["Asignaciones"])


@router.post("/")
def asignar_tarea(payload: Asignar_Tarea):
    with getConnection() as connection:
        repositorio_usuario_tarea = RepositorioUsuarioTarea(connection)
        repositorio_usuario_tarea.Asociar_Tareas_Usuarios(payload.tarea_id, payload.persona_ids)

    return {
        "tarea_id": payload.tarea_id,
        "persona_ids": payload.persona_ids,
        "asignadas": True,
    }
