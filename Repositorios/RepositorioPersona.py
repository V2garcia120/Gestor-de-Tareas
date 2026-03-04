from sqlite3 import Connection


class RepositorioPersona:

    def __init__(self, conexion: Connection):
        self.conn = conexion
    
    def crear_persona(self, nombre: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT INTO Persona (nombre) VALUES (?)
            ''',
            (nombre,)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def buscar_persona_por_nombre(self, nombre: str) -> dict | None:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT id, nombre FROM Persona WHERE nombre = ?
            ''',
            (nombre,)
        )
        fila = cursor.fetchone()
        if fila is None:
            return None
        return {"id": fila[0], "nombre": fila[1]}
    