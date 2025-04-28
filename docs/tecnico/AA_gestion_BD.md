# Documentacion Tecnica Inicial - T7AIChatModular

## Arquitectura del Interfaz

La arquitectura del proyecto **T7AIChatModular** se basa en una separacion modular de responsabilidades, permitiendo una evolucion sencilla y ordenada.

# Entidad: Usuario

## Descripcion General

La entidad `Usuario` representa a cada usuario operativo que interactua con el sistema. Ademas de su identificacion y rol, se lleva control sobre su consumo de recursos de IA, tokens utilizados y gastos asociados.

## Campos Principales

| Campo            | Tipo de dato | Descripcion                                         |
|------------------|--------------|-----------------------------------------------------|
| id               | INT          | Identificador unico del usuario                    |
| nombre           | TEXT         | Nombre del usuario                                 |
| email            | TEXT         | Correo electronico del usuario                     |
| password         | TEXT         | Contraseña (encriptada)                            |
| rol              | TEXT         | Rol asignado (ej: agente, admin)                   |
| fecha_alta       | DATE         | Fecha de registro                                 |
| ip_alta          | TEXT         | Direccion IP desde donde se realizo el alta         |
| modelo_ia        | TEXT         | Modelo IA asignado por defecto al usuario           |
| tokens_disponibles| INT         | Tokens disponibles actualmente                     |
| tokens_consumidos| INT          | Tokens consumidos totales                          |
| tokens_acumulados| INT          | Tokens acumulados historicos                       |
| gasto_total      | FLOAT        | Gasto acumulado derivado del consumo de tokens IA  |
| ultima_fecha_acceso | DATETIME   | Fecha y hora del ultimo acceso del usuario         |

## Relaciones

- Un `Usuario` puede estar asociado a un `Agente`.
- Cada `Usuario` tiene su propio control de tokens y gastos.

## Flujo Funcional

- El `Usuario` se autentica en el sistema.
- A medida que utiliza funcionalidades IA, se descuentan tokens y se actualiza el gasto.
- Se pueden configurar limites de tokens y/o gasto para cada usuario.

# Entidad: Registro de Consumo IA

## Descripcion General

La entidad `RegistroConsumoIA` almacena cada peticion realizada por los usuarios al sistema de IA, incluyendo su impacto en tokens y gasto economico, ademas de la trazabilidad del modelo y proveedor utilizados.

## Campos Principales

| Campo               | Tipo de dato | Descripcion                                     |
|---------------------|--------------|-------------------------------------------------|
| id_registro         | INT          | ID unico del registro                           |
| id_usuario          | INT          | ID del usuario que realizo la peticion          |
| fecha_hora          | DATETIME     | Momento en que se realizo la peticion           |
| tokens_consumidos   | INT          | Tokens consumidos en esta peticion              |
| gasto_asociado      | FLOAT        | Gasto economico correspondiente                |
| modelo_utilizado    | TEXT         | Modelo IA que proceso la consulta               |
| provider_utilizado  | TEXT         | Proveedor que sirvio el modelo IA               |
| resumen_prompt      | TEXT         | (Opcional) Breve descripcion del contenido enviado |
| ip_origen           | TEXT         | IP desde donde se lanzo la consulta             |

## Relaciones

- Cada `RegistroConsumoIA` esta asociado a un `Usuario` mediante `id_usuario`.
- Permite trazabilidad completa de consumo de recursos IA.

## Flujo Funcional

- Cada vez que un usuario realiza una peticion IA, se crea un nuevo registro.
- El sistema suma los tokens y gasto al perfil general del usuario.
- Permite informes de consumo por usuario, modelo, proveedor y fecha.

# Notas Finales

- Esta arquitectura permite tener un control integral del perfil del usuario y su comportamiento de consumo.
- Facilita futuras ampliaciones para soportar diferentes proveedores de IA y politicas de coste por modelo.
- La trazabilidad IP y resumen de prompts facilita tareas de auditoria y analisis de seguridad.

---

**Contenido:**
- [Entidad: Usuario](#entidad-usuario)
- [Entidad: Registro de Consumo IA](#entidad-registro-de-consumo-ia)
- [Notas Finales](#notas-finales)
