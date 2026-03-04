from sqlite3 import Connection

from schemas.DataClasses import Tarea


class RepositorioTareas:
    def __init__(self, conexion: Connection):
        self.conn = conexion

    def obtener_tareas_de_persona(self, id_persona: int) -> list[dict]:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT t.id, t.nombre, t.urgencia, t.descripcion, t.completada
            FROM Tarea t
            INNER JOIN AsignacionTarea a ON a.idTarea = t.id
            WHERE a.idPersona = ?
            ''',
            (id_persona,),
        )
        filas = cursor.fetchall()
        return [
            {
                "id": fila[0],
                "nombre": fila[1],
                "urgencia": fila[2],
                "descripcion": fila[3],
                "completada": fila[4],
            }
            for fila in filas
        ]

    def crear_tarea(self, tarea: Tarea) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO Tarea (nombre, urgencia, descripcion) VALUES (?, ?, ?)
            ''',
            (tarea.nombre, tarea.urgencia, tarea.descripcion),
        )
        self.conn.commit()
        return cursor.lastrowid

