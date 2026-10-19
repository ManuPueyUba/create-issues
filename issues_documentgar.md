## Épica: Usuarios y accesos

### HU-01 Autenticación de usuarios

<!-- Status: Etapa 1 -->

**Descripción**: Como **integrante del personal del hospital**, quiero **iniciar sesión con un usuario personal e intransferible** para **que cada acción que realizo en el sistema quede asociada a mi identidad**.

**Trazabilidad**: ISO 7101 7.5.3 / 7.5.6 | Story points: 3 | Matriz v1: Nueva

**Requisito**: La información documentada debe estar protegida contra el acceso no autorizado y los registros deben identificar de forma trazable al responsable de cada actividad.

El mecanismo concreto de autenticación (usuarios propios, directorio institucional, etc.) se define en la etapa de arquitectura junto con la Gerencia de Sistemas. Depende de la decisión de HU-39.

**Criterios de aceptación**

- CA 1: Login exitoso
  - Dado que un usuario activo tiene credenciales válidas
  - Cuando ingresa su usuario y contraseña
  - Entonces accede al sistema y su sesión queda asociada a su identidad.

- CA 2: Credenciales incorrectas
  - Dado que un usuario ingresa una contraseña incorrecta o un usuario inexistente
  - Cuando intenta iniciar sesión
  - Entonces el sistema muestra un error genérico sin revelar cuál de los dos datos es incorrecto.

- CA 3: Bloqueo por intentos fallidos
  - Dado que un usuario superó el límite de intentos fallidos consecutivos
  - Cuando intenta iniciar sesión nuevamente
  - Entonces el sistema bloquea temporalmente la cuenta y registra el evento en la pista de auditoría.

- CA 4: Sesión expirada por inactividad
  - Dado que un usuario dejó su sesión inactiva más tiempo que el configurado
  - Cuando intenta realizar una acción
  - Entonces el sistema le pide autenticarse nuevamente antes de continuar.

- CA 5: Usuario dado de baja
  - Dado que un usuario fue desactivado por el administrador
  - Cuando intenta iniciar sesión
  - Entonces el sistema le niega el acceso, pero sus acciones previas siguen visibles con su nombre en la pista de auditoría.

### HU-02 Gestión de usuarios y asignación a unidades y roles

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador del sistema**, quiero **dar de alta usuarios y asignarlos a una o más unidades funcionales con un rol** para **que los permisos, las notificaciones y las lecturas obligatorias lleguen a las personas correctas**.

**Trazabilidad**: ISO 7101 7.5.3 / 7.4.1 | Story points: 5 | Matriz v1: Nueva

**Requisito**: La distribución, el acceso y la comunicación de la información documentada deben llegar a quienes la necesitan según su función.

**Criterios de aceptación**

- CA 1: Alta de usuario
  - Dado que el administrador completa nombre, email institucional, unidad funcional y rol
  - Cuando confirma el alta
  - Entonces el usuario queda creado y activo, y aparece como integrante de esa unidad.

- CA 2: Usuario en varias unidades
  - Dado que un profesional trabaja en dos servicios
  - Cuando el administrador lo asigna a ambas unidades funcionales
  - Entonces el usuario recibe las notificaciones y lecturas obligatorias de los procesos de las dos unidades.

- CA 3: Email duplicado
  - Dado que ya existe un usuario con un email determinado
  - Cuando el administrador intenta dar de alta otro usuario con ese mismo email
  - Entonces el sistema rechaza el alta e indica que el email ya está en uso.

- CA 4: Cambio de unidad
  - Dado que un usuario es trasladado de servicio
  - Cuando el administrador cambia su unidad funcional
  - Entonces el usuario deja de tener asignados los documentos de la unidad anterior y pasa a tener los de la nueva; el cambio queda en la pista de auditoría.

- CA 5: Baja lógica
  - Dado que un usuario deja el hospital
  - Cuando el administrador lo da de baja
  - Entonces el usuario queda inactivo sin borrarse, para preservar la trazabilidad de sus acciones.

### HU-03 Control de acceso por rol

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador del sistema**, quiero **definir qué roles pueden ver, editar o aprobar cada tipo de documento** para **que la información sensible solo sea accesible a quien corresponde**.

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 5 | Matriz v1: N° 10

**Requisito**: Asegurar que la información documentada esté disponible y protegida contra acceso no autorizado.

Los permisos se asignan por rol (no por persona), según lo definido en la propuesta.

**Criterios de aceptación**

- CA 1: Acceso denegado y registrado
  - Dado que un documento está restringido al rol "Coordinación de Calidad"
  - Cuando un usuario sin ese rol intenta abrirlo
  - Entonces el sistema deniega el acceso y registra el intento en la pista de auditoría.

- CA 2: Acceso permitido según rol
  - Dado que un usuario tiene el rol con permiso de lectura sobre un documento
  - Cuando lo abre
  - Entonces puede verlo pero no tiene disponibles las acciones de edición ni de aprobación.

- CA 3: Cambio de rol con efecto inmediato
  - Dado que un usuario tenía permiso de edición sobre un documento
  - Cuando el administrador le quita ese rol
  - Entonces en su siguiente acción el usuario ya no puede editar el documento.

- CA 4: Permisos por rol, no por persona
  - Dado que el administrador quiere dar acceso a un documento
  - Cuando configura los permisos
  - Entonces solo puede asignarlos a roles o unidades funcionales, no a usuarios individuales.

- CA 5: Acceso directo por URL
  - Dado que un usuario sin permiso conoce la URL de un documento restringido
  - Cuando intenta acceder directamente por esa URL o por la API
  - Entonces el sistema deniega el acceso igual que desde la interfaz.

## Épica: Organigrama

### HU-04 Organigrama y alcance del sistema de gestión

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **cargar el organigrama del hospital y marcar qué unidades funcionales están dentro del alcance del sistema** para **tener trazabilidad del alcance de la certificación en todo momento**.

**Trazabilidad**: ISO 7101 4.3 | Story points: 5 | Matriz v1: N° 1

**Requisito**: Determinar el alcance del sistema de gestión de calidad (servicios, sitios, unidades funcionales incluidos).

**Criterios de aceptación**

- CA 1: Alta de unidad dentro del alcance
  - Dado que soy responsable de calidad y estoy en el módulo de organigrama
  - Cuando cargo una nueva unidad funcional, indico su unidad superior y la marco como "dentro del alcance"
  - Entonces el sistema la agrega al árbol organizacional y queda disponible para asociarle procesos.

- CA 2: Exclusión justificada
  - Dado que una unidad funcional queda fuera del alcance de la certificación
  - Cuando la marco como "fuera del alcance"
  - Entonces el sistema exige cargar la justificación de la exclusión y la conserva como parte del registro del alcance.

- CA 3: Reporte de alcance vigente
  - Dado que el organigrama tiene unidades dentro y fuera del alcance
  - Cuando consulto el reporte de alcance
  - Entonces veo el listado de unidades incluidas y excluidas con sus justificaciones y la fecha de la última modificación.

- CA 4: Baja de unidad con documentos asociados
  - Dado que una unidad funcional tiene procesos o usuarios asociados
  - Cuando intento darla de baja
  - Entonces el sistema no lo permite hasta que se reasignen sus procesos y usuarios.

- CA 5: Historial del alcance
  - Dado que el alcance cambió varias veces
  - Cuando consulto el historial del organigrama
  - Entonces veo cada cambio con usuario, fecha y hora.

### HU-05 Asociar procesos a unidades funcionales

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **asociar cada proceso documentado a la o las unidades funcionales que le corresponden** para **saber qué documentación aplica a cada sector del hospital**.

**Trazabilidad**: ISO 7101 4.4 / 7.5.1 | Story points: 3 | Matriz v1: N° 2

**Requisito**: Asociar procesos documentados a cada unidad funcional dentro del sistema de gestión de calidad.

**Criterios de aceptación**

