from DB.datos import  init_db
from schemas.DataClasses import Tarea
from Repositorios.RepositorioTareas import RepositorioTareas
from Repositorios.RepositorioUsuarioTarea import RepositorioUsuarioTarea
from Repositorios.RepositorioPersona import RepositorioPersona
from DB.datos import getConnection



if __name__ == '__main__':

    init_db()

    conection = getConnection()
    _repositorioTarea = RepositorioTareas(conection)
    _repositorioUsuarioTarea = RepositorioUsuarioTarea(conection)
    _repositorioPersona = RepositorioPersona(conection)

    tarea1 = Tarea(
        nombre="Prestar Atencion",
        urgencia="Inmediata",
        descripcion="clase de Desarrollo 3"

        )
    nombre = 'vimsil'

    idtarea = _repositorioTarea.CrearTarea(tarea1)
    idPersona = _repositorioPersona.CrearPersona(nombre)
    personasIds = [idPersona]
    _repositorioUsuarioTarea.Asociar_Tareas_Usuarios(idtarea, personasIds)

    buscartarea = _repositorioTarea.ObtenerTareas(idPersona)
    
    conection.commit()

    print(buscartarea)