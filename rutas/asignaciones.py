from fastapi import APIRouter, Depends

from Core.dependencies import get_servicio_asignaciones
from Servicios.Asignaciones.ServicioAsignaciones import ServicioAsignaciones
from schemas.Asignacion_Schema import Asignar_Tarea
from schemas.Response_Schema import AsignacionResponse

router = APIRouter(prefix="/asignaciones", tags=["Asignaciones"])


@router.post("/", response_model=AsignacionResponse)
def asignar_tarea(
    payload: Asignar_Tarea,
    servicio_asignaciones: ServicioAsignaciones = Depends(get_servicio_asignaciones),
):
    return servicio_asignaciones.asignar_tarea(payload)