- CA 1: Asociación a una unidad
  - Dado un proceso ya cargado en el sistema
  - Cuando lo asocio a la unidad funcional "Terapia Intensiva Pediátrica"
  - Entonces ese proceso aparece listado en la vista de documentos de esa unidad.

- CA 2: Proceso transversal
  - Dado un proceso que aplica a varias unidades (por ejemplo, lavado de manos)
  - Cuando lo asocio a varias unidades funcionales o a una unidad superior
  - Entonces aparece en la vista de cada una de esas unidades y de sus unidades hijas.

- CA 3: Unidad fuera del alcance
  - Dado que una unidad funcional está marcada como "fuera del alcance"
  - Cuando intento asociarle un proceso
  - Entonces el sistema me advierte que la unidad no está dentro del alcance del sistema de gestión antes de confirmar.

- CA 4: Desasociación
  - Dado un proceso asociado a una unidad
  - Cuando lo desasocio
  - Entonces deja de mostrarse en esa unidad, sus usuarios dejan de tenerlo como lectura obligatoria y el cambio queda registrado.

## Épica: Estructura documental

### HU-06 Código único e inmutable por documento

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de Organización y Métodos**, quiero **que cada documento reciba automáticamente un código único e inmutable al crearse** para **identificarlo y enlazarlo aunque su título cambie con el tiempo**.

**Trazabilidad**: ISO 7101 7.5.2 | Story points: 3 | Matriz v1: N° 19

**Requisito**: La identificación de la información documentada debe incluir un número de referencia, además de título, fecha y autor.

**Criterios de aceptación**

- CA 1: Asignación automática
  - Dado que inicio un documento nuevo en el sistema
  - Cuando confirmo la creación
  - Entonces el sistema le asigna un código único con el prefijo de su tipo documental (por ejemplo, POE-0001).

- CA 2: Inmutabilidad
  - Dado un documento con código asignado
  - Cuando cualquier usuario, incluido el administrador, intenta modificar el código
  - Entonces el sistema no lo permite.

- CA 3: Persistencia entre versiones
  - Dado un documento cuyo título cambia en una nueva versión
  - Cuando se publica esa versión
  - Entonces el código del documento sigue siendo el mismo.

- CA 4: Sin reutilización de códigos
  - Dado un documento que fue archivado o dado de baja
  - Cuando se crea un documento nuevo del mismo tipo
  - Entonces el sistema no reutiliza el código del documento archivado.

- CA 5: Creación concurrente
  - Dado que dos usuarios crean documentos del mismo tipo al mismo tiempo
  - Cuando ambos confirman la creación
  - Entonces cada documento recibe un código distinto.

### HU-07 Metadatos obligatorios del documento

<!-- Status: Etapa 1 -->

**Descripción**: Como **autor de un proceso**, quiero **que el sistema me pida completar título, autor, responsable del proceso, unidad y vigencia antes de enviar un documento a revisión** para **que ningún documento quede sin su identificación completa**.

**Trazabilidad**: ISO 7101 7.5.2 | Story points: 3 | Matriz v1: N° 8

**Requisito**: Al crear o actualizar información documentada se debe asegurar su identificación (título, fecha, autor), formato y revisión/aprobación.

**Criterios de aceptación**

- CA 1: Campo obligatorio faltante
  - Dado que intento enviar a revisión un documento sin completar el campo "responsable del proceso"
  - Cuando presiono "Enviar a revisión"
  - Entonces el sistema bloquea el envío y señala el campo faltante.

- CA 2: Metadatos completos
  - Dado que completé todos los metadatos obligatorios
  - Cuando envío el documento a revisión
  - Entonces el documento pasa al estado "en revisión" con sus metadatos guardados.

- CA 3: Metadatos automáticos
  - Dado que creo o modifico un documento
  - Cuando guardo los cambios
  - Entonces la fecha de creación, la fecha de modificación y el autor se completan automáticamente con mi usuario y no pueden editarse a mano.

- CA 4: Metadatos según tipo documental
  - Dado que el tipo documental elegido tiene metadatos propios (por ejemplo, el plazo de revisión)
  - Cuando creo un documento de ese tipo
  - Entonces el sistema pide también esos campos.

### HU-08 Jerarquía de tipos documentales

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **vincular cada POE a la actividad de la Tabla de Actividades que lo origina, y cada tabla a su Mapa de Procesos** para **recorrer la jerarquía completa de un proceso, desde el mapa hasta el procedimiento concreto**.

**Trazabilidad**: ISO 7101 7.5.1 | Story points: 8 | Matriz v1: N° 20

**Requisito**: El sistema de gestión de la calidad debe incluir la información documentada necesaria para su eficacia, representando la estructura y las interacciones entre procesos.

Los tipos documentales siguen la taxonomía de la Disposición 186: Mapa de Procesos, Tabla de Actividades, Procedimiento Operativo Estándar (POE), Diagrama de Flujo, Protocolo de Gestión, Lista de Verificación, Formulario y Manual de Calidad.

**Criterios de aceptación**

- CA 1: Navegación de la jerarquía
  - Dado un Mapa de Procesos con una Tabla de Actividades asociada
  - Cuando creo un POE y lo vinculo a una actividad específica de esa tabla
  - Entonces el sistema muestra el POE anidado bajo esa actividad al navegar el mapa de procesos.

- CA 2: Vínculo inválido
  - Dado que estoy vinculando dos documentos
  - Cuando intento colgar un Mapa de Procesos de un POE
  - Entonces el sistema rechaza el vínculo porque no respeta la jerarquía de tipos definida.

- CA 3: Documentos relacionados
  - Dado un POE que usa un Formulario y una Lista de Verificación
  - Cuando consulto el POE
  - Entonces veo enlaces a los documentos relacionados en su versión vigente.

- CA 4: Advertencia por vínculo a documento obsoleto
  - Dado un documento vinculado a otro que pasa a "obsoleto"
  - Cuando el documento relacionado queda obsoleto
  - Entonces el sistema avisa al responsable del documento que lo referencia que debe revisar el vínculo.

### HU-09 Plantillas por tipo documental

<!-- Status: Etapa 3 -->

**Descripción**: Como **autor de un proceso**, quiero **crear un documento a partir de la plantilla oficial de su tipo documental** para **respetar el formato que establece la Disposición 186 sin tener que copiarlo a mano**.

**Trazabilidad**: ISO 7101 7.5.2 b | Story points: 5 | Matriz v1: Nueva

**Requisito**: Al crear información documentada se debe asegurar el formato apropiado.

**Criterios de aceptación**

- CA 1: Documento desde plantilla
  - Dado que existe una plantilla vigente para el tipo "POE"
  - Cuando creo un POE nuevo
  - Entonces el documento se inicializa con la estructura y las secciones de esa plantilla.

- CA 2: Plantilla versionada
  - Dado que Organización y Métodos publica una nueva versión de una plantilla
  - Cuando se crea un documento nuevo de ese tipo
  - Entonces se usa la nueva versión; los documentos existentes no se modifican.

- CA 3: Solo O&M administra plantillas
  - Dado que un usuario no tiene el rol de Organización y Métodos
  - Cuando intenta modificar una plantilla
  - Entonces el sistema rechaza la operación.

### HU-10 Manual de Calidad dinámico

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **que el Manual de Calidad se genere automáticamente a partir de los documentos vigentes del repositorio** para **no mantener a mano un archivo que queda desactualizado apenas cambia un documento**.

**Trazabilidad**: ISO 7101 7.5.1 / 7.5.3 | Story points: 5 | Matriz v1: N° 26

**Requisito**: El Manual de Calidad, definido como repositorio único de los documentos del sistema de gestión de la calidad, debe estar disponible y actualizado.

**Criterios de aceptación**

- CA 1: Refleja la versión vigente
  - Dado que se aprueba una nueva versión de un procedimiento incluido en el Manual de Calidad
  - Cuando se consulta el Manual de Calidad
  - Entonces la vista generada muestra la versión vigente de ese procedimiento sin que nadie edite el Manual.

