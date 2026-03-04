from fastapi import APIRouter

from Servicios.Asignaciones.ServicioAsignaciones import ServicioAsignaciones
from schemas.Asignacion_Schema import Asignar_Tarea
from schemas.Response_Schema import AsignacionResponse

router = APIRouter(prefix="/asignaciones", tags=["Asignaciones"])
servicio_asignaciones = ServicioAsignaciones()


@router.post("/", response_model=AsignacionResponse)
def asignar_tarea(payload: Asignar_Tarea):
    return servicio_asignaciones.asignar_tarea(payload)
