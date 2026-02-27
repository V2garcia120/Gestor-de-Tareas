from DataClasses import Tarea
from sqlite3 import Connection
class RepositorioTareas:


    def __init__(self, conexion: Connection):
        self.conn = conexion
        pass

    def ObtenerTareas(self, idPErsona) -> Tarea:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT t.id, t.nombre, t.urgencia, t.descripccion, t.completada
            FROM Tarea t
            INNER JOIN AsignacionTarea a ON a.idTarea = t.id
            WHERE a.idPersona = ?
            ''',
            (idPErsona,)
        )
        return cursor.fetchall()

    def TotalTareas():
        pass

    def CrearTarea(self, tarea: Tarea) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO Tarea (nombre, urgencia, descripccion) VALUES (?, ?, ?)
            ''',
            (tarea.nombre, tarea.urgencia, tarea.descripcion)
        )
        self.conn.commit()
        return cursor.lastrowid


    def EliminarTarea():
        pass

    def CompletarTarea():
        pass
    
    pass