- CA 2: Carátula, índice y glosario
  - Dado que el repositorio tiene documentos vigentes
  - Cuando se consulta el Manual de Calidad
  - Entonces incluye carátula, índice navegable con código y versión de cada documento, y glosario.

- CA 3: Excluye obsoletos y borradores
  - Dado que existen documentos en borrador, en revisión u obsoletos
  - Cuando se genera el Manual de Calidad
  - Entonces esos documentos no aparecen.

- CA 4: Manual a una fecha
  - Dado que un auditor necesita ver el Manual tal como estaba en una fecha pasada
  - Cuando consulta el Manual indicando esa fecha
  - Entonces el sistema muestra las versiones que estaban vigentes en esa fecha (requiere HU-19).

### HU-11 Importación de documentos existentes

<!-- Status: Etapa 3 -->

**Descripción**: Como **administrador del sistema**, quiero **importar en bloque los documentos vigentes de los sistemas actuales** para **poner en marcha GeDoC sin cargar cada documento a mano**.

**Trazabilidad**: ISO 7101 7.5.5 | Story points: 8 | Matriz v1: Nueva

**Requisito**: Definir procesos de archivo, recuperación y retención de la información documentada, incluida la que proviene de otros sistemas.

Los documentos importados conservan la referencia a su versión original según la nomenclatura anterior (ver HU-40).

**Criterios de aceptación**

- CA 1: Importación exitosa
  - Dado un lote de documentos con sus metadatos en el formato de importación definido
  - Cuando el administrador ejecuta la importación
  - Entonces cada documento se crea con su código, tipo, unidad y estado "vigente", y la importación queda registrada en la pista de auditoría.

- CA 2: Registro con errores
  - Dado que algunos documentos del lote tienen metadatos obligatorios faltantes
  - Cuando se ejecuta la importación
  - Entonces esos documentos no se importan y el sistema genera un reporte con cada error, sin frenar el resto del lote.

- CA 3: Versión de origen conservada
  - Dado un documento importado que en el sistema anterior tenía la versión "4a"
  - Cuando se consulta en GeDoC
  - Entonces se ve la versión de origen como dato histórico, junto con la versión asignada por el sistema.

- CA 4: Reimportación sin duplicados
  - Dado que un lote ya fue importado
  - Cuando se intenta importar de nuevo el mismo lote
  - Entonces el sistema detecta los documentos ya existentes y no los duplica.

## Épica: Ciclo de vida y aprobación

### HU-12 Ciclo de vida documental con estados explícitos

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de Organización y Métodos**, quiero **que cada documento pase por estados explícitos desde borrador hasta archivado** para **saber en todo momento en qué etapa del circuito institucional está y quién debe actuar**.

**Trazabilidad**: ISO 7101 7.5.2 / 7.5.3 · Disposición 186/DME/2022 | Story points: 8 | Matriz v1: Nueva

**Requisito**: La información documentada debe revisarse y aprobarse antes de su uso, y controlarse durante todo su ciclo de vida.

Estados: `borrador` → `en revisión` → `aprobado por el responsable` → `aprobado institucionalmente` → `vigente` → `obsoleto` → `archivado`. Desde `en revisión` y desde `aprobado por el responsable` se puede volver a `borrador` si se rechaza. No se puede retroceder desde `vigente`: cualquier cambio genera una nueva versión que empieza su propio ciclo.

**Criterios de aceptación**

- CA 1: Avance por el circuito
  - Dado un documento en "borrador" con sus metadatos completos
  - Cuando el autor lo envía a revisión
  - Entonces pasa a "en revisión" y el responsable del proceso recibe la tarea de revisarlo.

- CA 2: Rechazo con observaciones
  - Dado un documento "en revisión"
  - Cuando el responsable del proceso lo rechaza
  - Entonces el sistema exige cargar las observaciones, el documento vuelve a "borrador" y el autor recibe las observaciones.

- CA 3: Transición inválida
  - Dado un documento en "borrador"
  - Cuando alguien intenta pasarlo directamente a "vigente"
  - Entonces el sistema rechaza la transición e informa cuál es el siguiente estado válido.

- CA 4: Transición según rol
  - Dado un documento "en revisión"
  - Cuando un usuario que no es el responsable del proceso intenta aprobarlo
  - Entonces el sistema no lo permite.

- CA 5: Autor no puede autoaprobarse
  - Dado que el autor de un documento es también responsable del proceso
  - Cuando intenta aprobar su propio documento
  - Entonces el sistema exige que la revisión la haga otro usuario con ese rol (regla a validar con Organización y Métodos).

- CA 6: Historial de estados
  - Dado un documento que pasó por varios estados
  - Cuando consulto su detalle
  - Entonces veo cada transición con usuario, fecha, hora y observaciones.

### HU-13 Doble aprobación: técnica e institucional

<!-- Status: Etapa 3 -->

**Descripción**: Como **responsable de Organización y Métodos**, quiero **registrar por separado la aprobación técnica del responsable del proceso y la aprobación institucional por Disposición de la Dirección Médica Ejecutiva** para **que el documento no quede vigente hasta que estén las dos**.

**Trazabilidad**: ISO 7101 7.5.2 · Disposición 186/DME/2022 | Story points: 8 | Matriz v1: N° 24

**Requisito**: La revisión y aprobación de idoneidad antes de publicar debe estar identificada, incluyendo quién revisó y quién aprobó.

El sistema registra la Disposición; no la emite. La Disposición se firma por el circuito administrativo habitual del hospital.

**Criterios de aceptación**

- CA 1: Bloqueo sin Disposición
  - Dado un documento con aprobación técnica registrada
  - Cuando intento marcarlo como "vigente" sin cargar el número y la fecha de la Disposición de la DME
  - Entonces el sistema bloquea el cambio de estado y pide completar esos datos.

- CA 2: Aprobación institucional completa
  - Dado un documento "aprobado por el responsable"
  - Cuando Organización y Métodos carga el número, la fecha y el PDF de la Disposición
  - Entonces el documento pasa a "aprobado institucionalmente" y queda listo para su publicación.

- CA 3: Número de Disposición duplicado
  - Dado que un número de Disposición ya está asociado a otros documentos
  - Cuando se carga ese mismo número para un documento nuevo
  - Entonces el sistema avisa que ya está en uso y pide confirmar (una misma Disposición puede aprobar varios documentos).

- CA 4: Fecha de Disposición inválida
  - Dado que se carga una Disposición con fecha futura o anterior a la aprobación técnica
  - Cuando se intenta guardar
  - Entonces el sistema rechaza la fecha e indica el motivo.

- CA 5: Constancia de ambas aprobaciones
  - Dado un documento vigente
  - Cuando un auditor consulta su detalle
  - Entonces ve por separado quién hizo la aprobación técnica y cuándo, y el número y fecha de la Disposición que lo aprobó.

### HU-14 Obsolescencia y archivo con retención

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **que los documentos obsoletos se archiven y se conserven durante el plazo de retención definido** para **poder consultarlos ante una auditoría sin que se confundan con los vigentes**.

**Trazabilidad**: ISO 7101 7.5.3 / 7.5.5 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Prevenir el uso no intencionado de información obsoleta y definir su retención y disposición final.

**Criterios de aceptación**

- CA 1: Obsolescencia por nueva versión
  - Dado un documento vigente
  - Cuando una nueva versión pasa a "vigente"
  - Entonces la versión anterior pasa automáticamente a "obsoleto".

- CA 2: Baja sin reemplazo
  - Dado un documento vigente que deja de aplicarse
  - Cuando Organización y Métodos lo da de baja cargando el motivo y la Disposición correspondiente
  - Entonces el documento pasa a "obsoleto" sin que exista una versión que lo reemplace.

- CA 3: Archivo con plazo de retención
  - Dado un documento obsoleto
  - Cuando se archiva
  - Entonces el sistema registra la fecha en que vence su plazo de retención según su tipo documental.

- CA 4: Prohibido borrar durante la retención
  - Dado un documento archivado cuyo plazo de retención no venció
  - Cuando cualquier usuario intenta eliminarlo
  - Entonces el sistema no lo permite.

