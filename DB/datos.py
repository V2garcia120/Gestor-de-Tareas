import sqlite3


DB_NAME = 'tareas.db'

def init_db():
    with getConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tarea (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                urgencia TEXT,
                descripccion TEXT,
                completada INTEGER DEFAULT 0
                
            )
        ''')

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