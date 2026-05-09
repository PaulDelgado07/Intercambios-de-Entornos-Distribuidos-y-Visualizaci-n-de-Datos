from fastapi import FastAPI, Query, HTTPException 
from pydantic import BaseModel, Field
from typing import List, Optional 

app = FastAPI(
    title= "API Demo developer",
    description = "Esta es una api para ver usuarios",
    version = "1.0.0",
)

class Estudiantes(BaseModel):
    nombre : str = Field(..., min_length=2, description="Nombre del Estuidante")
    carrera : str = Field(..., min_length=2, description="carrera del estudiante")
    nota : float = Field(...,ge=0 , le=10, description="Notas del estudiante")

class EstudianteOut(Estudiantes):
    id : str

db : List[dict] = [
    {"id":"1", "nombre": "Paul David", "carrera":"Ciencias de datos e Inteligencia Artifical", "Nota": 10},
    {"id":"2", "nombre": "Koraima Merchán", "carrera":"Gastronomía", "Nota": 9},
    {"id":"3", "nombre": "Carlos Estupiñan", "carrera":"Ingienería en Sistemas", "Nota": 8},
]


print("Hola mundo")
print("hola mundo")