- CA 5: Consulta de archivados
  - Dado un auditor interno
  - Cuando busca documentos archivados
  - Entonces puede verlos marcados claramente como "archivado", sin poder confundirlos con los vigentes.

### HU-15 Período de lectura previo a la vigencia

<!-- Status: Etapa 2 -->

**Descripción**: Como **jefe de servicio**, quiero **que un documento aprobado tenga un período de lectura antes de entrar en vigencia** para **que el personal lo conozca antes de tener que aplicarlo**.

**Trazabilidad**: ISO 7101 7.5.3 · Precedente QBN (estado "homologado") | Story points: 5 | Matriz v1: Nueva

**Requisito**: La información documentada debe estar disponible para su uso donde y cuando se necesite.

Este estado no figura en la Disposición 186 vigente; su incorporación requiere validación con Organización y Métodos.

**Criterios de aceptación**

- CA 1: Entrada en período de lectura
  - Dado un documento "aprobado institucionalmente" con un período de lectura de 7 días
  - Cuando se publica
  - Entonces pasa a "homologado", el personal de las unidades asociadas recibe la lectura obligatoria y la versión anterior sigue vigente.

- CA 2: Vigencia automática
  - Dado un documento "homologado"
  - Cuando se cumple el período de lectura
  - Entonces pasa automáticamente a "vigente" y la versión anterior a "obsoleto".

- CA 3: Vigencia inmediata por urgencia
  - Dado un cambio urgente (por ejemplo, una alerta de seguridad del paciente)
  - Cuando Organización y Métodos publica el documento con período de lectura cero
  - Entonces el documento pasa directamente a "vigente" y se registra el motivo de la urgencia.

### HU-16 Revisión periódica y solicitud de cambio

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de un proceso**, quiero **que el sistema me avise cuando un documento debe revisarse y que cualquier usuario pueda pedir un cambio** para **mantener los documentos actualizados sin depender de la memoria de nadie**.

**Trazabilidad**: ISO 7101 7.5.2 / 7.5.3 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Revisar y actualizar la información documentada cuando sea necesario, incluida su revisión periódica.

**Criterios de aceptación**

- CA 1: Revisión periódica vencida
  - Dado un documento vigente cuyo plazo de revisión según su tipo documental se cumple hoy
  - Cuando el sistema ejecuta el control diario
  - Entonces crea una tarea de revisión para el responsable del proceso y marca el documento como "revisión vencida".

- CA 2: Revisión sin cambios
  - Dado un documento con revisión periódica pendiente
  - Cuando el responsable confirma que sigue siendo adecuado sin cambios
  - Entonces se registra la revisión con fecha y usuario, y se reinicia el plazo sin generar una nueva versión.

- CA 3: Solicitud de cambio
  - Dado un usuario que detecta un error en un documento vigente
  - Cuando envía una solicitud de cambio con su motivo
  - Entonces el responsable del proceso la recibe y puede aceptarla (abre un borrador de nueva versión) o rechazarla con justificación.

- CA 4: Documento vigente mientras se revisa
  - Dado que se abrió un borrador de nueva versión
  - Cuando el personal consulta el documento
  - Entonces sigue viendo la versión vigente hasta que la nueva sea aprobada.

## Épica: Versionado

### HU-17 Historial de versiones con comparación

<!-- Status: Etapa 1 -->

**Descripción**: Como **usuario del sistema**, quiero **ver el historial completo de versiones de un documento y qué cambió en cada una** para **entender su evolución sin depender de la memoria institucional**.

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 8 | Matriz v1: N° 9

**Requisito**: Control de versiones y control de cambios de la información documentada.

**Criterios de aceptación**

- CA 1: Listado de versiones
  - Dado un documento con tres versiones publicadas
  - Cuando abro su historial de versiones
  - Entonces veo las tres versiones con número, fecha, autor, Disposición aprobatoria y resumen de cambios.

- CA 2: Comparación entre versiones
  - Dado un documento con al menos dos versiones
  - Cuando elijo dos versiones para comparar
  - Entonces el sistema muestra resaltado el texto agregado, eliminado y modificado.

- CA 3: Resumen de cambios obligatorio
  - Dado un autor que envía a revisión una nueva versión
  - Cuando no completa el resumen de cambios
  - Entonces el sistema no permite el envío.

- CA 4: Versión publicada no editable
  - Dado un documento vigente
  - Cuando un usuario intenta editarlo
  - Entonces el sistema no modifica esa versión y le ofrece crear un borrador de nueva versión.

- CA 5: Numeración automática
  - Dado un documento en la versión 3
  - Cuando se aprueba un nuevo cambio
  - Entonces el sistema asigna la versión siguiente según el esquema definido en HU-40, sin intervención manual.

### HU-18 Retiro automático de la versión obsoleta

<!-- Status: Etapa 1 -->

**Descripción**: Como **integrante del personal**, quiero **ver siempre y únicamente la versión vigente de cada documento** para **no aplicar por error un procedimiento desactualizado**.

**Trazabilidad**: ISO 7101 7.5.3 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Prevenir el uso no intencionado de información documentada obsoleta.

**Criterios de aceptación**

- CA 1: Retiro inmediato
  - Dado que la versión 2 de un POE está vigente
  - Cuando la versión 3 pasa a "vigente"
  - Entonces el personal deja de ver la versión 2 en búsquedas, listados y enlaces de la unidad.

- CA 2: Enlace a versión obsoleta
  - Dado que un usuario guardó el enlace directo a una versión que pasó a obsoleta
  - Cuando lo abre
  - Entonces el sistema le avisa que esa versión es obsoleta y lo redirige a la vigente.

- CA 3: Borradores invisibles para el personal
  - Dado que existe un borrador de nueva versión
  - Cuando un usuario sin rol de autor o revisor consulta el documento
  - Entonces no ve el borrador, solo la versión vigente.

- CA 4: Acceso a obsoletos por rol
  - Dado un usuario con rol de calidad o auditor interno
  - Cuando consulta el historial de un documento
  - Entonces puede abrir las versiones obsoletas, marcadas claramente como "obsoleta".

### HU-19 Reconstrucción de un documento a una fecha dada

<!-- Status: Etapa 2 -->

**Descripción**: Como **auditor interno**, quiero **ver qué versión de un documento estaba vigente en una fecha determinada** para **analizar un evento adverso con el procedimiento que se aplicaba en ese momento**.

**Trazabilidad**: ISO 7101 7.5.3 / 7.5.6 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Conservar la información documentada de forma que pueda recuperarse tal como estaba en un momento dado.

**Criterios de aceptación**

- CA 1: Versión vigente a una fecha
  - Dado un documento que tuvo varias versiones vigentes en el tiempo
  - Cuando consulto el documento indicando una fecha pasada
  - Entonces el sistema muestra la versión que estaba vigente ese día, con su estado y metadatos de ese momento.

- CA 2: Fecha anterior a la creación
  - Dado un documento creado en una fecha determinada
  - Cuando consulto una fecha anterior a su primera vigencia
  - Entonces el sistema informa que el documento no estaba vigente en esa fecha.

- CA 3: Consulta registrada
  - Dado que un usuario hace una consulta histórica
  - Cuando la ejecuta
  - Entonces la consulta queda registrada en la pista de auditoría.

## Épica: Consulta y difusión

### HU-20 Búsqueda y consulta de documentos vigentes

<!-- Status: Etapa 1 -->

**Descripción**: Como **integrante del personal**, quiero **buscar y abrir los documentos vigentes que aplican a mi servicio** para **tenerlos disponibles en el momento en que los necesito**.

**Trazabilidad**: ISO 7101 7.5.3 a | Story points: 5 | Matriz v1: Nueva

**Requisito**: La información documentada debe estar disponible y ser idónea para su uso donde y cuando se necesite.

**Criterios de aceptación**

- CA 1: Mis documentos
  - Dado un usuario asignado a una unidad funcional
  - Cuando entra al sistema
  - Entonces ve el listado de documentos vigentes asociados a su unidad.

