# 🌐 HTTP/REST, gRPC y WebSockets

![API Architecture](image.png)

> **Una guía sobre protocolos de comunicación web y diseño de APIs.**

---

## 📑 Tabla de Contenidos
- [1. HTTP: Protocolo de Hipertexto](#1--http-protocolo-de-hipertexto)
- [2. REST: Representational State Transfer](#2--rest-representational-state-transfer)
- [3. Tareas Asignadas](#-3-tareas-asignadas)
- [4. Elementos Extra](#-4-elementos-extra-de-markdown)

---

## 1. 📡 HTTP: Protocolo de Hipertexto

El **HTTP** (Hypertext Transfer Protocol) es el protocolo fundamental de transferencia de hipertexto que sustenta la comunicación entre clientes y servidores en la web.

![HTTP Protocol](image-1.png)

### 🔑 Cabeceras (Headers)
Son pares de `clave: valor` que transportan meta-información sobre la petición o respuesta. 
> 💡 *Nota: Son invisibles para el usuario final pero son **críticas** para el correcto funcionamiento de las APIs.*

### 🔄 Ciclo completo de una petición HTTP
1. **Resolución de DNS:** Se resuelve la dirección IP del servidor.
2. **Establecimiento de conexión TCP:** Se establece la conexión con el servidor.
3. **Envío de la petición:** Se envía la petición HTTP al servidor.
4. **Procesamiento:** El servidor procesa la petición.
5. **Envío de la respuesta:** El servidor envía la respuesta HTTP al cliente.
6. **Mantenimiento:** La conexión TCP puede mantenerse abierta para enviar más peticiones.

![HTTP Flow 1](image.png)
![HTTP Flow 2](image-1.png)

---

## 2. 🏛️ REST (Representational State Transfer)

**REST** es un estilo de arquitectura de software utilizado para diseñar APIs. Se basa en el protocolo HTTP y utiliza métodos estándar (`GET`, `POST`, `PUT`, `DELETE`) para realizar operaciones sobre recursos.

### 🏗️ Los 6 Principios de REST

| Principio | Descripción |
| :--- | :--- |
| **1. Cliente-Servidor** | Esta separación permite que los clientes y servidores se desarrollen de forma independiente. |
| **2. Sin estado (Stateless)** | Cada petición es independiente y contiene toda la información necesaria para ser procesada. |
| **3. Cachéable** | Las respuestas pueden ser cacheadas para mejorar el rendimiento. |
| **4. Interfaz Uniforme** | Las operaciones se realizan sobre recursos utilizando métodos HTTP estándar. |
| **5. Sistema en Capas** | La arquitectura puede tener capas intermedias para mejorar la seguridad o el rendimiento. |
| **6. Código bajo demanda** | *(Opcional)* El servidor puede enviar código para ser ejecutado por el cliente. |

### 🛠️ Diseño de una API RESTful
![RESTful Design](image-2.png)

---

## 📝 3. Tareas Asignadas

- [ ] **1. Buscar por ID**
  - Probar en: [http://localhost:8000/docs](http://localhost:8000/docs)
- [ ] **2. Completar método POST**
  - Completar un post que permita crear un nuevo dato.
- [ ] **3. Otra tarea (Pendiente de definir)**

---

## 🔧 4. Elementos Extra de Markdown

Aquí tienes ejemplos de cómo enriquecer tus documentos:

### 🔗 Enlaces e Imágenes
* Puedes agregar un enlace así: 📖 [Guía Oficial de Markdown](https://www.markdownguide.org/basic-syntax/)
* Y una imagen así: `![Descripción de la imagen](ruta/a/tu/imagen.jpg)`

### ✅ Tareas por hacer (Checklist)
- [x] Tarea completada
- [ ] Tarea pendiente
- [ ] Otra tarea pendiente

---
*Documentación creada para el proyecto.*
