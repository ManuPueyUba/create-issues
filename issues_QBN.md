<!-- Fuente: IT QBN -->

## Épica: Acceso y usuarios

### MVP-25 Entrar eligiendo el cargo con el que voy a trabajar

<!-- Status: Etapa 1 -->

**Descripción**: Como **profesional con más de un cargo**, quiero **elegir el cargo con el que entro al sistema** para **operar con los permisos que corresponden a la tarea que voy a hacer**.

**Trazabilidad**: IT QBN · Acceso | Story points: 8 | Matriz v1: Nueva

**Requisito**: La lógica del sistema es NOMBRE DE USUARIO - CARGO - PERMISO. El sistema reconoce los cargos que ocupa la persona y muestra arriba de la pantalla su nombre y el cargo elegido.

**Estado actual**: ⚠️ Implementado, no cumple. El login funciona, pero cada usuario tiene un solo rol (`HospitalUser.role`), no se elige cargo ni permiso al entrar, y los permisos salen directamente de ese rol.

**Comentarios**: El equipo definió entrar con mail y contraseña en lugar de un nombre de usuario.

**Criterios de aceptación**

- CA 1: Persona con varios cargos
  - Dado que tengo más de un cargo asignado
  - Cuando inicio sesión con credenciales válidas
  - Entonces el sistema me pide elegir el cargo y el permiso antes de entrar.

- CA 2: Persona con un solo cargo
  - Dado que tengo un único cargo asignado
  - Cuando inicio sesión con credenciales válidas
  - Entonces entro con ese cargo sin tener que elegirlo.

- CA 3: Permisos del cargo elegido
  - Dado que entré con uno de mis cargos
  - Cuando intento una acción que solo permite otro de mis cargos
  - Entonces el sistema la rechaza.

- CA 4: Identificación en pantalla
  - Dado que entré con un cargo
  - Cuando navego por el sistema
  - Entonces veo arriba de la pantalla mi nombre y el cargo elegido.

### MVP-26 Datos completos de la cuenta de usuario

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador u organizador**, quiero **que cada cuenta tenga todos los datos de la persona** para **identificarla correctamente en el sistema**.

**Trazabilidad**: IT QBN · Módulo Organización 1 | Story points: 3 | Matriz v1: Nueva

**Requisito**: El alta de usuarios registra nombre, apellido, usuario, contraseña, título de cortesía, e-mail y fecha de alta.

**Estado actual**: ⚠️ Implementado, no cumple. La cuenta guarda un único `name`, mail, contraseña y fecha de registro. Faltan apellido separado y título de cortesía.

**Criterios de aceptación**

- CA 1: Alta con todos los datos
  - Dado que estoy dando de alta a una persona
  - Cuando completo nombre, apellido, título de cortesía, e-mail y contraseña
  - Entonces la cuenta queda guardada con esos datos y con su fecha de alta.

- CA 2: Datos obligatorios
  - Dado que dejé vacío un dato obligatorio
  - Cuando intento guardar
  - Entonces el sistema no crea la cuenta y señala qué falta.

### MVP-27 Modificar las propiedades de un usuario

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador**, quiero **modificar los datos de un usuario desde la grilla** para **mantenerlos actualizados**.

**Trazabilidad**: IT QBN · Módulo Organización 1 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Se selecciona a la persona en la grilla y desde sus propiedades se hacen las modificaciones.

**Estado actual**: ❌ No implementado. Solo se puede cambiar el rol y sumar a un sector. No hay endpoint para editar los datos de la cuenta.

**Criterios de aceptación**

- CA 1: Modificación exitosa
  - Dado un usuario seleccionado en la grilla
  - Cuando cambio sus datos y guardo
  - Entonces la grilla muestra los datos nuevos.

- CA 2: Mail ya usado
  - Dado que otra cuenta ya usa ese mail
  - Cuando intento guardarlo en este usuario
  - Entonces el sistema rechaza el cambio.

### MVP-28 Dar de baja a una persona

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador**, quiero **dar de baja a una persona que ya no debe acceder** para **que solo entren quienes están autorizados**.

**Trazabilidad**: IT QBN · Acceso y Módulo Organización 1 | Story points: 3 | Matriz v1: Nueva

**Requisito**: El administrador incorpora y elimina a las personas autorizadas. Al dar de baja, el sistema pide confirmación.

**Estado actual**: ❌ No implementado. No hay forma de dar de baja una cuenta, ni desde el backend ni desde el front.

**Criterios de aceptación**

- CA 1: Baja con confirmación
  - Dado un usuario seleccionado en la grilla
  - Cuando elijo eliminarlo
  - Entonces el sistema pide confirmación antes de darlo de baja.

