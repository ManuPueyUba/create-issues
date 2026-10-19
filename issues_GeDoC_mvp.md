## Épica: Usuarios y accesos

### MVP-01 Iniciar sesión

<!-- Status: Etapa 1 -->

**Descripción**: Como **integrante del personal**, quiero **iniciar sesión con mi usuario personal** para **que todo lo que hago en el sistema quede a mi nombre**.

**Trazabilidad**: ISO 7101 7.5.3 / 7.5.6 | Story points: 3 | Matriz v1: Nueva

**Requisito**: La información documentada debe estar protegida y cada registro debe identificar a su responsable.

**Criterios de aceptación**

- CA 1: Login exitoso
  - Dado que un usuario activo tiene credenciales válidas
  - Cuando ingresa su usuario y contraseña
  - Entonces accede al sistema con su sesión iniciada.

- CA 2: Credenciales incorrectas
  - Dado que un usuario ingresa un usuario o una contraseña incorrectos
  - Cuando intenta iniciar sesión
  - Entonces el sistema muestra un error sin indicar cuál de los dos datos falló.

### MVP-02 Alta de usuarios con sector y rol

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador del sistema**, quiero **dar de alta usuarios indicando su sector y su rol** para **que cada persona vea y haga solo lo que le corresponde**.

**Comentarios**: Cada usuario se crea su propia cuenta, y al admin asigna roles (es la opción más común (autorregistro + admin asigna))

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 3 | Matriz v1: Nueva

**Requisito**: El acceso a la información documentada debe depender de la función de cada persona.

Roles mínimos: lector, autor, revisor (responsable del proceso), Organización y Métodos, responsable de calidad y administrador.

**Criterios de aceptación**

- CA 1: Alta de usuario
  - Dado que un usuario se registra con su email institucional
  - Cuando completa el registro
  - Entonces queda creado en estado "pendiente de rol", sin poder operar en el sistema hasta que el administrador le asigne sector y rol.

- CA 1b: Asignación de rol
  - Dado un usuario pendiente de rol
  - Cuando el administrador le asigna sector y rol
  - Entonces el usuario puede iniciar sesión y operar según los permisos de ese rol.

- CA 2: Email repetido
  - Dado que ya existe un usuario con ese email
  - Cuando un nuevo usuario intenta registrarse con el mismo email
  - Entonces el sistema rechaza el alta.

- CA 3: Baja sin borrar historial
  - Dado un usuario que deja el hospital
  - Cuando el administrador lo da de baja
  - Entonces ya no puede iniciar sesión, pero sus acciones anteriores siguen registradas con su nombre.

### MVP-03 Permisos por rol

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador del sistema**, quiero **que las acciones disponibles dependan del rol del usuario** para **que nadie pueda editar, acceder, aprobar o imprimir un documento sin estar autorizado**.

**Comentarios**: No existe editar, si no que se sube una nueva version.

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 5 | Matriz v1: N° 10

**Requisito**: Asegurar que la información documentada esté protegida contra acceso no autorizado.

**Criterios de aceptación**

- CA 1: Lector
  - Dado un usuario con rol "lector"
  - Cuando abre un documento vigente
  - Entonces puede verlo, pero no tiene disponibles las opciones de editar, aprobar ni imprimir copia controlada.

- CA 2: Acción no permitida
  - Dado un usuario sin el rol habilitado para aprobar
  - Cuando intenta aprobar un documento
  - Entonces el sistema rechaza la operación y la registra en la pista de auditoría.

- CA 3: Cambio de rol
  - Dado un usuario al que el administrador le cambia el rol
  - Cuando realiza su siguiente acción
  - Entonces el sistema ya aplica los permisos del rol nuevo.

## Épica: Organigrama

### MVP-04 Cargar sectores del hospital

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **cargar los sectores del hospital en forma de árbol** para **asignarles documentos y usuarios**.

**Trazabilidad**: ISO 7101 4.3 / 4.4 | Story points: 3 | Matriz v1: N° 1

