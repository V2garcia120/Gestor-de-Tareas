from DB.datos import getConnection
from Repositorios.RepositorioPersona import RepositorioPersona
from schemas.Persona_Schema import Crear_Persona
from schemas.Response_Schema import PersonaBusquedaResponse, PersonaResponse


class ServicioPersonas:
    def crear_persona(self, payload: Crear_Persona) -> PersonaResponse:
        with getConnection() as connection:
            repositorio_persona = RepositorioPersona(connection)
            persona_id = repositorio_persona.crear_persona(payload.nombre)

        return PersonaResponse(id=persona_id, nombre=payload.nombre)

    def buscar_persona(self, nombre: str) -> PersonaBusquedaResponse:
        with getConnection() as connection:
            repositorio_persona = RepositorioPersona(connection)
            persona = repositorio_persona.buscar_persona_por_nombre(nombre)

        if persona is None:
            return PersonaBusquedaResponse(encontrada=False, id=None, nombre=None)

        return PersonaBusquedaResponse(
            encontrada=True,
            id=persona["id"],
            nombre=persona["nombre"],
        )