- CA 2: Búsqueda por código, título o contenido
  - Dado que existen documentos vigentes
  - Cuando busco por código, título, palabra del contenido o tipo documental
  - Entonces el sistema devuelve los documentos vigentes que coinciden y que tengo permiso de ver.

- CA 3: Sin resultados
  - Dado que realizo una búsqueda
  - Cuando no hay documentos que coincidan
  - Entonces el sistema muestra un mensaje claro sin errores técnicos.

- CA 4: Filtros
  - Dado un listado de resultados
  - Cuando filtro por unidad funcional o tipo documental
  - Entonces solo veo los documentos que cumplen esos filtros.

- CA 5: Respeta permisos
  - Dado un documento restringido a un rol que no tengo
  - Cuando hago una búsqueda que coincidiría con él
  - Entonces no aparece en los resultados.

### HU-21 Acuse de lectura de documentos

<!-- Status: Etapa 2 -->

**Descripción**: Como **jefe de servicio**, quiero **que mi equipo confirme la lectura de los documentos que le aplican, incluida la política de calidad** para **demostrar en una auditoría que fueron comunicados y comprendidos**.

**Trazabilidad**: ISO 7101 5.2 / 7.5.3 | Story points: 3 | Matriz v1: N° 3

**Requisito**: La política de calidad y los procesos documentados deben comunicarse, entenderse y aplicarse en la organización.

**Criterios de aceptación**

- CA 1: Confirmación de lectura
  - Dado que la política de calidad fue publicada y me aplica
  - Cuando la abro y confirmo "Leído y comprendido"
  - Entonces el sistema registra fecha, hora, usuario y versión leída, y actualiza el porcentaje de adhesión del servicio.

- CA 2: Lecturas pendientes
  - Dado que tengo documentos con lectura obligatoria sin confirmar
  - Cuando entro al sistema
  - Entonces veo el listado de lecturas pendientes con su fecha de publicación.

- CA 3: Nueva versión pide nueva lectura
  - Dado que ya confirmé la lectura de la versión 2 de un documento
  - Cuando se publica la versión 3
  - Entonces el documento vuelve a figurar como lectura pendiente para mí.

- CA 4: Confirmación única
  - Dado que ya confirmé la lectura de una versión
  - Cuando intento confirmarla otra vez
  - Entonces el sistema conserva la primera confirmación y no crea un registro duplicado.

### HU-22 Reporte de adhesión por servicio

<!-- Status: Etapa 2 -->

**Descripción**: Como **jefe de servicio**, quiero **ver qué porcentaje de mi equipo confirmó la lectura de cada documento** para **actuar sobre quienes todavía no lo hicieron antes de una auditoría**.

**Trazabilidad**: ISO 7101 7.5.3 / 7.5.6 | Story points: 5 | Matriz v1: N° 11

**Requisito**: Registrar quién leyó cada documento, para verificar la toma de conocimiento del personal correspondiente.

**Criterios de aceptación**

- CA 1: Pendientes y recordatorio
  - Dado un proceso publicado hace 15 días con 60% de lectura confirmada en mi servicio
  - Cuando abro el reporte de adhesión
  - Entonces veo quiénes aún no confirmaron la lectura, con la opción de reenviarles el recordatorio.

- CA 2: Solo mi servicio
  - Dado que soy jefe de un servicio
  - Cuando consulto el reporte
  - Entonces solo veo los datos de las personas de mi servicio.

- CA 3: Vista institucional para calidad
  - Dado un usuario con rol de calidad
  - Cuando consulta el reporte
  - Entonces ve la adhesión de todos los servicios y puede exportarla.

- CA 4: Recordatorios sin repetición
  - Dado que ya se envió un recordatorio a una persona hoy
  - Cuando el jefe intenta reenviarlo
  - Entonces el sistema avisa que ya se envió y no manda un duplicado ese mismo día.

### HU-23 Marca de copia no controlada al imprimir

<!-- Status: Etapa 2 -->

**Descripción**: Como **integrante del personal**, quiero **que al imprimir un documento se agregue automáticamente una marca de "copia no controlada"** para **que quien reciba la copia sepa que debe verificar la vigencia en el sistema**.

**Trazabilidad**: Requisito institucional (Área de Calidad) | Story points: 3 | Matriz v1: N° 23

**Requisito**: Toda copia impresa es una copia no controlada: el documento válido es siempre el digital vigente en el repositorio. Es un criterio del Área de Calidad que todavía no figura explícito en la Disposición 186.

**Criterios de aceptación**

- CA 1: Marca en el PDF
  - Dado que abro un documento vigente para imprimirlo
  - Cuando genero el PDF de impresión
  - Entonces el sistema agrega un encabezado o marca de agua con "Copia no controlada. Impresa el [fecha]. Verifique la vigencia en el sistema.", junto con el código y la versión del documento.

- CA 2: Sin descarga sin marca
  - Dado un usuario sin rol de administración documental
  - Cuando intenta descargar el archivo original
  - Entonces el sistema solo le entrega la versión con la marca.

- CA 3: Registro de impresiones
  - Dado que un usuario genera un PDF de impresión
  - Cuando se genera el archivo
  - Entonces queda registrado en la pista de auditoría quién lo imprimió y cuándo.

## Épica: Notificaciones y vencimientos

### HU-24 Motor de notificaciones configurable

<!-- Status: Etapa 2 -->

**Descripción**: Como **administrador del sistema**, quiero **configurar qué eventos disparan notificaciones y a quién llegan** para **adaptar la comunicación a la estructura de cada servicio**.

**Trazabilidad**: ISO 7101 7.4.1 | Story points: 5 | Matriz v1: N° 7

**Requisito**: Determinar qué, cuándo, a quién y cómo se comunica dentro del sistema de gestión de calidad.

**Criterios de aceptación**

- CA 1: Notificación por unidad
  - Dado que configuro el evento "actualización de proceso" para notificar a "todo el personal asociado a la unidad funcional"
  - Cuando un proceso de Farmacia se actualiza
  - Entonces todos los usuarios de Farmacia reciben un correo con el enlace a la nueva versión.

- CA 2: Tareas del circuito de aprobación
  - Dado un documento que cambia de estado en el ciclo de vida
  - Cuando queda a la espera de un revisor o aprobador
  - Entonces el usuario que debe actuar recibe una notificación con el enlace a la tarea.

- CA 3: Sin duplicados
  - Dado un usuario que pertenece a dos unidades asociadas al mismo proceso
  - Cuando se dispara la notificación de actualización
  - Entonces recibe un solo correo.

- CA 4: Falla de envío
  - Dado que el servidor de correo no está disponible
  - Cuando se intenta enviar una notificación
  - Entonces el sistema la reintenta y, si sigue fallando, la registra en el log de incidentes técnicos.

- CA 5: Historial de envíos
  - Dado que se enviaron notificaciones por un evento
  - Cuando un responsable de calidad consulta el evento
  - Entonces ve a quién se envió cada notificación y cuándo.

### HU-25 Calendario de vencimientos

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **un calendario con los vencimientos de documentos, auditorías, capacitaciones y certificaciones con alertas escalonadas** para **no caer en una no conformidad por un vencimiento no detectado a tiempo**.

**Trazabilidad**: ISO 7101 7.5.3 / 9.1.1 | Story points: 8 | Matriz v1: N° 12

**Requisito**: Hacer seguimiento de los vencimientos de la documentación y de las auditorías y certificaciones periódicas.

**Criterios de aceptación**

- CA 1: Alerta previa al vencimiento
  - Dado un documento con vigencia de 2 años que vence en 30 días
  - Cuando faltan 30 días
  - Entonces el sistema notifica al autor y al responsable de calidad, y marca el documento como "próximo a vencer" en el panel principal.

- CA 2: Alertas escalonadas
  - Dado un vencimiento con alertas configuradas a 30, 15 y 5 días
  - Cuando se llega a cada uno de esos plazos sin que se haya resuelto
  - Entonces se envía la alerta correspondiente, y la de 5 días también llega al jefe del servicio.