**Requisito**: Determinar el alcance del sistema de gestión de la calidad y asociar los procesos a cada unidad funcional.

**Criterios de aceptación**

- CA 1: Alta de sector
  - Dado que estoy en el organigrama
  - Cuando creo un sector e indico de qué sector depende
  - Entonces el sector aparece en el árbol en el lugar correcto.

- CA 2: Sector con contenido
  - Dado un sector que tiene documentos o usuarios asignados
  - Cuando intento eliminarlo
  - Entonces el sistema no lo permite hasta que se reasignen.

- CA 3: Asociar proceso a unidad funcional
  - Dado un Mapa de Procesos ya creado.
  - Cuando se lo vincula a uno o más sectores del organigrama
  - Entonces ese proceso queda asociado a esas unidades funcionales, y sus documentos heredan la visibilidad de ese sector para los usuarios.

## Épica: Jerarquía documental (nuevo)

### MVP-05 Mapa de Procesos y Tabla de Actividades
<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **crear Mapas de Procesos y, dentro de cada uno, Tablas de Actividades**, para **reflejar la estructura jerárquica con la que el hospital organiza su documentación.**

**Trazabilidad**: ISO 7101 4.4 | Story points: 3

**Requisito**: gestión del vínculo entre documentos (un POE pertenece a una actividad de una tabla, que pertenece a un proceso de un mapa).

**Criterios de aceptación:**

- CA 1: Alta de mapa y tabla
  - Dado un responsable de calidad en el módulo de procesos
  - Cuando crea un Mapa de Procesos y le agrega una o más Tablas de Actividades
  - Entonces la jerarquía queda disponible para asociar documentos.

- CA 2: Mapa con contenido
  - Dado un Mapa de Procesos que ya tiene tablas o documentos asociados
  - Cuando se intenta eliminar
  - Entonces el sistema no lo permite hasta reasignar su contenido.

### MVP-06 Asociar un documento a su actividad y proceso
<!-- Status: Etapa 1 -->

**Descripción:** Como **autor**, quiero **asociar el documento que estoy cargando a una Actividad de una Tabla existente,** para **que quede ubicado en el lugar correcto de la jerarquía documental del hospital.**

**Trazabilidad:** ISO 7101 4.4 · 7.5.2 | Story points: 3 

**Requisito:** mismo que MVP-05, aplicado a la carga de cada documento.

**Criterios de aceptación:**

- CA 1: Asociación obligatoria
  - Dado un documento en carga
  - Cuando se completan sus datos obligatorios
  - Entonces no se puede guardar sin asociarlo a una actividad existente.

- CA 2: Navegación jerárquica
  - Dado un proceso del mapa
  - Cuando un usuario lo consulta
  - Entonces ve todas las tablas, actividades y documentos vigentes que dependen de él.


## Épica: Documentos

### MVP-07 Cargar un documento con sus datos obligatorios

<!-- Status: Etapa 1 -->

**Descripción**: Como **autor**, quiero **subir un documento completando sus datos obligatorios** para **que quede identificado según la Disposición 186**.

**Trazabilidad**: ISO 7101 7.5.2 · Disposición 186/DME/2022 | Story points: 5 | Matriz v1: N° 8

**Requisito**: La información documentada debe estar identificada con título, fecha, autor y un número de referencia.

Datos obligatorios: título, sector, tipo documental, realizó, revisó y aprobó. "Realizó" y "revisó" admiten más de una persona. El sistema asigna el código, la versión y la fecha.

**Criterios de aceptación**

- CA 1: Carga exitosa con código automático
  - Dado que completé todos los datos obligatorios y adjunté el archivo
  - Cuando guardo el documento
  - Entonces queda en estado "borrador" con un código único asignado por el sistema (por ejemplo, POE-0001), que no se puede modificar.

- CA 2: Datos faltantes
  - Dado que dejé vacío algún dato obligatorio
  - Cuando intento guardar
  - Entonces el sistema no lo guarda y señala qué falta.

