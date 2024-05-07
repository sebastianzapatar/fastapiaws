from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float

class Persona(BaseModel):
    nombre: str
    edad: int
    estatura: float
    peso: float

def IMC(persona: Persona):
    return persona.peso / (persona.estatura ** 2)

normal = []
sobrepeso = []
obesidad = []


@app.post("/persona")
def create_persona(persona: Persona):
    imc = IMC(persona)
    if imc < 25:
        print(imc)
        normal.append(persona)
    elif imc < 30:
        print(imc)
        sobrepeso.append(persona)
    else:
        print(imc)
        obesidad.append(persona)
    return {"message": "Persona creada"}
@app.get("/personaObesidad")
def get_obesidad():
    return {"Obesos":obesidad}
@app.get("/personaSobrepeso")
def get_sobrepeso():
    return {"Sobrepeso":sobrepeso}
@app.get("/personaNormal")
def get_normal():
    return {"Normal":normal}
"""
Crear un modelo que reciba la edad de una persona, el nombre, la edad
estatura y peso, dependeindo del peso y la estatura calcular el IMC,
Clasificarlos como bajo peso, normal, sobrepeso, obesidad
Cada uno tiene un vector, luego listar los datos de las personas
con peso normal, sobrepeso y obesidad (Cada uno es una lista)
"""
items = []


@app.get("/")
def read_root():
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items")
def create_item(item: Item):
    # Add item to the list
    items.append(item)
    return {"message": item}

    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)