- CA 2: Sin acceso
  - Dado un usuario dado de baja
  - Cuando intenta iniciar sesión
  - Entonces el sistema no lo deja entrar.

- CA 3: Historial conservado
  - Dado un usuario dado de baja
  - Cuando consulto documentos o registros en los que participó
  - Entonces su nombre sigue apareciendo.

### MVP-29 Ver los pendientes de cualquier usuario

<!-- Status: Etapa 1 -->

**Descripción**: Como **administrador**, quiero **ver los documentos pendientes de un usuario en cualquier estado** para **hacer seguimiento o reasignar lo que quedó sin resolver**.

**Trazabilidad**: IT QBN · Módulo Organización 1 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Desde la grilla de usuarios, "Pendientes por usuario" muestra los documentos pendientes en cualquier estado.

**Estado actual**: ⚠️ Implementado, no cumple. `GET /users/{id}/pending-reviews` devuelve solo revisiones y aprobaciones, y no hay acceso desde la grilla de usuarios.

**Criterios de aceptación**

- CA 1: Pendientes de un usuario
  - Dado un usuario seleccionado en la grilla
  - Cuando elijo "Pendientes por usuario"
  - Entonces veo sus documentos pendientes en cualquier estado.

## Épica: Organización

### MVP-30 Administrar las áreas funcionales

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **crear, modificar y eliminar áreas funcionales en un árbol de jerarquías** para **que el sistema refleje el organigrama por sectores**.

**Trazabilidad**: IT QBN · Módulo Organización 2 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Cada área tiene denominación, área de la que es subordinada y fecha de alta. Se puede eliminar desde la grilla, con confirmación.

**Estado actual**: ⚠️ Implementado, no cumple. Se pueden crear sectores con nombre, sigla y padre, y verlos en árbol. Falta la fecha de alta, y no se pueden modificar ni eliminar.

**Criterios de aceptación**

- CA 1: Alta
  - Dado que completo denominación y área superior
  - Cuando guardo
  - Entonces el área aparece en el árbol con su fecha de alta.

- CA 2: Modificación
  - Dado un área existente
  - Cuando cambio sus propiedades
  - Entonces el árbol muestra los datos nuevos.

- CA 3: Eliminación con confirmación
  - Dado un área seleccionada en la grilla
  - Cuando elijo eliminarla
  - Entonces el sistema pide confirmación antes de hacerlo.

### MVP-31 Ver los documentos que debe leer un área

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de un área**, quiero **ver desde el árbol qué documentos debe leer esa área** para **controlar que tenga lo que necesita**.

**Trazabilidad**: IT QBN · Módulo Organización 2 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Con doble clic en un área se ven sus propiedades y, con una casilla, los documentos que debe leer.

**Estado actual**: ⚠️ Implementado, no cumple. El detalle del sector muestra los documentos del sector, y los lectores de un documento se definen por rol o por usuario. No se pueden consultar los documentos que un área debe leer.

**Criterios de aceptación**

- CA 1: Documentos a leer
  - Dado un área del árbol
  - Cuando abro sus propiedades y marco la casilla de documentos
  - Entonces veo los documentos que esa área debe leer.

### MVP-32 Administrar cargos y asignarlos a personas

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **crear cargos en una jerarquía y asignarlos a personas** para **representar quién ocupa cada función y con qué permisos**.

**Trazabilidad**: IT QBN · Módulo Organización 3 | Story points: 8 | Matriz v1: Nueva

**Requisito**: Cada cargo tiene denominación, tipo, cargo del que es subordinado, áreas funcionales, permisos, usuarios y capacidad requerida.

**Estado actual**: ⚠️ Implementado, no cumple. Los cargos son una lista fija en el código (enum `Role`), sin jerarquía ni datos propios, y una persona tiene un solo cargo.

**Criterios de aceptación**

- CA 1: Alta de cargo
  - Dado que completo los datos del cargo
  - Cuando guardo
  - Entonces aparece en la jerarquía de cargos, subordinado al cargo indicado.

- CA 2: Varios cargos
  - Dado una persona que ocupa dos cargos
  - Cuando se los asigno
  - Entonces puede elegir cualquiera de los dos al entrar.

- CA 3: Sin cambiar el código
  - Dado que el hospital necesita un cargo nuevo
  - Cuando el organizador lo crea
  - Entonces queda disponible sin modificar el sistema.

### MVP-33 Permisos de cada cargo según QBN

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **que cada cargo tenga los permisos definidos en el instructivo** para **que cada persona pueda hacer solo lo que le corresponde**.

**Trazabilidad**: IT QBN · Módulo Organización 3 | Story points: 5 | Matriz v1: N° 10

