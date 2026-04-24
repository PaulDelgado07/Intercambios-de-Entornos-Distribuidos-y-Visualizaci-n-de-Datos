# HTTP/rest, gRCP y WebSockets

## El modelo cliente-servidor y pila de protocolos.

Toda la comunicacion en red se organiza en capas. El modelo OSI (Open System Interconnection) define 7 capas, y la pila TCP/IP del internet real simplifica esto a 4 capas. Los protocols que estudiaremos operan en la capa de aplicación, la más alta, y se apoyan en las capas inferiones para el transporte y direccionamiento (TCP/IP) .....

# tabla

| Capa                      | Protocolo                        | Responsabilidad                                           |
| :------------------------ | :------------------------------- | :-------------------------------------------------------- |
| **Aplicación** (capa 7/4) | HTTP, gRPC, WebSocket, DNS, SMTP | Lógica de la aplicación: qué datos y cómo se interpretan. |
| **Transporte** (capa 4/3) | TCP, UDP                         | Entrega confiable (TCP) o rápida sin garantía (UDP).      |
| **Red** (capa 3/2)        | IP, ICMP                         | Enrutamiento entre redes: de origen a destino.            |
| **Enlace** (capa 2/1)     | Ethernet, WiFi                   | Transmisión física en la red local.                       |

## 1. HTTP protocolo de hipertextos

EL HHTP es un protocolo de transferencia de hipertexto que sustenta la web. Ha evolucionado significativamente desde su invencion en 1991 y es importante que el estudiante conozca las diferencias entre versiones porque afectan el redimiento y las capacidades de las APis que se construyan.

| Versión      | Año  | Conexiones               | Características principales                                                              |
| :----------- | :--- | :----------------------- | :--------------------------------------------------------------------------------------- |
| **HTTP/0.9** | 1991 | Una por petición         | Solo GET, solo HTML, sin cabeceras.                                                      |
| **HTTP/1.0** | 1996 | Una por petición         | Métodos GET/POST/HEAD, cabeceras, códigos de estado, tipos MIME.                         |
| **HTTP/1.1** | 1997 | Persistente (keep-alive) | Host obligatorio, chunked transfer, pipelining, compresión gzip.                         |
| **HTTP/2**   | 2015 | Multiplexada             | Múltiples peticiones en paralelo por una sola conexión TCP. HPACK, Server push, Binario. |
| **HTTP/3**   | 2022 | QUIC (sobre UDP)         | Abandona TCP por QUIC. Elimina head-of-line blocking. Más rápido en redes inestables.    |

Las cabeceras son pares de clave-valor que transportan metainformacion sobre la peticion o respuestas. Son inivisbles para el usuario final pero son criticas para el correcto funcionamiento de las APIs.

| Término                | Definición / Descripción                                                                                                               |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| **Content-Type**       | Indica el formato del cuerpo del mensaje. Ej: `application/json`, `text/xml`, `multipart/form-data`.                                   |
| **Accept**             | Indica los formatos que el cliente acepta en la respuesta. Negociación de contenido.                                                   |
| **Authorization**      | Credenciales de autenticación: `Basic <base64>`, `Bearer <token>`, `ApiKey <clave>`.                                                   |
| **Cache-Control**      | Directivas de caché: `no-cache`, `max-age=3600`, `no-store`, `must-revalidate`.                                                        |
| **Content-Encoding**   | Compresión aplicada al cuerpo: `gzip`, `deflate`, `br` (Brotli).                                                                       |
| **ETag**               | Identificador de versión de un recurso. Permite caché condicional.                                                                     |
| **If-None-Match**      | El cliente envía el ETag que tiene; el servidor solo responde si el recurso cambió (`304 Not Modified` si no hay cambio).              |
| **X-Request-ID**       | ID único de la petición para trazabilidad en sistemas distribuidos. No es estándar pero es una práctica universal.                     |
| **CORS (3 cabeceras)** | `Access-Control-Allow-Origin`, `-Methods`, `-Headers`: controlan qué orígenes pueden hacer peticiones cross-domain desde el navegador. |

## El ciclo completo de una peticion HTTP

