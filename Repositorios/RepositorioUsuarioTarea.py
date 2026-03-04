from sqlite3 import Connection


class RepositorioUsuarioTarea:

    def __init__(self, conexion: Connection):
        self.conn = conexion

    def asociar_tareas_usuarios(self, tarea_id: int, usuario_ids: list[int] | int):
        cursor = self.conn.cursor()
        if isinstance(usuario_ids, (list, tuple, set)):
            ids = usuario_ids
        else:
            ids = [usuario_ids]

        for persona_id in ids:
            cursor.execute(
                '''
                INSERT OR IGNORE INTO AsignacionTarea (idTarea, idPersona) VALUES (?, ?)
                ''',
                (tarea_id, persona_id)
            )

        self.conn.commit()