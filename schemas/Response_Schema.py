from pydantic import BaseModel


class PersonaResponse(BaseModel):
    id: int
    nombre: str


class PersonaBusquedaResponse(BaseModel):
    encontrada: bool
    id: int | None
    nombre: str | None


class TareaResponse(BaseModel):
    id: int
    nombre: str
    urgencia: str
    descripcion: str
    completada: bool


class TareaCreadaResponse(BaseModel):
    id: int
    nombre: str


class TareasDePersonaResponse(BaseModel):
    persona_id: int
    tareas: list[TareaResponse]


class AsignacionResponse(BaseModel):
    tarea_id: int
    persona_ids: list[int]
    asignadas: bool
