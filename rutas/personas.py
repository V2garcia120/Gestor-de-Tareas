from fastapi import APIRouter, Depends

from Core.dependencies import get_servicio_personas
from Servicios.Personas.ServicioPersonas import ServicioPersonas
from schemas.Persona_Schema import Crear_Persona
from schemas.Response_Schema import PersonaBusquedaResponse, PersonaResponse

router = APIRouter(prefix="/personas", tags=["Personas"])


@router.post("/", response_model=PersonaResponse)
def crear_persona(
    payload: Crear_Persona,
    servicio_personas: ServicioPersonas = Depends(get_servicio_personas),
):
    return servicio_personas.crear_persona(payload)


@router.get("/{nombre}", response_model=PersonaBusquedaResponse)
def buscar_persona(
    nombre: str,
    servicio_personas: ServicioPersonas = Depends(get_servicio_personas),
):
    return servicio_personas.buscar_persona(nombre)
