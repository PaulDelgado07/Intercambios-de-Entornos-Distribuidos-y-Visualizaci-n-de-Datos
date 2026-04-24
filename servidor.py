from fastapi import FastAPI, WebSocket, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title = "API DEMO Academico",
    description = "API DEMO Academico prueba",
    version = "0.0.1", 
)

class Estudiante(BaseModel):
    nombre: str = Field(..., min_length=2),
    carrera: str = Field(...,min_length=2),
    nota: int = Field(...,ge=0, le=10)
    
class EstudiantesOut(Estudiante):
    id: str


db: list[dict] = [
    {
        "id" : "1",
        "nombre" : "Paul",
        "carrera" : "Ingenieria de Datos en IA",
        "nota": 10,
    },
    {
        "id" : "2",
        "nombre" : "Andres",
        "carrera" : "Ingenieria de Software",
        "nota": 8,
    },
    {
        "id" : "3",
        "nombre" : "Daniela",
        "carrera" : "Ingenieria de Gastronomia",
        "nota": 7,
    }
]

def buscar(id:str):
    return next(
        (e for e in db if e["id"] == id), None
    )


@app.get("/",tags=["Inicio"])
def raiz():
    return {
        "API": "Gestion Academica",
        "version": "1.0.0",
    }

@app.get(path="/estudiantes",tags=["Estudiantes"])
def listar(
    carrera: Optional[str] = Query(None, min_length=2),
    min_nota: Optional[float] = Query(None, ge=0, le=10),
    max_nota: Optional[float] = Query(None, ge=0, le=10)
):
    resultado = db[:]
    if carrera:
        resultado = [e for e in resultado if e['carrera'].upper() == carrera.upper()]
    if nota_min is not None:
        resultado = [e for e in resultado if e['nota'] >= nota_min]
    if nota_max is not None:
        resultado = [e for e in resultado if e['nota'] <= nota_max]
    return {
        "total": len(resultado),
        "Filtro": {
            "carrera" : carrera,
            "min_nota": nota_min,
            "max_nota": nota_max,
        },
        "data": resultado,
    }

@app.get(path="/estudiantes/{id}",tags=["Estudiantes"])
def obtener(id:str):
    for estudiante in db:
        if estudiante["id"] == id:
            return estudiante
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")
