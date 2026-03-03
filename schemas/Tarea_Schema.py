from pydantic import BaseModel

class Crear_Tarea(BaseModel):
    nombre: str
    urgencia: str
    descripcion: str
