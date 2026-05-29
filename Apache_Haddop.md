# Que es el Apache Haddop

El software Apache Hadoop es un framework de código abierto que permite usar modelos sencillos de programación para almacenar y procesar de forma distribuida grandes conjuntos de datos de distintos clústeres de ordenadores.

Hadoop se ha diseñado para facilitar el escalado vertical de un solo ordenador a miles de ordenadores agrupados en clústeres, cada uno de ellos con funciones locales de computación y almacenamiento.

Gracias a ese diseño, Hadoop puede, Haddop puede almacenar y procesar conjuntos de datos de muchos gigabytes o insluso petabytes de manera eficiente.

# Como nace Apache Haddop

Hadoop nace como iniciativa de Apache para dar soporte al paradigma de programación **Map-Reduce**, que fue inicialmente publicado por Google.

El **propósito principal** del framework es almacenar grandes cantidades de datos y permitir consultas sobre dichos datos, que se ofrecerán con un bajo tiempo de respuesta. Esto se consigue mediante la ejecución distribuida de código en múltiples nodos (máquinas), cada uno de los cuales se encarga de **procesar** una parte del trabajo a realizar.

---

### Componentes de la Arquitectura (Diagrama)

* **Capas Superiores (Herramientas y Motores):**
  * **SQL**: Hive
  * **Real-Time**: HBase
  * **Script**: Pig
  * **Otros**: Storm, Solr,...

* **Capa Intermedia (Procesamiento y Gestión):**
  * **Map-Reduce**: Gestor de recursos distribuidos y procesamiento de datos

* **Capa Inferior (Almacenamiento):**
  * **HDFS**: Sistema de archivos distribuidos Hadoop

# Características de Apache Haddop

El framework principal de Hadoop consta de cuatro módulos que funcionan de manera conjunta para constituir el ecosistema de Hadoop:

* **HDFS:** es el componente principal del ecosistema de Hadoop. Este sistema de archivos distribuidos franquea el acceso de alto rendimiento a los datos de las aplicaciones sin tener que definir esquemas con antelación.

* **YARN:** esta plataforma gestiona los recursos de computación de los clústeres y los utiliza para programar las aplicaciones de los usuarios. Se encarga de programar y asignar los recursos de todo el sistema de Hadoop.

* **MapReduce:** este modelo de programación permite procesar los datos a gran escala. Emplea algoritmos de computación distribuida y en paralelo para trasladar la lógica de procesamiento y facilitar la escritura de aplicaciones que transformen los conjuntos de datos grandes en un conjunto fácil de gestionar.

* **Hadoop Common:** incluye las bibliotecas y las utilidades que emplean y comparten otros módulos de Hadoop.

# ¿Cuáles son las herramientas de Hadoop?

* **Tolerancia a fallos:** En el ecosistema de Hadoop, por mucho que los nodos, discos o bastidores fallen al ejecutar tareas en clústeres grandes, los recuperas fácilmente, ya que los datos se replican en otras partes de los clústeres.

* **Control de costes:** Para mantener los costes a raya, el precio por terabyte de datos almacenados es menor en Hadoop que en otras plataformas. Hadoop ofrece las funciones de computación y almacenamiento en un hardware básico estándar más asequible, apenas unos cientos de dólares por terabyte.

* **Innovación con el framework de código abierto:** Hadoop tiene el respaldo de comunidades de todo el mundo cuyo afán común es presentar funciones y conceptos nuevos con más rapidez y eficacia que los equipos internos de las empresas que trabajan en soluciones propias. La ventaja de estas comunidades de software libre es el potencial colectivo para aportar más ideas, desarrollarlas más rápido y solucionar los problemas en cuanto aparecen. Todo ello se traduce en un tiempo de lanzamiento más corto.

# ¿Para qué se usa Haddop?