- CA 3: Varias personas en "realizó"
  - Dado un documento elaborado por tres personas
  - Cuando las cargo en el campo "realizó"
  - Entonces el documento las muestra a las tres.

### MVP-08 Modificar un documento descargándolo

<!-- Status: Etapa 1 -->

**Descripción**: Como **autor**, quiero **descargar un documento vigente, modificarlo y volver a subirlo** para **actualizarlo sin tener que reescribirlo desde cero**.

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Controlar los cambios de la información documentada.

**Criterios de aceptación**

- CA 1: Nueva versión en borrador
  - Dado un documento vigente del que soy autor
  - Cuando lo descargo, lo modifico y lo vuelvo a subir
  - Entonces se crea un borrador de nueva versión con el mismo código, y la versión vigente sigue publicada hasta que la nueva se apruebe.

- CA 2: Un solo borrador a la vez
  - Dado que un documento ya tiene un borrador en curso
  - Cuando otro autor intenta subir otro borrador del mismo documento
  - Entonces el sistema le avisa que ya hay uno en curso y quién lo tiene.


## Épica: Ciclo de vida y aprobación

### MVP-09 Revisión y aprobación del responsable del proceso

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable del proceso**, quiero **revisar un borrador y aprobarlo o devolverlo con observaciones** para **que ningún documento avance sin una revisión técnica**.

**Trazabilidad**: ISO 7101 7.5.2 · Disposición 186/DME/2022 | Story points: 5 | Matriz v1: Nueva

**Requisito**: La información documentada debe revisarse y aprobarse antes de su uso.

Estados del MVP: `borrador` → `en revisión` → `aprobado por el responsable` → `aprobado institucionalmente` → `vigente` → `obsoleto` → `archivado` .

**Criterios de aceptación**

- CA 1: Aprobación técnica
  - Dado un documento "en revisión"
  - Cuando el responsable del proceso lo aprueba
  - Entonces pasa a "aprobado por el responsable" y queda registrado quién y cuándo lo aprobó.

- CA 2: Devolución con observaciones
  - Dado un documento "en revisión"
  - Cuando el responsable lo devuelve
  - Entonces el sistema exige escribir las observaciones y el documento vuelve a "borrador".

- CA 3: Sin saltear pasos
  - Dado un documento en "borrador"
  - Cuando alguien intenta pasarlo directamente a "vigente"
  - Entonces el sistema no lo permite.

### MVP-10 Aprobación institucional por Disposición

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de Organización y Métodos**, quiero **cargar el número y la fecha de la Disposición de la DME que aprueba el documento** para **que solo entre en vigencia con la aprobación institucional**.

**Trazabilidad**: ISO 7101 7.5.2 · Disposición 186/DME/2022 | Story points: 3 | Matriz v1: N° 24

**Requisito**: La aprobación de la información documentada debe estar identificada, incluyendo quién la aprobó.

**Criterios de aceptación**

- CA 1: Entrada en vigencia
  - Dado un documento "aprobado por el responsable"
  - Cuando cargo el número y la fecha de la Disposición
  - Entonces el documento pasa a "vigente".

- CA 2: Falta la Disposición
  - Dado un documento "aprobado por el responsable"
  - Cuando intento ponerlo vigente sin número o sin fecha de Disposición
  - Entonces el sistema no lo permite.

### MVP-11 Vigencia y vencimiento de documentos

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **que cada documento tenga una fecha de vencimiento y que el sistema avise antes de que venza** para **renovarlo a tiempo y que nadie use un documento vencido**.

**Trazabilidad**: ISO 7101 7.5.3 · Disposición 186/DME/2022 | Story points: 5 | Matriz v1: N° 12

**Requisito**: Revisar periódicamente la información documentada y hacer seguimiento de sus vencimientos.

Los documentos operativos tienen vigencia de 2 años (Disposición 186). El plazo de aviso previo es configurable.

**Criterios de aceptación**

