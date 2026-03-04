from fastapi import APIRouter

from Servicios.Personas.ServicioPersonas import ServicioPersonas
from schemas.Persona_Schema import Crear_Persona
from schemas.Response_Schema import PersonaBusquedaResponse, PersonaResponse

router = APIRouter(prefix="/personas", tags=["Personas"])
servicio_personas = ServicioPersonas()


@router.post("/", response_model=PersonaResponse)
def crear_persona(payload: Crear_Persona):
    return servicio_personas.crear_persona(payload)


@router.get("/{nombre}", response_model=PersonaBusquedaResponse)
def buscar_persona(nombre: str):
    return servicio_personas.buscar_persona(nombre)
