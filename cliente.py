import json
import requests

BASE = "http://localhost:8000"

def separador(titulo: str):
    print(f"\n{'-'*50}")
    print(f"  {titulo}")
    print(f"{'*'*50}")

def mostrar(resp):
    print(f"Status: {resp.status_code} | OK: {resp.ok}")
    try:
        body = resp.json()
        print(f"body: {json.dumps(body, indent=2, ensure_ascii=False)}")
    except ValueError:
        print(f"body: {resp.text}")
    except requests.exceptions.ConnectionError:
        print("No se pudo establecer conexion con el servidor")

separador("GET / - Raiz")
mostrar(requests.get(BASE + "/"))

separador("GET /estudiantes")
mostrar(requests.get(BASE + "/estudiantes"))

separador(" GET /estudiantes/1 - Por id" )
mostrar(requests.get(BASE + "/estudiantes/1"))

# if __name__ == "__main__":
#     print("Servidor iniciado")
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# import json
# import requests


# BASE = "http://localhost:8000"


# def separador(titulo: str):
#     print(f"\n {'-'*50}")
#     print(f"{titulo}")
#     print(f"\n {'-'*50}")


# def mostrar(resp):
#     if resp.status_code:
#         print(f"Body: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")


# separador("GET / - Raiz")
# mostrar(requests.get(f"{BASE}/"))

# separador("GET / - Estudiantes")
# mostrar(requests.get(f"{BASE}/students"))

# separador("GET / - Estudiante ID 1")
# mostrar(requests.get(f"{BASE}/students/1/"))