- CA 1: Aviso previo
  - Dado un documento vigente al que le faltan 3 meses para vencer
  - Cuando el sistema hace su control diario
  - Entonces avisa por mail al autor y al responsable de calidad para que inicien la revisión.

- CA 2: Vencimiento sin renovar
  - Dado un documento que llegó a su fecha de vencimiento sin una nueva versión aprobada
  - Cuando el sistema hace su control diario
  - Entonces lo pasa automáticamente a "obsoleto".

- CA 3: Revisión sin cambios
  - Dado un documento revisado al que no hubo que hacerle cambios
  - Cuando se aprueba la revisión siguiendo el mismo circuito, incluida la Disposición
  - Entonces se registra una nueva versión "revisada sin modificaciones" y la fecha de vencimiento se extiende por un nuevo período.

### MVP-12 Archivado y disposición final (nuevo)
<!-- Status: Etapa 2 -->

**Descripción:** Como **responsable de calidad**, quiero **que un documento obsoleto pase a "archivado" tras un plazo de retención configurable por tipo documental, y que el sistema me avise antes de su disposición final,** para **conservar evidencia histórica sin acumular información indefinidamente ni perder trazabilidad.**

**Trazabilidad:** ISO 7101 7.5.3 (control de información documentada: retención y disposición) | Story points: 3 

**Requisito:** política de retención y disposición configurable por tipo documental (requisito 12 de la lista mínima).

**Criterios de aceptación:**

- CA 1: Transición automática a archivado
  - Dado un documento obsoleto que cumplió su plazo de retención (configurable por tipo documental)
  - Cuando el sistema hace su control diario
  - Entonces el documento pasa a estado "archivado" y notifica al responsable de calidad.

- CA 2: Disposición final con confirmación humana
  - Dado un documento archivado al que corresponde su disposición final
  - Cuando el sistema detecta el vencimiento del plazo de archivado
  - Entonces notifica al responsable de calidad y no elimina nada sin su confirmación explícita.

- CA 3: Acceso a lo archivado
  - Dado un documento en estado "archivado"
  - Cuando un usuario con rol de calidad o auditoría lo busca
  - Entonces puede consultarlo; el resto de los roles no lo ve en listados ni búsquedas.

## Épica: Versionado

### MVP-13 Historial de versiones

<!-- Status: Etapa 1 -->

**Descripción**: Como **usuario del sistema**, quiero **ver todas las versiones de un documento** para **saber cómo fue cambiando y quién aprobó cada una**.

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 3 | Matriz v1: N° 9

**Requisito**: Control de versiones de la información documentada.

**Criterios de aceptación**

- CA 1: Listado de versiones
  - Dado un documento con tres versiones
  - Cuando abro su historial
  - Entonces veo las tres con número, fecha, autor, Disposición y estado.

- CA 2: Versiones anteriores solo para algunos roles
  - Dado un usuario con rol "lector"
  - Cuando abre el historial
  - Entonces no puede abrir las versiones obsoletas; los roles de calidad y Organización y Métodos sí.

### MVP-14 Retiro automático de la versión anterior

<!-- Status: Etapa 1 -->

**Descripción**: Como **integrante del personal**, quiero **ver únicamente la versión vigente de cada documento** para **no usar por error una versión vieja**.

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 2 | Matriz v1: Nueva

**Requisito**: Prevenir el uso no intencionado de información documentada obsoleta.

**Criterios de aceptación**

- CA 1: Reemplazo automático
  - Dado que la versión 2 de un documento está vigente
  - Cuando la versión 3 entra en vigencia
  - Entonces la versión 2 pasa a "obsoleto" y deja de aparecer en búsquedas y listados.

- CA 2: Borradores ocultos
  - Dado un documento con un borrador en curso
  - Cuando un lector lo consulta
  - Entonces solo ve la versión vigente.

## Épica: Consulta y difusión

### MVP-15 Buscar documentos vigentes

<!-- Status: Etapa 1 -->