**Requisito**: Permisos posibles: administrador, organizador, iniciador, lector, revisor, aprobador e impresor de copia no controlada, entre otros.

Coordinador de laboratorios, Jefe de Área y Responsable de Calidad: administrador, organizador, aprobador, iniciador, lector, revisor y copia controlada. Bioquímico Jefe de Clínica y Responsable de sector: aprobador, iniciador, lector, revisor e impresor de copia controlada. Bioquímicos y Profesionales Asistentes: iniciador, lector y revisor, y aprobador si fuera necesario. Técnicos, Bioquímicos Residentes y Becarios: lector, e iniciador de ser necesario.

**Estado actual**: ⚠️ Implementado, no cumple. La tabla de `RolePermissions` se parece a la del instructivo, pero no existen los permisos "organizador" e "impresor de copia no controlada". El "si fuera necesario" se resolvió con roles separados (`_APROBADOR`, `_INICIADOR`) en vez de asignarlo a la persona.

**Criterios de aceptación**

- CA 1: Permisos por cargo
  - Dado un usuario con uno de los cargos del instructivo
  - Cuando usa el sistema
  - Entonces tiene exactamente los permisos que el instructivo indica para ese cargo.

- CA 2: Permiso adicional si es necesario
  - Dado un profesional asistente que necesita aprobar
  - Cuando se le habilita el permiso de aprobador
  - Entonces puede aprobar, sin cambiar de cargo.

- CA 3: Acción no permitida
  - Dado un usuario sin el permiso necesario
  - Cuando intenta esa acción
  - Entonces el sistema la rechaza.

## Épica: Clasificación de documentos

### MVP-34 Grupos de documentos con sigla de tres letras

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **crear grupos de documentos con un código de tres letras** para **que el código de cada documento identifique su sector**.

**Trazabilidad**: IT QBN · Módulo Documentos 1 | Story points: 2 | Matriz v1: Nueva

**Requisito**: El nombre del grupo lleva adelante tres letras y un espacio, que son su código. Ejemplo: LAC Laboratorio Central. El grupo es el sector al que pertenece el documento.

**Estado actual**: ⚠️ Implementado, no cumple. El sector funciona como grupo y tiene sigla, pero la sigla admite hasta 20 caracteres y no se puede dar de baja el grupo.

**Criterios de aceptación**

- CA 1: Sigla válida
  - Dado que cargo un grupo con una sigla de tres letras
  - Cuando guardo
  - Entonces queda creado, y esa sigla se usa en el código de sus documentos.

- CA 2: Sigla inválida
  - Dado que cargo una sigla que no tiene tres letras
  - Cuando intento guardar
  - Entonces el sistema la rechaza.

- CA 3: Documentos del grupo
  - Dado un grupo existente
  - Cuando elijo ver sus documentos
  - Entonces veo los documentos que pertenecen a ese grupo.

### MVP-35 Tipos de documento configurables

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **contar con todos los tipos de documento y poder crear otros** para **clasificar toda la documentación del laboratorio**.

**Trazabilidad**: IT QBN · Módulo Documentos 2 y 4 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Tipos: MS. Manual de Sección, INS Inserto de técnicas analíticas, IT. Instructivo de trabajo, MC. Manual de Calidad, MOI Metas, objetivos e indicadores, PG. Procedimiento general, PC. Política de Calidad, POE Procedimiento Operativo, REG Registro y LIS Lista. La sigla tiene tres caracteres: si tiene menos, se completa con un punto. Los tipos se subordinan a una raíz.

**Estado actual**: ⚠️ Implementado, no cumple. Solo existen `POE`, `MAPA_PROCESOS` y `TABLA_ACTIVIDADES`, fijos en el código. De los tipos del instructivo solo está POE, y no se pueden crear otros.

**Criterios de aceptación**

- CA 1: Tipos disponibles
  - Dado que estoy cargando un documento
  - Cuando elijo el tipo
  - Entonces puedo elegir cualquiera de los tipos del instructivo.

- CA 2: Tipo nuevo
  - Dado que el organizador crea un tipo nuevo
  - Cuando guarda
  - Entonces el tipo queda disponible para cargar documentos.

- CA 3: Sigla corta
  - Dado un tipo con sigla de dos letras, como IT
  - Cuando se genera el código de un documento
  - Entonces la sigla se completa con un punto (IT.).

### MVP-36 Jerarquía de actividades y procesos

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **crear actividades y procesos en una jerarquía, y asociarles documentos** para **ubicar cada documento en el proceso al que pertenece**.

**Trazabilidad**: IT QBN · Módulo Documentos 3 y 8 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Las actividades se crean con Nuevo y se subordinan a una raíz. Al cargar un documento, la solapa de procesos no es obligatoria, pero es importante completarla.