- CA 3: Vencimiento cumplido
  - Dado un documento cuyo plazo de revisión venció sin ser revisado
  - Cuando el sistema ejecuta el control diario
  - Entonces lo marca como "vencido" en el calendario y en el panel de calidad.

- CA 4: Vista de calendario
  - Dado que existen vencimientos de distintos tipos
  - Cuando abro el calendario
  - Entonces veo los vencimientos por mes, filtrables por tipo y por unidad funcional.

- CA 5: Alerta cancelada al resolverse
  - Dado un documento con alerta de vencimiento enviada
  - Cuando se registra su revisión
  - Entonces no se envían las alertas siguientes de ese vencimiento.

## Épica: Gestión de la calidad

### HU-26 Registro de riesgos

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **registrar un riesgo detectado con su calificación, responsable y plan de mitigación** para **seguir su evolución hasta el cierre**.

**Trazabilidad**: ISO 7101 6.1.3 | Story points: 8 | Matriz v1: N° 4

**Requisito**: Mantener un registro documentado de riesgos y oportunidades, con responsables y planes de mitigación.

**Criterios de aceptación**

- CA 1: Alta de riesgo
  - Dado que detecto un riesgo asistencial
  - Cuando lo cargo con su calificación de probabilidad e impacto y asigno un responsable
  - Entonces el sistema lo agrega al registro de riesgos activos, calcula su nivel y notifica al responsable.

- CA 2: Riesgo sin responsable
  - Dado que estoy cargando un riesgo
  - Cuando intento guardarlo sin responsable o sin calificación
  - Entonces el sistema no lo guarda y señala los campos faltantes.

- CA 3: Seguimiento del plan
  - Dado un riesgo con plan de mitigación
  - Cuando el responsable registra un avance
  - Entonces queda en el historial del riesgo con fecha y usuario.

- CA 4: Cierre con recalificación
  - Dado un riesgo con plan de mitigación completado
  - Cuando el responsable de calidad lo cierra
  - Entonces el sistema exige registrar el nivel de riesgo residual.

- CA 5: Matriz de riesgos
  - Dado que existen riesgos activos
  - Cuando consulto el registro
  - Entonces los veo ordenados por nivel y filtrables por unidad funcional.

### HU-27 Objetivos de calidad

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **definir objetivos con su indicador, meta y frecuencia de revisión** para **que el sistema me avise cuando corresponde actualizarlos**.

**Trazabilidad**: ISO 7101 6.2 | Story points: 5 | Matriz v1: N° 5

**Requisito**: Los objetivos de calidad deben ser medibles, tener seguimiento y actualizarse a intervalos definidos.

**Criterios de aceptación**

- CA 1: Objetivo vencido
  - Dado un objetivo de calidad con frecuencia de revisión trimestral
  - Cuando se cumple el plazo sin que se haya cargado una actualización
  - Entonces el sistema marca el objetivo como "vencido" y notifica al responsable por correo.

- CA 2: Carga de medición
  - Dado un objetivo con indicador y meta
  - Cuando el responsable carga el valor medido del período
  - Entonces el sistema actualiza el estado (en curso / cumplido / no cumplido) comparando con la meta.

- CA 3: Objetivo no medible
  - Dado que estoy creando un objetivo
  - Cuando intento guardarlo sin indicador, meta o frecuencia
  - Entonces el sistema no lo guarda.

- CA 4: Evolución
  - Dado un objetivo con varias mediciones
  - Cuando consulto su detalle
  - Entonces veo la evolución de las mediciones contra la meta.

### HU-28 Legajo de competencias del personal

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de Recursos Humanos**, quiero **cargar las capacitaciones de cada profesional con su fecha de vencimiento** para **tener evidencia documentada de su competencia ante una auditoría**.

**Trazabilidad**: ISO 7101 7.2 | Story points: 5 | Matriz v1: N° 6

**Requisito**: Mantener evidencia documentada de la competencia (educación, capacitación, experiencia) del personal.

**Criterios de aceptación**

- CA 1: Alerta de capacitación por vencer
  - Dado que un profesional tiene una capacitación que vence en 30 días
  - Cuando el sistema detecta ese plazo
  - Entonces notifica al profesional y a su jefe de servicio.

- CA 2: Evidencia adjunta
  - Dado que cargo una capacitación
  - Cuando adjunto el certificado
  - Entonces queda guardado en el legajo del profesional con fecha de realización y vencimiento.

- CA 3: Capacitaciones obligatorias faltantes
  - Dado que un servicio tiene capacitaciones obligatorias definidas
  - Cuando el jefe consulta el estado de su equipo
  - Entonces ve quiénes no tienen cada capacitación obligatoria o la tienen vencida.

- CA 4: Privacidad del legajo
  - Dado un usuario que no es RRHH, el propio profesional ni su jefe
  - Cuando intenta ver el legajo de un profesional
  - Entonces el sistema le niega el acceso.

### HU-29 Planificación de auditorías internas

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **planificar el programa anual de auditorías internas** para **asegurar que cada unidad dentro del alcance se audite al menos una vez cada doce meses**.

**Trazabilidad**: ISO 7101 9.2.2 | Story points: 5 | Matriz v1: N° 14

**Requisito**: Realizar auditorías internas al menos una vez cada doce meses, con evidencia documentada.

La historia N° 14 de la matriz v1 (13 puntos) se dividió en planificación (HU-29) y ejecución (HU-30).

**Criterios de aceptación**

- CA 1: Programa anual
  - Dado que existen unidades dentro del alcance
  - Cuando armo el programa anual asignando fecha, auditor y cláusulas a cada unidad
  - Entonces las auditorías quedan planificadas en el calendario de vencimientos.

- CA 2: Unidad sin auditoría planificada
  - Dado un programa anual que no incluye alguna unidad dentro del alcance
  - Cuando lo guardo
  - Entonces el sistema me advierte qué unidades quedaron sin auditoría en los próximos doce meses.

- CA 3: Independencia del auditor
  - Dado un auditor que pertenece a la unidad a auditar
  - Cuando intento asignarlo
  - Entonces el sistema no lo permite.

### HU-30 Ejecución de auditoría interna con checklist

<!-- Status: Etapa 2 -->

**Descripción**: Como **auditor interno**, quiero **ejecutar una auditoría con un checklist basado en las cláusulas de la ISO 7101** para **documentar hallazgos y evidencias de forma estructurada**.

**Trazabilidad**: ISO 7101 9.1.2 / 9.2.2 | Story points: 8 | Matriz v1: N° 14

**Requisito**: Definir indicadores de calidad y realizar auditorías internas con evidencia documentada.

**Criterios de aceptación**

- CA 1: No conformidad generada desde el hallazgo
  - Dado que inicio una auditoría interna del servicio de Farmacia
  - Cuando marco la cláusula 8.12.4 (seguridad de medicamentos) como "no conforme" y adjunto evidencia
  - Entonces el sistema genera una no conformidad vinculada a esa auditoría.

- CA 2: Hallazgo sin evidencia
  - Dado que marco una cláusula como "no conforme"
  - Cuando intento guardar sin descripción ni evidencia
  - Entonces el sistema no lo permite.

- CA 3: Cierre de auditoría
  - Dado que todas las cláusulas del checklist tienen resultado
  - Cuando cierro la auditoría
  - Entonces se genera el informe con hallazgos y evidencias, y la auditoría deja de poder editarse.

- CA 4: Checklist incompleto
  - Dado que quedan cláusulas sin evaluar
  - Cuando intento cerrar la auditoría
  - Entonces el sistema indica qué cláusulas faltan.

### HU-31 Gestión de no conformidades

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **gestionar cada no conformidad a través de un flujo de estados definido** para **que no se cierre sin verificar que la acción correctiva fue eficaz**.

**Trazabilidad**: ISO 7101 10.2.1 / 10.2.2 | Story points: 8 | Matriz v1: N° 16