**Descripción**: Como **integrante del personal**, quiero **buscar documentos vigentes por código, título, sector o tipo** para **encontrar rápido el procedimiento que necesito**.

**Trazabilidad**: ISO 7101 7.5.3 a | Story points: 3 | Matriz v1: Nueva

**Requisito**: La información documentada debe estar disponible donde y cuando se necesite.

**Criterios de aceptación**

- CA 1: Búsqueda con resultados
  - Dado que existen documentos vigentes
  - Cuando busco por código, título, sector o tipo documental
  - Entonces veo los documentos vigentes que coinciden y que tengo permiso de ver.

- CA 2: Mi sector
  - Dado un usuario asignado a un sector
  - Cuando entra al sistema
  - Entonces ve directamente la lista de documentos vigentes de su sector.

### MVP-16 Impresión controlada

<!-- Status: Etapa 1 -->

**Descripción**: Como **jefe de servicio**, quiero **imprimir un documento eligiendo si sale como copia controlada o como copia de visualización** para **distribuir el procedimiento al personal que no usa el sistema**.


**Trazabilidad**: ISO 7101 7.5.3 · Criterio del Área de Calidad | Story points: 3 | Matriz v1: N° 23

**Requisito**: Controlar la distribución de la información documentada. La impresión es siempre controlada y se restringe a algunos puestos (jefaturas, responsable de calidad).

**Criterios de aceptación**

- CA 1: Copia controlada
  - Dado un usuario autorizado a imprimir
  - Cuando genera una copia controlada
  - Entonces el documento sale con la leyenda "Copia controlada", el código, la versión y la fecha, y la impresión queda registrada.

- CA 2: Copia de visualización
  - Dado un usuario autorizado a imprimir
  - Cuando elige "copia de visualización"
  - Entonces el documento sale con una leyenda que indica que no es una copia controlada.

- CA 3: Usuario no autorizado
  - Dado un usuario sin permiso de impresión
  - Cuando abre un documento
  - Entonces no tiene disponible la opción de imprimir.

### MVP-17 Registro de lectura

<!-- Status: Etapa 1 -->

**Descripción**: Como **jefe de servicio**, quiero **registrar que mi equipo leyó cada documento, ya sea en el sistema o con la copia firmada** para **tener evidencia ante una auditoría**.

**Trazabilidad**: ISO 7101 5.2 / 7.5.3 | Story points: 5 | Matriz v1: N° 11

**Requisito**: Registrar quién tomó conocimiento de cada documento.

**Criterios de aceptación**

- CA 1: Lectura en el sistema
  - Dado un usuario con un documento pendiente de lectura
  - Cuando lo abre y confirma "Leído"
  - Entonces se registra con fecha, hora y versión.

- CA 2: Lectura con copia firmada
  - Dado personal que no usa el sistema y firmó la copia controlada
  - Cuando el jefe de servicio sube el escaneo de la planilla firmada
  - Entonces queda guardada como evidencia de lectura de esa versión.

- CA 3: Quién falta leer
  - Dado un documento publicado en mi sector
  - Cuando consulto su estado de lectura
  - Entonces veo quiénes confirmaron la lectura y quiénes no.


## Épica: Exportación (nuevo)

### MVP-18 Exportación de datos y metadatos
<!-- Status: Etapa 2 -->

**Descripción:** Como **responsable de calidad o administrador,** quiero **exportar documentos junto con sus metadatos y su pista de auditoría en un formato estándar,** para **que la información del hospital nunca quede cautiva dentro del sistema.**

**Trazabilidad:** Requisito propio del relevamiento (sin cláusula ISO puntual) | Story points: 3 

**Requisito:** exportación completa de datos y metadatos.

**Criterios de aceptación:**

- CA 1: Exportación limitada por rol
  - Dado un responsable de proceso
  - Cuando exporta documentación
  - Entonces solo exporta la de su sector; un administrador exporta la totalidad.