**Estado actual**: ⚠️ Implementado, no cumple. Existe la jerarquía mapa → proceso → tabla → actividad → POE, pero está armada con documentos y solo admite POE en la actividad. Al cargar un documento no se puede indicar su proceso.

**Criterios de aceptación**

- CA 1: Nueva actividad
  - Dado que el organizador crea una actividad
  - Cuando guarda
  - Entonces aparece en la jerarquía de actividades y procesos.

- CA 2: Proceso opcional
  - Dado que estoy cargando un documento de cualquier tipo
  - Cuando elijo su proceso, o lo dejo vacío
  - Entonces el documento se guarda de las dos formas.

## Épica: Carga de documentos

### MVP-37 Crear un documento nuevo como iniciador

<!-- Status: Etapa 1 -->

**Descripción**: Como **iniciador**, quiero **crear un documento completando su estructura** para **que entre al circuito de revisión y aprobación**.

**Trazabilidad**: IT QBN · Módulo Documentos 8 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Campos: propietario, grupo, tipo, estado (borrador por defecto), código, título, fecha de iniciación (hoy por defecto), tope de revisión, tope de aprobación, revisión periódica (6 meses o 1 año), versión 0 y versión anterior 0. El propietario se elige entre los cargos de quien inició sesión.

**Estado actual**: ⚠️ Implementado, no cumple. La carga, el estado borrador, la versión 0 y las fechas existen. Pero el propietario puede ser cualquier usuario, sin relación con la sesión, y la revisión periódica admite cualquier cantidad de meses.

**Criterios de aceptación**

- CA 1: Valores por defecto
  - Dado que abro un documento nuevo
  - Cuando veo la estructura
  - Entonces el estado es borrador, la fecha de iniciación es la de hoy y la versión y la versión anterior son 0.

- CA 2: Propietario
  - Dado que tengo dos cargos
  - Cuando elijo el propietario
  - Entonces el sistema me ofrece solo mis cargos, y rechaza cualquier otro propietario.

- CA 3: Revisión periódica
  - Dado que completo la revisión periódica
  - Cuando elijo el plazo
  - Entonces solo puedo elegir 6 meses o 1 año.

- CA 4: Datos obligatorios
  - Dado que falta un dato obligatorio
  - Cuando intento guardar
  - Entonces el sistema no lo guarda y señala qué falta.

### MVP-38 Código de documento con serie por sector

<!-- Status: Etapa 1 -->

**Descripción**: Como **iniciador**, quiero **que el sistema genere el código con el formato del instructivo** para **que cada documento quede identificado sin errores**.

**Trazabilidad**: IT QBN · Módulo Documentos 4 y 8 | Story points: 2 | Matriz v1: Nueva

**Requisito**: Código ---.---.0000: siglas del sector, siglas del tipo y serie ordinal dentro del sector. Se genera automáticamente, y se puede colocar otro siempre que no exista.

**Estado actual**: ⚠️ Implementado, no cumple. El formato coincide, pero la serie se cuenta por sector y tipo, no por sector. Tampoco se puede indicar un código a mano.

**Criterios de aceptación**

- CA 1: Código automático
  - Dado un sector LAC con cinco documentos, de cualquier tipo
  - Cuando creo un POE en ese sector
  - Entonces su código es LAC.POE.0006.

- CA 2: Código manual
  - Dado que escribo un código que no existe
  - Cuando guardo
  - Entonces el documento queda con ese código.

- CA 3: Código repetido
  - Dado que escribo un código que ya existe
  - Cuando intento guardar
  - Entonces el sistema lo rechaza.

### MVP-39 Importar un documento existente como vigente

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **cargar directamente como vigente un documento que ya está aprobado** para **incorporar la documentación existente sin repetir el circuito**.

**Trazabilidad**: IT QBN · Módulo Documentos 4 | Story points: 8 | Matriz v1: Nueva

**Requisito**: Desde Organizador - Importar se completan estructura, proceso y permisos. El estado es vigente y las fechas son todas iguales, salvo la revisión periódica. El asterisco indica los datos obligatorios.

**Estado actual**: ❌ No implementado. Todo documento cargado por `POST /documents` empieza en borrador.

**Criterios de aceptación**

- CA 1: Importación exitosa
  - Dado que soy organizador y completé los datos obligatorios
  - Cuando importo el documento con su archivo
  - Entonces queda vigente y aparece en los documentos disponibles.

- CA 2: Sin permiso
  - Dado un usuario sin permiso de organizador
  - Cuando intenta importar un documento
  - Entonces el sistema lo rechaza.

### MVP-40 Corregir un documento en elaboración

