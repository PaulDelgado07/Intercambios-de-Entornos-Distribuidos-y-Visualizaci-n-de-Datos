### Contenedores Docker

Docker es una plataforma de codigo abierto que permite a los desarrolladores crear, desplegar y ejecutar aplicaciones en contenedores

Los contenedores son componentes estandarizados y ejecutables que combinan el codigo fuente de la aplicacion con las bibliotecas del sistema operativo (SO) y las dependencia necesarias para ejecutar ese codigo en cualquier entorno.

Los contenedores simplifican el desarrollo y la entrega de aplicaciones distribuidas.
Se han vuelto cada vez más populares a medida que las organizaciones pasan al desarrollo nativo de la nube y a los entornos híbridos multinube.
Los desarrolladores pueden crear contenedores sin Docker trabajando directamente con las capacidades integradas en Linux y otros sistemas operativos, pero Docker hace que la contenerización sea más rápida y sencilla.

Es importante señalar que cuando la gente habla de Docker, normalmente se refiere a Docker Engine, el tiempo de ejecución para crear y ejecutar contenedores. Docker también se refiere a Docker, Inc.¹, la empresa que vende la versión comercial de Docker. También está relacionado con el proyecto de código Docker², al que contribuyen Docker, Inc. y muchas otras organizaciones y personas.

Se denominan contenedores por su analogía con los contenedores de los barcos, las características que comparten son muchas: su contenido está aislado, pueden alojar cualquier objeto, se pueden transportar fácilmente. Los contenedores revolucionaron el transporte, redujeron el coste, los tiempos de carga y descarga, los daños en la mercancía... hoy en día el 90% de los envíos se realizan en contenedores estándar.

# Introducción a Docker y Contenedores

Es importante señalar que cuando la gente habla de Docker, normalmente se refiere a **Docker Engine**, el tiempo de ejecución para crear y ejecutar contenedores. Docker también se refiere a **Docker, Inc.¹**, la empresa que vende la versión comercial de Docker. También está relacionado con el proyecto de código **Docker²**, al que contribuyen Docker, Inc. y muchas otras organizaciones y personas.

## ¿Qué son los contenedores?

Se denominan **contenedores** por su analogía con los contenedores de los barcos, las características que comparten son muchas: su contenido está **aislado**, pueden alojar cualquier objeto, se pueden transportar **fácilmente**. Los contenedores revolucionaron el transporte, redujeron el coste, los tiempos de carga y descarga, los daños en la mercancía... hoy en día el 90% de los envíos se realizan en contenedores estándar.

## Resolución de problemas en el software

En el mundo del software, los contenedores resuelven varios problemas críticos:

| Problema                      | Solución con Docker                          |
| :---------------------------- | :------------------------------------------- |
| Inconsistencia entre entornos | Empaqueta todo lo necesario en un contenedor |
| Conflictos de dependencias    | Aislamiento completo entre aplicaciones      |
| Tiempo de configuración       | Entornos reproducibles con un solo comando   |
| Recursos desperdiciados       | Uso eficiente y compartido de recursos       |

## Caso real de uso

Imagina un proyecto con una aplicación Python que requiere una versión específica de TensorFlow.

El equipo de ciencia de datos necesita Python 3.8, mientras que el equipo de backend usa Python 3.9.

Sin contenedores, esto sería una pesadilla de configuración.

Con Docker, cada equipo trabajaba en su propio contenedor, sin conflictos y con total independencia.

### ¿Qué problemas solucionamos con esto?

| Dolor tradicional               | Solución Docker                   |
| :------------------------------ | :-------------------------------- |
| "En mi PC funciona"             | Todo empaquetado en un contenedor |
| "Se me rompió otra dependencia" | Aislamiento total entre apps      |
| Configurar entornos eternos     | docker-compose up y listo         |
| Máquinas virtuales obesas       | Contenedores ligeros y ágiles     |

### Contenedores Docker versus Linux: ¿Cuál es la diferencia?

Los contenedores de Linux tradicionales usan un sistema init que puede gestionar varios procesos. Esto significa que las aplicaciones completas se pueden ejecutar como una sola. La tecnología Docker favorece la división de las aplicaciones en sus procesos individuales y ofrece las herramientas para hacerlo. Este enfoque de separación de los elementos tiene sus ventajas.

### ¿Cómo funciona Docker?

Docker utiliza una arquitectura cliente-servidor donde:

- **Docker Daemon (dockerd)** es el servidor que:
  - Gestiona contenedores
  - Maneja imágenes
  - Administra redes y almacenamiento
- **Docker Client (docker)** es la interfaz de usuario que:
  - Acepta comandos
  - Se comunica con el daemon
  - Puede conectarse a múltiples daemons

A continuación se muestra un desglose de los componentes principales asociados a Docker, junto con otros términos y herramientas de Docker.

- **Host Docker:** es una máquina física o virtual que ejecuta Linux (u otro sistema operativo compatible con Docker-Engine).
- **Docker Engine:** es una aplicación cliente/servidor que consta del Daemon de Docker, una API de Docker que interactúa con el Daemon y una interfaz de línea de comandos (CLI) que se comunica con el Daemon.

- **Objetos Docker:** los objetos Docker son componentes de una implementación de Docker que ayudan a empaquetar y distribuir aplicaciones. Incluyen imágenes, contenedores, redes, volúmenes, complementos y mucho más.

- **Contenedores Docker:** los contenedores Docker son las instancias vivas y en ejecución de las imágenes Docker. Mientras que las imágenes Docker son archivos de sólo lectura, los contenedores son contenidos vivos, efímeros y ejecutables. Los usuarios pueden interactuar con ellos y los administradores pueden ajustar su configuración y condiciones mediante comandos Docker.

- **Imágenes Docker:** una imagen Docker es un paquete de software que incluye todo lo necesario para ejecutar una aplicación: el código de la aplicación, los archivos de configuración, las bibliotecas y los archivos de tiempo de ejecución.

- **Dockerfile:** es un archivo de texto que contiene las instrucciones necesarias para crear una imagen Docker.

- **Docker build:** es un comando que se utiliza para crear una imagen Docker a partir de un Dockerfile.

- **docker hub:** es un repositorio en la nube de imágenes Docker.

- **docker desktop:** es una aplicacion que permite ejecutar Docker en Windows y macOS.

En resumen : Docker funciona de manera similar a como lo hace un contenedor de carga. En lugar de construir un barco para cada tipo de mercancía, se utilizan contenedores estándar que se pueden transportar en cualquier barco. Lo mismo ocurre con Docker: una vez que se crea una imagen, se puede ejecutar en cualquier entorno que tenga Docker instalado.