- Resolucion de DNS: Se resuelve el nombre de dominio de una IP (generalmente cacheada).
- Establecimiento de conexion TCP: Se establece una conexion TCP con el servidor
- Conexion TCP: Una vez establecida la conexion se establecen las negociaciones de TLS/SSL ()
- Envio de la peticion HTTP al servidor: linea de petición + cabeceras + cuerpo (opcional)
- Procesamiento en el servidor: El servidor parsea la petición, ejecutra la lógica, la consulta de la base de datos.
- Envio de la respuesta HTTP al cliente: linea de respuesta + cabeceras + cuerpo JSON/XML.
- La conexcion TCP puede mantenerse (Keep-alive en HTTP/1.1) o cerrarse.

| Término     | Definición                                                                |
| :---------- | :------------------------------------------------------------------------ |
| **GET**     | Solicita un recurso. No modifica el estado del servidor. Idempotente.     |
| **POST**    | Envía datos para crear un nuevo recurso. No idempotente.                  |
| **PUT**     | Reemplaza completamente un recurso existente. Idempotente.                |
| **PATCH**   | Modifica parcialmente un recurso. Puede no ser idempotente.               |
| **DELETE**  | Elimina un recurso. Idempotente.                                          |
| **HEAD**    | Igual que GET pero sin cuerpo en la respuesta. Para verificar existencia. |
| **OPTIONS** | Consulta los métodos disponibles para un recurso (usado en CORS).         |

## Codigos de estado HTTP

Los codigos de estado comunican el resultado de la peticón. Se agrupan en centenas:

