from pydantic import BaseModel


class Asignar_Tarea(BaseModel):
    tarea_id: int
    persona_ids: list[int]