<!-- Status: Etapa 1 -->

**Descripción**: Como **iniciador**, quiero **cambiar las propiedades y el archivo de un documento devuelto** para **hacer las correcciones que me pidieron y volver a enviarlo**.

**Trazabilidad**: IT QBN · Módulo Documentos 8 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Las propiedades solo las pueden cambiar el organizador y el iniciador. Si hay una modificación para hacer, el documento vuelve al propietario como borrador.

**Estado actual**: ❌ No implementado. Un documento devuelto vuelve a borrador con las observaciones, pero no hay endpoint para cambiar sus datos ni su archivo: `new-version` solo funciona desde un vigente.

**Criterios de aceptación**

- CA 1: Corrección del borrador
  - Dado un documento mío devuelto como borrador
  - Cuando cambio sus propiedades o subo otro archivo
  - Entonces se guardan los cambios y lo puedo enviar de nuevo a revisión.

- CA 2: Sin permiso
  - Dado un usuario que no es iniciador del documento ni organizador
  - Cuando intenta cambiar sus propiedades
  - Entonces el sistema lo rechaza.

### MVP-41 Reemplazar el archivo de un documento vigente

<!-- Status: Etapa 1 -->

**Descripción**: Como **iniciador u organizador**, quiero **subir otro archivo sobre un documento vigente** para **corregirlo sin generar una versión nueva**.

**Trazabilidad**: IT QBN · Módulo Documentos 4 | Story points: 3 | Matriz v1: Nueva

**Requisito**: El archivo de un documento vigente se pisa al subir otro. Es una función solo para iniciador u organizador.

**Estado actual**: ❌ No implementado. La única forma de cambiar el archivo de un vigente es crear una versión nueva.

**Comentarios**: Antes de implementarla hay que resolver la duda abierta sobre esta función.

**Criterios de aceptación**

- CA 1: Reemplazo
  - Dado un documento vigente y un usuario iniciador u organizador
  - Cuando elige Modificar propiedades y sube otro archivo
  - Entonces el documento conserva su versión y muestra el archivo nuevo.

- CA 2: Sin permiso
  - Dado un usuario sin esos permisos
  - Cuando intenta reemplazar el archivo
  - Entonces el sistema lo rechaza.

### MVP-42 Crear una nueva versión de un documento vigente

<!-- Status: Etapa 1 -->

**Descripción**: Como **iniciador**, quiero **crear una nueva versión desde un documento vigente** para **actualizarlo sin perder la anterior**.

**Trazabilidad**: IT QBN · Módulo Documentos 5 | Story points: 3 | Matriz v1: Nueva

**Requisito**: En la grilla de documentos activos, la pantalla del documento tiene la opción Nueva Versión.

**Estado actual**: ✅ Implementado, a validar. Existe `POST /documents/{id}/new-version`, disponible solo desde un vigente, y el vigente se mantiene hasta que se publica la versión nueva.

**Criterios de aceptación**

- CA 1: Versión nueva
  - Dado un documento vigente
  - Cuando elijo Nueva Versión y subo el archivo
  - Entonces se crea un borrador con el mismo código y la versión siguiente, y el vigente se mantiene.

## Épica: Circuito de revisión y aprobación

### MVP-43 Enviar a revisión con un aviso para el revisor

<!-- Status: Etapa 1 -->

**Descripción**: Como **iniciador**, quiero **pasar el borrador a revisión dejando un aviso** para **que el revisor sepa que tiene algo pendiente y qué mirar**.

**Trazabilidad**: IT QBN · Módulo Documentos 8 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Al cambiar de estado se puede colocar un aviso para el revisor. Al aceptar, el documento pasa a revisión y se genera un mail para el revisor.

**Estado actual**: ⚠️ Implementado, no cumple. El paso a revisión existe, pero no admite un aviso y no se envía ningún mail: el backend no tiene envío de correo.

**Criterios de aceptación**

- CA 1: Aviso
  - Dado un documento en borrador
  - Cuando lo paso a revisión con un aviso
  - Entonces el revisor ve ese aviso en el documento.

- CA 2: Mail
  - Dado un documento que pasa a revisión
  - Cuando se confirma el cambio de estado
  - Entonces cada revisor recibe un mail.

### MVP-44 Revisar con varios revisores y pasar a aprobación

<!-- Status: Etapa 1 -->

**Descripción**: Como **revisor**, quiero **registrar mi revisión o devolver el documento** para **que solo llegue a aprobación cuando lo aceptaron todos**.

**Trazabilidad**: IT QBN · Módulo Documentos 8 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Si hay dos revisores, el primero registra sin cambiar el estado. El último registra y cambia el estado a aprobación. Si hay una modificación para hacer, se devuelve al propietario, a quien le aparece como borrador.

