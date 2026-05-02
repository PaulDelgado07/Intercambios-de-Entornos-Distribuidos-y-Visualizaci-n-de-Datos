import json
import requests

BASE = "http://localhost:8000"

def separador(titulo: str):
    print(f"\n{'-'*50}")
    print(f"  {titulo}")
    print(f"{'-'*50}")

def mostrar(url: str):
    try:
        resp = requests.get(url)
        print(f"Status: {resp.status_code} | OK: {resp.ok}")
        
        try:
            body = resp.json()
            print(json.dumps(body, indent=2, ensure_ascii=False))
        except ValueError:
            print(resp.text)

    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con el servidor")

# Pruebas
separador("GET / - Raiz")
mostrar(BASE + "/")

separador("GET /estudiantes")
mostrar(BASE + "/estudiantes")

separador("GET /estudiantes/1 - Por ID")
mostrar(BASE + "/estudiantes/1")

# Ejemplo con filtros
separador("GET /estudiantes?min_nota=8")
mostrar(BASE + "/estudiantes?min_nota=8")