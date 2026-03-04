from fastapi import APIRouter

from Servicios.Tareas.ServicioTareas import ServicioTareas
from schemas.Response_Schema import TareaCreadaResponse, TareasDePersonaResponse
from schemas.Tarea_Schema import Crear_Tarea

router = APIRouter(prefix="/tareas", tags=["Tareas"])
servicio_tareas = ServicioTareas()


@router.post("/", response_model=TareaCreadaResponse)
def crear_tarea(payload: Crear_Tarea):
    return servicio_tareas.crear_tarea(payload)


@router.get("/persona/{persona_id}", response_model=TareasDePersonaResponse)
def obtener_tareas_de_persona(persona_id: int):
    return servicio_tareas.obtener_tareas_de_persona(persona_id)