**Estado actual**: ⚠️ Implementado, no cumple. Se registra la revisión de cada revisor y se puede devolver, pero el último revisor no cambia el estado: el documento sigue en revisión hasta que alguien aprueba. No hay estado de pendiente de aprobación en este flujo.

**Criterios de aceptación**

- CA 1: Primer revisor
  - Dado un documento con dos revisores
  - Cuando el primero registra su revisión
  - Entonces el documento sigue en revisión.

- CA 2: Último revisor
  - Dado que solo falta un revisor
  - Cuando registra su revisión
  - Entonces el documento pasa a pendiente de aprobación y le aparece al aprobador.

- CA 3: Devolución
  - Dado un documento en revisión que necesita cambios
  - Cuando el revisor lo devuelve
  - Entonces le aparece al propietario como borrador.

### MVP-45 Aprobar o devolver, y pasar a homologado

<!-- Status: Etapa 1 -->

**Descripción**: Como **aprobador**, quiero **aprobar el documento o devolverlo al iniciador** para **que solo avancen los que están en condiciones**.

**Trazabilidad**: IT QBN · Módulo Documentos 8 | Story points: 3 | Matriz v1: Nueva

**Requisito**: El aprobador puede devolver al iniciador. El iniciador cambia el estado a Homologado, que es el tiempo de lectura antes de estar vigente.

**Estado actual**: ⚠️ Implementado, no cumple. Al aprobar, el documento pasa directamente a homologado por acción del aprobador. El iniciador no interviene en ese paso, y el aprobador solo puede devolver mientras el documento sigue en revisión.

**Criterios de aceptación**

- CA 1: Aprobación
  - Dado un documento pendiente de aprobación
  - Cuando el aprobador lo aprueba
  - Entonces el iniciador lo ve disponible para pasar a homologado.

- CA 2: Devolución
  - Dado un documento pendiente de aprobación
  - Cuando el aprobador lo devuelve
  - Entonces le aparece al iniciador como borrador.

- CA 3: Homologación
  - Dado un documento aprobado
  - Cuando el iniciador lo pasa a homologado
  - Entonces empieza el período de lectura.

### MVP-46 Período de lectura antes de estar vigente

<!-- Status: Etapa 1 -->

**Descripción**: Como **lector**, quiero **tener un tiempo para leer el documento antes de que esté vigente** para **conocerlo antes de tener que aplicarlo**.

**Trazabilidad**: IT QBN · Módulo Documentos 8 | Story points: 2 | Matriz v1: Nueva

**Requisito**: Homologado es el tiempo de lectura antes de estar vigente.

**Estado actual**: ✅ Implementado, a validar. Existe el estado `HOMOLOGADO` con una duración configurable, y un proceso programado lo pasa a vigente al terminar.

**Criterios de aceptación**

- CA 1: Paso a vigente
  - Dado un documento homologado
  - Cuando termina su período de lectura
  - Entonces pasa a vigente y la versión anterior deja de estarlo.

### MVP-47 Registrar la demora de revisión y aprobación

<!-- Status: Etapa 1 -->

**Descripción**: Como **responsable de calidad**, quiero **que el sistema registre cuándo se pasó una fecha tope** para **detectar demoras en el circuito**.

**Trazabilidad**: IT QBN · Módulo Documentos 8 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Tope de revisión es la fecha máxima para la revisión. Pasada esa fecha, el sistema comienza a registrar la demora. También existe un tope de aprobación.

**Estado actual**: ⚠️ Implementado, no cumple. Las fechas tope se guardan y se muestran, pero el sistema no calcula ni registra ninguna demora.

**Criterios de aceptación**

- CA 1: Demora de revisión
  - Dado un documento en revisión con la fecha tope vencida
  - Cuando lo consulto
  - Entonces veo cuántos días de demora lleva.

- CA 2: Demora de aprobación
  - Dado un documento pendiente de aprobación con la fecha tope vencida
  - Cuando lo consulto
  - Entonces veo cuántos días de demora lleva.

- CA 3: Sin fecha tope
  - Dado un documento sin fecha tope
  - Cuando lo consulto
  - Entonces no muestra demora.

## Épica: Consulta de documentos

### MVP-48 Mis pendientes por estado

<!-- Status: Etapa 1 -->

**Descripción**: Como **usuario del sistema**, quiero **ver mis documentos pendientes separados por estado** para **saber qué tengo que hacer en cada uno**.

**Trazabilidad**: IT QBN · Módulo Documentos | Story points: 5 | Matriz v1: Nueva