**Requisito**: Gestionar no conformidades desde su detección hasta el cierre, con verificación de eficacia de la acción correctiva.

Estados: `detectada` → `en análisis` → `acción implementada` → `eficacia verificada` → `cerrada`.

**Criterios de aceptación**

- CA 1: Bloqueo de cierre sin eficacia
  - Dado una no conformidad en estado "acción implementada"
  - Cuando el responsable intenta cerrarla sin cargar la verificación de eficacia
  - Entonces el sistema bloquea el cierre y pide completar ese campo.

- CA 2: Análisis de causa
  - Dado una no conformidad "en análisis"
  - Cuando se registra la acción correctiva
  - Entonces el sistema exige cargar la causa raíz, el responsable y la fecha comprometida.

- CA 3: Acción no eficaz
  - Dado que la verificación de eficacia resulta negativa
  - Cuando se registra
  - Entonces la no conformidad vuelve a "en análisis" y se notifica al responsable.

- CA 4: Plazo vencido
  - Dado una acción correctiva con fecha comprometida
  - Cuando vence sin haberse implementado
  - Entonces el sistema notifica al responsable y al responsable de calidad.

- CA 5: Vínculo con documentos
  - Dado una acción correctiva que requiere modificar un procedimiento
  - Cuando se vincula la no conformidad al documento
  - Entonces el documento muestra la no conformidad asociada y se abre una solicitud de cambio (HU-16).

### HU-32 Reporte rápido de no conformidades

<!-- Status: Etapa 2 -->

**Descripción**: Como **enfermero de planta**, quiero **reportar una no conformidad que detecté en mi turno con pocos clics** para **que se investigue sin tener que pasar por trámites largos**.

**Trazabilidad**: ISO 7101 10.2.2 | Story points: 3 | Matriz v1: N° 17

**Requisito**: Permitir que las partes interesadas (personal, usuarios, cuidadores) informen no conformidades reales y potenciales.

**Criterios de aceptación**

- CA 1: Número de seguimiento
  - Dado que detecto una no conformidad durante mi turno
  - Cuando completo el formulario rápido de reporte
  - Entonces recibo un número de seguimiento y puedo consultar más adelante el estado de mi reporte.

- CA 2: Formulario mínimo
  - Dado que abro el formulario de reporte
  - Cuando lo completo
  - Entonces solo se me piden descripción, unidad y fecha; la adjunción de fotos o archivos es opcional.

- CA 3: Llega a calidad
  - Dado que se envió un reporte
  - Cuando se registra
  - Entonces se crea una no conformidad en estado "detectada" y se notifica al responsable de calidad.

- CA 4: Descripción vacía
  - Dado que intento enviar el reporte sin descripción
  - Cuando presiono "Enviar"
  - Entonces el sistema no lo envía y señala el campo.

### HU-33 Panel de revisión por la dirección

<!-- Status: Etapa 2 -->

**Descripción**: Como **director del hospital**, quiero **ver un panel con el estado consolidado del sistema de calidad** para **tomar decisiones en la revisión por la dirección sin pedir reportes manuales a cada área**.

**Trazabilidad**: ISO 7101 9.3 | Story points: 8 | Matriz v1: N° 15

**Requisito**: La revisión por la dirección debe incluir el desempeño del sistema, no conformidades, resultados de auditorías e indicadores.

**Criterios de aceptación**

- CA 1: Panel consolidado
  - Dado que se aproxima la reunión trimestral de revisión por la dirección
  - Cuando abro el panel ejecutivo
  - Entonces veo los indicadores y objetivos de calidad, las no conformidades abiertas, el estado de las auditorías y los riesgos principales del período.

- CA 2: Período seleccionable
  - Dado que estoy en el panel
  - Cuando cambio el período
  - Entonces todos los indicadores se recalculan para ese período.

- CA 3: Detalle desde el panel
  - Dado un indicador del panel
  - Cuando lo selecciono
  - Entonces accedo al detalle de los registros que lo componen.

- CA 4: Exportación para el acta
  - Dado que se realizó la revisión
  - Cuando exporto el panel
  - Entonces obtengo un PDF con los datos del período para adjuntar al acta de la revisión.

## Épica: Auditoría y seguridad

### HU-34 Pista de auditoría inalterable

<!-- Status: Etapa 1 -->

**Descripción**: Como **auditor interno**, quiero **consultar el registro completo de acciones sobre un documento** para **verificar quién hizo qué y cuándo, con la certeza de que el registro no fue alterado**.

**Trazabilidad**: ISO 7101 7.5.6 | Story points: 8 | Matriz v1: N° 18

**Requisito**: Realizar auditorías periódicas de registros, verificando fecha, hora e identidad del responsable de cada actividad.

Se subió de 5 a 8 puntos: el gap analysis de Alfresco mostró que el administrador puede borrar entradas de auditoría por API, así que la inalterabilidad hay que construirla aparte (registro de solo agregado).

**Criterios de aceptación**

- CA 1: Registro de cada acción
  - Dado un documento con varias ediciones
  - Cuando consulto su pista de auditoría
  - Entonces veo cada acción (creación, edición, cambio de estado, aprobación, lectura, impresión) con usuario, fecha y hora.

- CA 2: Ni el administrador puede alterarla
  - Dado un usuario con rol de administrador
  - Cuando intenta modificar o borrar una entrada de la pista de auditoría, por interfaz o por API
  - Entonces el sistema no lo permite y el intento queda registrado.

- CA 3: Detección de manipulación
  - Dado que alguien modificó directamente en la base de datos una entrada de auditoría
  - Cuando se ejecuta la verificación de integridad
  - Entonces el sistema detecta la inconsistencia y genera un incidente técnico.

- CA 4: Exportación para auditoría externa
  - Dado un auditor interno
  - Cuando exporta la pista de un documento o de un período
  - Entonces obtiene un archivo en formato abierto con todas las entradas.

- CA 5: Filtros
  - Dado que la pista tiene muchas entradas
  - Cuando filtro por usuario, tipo de acción o rango de fechas
  - Entonces solo veo las entradas que coinciden.

### HU-35 Backups y restauración

<!-- Status: Etapa 2 -->

**Descripción**: Como **administrador del sistema**, quiero **que el sistema haga backups automáticos diarios y pueda restaurarse ante una falla** para **no perder evidencia documentada crítica para la certificación**.

**Trazabilidad**: ISO 7101 7.5.4 | Story points: 8 | Matriz v1: N° 13

**Requisito**: El sistema de gestión de la información debe tener backups, planes de contingencia y protección de ciberseguridad.

**Criterios de aceptación**

- CA 1: Restauración sin pérdida
  - Dado que el sistema ejecuta un backup automático diario
  - Cuando simulo una restauración desde el backup del día anterior
  - Entonces toda la información documentada, los metadatos y la pista de auditoría se recuperan sin pérdida.

- CA 2: Falla del backup
  - Dado que el backup programado falla
  - Cuando termina la ejecución con error
  - Entonces se registra un incidente técnico y se notifica al administrador.

- CA 3: Backup fuera del servidor
  - Dado que se completó un backup
  - Cuando se verifica su ubicación
  - Entonces existe una copia en un almacenamiento distinto del servidor principal.

- CA 4: Prueba periódica documentada
  - Dado el plan de contingencia
  - Cuando se cumple el período de prueba definido
  - Entonces se ejecuta una restauración de prueba y su resultado queda registrado como evidencia.

### HU-36 Log de incidentes técnicos

<!-- Status: Etapa 2 -->

**Descripción**: Como **administrador del sistema**, quiero **que cada falla del sistema quede registrada automáticamente en un log de incidentes técnicos** para **revisarlo periódicamente y demostrar que el sistema está monitoreado**.

**Trazabilidad**: ISO 7101 7.5.4 d | Story points: 5 | Matriz v1: N° 22

**Requisito**: El sistema de gestión de la información debe incluir el registro de incidentes de cualquier mal funcionamiento del propio sistema.

**Criterios de aceptación**