* **Analíticas y Big Data:** Hadoop permite que empresas y organizaciones de toda clase hagan investigaciones o analíticas y procesen los datos de producción, es decir, tareas que exigen procesar terabytes o petabytes de Big Data, a veces en paralelo, y almacenar conjuntos de datos diversos.

* **Sectores verticales:** Las empresas de innumerables sectores (entre otros, tecnología, educación, sanidad y servicios financieros) confían en Hadoop para ejecutar tareas que tienen en común la gran diversidad, volumen y velocidad de los datos estructurados y sin estructurar que emplean.

* **IA y aprendizaje automático:** Los ecosistemas de Hadoop también son fundamentales para facilitar el desarrollo de aplicaciones de inteligencia artificial (IA) y aprendizaje automático.

* **Cloud computing:** Por lo general, las empresas prefieren ejecutar los clústeres de Hadoop en recursos de nubes públicas, privadas o híbridas antes que en hardware on-premise porque no solo se benefician de más flexibilidad y disponibilidad, sino que también mantienen los costes bajo control.

# HDFS

HDFS (Hadoop Distributed File System) es el componente principal del ecosistema Hadoop. Esta pieza hace posible almacenar data sets masivos con tipos de datos estructurados, semi-estructurados y no estructurados como imágenes, vídeo, datos de sensores, etc. Está optimizado para almacenar grandes cantidades de datos y mantener varias copias para garantizar una alta disponibilidad y la tolerancia a fallos. Con todo esto, HDFS es una tecnología fundamental para Big Data, o dicho de otra forma, es el *Big Data File System* o almacenamiento Big Data por excelencia.

# CARACTERISTICAS DE HDFS

En HDFS, los ficheros que se almacenan son divididos en bloques de un mismo tamaño (128 MB) y estos se distribuyen en los nodos que forman el clúster. Esta característica hace que el sistema de ficheros no funcione de forma óptima con ficheros pequeños, por lo que deben evitarse. El tamaño de bloque es configurable.

---

### Componentes de la Imagen (Diagrama del Ecosistema Hadoop)

* **Gestión y Coordinación (Capas Externas):**
  * **Superior:** Ambari
  * **Lateral Izquierdo:** Zookeeper
  * **Lateral Derecho:** Oozie

* **Capas de Aplicación y Consulta:**
  * **Herramientas de Script/SQL:** Pig, Hive
  * **Base de Datos NoSQL:** HBase
  * **Motores de Procesamiento:** Spark, Tez, MapReduce

* **Capas de Infraestructura Core:**
  * **Gestión de Recursos:** YARN
  * **Almacenamiento:** HDFS


# ARQUITECTURA Y COMPONENTES DE HDFS

* **NameNode (NN)** es el maestro o nodo principal del sistema. No se encarga de almacenar los datos en sí, sino de gestionar su acceso y almacenar sus **metadatos**. Se asemeja a una tabla de contenidos, en la que se asignan bloques de datos a DataNodes. Debido a esto, necesita menos espacio de disco, pero más recursos computacionales (memoria y CPU) que los DataNodes.

* **DataNode (DN)** se corresponden con los nodos del clúster que almacenan los datos. Se encarga de gestionar el almacenamiento del nodo. Generalmente usan **hardware básico con varios discos y una gran capacidad**. A causa de su tipología, permiten aumentar la capacidad del sistema de una forma horizontal de forma efectiva y con un coste reducido.

# FUNCIONAMIENTO

HDFS tiene un modelo ***Write once read many***. Significa que no se pueden editar ficheros almacenados HDFS, pero sí se pueden añadir datos. Antes de poder usar HDFS, debemos formatear el NameNode con el comando *hdfs namenode -format*.

* En las **operaciones de escritura**, el cliente debe comunicar la instrucción previamente al NameNode. El NameNode comprueba los permisos y responde entonces al cliente con la dirección de los DataNodes en los que el cliente deberá empezar a escribir. El primer DataNode copiará el bloque a otro DataNode, que entonces lo copiará a un tercero. Una vez que se han completado estas réplicas se enviará al cliente la confirmación de escritura.