- CA 2: Formato estándar
  - Dado un conjunto de documentos a exportar
  - Cuando se genera la exportación
  - Entonces se entrega un archivo con metadatos en CSV/JSON junto con los documentos originales en su formato nativo

## Épica: Notificaciones

### MVP-19 Aviso de nueva versión por mail

<!-- Status: Etapa 1 -->

**Descripción**: Como **integrante del personal**, quiero **recibir un mail cuando se publica o se actualiza un documento de mi sector** para **enterarme sin tener que revisar el sistema todos los días**.

**Trazabilidad**: ISO 7101 7.4.1 | Story points: 3 | Matriz v1: N° 7

**Requisito**: Determinar qué, cuándo y a quién se comunica dentro del sistema de gestión de la calidad.

**Criterios de aceptación**

- CA 1: Aviso al sector
  - Dado un documento asignado al sector Farmacia
  - Cuando una nueva versión entra en vigencia
  - Entonces todos los usuarios de Farmacia reciben un mail con el nombre del documento actualizado.

- CA 2: Aviso de tarea pendiente
  - Dado un documento que pasa a "en revisión"
  - Cuando cambia de estado
  - Entonces el responsable del proceso recibe un mail indicando que tiene una revisión pendiente.

## Épica: Auditoría

### MVP-20 Registro de auditoría

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **ver todo lo que se hizo sobre un documento, por quién y cuándo** para **demostrarlo en una auditoría**.

**Trazabilidad**: ISO 7101 7.5.6 | Story points: 5 | Matriz v1: N° 18

**Requisito**: Verificar la fecha, la hora y la identidad del responsable de cada actividad sobre los registros.

**Criterios de aceptación**

- CA 1: Registro de acciones
  - Dado un documento que fue creado, revisado, aprobado y leído
  - Cuando consulto su registro de auditoría
  - Entonces veo cada acción con usuario, fecha y hora.

- CA 2: No se puede alterar
  - Dado cualquier usuario, incluido el administrador
  - Cuando intenta modificar o borrar una entrada del registro
  - Entonces el sistema no lo permite.


## Épica: No Conformidades y Acciones Correctivas (nuevo)

### MVP-21 Registrar una no conformidad o evento adverso
<!-- Status: Etapa 2 -->

**Descripción:** Como **cualquier integrante del personal,** quiero **reportar un desvío o hallazgo de auditoría vinculado a un proceso o documento,** para **que quede registrado y se pueda investigar y corregir.**

**Trazabilidad:** ISO 7101, cláusula 10 (Mejora) | Story points: 5 

**Requisito:** cierre del ciclo PDCA, evaluación de eventos adversos y su corrección.

**Criterios de aceptación**

- CA 1: Alta de no conformidad
  - Dado un usuario que detecta un desvío
  - Cuando completa descripción, proceso o documento asociado y fecha
  - Entonces se crea en estado "reportada" y se notifica al responsable del proceso.

- CA 2: Vinculación con documentos
  - Dado una no conformidad vinculada a un POE específico
  - Cuando se consulta el historial de ese documento
  - Entonces la no conformidad aparece referenciada.


### MVP-22 Gestionar la acción correctiva hasta su cierre
<!-- Status: Etapa 2 -->

**Descripción:** Como **responsable del proceso,** quiero **definir una acción correctiva para una no conformidad y verificar su eficacia antes de cerrarla,** para **asegurar que la corrección realmente funcionó y no solo que se aplicó.**

**Trazabilidad:** ISO 7101, cláusula 10 | Story points: 5 

**Requisito:** mismo que la historia anterior.

**Criterios de aceptación:**

- CA 1: Flujo de estados
  - Dado una no conformidad reportada
  - Cuando avanza en su gestión
  - Entonces pasa por: reportada → en investigación → acción correctiva definida → acción correctiva aplicada → verificada → cerrada, sin saltear pasos.

