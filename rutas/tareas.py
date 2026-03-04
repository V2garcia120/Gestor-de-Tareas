from fastapi import APIRouter, Depends

from Core.dependencies import get_servicio_tareas
from Servicios.Tareas.ServicioTareas import ServicioTareas
from schemas.Response_Schema import TareaCompletadaResponse, TareaCreadaResponse, TareasDePersonaResponse
from schemas.Tarea_Schema import Crear_Tarea

router = APIRouter(prefix="/tareas", tags=["Tareas"])


@router.post("/", response_model=TareaCreadaResponse)
def crear_tarea(
    payload: Crear_Tarea,
    servicio_tareas: ServicioTareas = Depends(get_servicio_tareas),
):
    return servicio_tareas.crear_tarea(payload)


@router.get("/persona/{persona_id}", response_model=TareasDePersonaResponse)
def obtener_tareas_de_persona(
    persona_id: int,
    servicio_tareas: ServicioTareas = Depends(get_servicio_tareas),
):
    return servicio_tareas.obtener_tareas_de_persona(persona_id)


@router.put("/tarea/completar/{tarea_id}", response_model=TareaCompletadaResponse)
def completar_tarea(
    tarea_id: int,
    servicio_tareas: ServicioTareas = Depends(get_servicio_tareas),
):
    return servicio_tareas.completar_tarea(tarea_id)