- CA 1: Registro automático
  - Dado que el sistema detecta un error interno (por ejemplo, una falla al guardar un documento)
  - Cuando ocurre el error
  - Entonces se crea un registro con fecha, hora, tipo de error y componente afectado, visible para el administrador.

- CA 2: Separado de la pista documental
  - Dado que existe un incidente técnico
  - Cuando un auditor consulta la pista de auditoría de documentos
  - Entonces el incidente no aparece ahí; solo figura en el log de incidentes.

- CA 3: Revisión periódica
  - Dado un incidente abierto
  - Cuando el responsable lo revisa
  - Entonces registra el análisis y la resolución, y el incidente pasa a "cerrado" con fecha y usuario.

- CA 4: Incidente crítico
  - Dado un incidente clasificado como crítico (por ejemplo, el sistema no disponible)
  - Cuando se registra
  - Entonces se notifica de inmediato al administrador.

### HU-37 Evidencia de validación del sistema

<!-- Status: Etapa 2 -->

**Descripción**: Como **administrador del sistema**, quiero **registrar la evidencia de las pruebas de validación antes de poner en producción cada cambio** para **demostrar en una auditoría que el sistema fue validado antes de usarse**.

**Trazabilidad**: ISO 7101 7.5.4 | Story points: 8 | Matriz v1: N° 21

**Requisito**: Validar los sistemas de gestión de la información antes de su uso, y volver a validarlos ante cualquier cambio, incluida la configuración.

**Criterios de aceptación**

- CA 1: Bloqueo sin validación
  - Dado que voy a desplegar un cambio de configuración en producción
  - Cuando el protocolo de validación no está cargado y aprobado
  - Entonces el sistema bloquea el despliegue.

- CA 2: Evidencia vinculada a la versión
  - Dado que completé el protocolo con resultados esperados y obtenidos
  - Cuando se aprueba
  - Entonces queda guardado como evidencia vinculada a esa versión del sistema.

- CA 3: Prueba fallida
  - Dado un protocolo con al menos un resultado obtenido distinto del esperado
  - Cuando se intenta aprobar
  - Entonces el sistema exige justificar el desvío o rechaza la aprobación.

- CA 4: Trazabilidad requisito–prueba
  - Dado el conjunto de pruebas de aceptación
  - Cuando se consulta la evidencia de una versión
  - Entonces cada caso de aceptación ejecutado aparece vinculado a su historia de usuario y a su cláusula de la norma.

### HU-38 Exportación en formatos abiertos

<!-- Status: Etapa 2 -->

**Descripción**: Como **administrador del sistema**, quiero **exportar los documentos con sus metadatos e historial de versiones en formatos estándar** para **que la información nunca quede cautiva de la herramienta si en el futuro se cambia de sistema**.

**Trazabilidad**: ISO 7101 7.5.5 | Story points: 5 | Matriz v1: N° 25

**Requisito**: Definir procesos de archivo, recuperación y retención de la información documentada, sin que quede cautiva de un único sistema.

**Criterios de aceptación**

- CA 1: Exportación completa
  - Dado que soy administrador del sistema
  - Cuando pido una exportación completa de la base documental
  - Entonces el sistema genera un paquete con los archivos, sus metadatos y el historial de versiones en formatos abiertos (PDF/CSV/JSON).

- CA 2: Exportación filtrada
  - Dado que necesito solo una parte de la base
  - Cuando filtro por unidad funcional, tipo documental o estado antes de exportar
  - Entonces el paquete contiene solo esos documentos.

- CA 3: Solo administradores
  - Dado un usuario sin rol de administrador
  - Cuando intenta pedir una exportación completa
  - Entonces el sistema no lo permite.

- CA 4: Exportación registrada
  - Dado que se realizó una exportación
  - Cuando se completa
  - Entonces queda registrada en la pista de auditoría con usuario, fecha y filtros usados.

## Épica: Decisiones con Organización y Métodos

### HU-39 Identidad autenticada vs. firma por iniciales

<!-- Status: Etapa 1 -->

**Descripción**: Como **equipo de proyecto**, quiero **una decisión formal de Organización y Métodos sobre si la identidad autenticada del sistema reemplaza la firma por iniciales de la Disposición 186** para **no generar un desvío respecto de la normativa vigente sin haberlo consultado**.

**Trazabilidad**: ISO 7101 7.5.2 / 7.5.5 · Disposición 186/DME/2022 [PUNTO DE FRICCIÓN] | Story points: 2 | Matriz v1: N° 27

**Requisito**: La norma exige una identidad autenticada y trazable en la creación, revisión y aprobación; la Disposición 186 vigente permite identificar a quien hizo, revisó o aprobó solo con sus iniciales.

Bloquea: HU-01, HU-12, HU-13.

**Criterios de aceptación**

- CA 1: Constancia de la decisión
  - Dado que el sistema registra la identidad autenticada en lugar de iniciales tipeadas
  - Cuando se audite el cumplimiento de la Disposición 186 vigente
  - Entonces existe una constancia escrita de Organización y Métodos que valida este criterio o indica cuál implementar.

- CA 2: Impacto en el diseño
  - Dado que la decisión está tomada
  - Cuando se diseña el circuito de aprobación
  - Entonces las historias afectadas (HU-01, HU-12, HU-13) se actualizan según lo decidido.

### HU-40 Esquema único de versionado

<!-- Status: Etapa 1 -->

**Descripción**: Como **equipo de proyecto**, quiero **acordar con Organización y Métodos un esquema de versionado único y automático** para **que las versiones puedan asignarse y compararse por software, cosa que no permite la flexibilidad actual de la Disposición 186 (v1, 3.2, 4a...)**.

**Trazabilidad**: ISO 7101 7.5.3 · Disposición 186/DME/2022 [PUNTO DE FRICCIÓN] | Story points: 2 | Matriz v1: N° 28

**Requisito**: La norma pide un control de versiones consistente; la Disposición 186 permite nomenclaturas de versión flexibles.

Bloquea: HU-11, HU-17.

**Criterios de aceptación**

- CA 1: Esquema documentado
  - Dado que el sistema debe asignar las versiones automáticamente
  - Cuando se define el esquema
  - Entonces existe una decisión documentada y validada con Organización y Métodos sobre el formato único, acorde a la Disposición 186 vigente o con una excepción formal.

- CA 2: Criterio para documentos existentes
  - Dado que hay documentos vigentes con nomenclaturas anteriores (por ejemplo, "4a")
  - Cuando se acuerda el esquema
  - Entonces la decisión también define cómo se convierten o conservan esas versiones al importarlas (HU-11).

### HU-41 Alcance de la integración con el SIG

<!-- Status: Etapa 1 -->

**Descripción**: Como **equipo de proyecto**, quiero **definir con la Gerencia de Sistemas y Organización y Métodos qué formularios siguen en el SIG y cuáles pasan a GeDoC** para **que ambos sistemas convivan sin dos fuentes de verdad para un mismo documento**.

**Trazabilidad**: ISO 7101 7.5.5.i [PUNTO DE FRICCIÓN] | Story points: 3 | Matriz v1: N° 29

**Requisito**: La organización debe definir procesos para integrar la información documentada que se genera en distintos sistemas e interfaces.

Bloquea: HU-08 (tipo Formulario), HU-11.

**Criterios de aceptación**

- CA 1: Documento de decisión
  - Dado que existen formularios que hoy emite el SIG
  - Cuando se define el alcance del nuevo sistema
  - Entonces hay un documento de decisión firmado que establece qué tipos de formularios quedan en el SIG y cuáles pasan al nuevo sistema.

- CA 2: Sin gestión duplicada
  - Dado un tipo de formulario asignado al SIG
  - Cuando alguien intenta crearlo como documento controlado en GeDoC
  - Entonces el sistema le indica que ese tipo se gestiona en el SIG.

- CA 3: Mecanismo de integración definido
  - Dado que algún documento debe verse en ambos sistemas
  - Cuando se cierra la decisión
  - Entonces se define cuál de los dos es la fuente de verdad y cómo la consulta el otro (enlace, API o ninguno).