- CA 2: Generación de nueva versión documental
  - Dado que la acción correctiva requiere modificar un procedimiento
  - Cuando se confirma esa necesidad
  - Entonces se habilita la creación de un nuevo borrador de ese documento, quedando vinculado a la no conformidad que lo originó.

- CA 3: Cierre sin verificación
  - Dado una acción correctiva aplicada pero sin verificación de eficacia
  - Cuando se intenta cerrar la no conformidad
  - Entonces el sistema no lo permite.


## Épica: Análisis con IA — Opcional (nuevo, stretch goal)

### MVP-23 Búsqueda semántica sobre el contenido de los documentos
<!-- Status: Opcional / sujeto a tiempo disponible -->

**Descripción:** Como **integrante del personal,** quiero **buscar un procedimiento describiendo lo que necesito con mis propias palabras,** para **encontrarlo aunque no coincida literalmente con su título.**

**Trazabilidad:** Extiende el requisito de búsqueda por contenido | Story points: 5 

**Requisito:** mejora incremental, no forma parte de los 15 requisitos mínimos.

**Criterios de aceptación:**

- CA 1: Búsqueda por concepto
  - Dado un documento vigente cuyo título no coincide literalmente con la búsqueda
  - Cuando el usuario busca por su significado (ej. "limpieza de instrumental" encuentra "Protocolo de esterilización")
  - Entonces el documento aparece entre los resultados.

### MVP-24 Respuesta redactada con cita de fuente
<!-- Status: Opcional / sujeto a tiempo disponible -->

**Dependencias**: MVP-23 Búsqueda semántica sobre el contenido de los documentos

**Descripción:** Como **integrante del personal,** quiero **hacer una pregunta en lenguaje natural y recibir una respuesta redactada en vez de solo una lista de documentos,** para **resolver dudas operativas más rápido.**

**Trazabilidad:** Extiende el requisito 9 | Story points: 8 

**Requisito:** mejora incremental, condicionada a la política de red y datos que defina el hospital (API externa vs. modelo local).

**Criterios de aceptación:**

- CA 1: Respuesta con fuente citada
  - Dado una pregunta en lenguaje natural
  - Cuando el sistema encuentra documentos relevantes
  - Entonces redacta una respuesta citando el documento y versión de origen.

- CA 2: Sin información disponible
  - Dado una pregunta sin documentos relevantes asociados
  - Cuando el sistema no encuentra contenido suficiente
  - Entonces responde que no encontró información en la documentación vigente, sin inventar una respuesta.

<!--
Prioridades (el script las usa para asignar labels de prioridad)

## No negociables

- MVP-01 Iniciar sesión
- MVP-02 Alta de usuarios con sector y rol
- MVP-03 Permisos por rol
- MVP-07 Cargar documento con datos obligatorios
- MVP-08 Modificar documento descargándolo
- MVP-09 Revisión y aprobación del responsable
- MVP-10 Aprobación institucional por Disposición
- MVP-11 Vigencia y vencimiento de documentos 
- MVP-12 Archivado y disposición final 
- MVP-13 Historial de versiones
- MVP-14 Retiro automático de la versión anterior
- MVP-20 Registro de auditoría

## Recomendables

- MVP-04 Cargar sectores del hospital
- MVP-05 Mapa de Procesos y Tabla de Actividades
- MVP-06 Asociar documento a actividad y proceso
- MVP-15 Buscar documentos vigentes
- MVP-16 Impresión controlada
- MVP-17 Registro de lectura
- MVP-18 Exportación de datos y metadatos
- MVP-19 Aviso de nueva versión por mail

## Fuera de los 15 requisitos mínimos — valor agregado

- MVP-21 Registrar una no conformidad
- MVP-22 Gestionar la acción correctiva hasta su cierre
- MVP-23 Búsqueda semántica
- MVP-24 Respuesta redactada con cita de fuente 


Dudas abiertas (se publican como comentario en las issues mencionadas):
- El rol "jefe de servicio" (usado en MVP-16 y MVP-17) todavía no está en la lista oficial de seis roles de MVP-02.
-->