- 1xx: Informativo
- 2xx: Exito (200 OK, 201 Creado, 204 No contenido)
- 3xx: Redireccion (301 Moved Permanently, 302 Found, 304 Not Modified)
- 4xx: Error del cliente (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
- 5xx: Error del servidor (500 Internal Server Error, 501 Not Implemented, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout)

# 2. REST (Representational State Transfer)

## REST - Representational State Transfer - Analisis profundo

REST fue definido por Roy Fielding en su disertacion doctoral en el 2000. No es un protocolo, sino un estilo de arquitectura de software que se basa en el protocolo HTTP y utiliza métodos HTTP (GET, POST, PUT, DELETE) para realizar operaciones sobre recursos.

## Los 6 principios de REST son:

1. Cliente-Servidor : Esta separacion permite que los clientes y servidores se desarrollen de forma independiente.
2. Sin estado : Cada peticion es independiente y contiene toda la informacion necesaria para ser procesada.
3. Cachéable : Las respuestas pueden ser cacheadas para mejorar el rendimiento.
4. Interfaz uniforme : Las operaciones se realizan sobre recursos utilizando metodos HTTP estandar.
5. Sistema en capas : La arquitectura puede tener capas intermedias para mejorar la seguridad o el rendimiento.
6. Código bajo demanda (opcional) : El servidor puede enviar codigo para ser ejecutado por el cliente

### Diseño de una API RESTful

| Metodo     | URL                        | Accion                       | Respuesta exitosa        |
| :--------- | :------------------------- | :--------------------------- | :----------------------- |
| **GET**    | `/cursos`                  | Lista todos los cursos       | 200 + array JSON         |
| **GET**    | `/cursos/{id}`             | Obtiene un curso específico  | 200 + objeto JSON        |
| **POST**   | `/cursos`                  | Crea un nuevo curso          | 201 + objeto creado      |
| **PUT**    | `/cursos/{id}`             | Reemplaza un curso           | 200 + objeto actualizado |
| **PATCH**  | `/cursos/{id}`             | Actualiza campos específicos | 200 + objeto parcial     |
| **DELETE** | `/cursos/{id}`             | Elimina un curso             | 204 sin cuerpo           |
| **GET**    | `/cursos/{id}/estudiantes` | Lista estudiantes del curso  | 200 + array JSON         |

## Autenticación en APis REST

las Apis REST son sin estado, por lo que no mantienen sesiones. La autenticación se delega a tokens que el cliente envia en cada petición. Los mecanismos más comunes son:

- API keys : una clave unica que se envia en cada peticion. Simple pero sin control de expiración.
- Bearer tokens (JWT) : El servidor emite un token firmado digitalmente que incluye en Authorization: Bearer <token>. El servidor verifica la firma sin consultar la base de datos.
  -OAuth 2.0 : Flujo de autorización delegada. Permite que una app actue en nombre del usuario sin conocer su contraseña (usando por google, github, etc).

# 3. gRPC (Google Remote Procedure Call)

gRPC es un framework de comunicación de alto rendimiento desarrollado por google y publicado como codigo abierto en 2016. Mientras REST modela la comunicación como acceso a recursos, gRPC modela como llamadas a funciones remotas, como si el servicio remoto fuera una biblioteca local.

## Protocol buffers (Protobuf)

gRPC usa Potocol Burffers como formato de serialización binaria. A diferencia de JSON, Protobuf serializa los datos en bytes de forma compacta. Un mensaje JSON que ocupa 200 bytes puede ocupar 40 bytes en Protobuf. Además, la serialización y deserialización es entre 5 a 10 veces más rápida en Protobuf que en JSON.

## Cuando elegir gRPC sobre REST?

- Comunicación interna entre microservicios donde la velocidad es crítica.
- Contratos de interfaz estrictos que varios equipos deben respetar.
- Streaming bidireccional donde el cliente y el servidor envian mensajes de forma continua.
- Ambientes polyglota donde los servicios se implementan en diferentes lenguajes de programación. (el.proto genera codigo para Go, python, java, Java, C++, C#, Ruby etc).

## gRPC vs REST

| Característica    | REST                                          | gRPC                                         | Ventaja para el estudiante                               |
| ----------------- | --------------------------------------------- | -------------------------------------------- | -------------------------------------------------------- |
| Formato de datos  | JSON (texto, legible)                         | Protobuf (binario, compacto)                 |                                                          |
| Rendimiento       | Más lento (analisis de texto)                 | Más rápido (serialización binaria)           | gRPC consume menos ancho de banda y es más rápido        |
| Contrato de datos | Flexible, no obligatorio                      | Esquema obligatorio (definido en .proto)     | gRPC fuerza contratos bien definidos, reduciendo errores |
| Casos de uso      | APIs web públicas, integración entre sistemas | Microservicios, comunicación interna, mobile | gRPC es ideal para sistemas distribuidos                 |

# WebSocket -- Comunicación bidireccional persistente

HTTP sigue el modelo pull: el cliente pregunta y el servidor responde. En aplicaciones que necesitan que el servidor envie datos sin que el cliente lo soicite (dashboard en vivo, notificaciones, sensores loT), HTTP obliga a usar técnicas ineficientes como polling o long-polling.

Websocket resuelvre esto con una conexión TCP persistente y full duplex: una vez establecida, tanto cliente como servidor pueden enviar datos en cualquier momento sin necesidad de nuevas peticiones HTTP.

## Caso de uso: dashboards en tiempo real

Imaginemos que queremos construir un dashboard que muestre en tiempo real el precio de las acciones. Sin websocket, tendríamos que usar long-polling:

1. El cliente hace una petición GET al servidor asking por el precio.
2. El servidor espera hasta que el precio cambie o hasta que pase un tiempo máximo (ej. 5 segundos) y responde.
3. El cliente vuelve a hacer la petición GET.
4. Se repite el proceso.

| Característica              | HTTP/REST                | gRPC                     | WebSockets               |
| :-------------------------- | :----------------------- | :----------------------- | :----------------------- |
| **Modelo**                  | Petición-Respuesta       | Llamada a función remota | Mensajería bidireccional |
| **Conexión**                | Se cierra tras respuesta | Se cierra tras respuesta | Permanente               |
| **Formato**                 | JSON / XML (texto)       | Protobuf (binario)       | Texto o binario          |
| **Velocidad relativa**      | Media                    | Alta                     | Alta                     |
| **Streaming**               | No nativo                | Sí (4 modos)             | Sí (bidireccional)       |
| **Facilidad de uso**        | Muy alta                 | Media                    | Media                    |
| **APIs públicas**           | Ideal                    | No recomendado           | No recomendado           |
| **Microservicios internos** | Aceptable                | Ideal                    | Posible                  |
| **Tiempo real / push**      | No                       | Parcialmente             | Ideal                    |
| **En este curso**           | FastAPI                  | Introducción teórica     | Con Kafka                |

## tarea

1. Buscar por ID  
   http://localhost:8000/docs
2. completar el post solo un post que permita crear un nuevo dato.

---
