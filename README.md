# EcoLogistics - Evaluación Práctica (CSV -> JSON -> API REST)

## Requisitos
- Python 3.10+ (probado en macOS)
- pip y venv disponibles

## Instalación y ejecución
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pydantic
uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload





```

## Logs esperados
```
[INFO] Archivo cargado con 3 registros.
[INFO] Datos transformados a formato JSON.
[INFO] API iniciada en puerto 8080.
```

## Endpoints
- GET http://127.0.0.1:8080/envios  
- GET http://127.0.0.1:8080/envios/{id}  
- POST http://127.0.0.1:8080/envios  

## OpenAPI
Archivo `openapi.yaml` incluido. (FastAPI también expone `/docs` y `/openapi.json`).

## Pruebas con Postman / Newman
- Importa `postman_collection.json` en Postman y ejecútala.
- O bien:
```bash
npm install -g newman
newman run postman_collection.json
```

## Estructura del proyecto
```
src/main.py
envios.csv
openapi.yaml
postman_collection.json
README.md
reflexion.pdf
```

## Notas
- Los datos se mantienen en memoria (no hay base de datos).
- JSON estandarizado: `{id, cliente, direccion, estado}`.
