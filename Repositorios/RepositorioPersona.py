from schemas.DataClasses import Tarea
from sqlite3 import Connection

class RepositorioPersona:

    def __init__(self, conexion: Connection):
        self.conn = conexion
    
    def CrearPersona(self, nombre: str):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO Persona (nombre) VALUES (?)
            ''',
            (nombre,)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def ActualizarPersona(self):
        pass
    
    def BuscarPersona(self, nombre) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT id FROM Persona WHERE nombre = ?
            ''',
            (nombre,)
        )
        return cursor.fetchone()

    def EliminarPersona(self):
        pass
    