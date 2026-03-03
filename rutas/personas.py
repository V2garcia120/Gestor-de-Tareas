from fastapi import APIRouter

from DB.datos import getConnection
from Repositorios.RepositorioPersona import RepositorioPersona
from schemas.Persona_Schema import Crear_Persona

router = APIRouter(prefix="/personas", tags=["Personas"])


@router.post("/")
def crear_persona(payload: Crear_Persona):
    with getConnection() as connection:
        repositorio_persona = RepositorioPersona(connection)
        persona_id = repositorio_persona.CrearPersona(payload.nombre)

    return {"id": persona_id, "nombre": payload.nombre}


@router.get("/{nombre}")
def buscar_persona(nombre: str):
    with getConnection() as connection:
        repositorio_persona = RepositorioPersona(connection)
        persona = repositorio_persona.BuscarPersona(nombre)

    if persona is None:
        return {"encontrada": False, "id": None}

    return {"encontrada": True, "id": persona[0], "nombre": nombre}
