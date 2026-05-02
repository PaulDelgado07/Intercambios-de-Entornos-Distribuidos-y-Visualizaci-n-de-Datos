from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(
    title="API DEMO Academico",
    description="API DEMO Academico prueba",
    version="1.0.0",
)

 
class Estudiante(BaseModel):
    nombre: str = Field(..., min_length=2)
    carrera: str = Field(..., min_length=2)
    nota: float = Field(..., ge=0, le=10)


class EstudianteOut(Estudiante):
    id: str


db: List[dict] = [
    {
        "id": "1",
        "nombre": "Paul",
        "carrera": "Ingenieria de Datos en IA",
        "nota": 10,
    },
    {
        "id": "2",
        "nombre": "Andres",
        "carrera": "Ingenieria de Software",
        "nota": 8,
    },
    {
        "id": "3",
        "nombre": "Daniela",
        "carrera": "Ingenieria de Gastronomia",
        "nota": 7,
    }
]


def buscar(id: str):
    return next((e for e in db if e["id"] == id), None)


@app.get("/", tags=["Inicio"])
def raiz():
    return {
        "API": "Gestion Academica",
        "version": "1.0.0",
    }


@app.get("/estudiantes", tags=["Estudiantes"])
def listar(
    carrera: Optional[str] = Query(None, min_length=2),
    min_nota: Optional[float] = Query(None, ge=0, le=10),
    max_nota: Optional[float] = Query(None, ge=0, le=10),
):
    resultado = db[:]

    if carrera:
        resultado = [e for e in resultado if e["carrera"].lower() == carrera.lower()]

    if min_nota is not None:
        resultado = [e for e in resultado if e["nota"] >= min_nota]

    if max_nota is not None:
        resultado = [e for e in resultado if e["nota"] <= max_nota]

    return {
        "total": len(resultado),
        "filtros": {
            "carrera": carrera,
            "min_nota": min_nota,
            "max_nota": max_nota,
        },
        "data": resultado,
    }


@app.get("/estudiantes/{id}", tags=["Estudiantes"])
def obtener(id: str):
    estudiante = buscar(id)
    if estudiante:
        return estudiante
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")


@app.post("/estudiantes", tags=["Estudiantes"], status_code=201)
def crear(estudiante: Estudiante):
    nuevo_id = str(max(int(e["id"]) for e in db) + 1) if db else "1"

    nuevo = {
        "id": nuevo_id,
        "nombre": estudiante.nombre,
        "carrera": estudiante.carrera,
        "nota": estudiante.nota,
    }

    db.append(nuevo)

    return {
        "mensaje": "Estudiante creado exitosamente",
        "data": nuevo,
    }


#uvicorn servidor:app --reload