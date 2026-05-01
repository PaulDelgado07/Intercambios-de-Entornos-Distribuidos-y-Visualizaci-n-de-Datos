from fastapi import FastAPI, WebSocket, Query, HTTPException # me falto importar HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title = "API DEMO Academico",
    description = "API DEMO Academico prueba",
    version = "0.0.1", 
)

class Estudiante(BaseModel):
    nombre: str = Field(..., min_length=2)
    carrera: str = Field(...,min_length=2)
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
    carrera: Optional[str] = Query(None, min_length=2), # habia puesto mal 'min_nota' por 'nota_min' y viceversa.
    min_nota: Optional[float] = Query(None, ge=0, le=10),
    max_nota: Optional[float] = Query(None, ge=0, le=10),
):
    resultado = db[:]
    if carrera:
        resultado = [e for e in resultado if e['carrera'].upper() == carrera.upper()] # aqui corregi bien los nombres que eran de la funcion listar 
    if min_nota is not None:
        resultado = [e for e in resultado if e['nota'] >= min_nota]
    if max_nota is not None:
        resultado = [e for e in resultado if e['nota'] <= max_nota]
    return {
        "total": len(resultado),
        "Filtro": {
            "carrera" : carrera,
            "min_nota": min_nota,
            "max_nota": max_nota,
        },
        "data": resultado,
    }

@app.get(path="/estudiantes/{id}",tags=["Estudiantes"]) # Aqui habia añadido el formato "f" y no me salia, así que le quité 
def obtener(id:str):
    for estudiante in db:
        if estudiante["id"] == id:
            return estudiante
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
#Para encender mi servidor es: uvicorn servidor:app --reload