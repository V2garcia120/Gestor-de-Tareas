import sqlite3


DB_NAME = 'tareas.db'


def _migrar_columna_descripcion(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Tarea)")
    columnas = {fila[1] for fila in cursor.fetchall()}

    if "descripccion" in columnas and "descripcion" not in columnas:
        cursor.execute("PRAGMA foreign_keys = OFF;")
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Tarea_nueva (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                urgencia TEXT,
                descripcion TEXT,
                completada INTEGER DEFAULT 0
            )
            '''
        )
        cursor.execute(
            '''
            INSERT INTO Tarea_nueva (id, nombre, urgencia, descripcion, completada)
            SELECT id, nombre, urgencia, descripccion, completada
            FROM Tarea
            '''
        )
        cursor.execute('DROP TABLE Tarea')
        cursor.execute('ALTER TABLE Tarea_nueva RENAME TO Tarea')
        cursor.execute("PRAGMA foreign_keys = ON;")


def init_db():
    with getConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tarea (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                urgencia TEXT,
                descripcion TEXT,
                completada INTEGER DEFAULT 0
                
            )
        ''')

        _migrar_columna_descripcion(conn)

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Persona (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS AsignacionTarea (
                idTarea INTEGER NOT NULL,
                idPersona INTEGER NOT NULL,
                PRIMARY KEY (idTarea, idPersona),
                FOREIGN KEY (idTarea) REFERENCES TAREA(id) ON DELETE CASCADE,
                FOREIGN KEY (idPersona) REFERENCES Persona(id) 
            )
        ''')

def getConnection():
    return sqlite3.connect(DB_NAME)