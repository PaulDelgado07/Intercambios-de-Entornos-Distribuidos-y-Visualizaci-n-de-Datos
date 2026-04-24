import json
import requests

BASE = "http://localhost:8000"

def separador(titulo: str):
    print(f"\n{'-'*50}")
    print(f"  {titulo}")
    print(f"{'*'*50}")

def mostrar(resp):
    print("Status: {resp.status_code}")
    if resp.status_code:
        print("body: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    else:
        print("body: {resp.text}")

separador("GET / - Raiz")
mostrar(requests.get(BASE + "/"))

separador("GET /estudiantes")
mostrar(requests.get(BASE + "/estudiantes"))

separador(" GET /estudiantes/1 - Por id" )
mostrar(requests.get(BASE + "/estudiantes/1/"))

if __name__ == "__main__":
    print("Servidor iniciado")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)