**Requisito**: Documentos - Mis Pendientes incluye En borrador, En elaboración (borradores y otros estados) y En revisión, además de los pendientes de aprobación.

**Estado actual**: ⚠️ Implementado, no cumple. La sección Pendientes tiene Lecturas, Revisiones y Aprobaciones. Faltan En borrador y En elaboración.

**Criterios de aceptación**

- CA 1: Borradores
  - Dado que tengo documentos en borrador
  - Cuando entro a Mis Pendientes - En borrador
  - Entonces los veo, y con doble clic abro su estructura.

- CA 2: En elaboración
  - Dado que inicié documentos que siguen en el circuito
  - Cuando entro a Mis Pendientes - En elaboración
  - Entonces los veo con su estado actual.

- CA 3: Revisor y aprobador
  - Dado que soy revisor o aprobador de un documento
  - Cuando entro a Mis Pendientes
  - Entonces el documento aparece en el listado que corresponde.

### MVP-49 Documentos disponibles y vista de organizador

<!-- Status: Etapa 1 -->

**Descripción**: Como **usuario del sistema**, quiero **ver los documentos disponibles, y como organizador todos los demás** para **que cada persona vea lo que le corresponde**.

**Trazabilidad**: IT QBN · Módulo Documentos y Documentos 6 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Un documento dado de baja no se ve en Documentos - Disponible - Activos. Desde Documentos - Organizador - Documentos se ven los vigentes, históricos y en elaboración.

**Estado actual**: ⚠️ Implementado, no cumple. Hay una sola lista con filtros de estado, tipo y sector, y `GET /documents` no limita los resultados según el permiso.

**Criterios de aceptación**

- CA 1: Disponibles
  - Dado un usuario lector
  - Cuando entra a Disponibles
  - Entonces ve solo los documentos activos.

- CA 2: Vista de organizador
  - Dado un usuario organizador
  - Cuando entra a Organizador - Documentos
  - Entonces ve los vigentes, históricos y en elaboración.

- CA 3: Sin permiso
  - Dado un usuario que no es organizador
  - Cuando intenta consultar los documentos dados de baja
  - Entonces el sistema lo rechaza.

### MVP-50 Dar de baja un documento indicando la causa

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **dar de baja un documento indicando la causa** para **sacarlo de circulación sin perderlo**.

**Trazabilidad**: IT QBN · Módulo Documentos 6 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Al elegir Dar de baja se abre un cuadro de causa. A diferencia de eliminar, el documento dado de baja queda en el sistema.

**Estado actual**: ⚠️ Implementado, no cumple. Se puede pasar un documento a estados finales con el cambio de estado general, pero no se pide ninguna causa, y lo habilita el permiso de aprobación institucional en vez del de organizador.

**Criterios de aceptación**

- CA 1: Baja con causa
  - Dado un documento vigente y un organizador
  - Cuando lo da de baja e indica la causa
  - Entonces deja de verse en Disponibles y queda en la vista de organizador con su causa.

- CA 2: Causa obligatoria
  - Dado que no se indicó la causa
  - Cuando el organizador intenta dar de baja
  - Entonces el sistema no lo permite.

### MVP-51 Eliminar un documento con confirmación de identidad

<!-- Status: Etapa 1 -->

**Descripción**: Como **organizador**, quiero **eliminar un documento confirmando mi identidad** para **quitar del sistema lo que no debe permanecer, sin hacerlo por error**.

**Trazabilidad**: IT QBN · Módulo Documentos 7 | Story points: 3 | Matriz v1: Nueva

**Requisito**: Eliminar es función del organizador. El sistema pide confirmación, nombre y contraseña del usuario.

**Estado actual**: ❌ No implementado. No hay forma de eliminar documentos.

**Comentarios**: Antes de implementarla hay que resolver la duda abierta sobre esta función.

**Criterios de aceptación**

- CA 1: Eliminación confirmada
  - Dado un documento marcado por un organizador
  - Cuando confirma con su usuario y contraseña
  - Entonces el documento se elimina.

- CA 2: Contraseña incorrecta
  - Dado que el organizador ingresó una contraseña incorrecta
  - Cuando confirma
  - Entonces el documento no se elimina.

- CA 3: Sin permiso
  - Dado un usuario que no es organizador
  - Cuando intenta eliminar un documento
  - Entonces el sistema lo rechaza.

### MVP-52 Imprimir copias controladas y no controladas

<!-- Status: Etapa 1 -->

**Descripción**: Como **impresor autorizado**, quiero **imprimir copias según mi permiso** para **que solo circulen las copias autorizadas**.

**Trazabilidad**: IT QBN · Acceso y Módulo Organización 3 | Story points: 5 | Matriz v1: Nueva

