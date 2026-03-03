from contextlib import asynccontextmanager

from fastapi import FastAPI

from DB.datos import init_db
from rutas.asignaciones import router as asignaciones_router
from rutas.personas import router as personas_router
from rutas.tareas import router as tareas_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(title="Aburri2 API", lifespan=lifespan)


@app.get("/")
def health_check():
    return {"status": "ok"}


app.include_router(personas_router)
app.include_router(tareas_router)
app.include_router(asignaciones_router)