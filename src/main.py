import csv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

class Envio(BaseModel):
    id: str
    cliente: str
    direccion: str
    estado: str

app = FastAPI(title="EcoLogistics API", version="1.0.0")

# Almacenamiento en memoria
ENVIOS: List[Envio] = []

def cargar_csv_a_memoria(ruta_csv: str) -> List[Envio]:
    registros = []
    with open(ruta_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Transformación CSV -> JSON estandarizado {id, cliente, direccion, estado}
            registros.append(Envio(
                id=row["id_envio"],
                cliente=row["cliente"],
                direccion=row["direccion"],
                estado=row["estado"]
            ))
    return registros

@app.on_event("startup")
def startup_event():
    global ENVIOS
    ENVIOS = cargar_csv_a_memoria("envios.csv")
    print(f"[INFO] Archivo cargado con {len(ENVIOS)} registros.")
    print("[INFO] Datos transformados a formato JSON.")
    print("[INFO] API iniciada en puerto 8080 (cuando uvicorn arranque).")

@app.get("/envios", response_model=List[Envio], summary="Lista todos los envíos")
def listar_envios():
    return ENVIOS

@app.get("/envios/{id}", response_model=Envio, summary="Obtiene un envío por ID")
def obtener_envio(id: str):
    for e in ENVIOS:
        if e.id == id:
            return e
    raise HTTPException(status_code=404, detail="Envío no encontrado")

@app.post("/envios", response_model=Envio, status_code=201, summary="Crea un nuevo envío")
def crear_envio(envio: Envio):
    # Validar duplicado simple
    if any(e.id == envio.id for e in ENVIOS):
        raise HTTPException(status_code=409, detail="ID duplicado")
    ENVIOS.append(envio)
    print(f"[INFO] Nuevo envío registrado: {envio.id}")
    return envio

if __name__ == "__main__":
    # Ejecución directa opcional
    uvicorn.run("src.main:app", host="0.0.0.0", port=8080, reload=True)