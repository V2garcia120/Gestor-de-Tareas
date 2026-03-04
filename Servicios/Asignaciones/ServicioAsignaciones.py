from Repositorios.RepositorioUsuarioTarea import RepositorioUsuarioTarea
from schemas.Asignacion_Schema import Asignar_Tarea
from schemas.Response_Schema import AsignacionResponse


class ServicioAsignaciones:
    def __init__(self, repositorio_usuario_tarea: RepositorioUsuarioTarea):
        self.repositorio_usuario_tarea = repositorio_usuario_tarea

    def asignar_tarea(self, payload: Asignar_Tarea) -> AsignacionResponse:
        self.repositorio_usuario_tarea.asociar_tareas_usuarios(payload.tarea_id, payload.persona_ids)

        return AsignacionResponse(
            tarea_id=payload.tarea_id,
            persona_ids=payload.persona_ids,
            asignadas=True,
        )
