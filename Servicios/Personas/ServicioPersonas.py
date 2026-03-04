from Repositorios.RepositorioPersona import RepositorioPersona
from schemas.Persona_Schema import Crear_Persona
from schemas.Response_Schema import PersonaBusquedaResponse, PersonaResponse


class ServicioPersonas:
    def __init__(self, repositorio_persona: RepositorioPersona):
        self.repositorio_persona = repositorio_persona

    def crear_persona(self, payload: Crear_Persona) -> PersonaResponse:
        persona_id = self.repositorio_persona.crear_persona(payload.nombre)

        return PersonaResponse(id=persona_id, nombre=payload.nombre)

    def buscar_persona(self, nombre: str) -> PersonaBusquedaResponse:
        persona = self.repositorio_persona.buscar_persona_por_nombre(nombre)

        if persona is None:
            return PersonaBusquedaResponse(encontrada=False, id=None, nombre=None)

        return PersonaBusquedaResponse(
            encontrada=True,
            id=persona["id"],
            nombre=persona["nombre"],
        )
