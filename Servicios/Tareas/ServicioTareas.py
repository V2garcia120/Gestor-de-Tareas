from DB.datos import getConnection
from Repositorios.RepositorioTareas import RepositorioTareas
from schemas.DataClasses import Tarea
from schemas.Response_Schema import TareaCreadaResponse, TareaResponse, TareasDePersonaResponse
from schemas.Tarea_Schema import Crear_Tarea


class ServicioTareas:
    def crear_tarea(self, payload: Crear_Tarea) -> TareaCreadaResponse:
        tarea = Tarea(
            nombre=payload.nombre,
            urgencia=payload.urgencia,
            descripcion=payload.descripcion,
        )

        with getConnection() as connection:
            repositorio_tareas = RepositorioTareas(connection)
            tarea_id = repositorio_tareas.crear_tarea(tarea)

        return TareaCreadaResponse(id=tarea_id, nombre=payload.nombre)

    def obtener_tareas_de_persona(self, persona_id: int) -> TareasDePersonaResponse:
        with getConnection() as connection:
            repositorio_tareas = RepositorioTareas(connection)
            tareas = repositorio_tareas.obtener_tareas_de_persona(persona_id)

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