**Requisito**: Entre los permisos están el de impresor de copia controlada y el de impresor de copia no controlada. Intervinientes del documento: iniciador, revisor, aprobador, lector, impresor y colaborador.

**Estado actual**: ❌ No implementado. El permiso `IMPRIMIR_CONTROLADA` existe, pero no hay ninguna función de impresión, y el permiso de copia no controlada no existe. Tampoco se puede indicar un impresor en el documento.

**Criterios de aceptación**

- CA 1: Copia controlada
  - Dado un usuario con permiso de copia controlada
  - Cuando imprime un documento vigente
  - Entonces obtiene una copia identificada como controlada.

- CA 2: Copia no controlada
  - Dado un usuario con permiso de copia no controlada
  - Cuando imprime un documento vigente
  - Entonces obtiene una copia identificada como no controlada.

- CA 3: Sin permiso
  - Dado un usuario sin permiso de impresión
  - Cuando consulta un documento
  - Entonces no tiene disponible la opción de imprimir.

### MVP-53 Reportes y estadísticas de documentos

<!-- Status: Etapa 2 -->

**Descripción**: Como **responsable de calidad**, quiero **consultar reportes y estadísticas de documentos** para **conocer el estado de la documentación**.

**Trazabilidad**: IT QBN · Módulo Documentos | Story points: 5 | Matriz v1: Nueva

**Requisito**: El menú Documentos incluye Reportes y Estadísticas. El instructivo no detalla su contenido.

**Estado actual**: ❌ No implementado.

**Criterios de aceptación**

- CA 1: Consulta
  - Dado un usuario autorizado
  - Cuando entra a Reportes o a Estadísticas
  - Entonces ve la información definida con el laboratorio.

## Prioridades

<!--
Prioridades (el script las usa para asignar labels de prioridad)

## No negociables

- MVP-25 Entrar eligiendo el cargo
- MVP-28 Dar de baja a una persona
- MVP-32 Administrar cargos y asignarlos a personas
- MVP-33 Permisos de cada cargo según QBN
- MVP-35 Tipos de documento configurables
- MVP-37 Crear un documento nuevo como iniciador
- MVP-38 Código de documento con serie por sector
- MVP-39 Importar un documento existente como vigente
- MVP-40 Corregir un documento en elaboración
- MVP-42 Crear una nueva versión de un documento vigente
- MVP-43 Enviar a revisión con un aviso para el revisor
- MVP-44 Revisar con varios revisores y pasar a aprobación
- MVP-45 Aprobar o devolver, y pasar a homologado
- MVP-46 Período de lectura antes de estar vigente
- MVP-48 Mis pendientes por estado
- MVP-50 Dar de baja un documento indicando la causa

## Recomendables

- MVP-26 Datos completos de la cuenta de usuario
- MVP-27 Modificar las propiedades de un usuario
- MVP-29 Ver los pendientes de cualquier usuario
- MVP-30 Administrar las áreas funcionales
- MVP-31 Ver los documentos que debe leer un área
- MVP-34 Grupos de documentos con sigla de tres letras
- MVP-36 Jerarquía de actividades y procesos
- MVP-41 Reemplazar el archivo de un documento vigente
- MVP-47 Registrar la demora de revisión y aprobación
- MVP-49 Documentos disponibles y vista de organizador
- MVP-51 Eliminar un documento con confirmación de identidad
- MVP-52 Imprimir copias controladas y no controladas

## Fuera de los 15 requisitos mínimos — valor agregado

- MVP-53 Reportes y estadísticas de documentos


Dudas abiertas (se publican como comentario en las issues mencionadas):
- En MVP-41: el instructivo permite pisar el archivo de un documento vigente sin crear una versión. El proyecto había definido que "no existe editar, sino que se sube una nueva versión", y puede afectar el control de cambios de ISO 7101. ¿Se implementa así o se descarta?
- En MVP-51: el instructivo permite eliminar documentos. ¿Se puede eliminar cualquier documento, o solo los que nunca estuvieron vigentes, para conservar el historial que pide ISO 7101?
- En MVP-39: importar como vigente saltea la revisión y la aprobación institucional por Disposición 186. ¿Se limita a la migración inicial, y se pide el número de Disposición?
- En MVP-45: el instructivo no menciona la aprobación institucional por Disposición 186, que hoy es una aprobación aparte. ¿Cómo se combina con el paso a homologado?
- En MVP-26: el instructivo dice que el alta la hace el administrador u organizador, y el equipo implementó autorregistro con asignación posterior del rol. ¿Se mantiene el autorregistro?
- En MVP-25: el instructivo pide un nombre de usuario y el equipo definió entrar con el mail. ¿El laboratorio está de acuerdo?
-->