* En las **operaciones de lectura**, el cliente pide al NameNode la localización de un fichero. Una vez que se han comprobado los permisos del cliente, el NameNode envía la localización de los DataNodes que contienen los bloques que componen el fichero al cliente. También envía un *token* de seguridad que usará en los DataNodes como autenticación.

Por ejemplo, para escribir un fichero en HDFS se puede hacer con la opción *-put* del comando de terminal. Como ejemplos de operaciones de lectura de ficheros tenemos las opciones *-get*, *-cat* o *-text*. Para hacer referencia al sistema de ficheros de HDFS, generalmente deberemos usar una ruta que comience con *hdfs://*.

# PARADIGMA MAP-REDUCE

El procesado propuesto dentro del framework de Hadoop es el llamado MapReduce, propuesto por Google.

Como se puede deducir por su nombre, el procesado se realiza en dos tareas, el Map y el Reduce:

* **Map:** esta tarea es la encargada de "etiquetar" o "clasificar" los datos que se leen desde disco, típicamente de HDFS, en función del procesado que estemos realizando.

* **Reduce:** esta tarea es la responsable de agregar los datos etiquetados por la tarea Map. Puede dividirse en dos etapas, la shuffle y el propio reduce o agregado.

# EJEMPLO

### [Datos de Entrada]
| Producto | Monto de Venta |
| :--- | :--- |
| A | 100 |
| B | 150 |
| A | 200 |
| C | 120 |
| B | 80 |
| A | 50 |

---

### [Fase Map]
**Fase Map:** Cada bloque de datos se procesa en paralelo en diferentes nodos. Para cada registro, el nodo emite pares clave-valor, donde la clave es el nombre del producto y el valor es el monto de la venta.

* `Mapper 1: (A, 100), (B, 150), (A, 200)`
* `Mapper 2: (C, 120), (B, 80), (A, 50)`

---

### [Shuffle & Sort]
Los resultados intermedios se agrupan y ordenan por clave.

* `(A, [100, 200, 50])`
* `(B, [150, 80])`
* `(C, [120])`

---

### [Fase Reduce]
**Fase Reduce:** Cada nodo de reducción suma los valores asociados a cada clave (producto).

* `Reducer 1: (A, [100, 200, 50]) -> (A, 350)`
* `Reducer 2: (B, [150, 80])      -> (B, 230)`
* `Reducer 3: (C, [120])          -> (C, 120)`

---

### [Resultado Final]
| Producto | Total de Ventas |
| :--- | :--- |
| A | 350 |
| B | 230 |
| C | 120 |

# YARN

YARN (Yet Another Resource Negotiator) es un componente clave de Hadoop que se utiliza para la gestión de recursos y la programación de tareas en clústeres Hadoop.

YARN se encarga de la administración de recursos y la planificación de tareas en un clúster Hadoop, permitiendo que múltiples aplicaciones compartan de manera eficiente los recursos del clúster. Proporciona un marco para la ejecución de aplicaciones y servicios en un entorno distribuido.

---

### Componentes del Diagrama de Arquitectura de YARN

* **Client (Cliente):** Envía los trabajos (Job Submission) al Resource Manager.
* **Resource Manager:** Nodo maestro que centraliza la asignación de recursos de todo el clúster.
* **Node Manager:** Agente instalado en cada nodo del clúster encargado de monitorear el uso de los recursos.
* **Application Master:** Componente específico de cada aplicación que coordina sus tareas y solicita recursos adicionales al Resource Manager.
* **Container (Contenedor):** Fracción física de recursos (memoria, CPU) asignada en un Node Manager donde se ejecutan los procesos de las tareas.

**Leyenda de conexiones:**
* Job Submission (Envío de trabajo)
* Node Status (Estado del nodo)
* Resource Request (Solicitud de recursos)
* MapReduce Status (Estado de MapReduce)
