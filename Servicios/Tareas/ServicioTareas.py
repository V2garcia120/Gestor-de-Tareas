from Repositorios.RepositorioTareas import RepositorioTareas
from schemas.DataClasses import Tarea
from schemas.Response_Schema import (
    TareaCompletadaResponse,
    TareaCreadaResponse,
    TareaResponse,
    TareasDePersonaResponse,
)
from schemas.Tarea_Schema import Crear_Tarea


class ServicioTareas:
    def __init__(self, repositorio_tareas: RepositorioTareas):
        self.repositorio_tareas = repositorio_tareas

    def crear_tarea(self, payload: Crear_Tarea) -> TareaCreadaResponse:
        tarea = Tarea(
            nombre=payload.nombre,
            urgencia=payload.urgencia,
            descripcion=payload.descripcion,
        )

        tarea_id = self.repositorio_tareas.crear_tarea(tarea)

        return TareaCreadaResponse(id=tarea_id, nombre=payload.nombre)

    def obtener_tareas_de_persona(self, persona_id: int) -> TareasDePersonaResponse:
        tareas = self.repositorio_tareas.obtener_tareas_de_persona(persona_id)

        return TareasDePersonaResponse(
            persona_id=persona_id,
            tareas=[
                TareaResponse(
                    id=tarea["id"],
                    nombre=tarea["nombre"],
                    urgencia=tarea["urgencia"],
                    descripcion=tarea["descripcion"],
                    completada=bool(tarea["completada"]),
                )
                for tarea in tareas
            ],
        )

    def completar_tarea(self, tarea_id: int) -> TareaCompletadaResponse:
        completada = self.repositorio_tareas.completar_tarea(tarea_id)
        return TareaCompletadaResponse(tarea_id=tarea_id, completada=completada)
