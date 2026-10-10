# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

No es una aplicación: es el espacio de trabajo de **UrbanSIP** (casas SIP prediseñadas llave en mano; el prototipo es el modelo **Aura**, ~78 m², y se está armando **Origen**). Contiene planillas Excel, documentos Word/PDF, planos DWG, metodología en Markdown y un único script Python que genera presupuestos. El usuario (Adrián) **no es técnico**: responder en castellano, sin jerga y con pasos literales. Las decisiones de negocio (precios, márgenes, criterios) son suyas.

## Comandos

Dependencias (una sola vez): `pip install pandas openpyxl`

Generar un presupuesto (único script ejecutable):

```bash
python3 generar_presupuesto.py --origen <ORIGEN_COMPUTO.xlsx> --aura <Aura_Costo.xlsx> --output <presupuesto.xlsx>
```

No hay tests, linter ni build. Crear estructura para un modelo u obra nueva (ejecutar **desde `URBANSIP/`**, porque usan rutas relativas `catalogo/` y `obras/`):

```bash
./herramientas/crear_modelo.sh <MODELO>
./herramientas/crear_obra.sh <MODELO> <CLIENTE>
```

## Arquitectura

**Flujo de datos del presupuesto.** `generar_presupuesto.py` cruza dos Excel: el cómputo de Origen (hoja `PerimySup`: locales con perímetro, superficie y altura, filas 3-7) y la lista de precios de Aura (hoja `Materiales`, desde la fila 5). Para cada ítem de Aura, `calcular_cantidad_origen()` decide la cantidad de Origen por coincidencia de palabras en la descripción (placa/pintura → superficie, zócalo → perímetro, siding, piso, etc.). Genera un xlsx de 3 hojas (`PerimySup`, `Materiales`, `Totales`) con fórmulas de Excel; el dólar está fijo en **1550** dentro del script.

**Cuidado con ese script.** Muchas cantidades están **hardcodeadas** (55.75, 137.5, 88.7, 136.93, 62.7, 78, 47 bocas…) y corresponden a Origen Esencial, no se derivan de los datos leídos. Si cambian los planos o el modelo, hay que editar `calcular_cantidad_origen()`. Los ítems que no matchean ninguna palabra clave quedan en cantidad 0 y se omiten del presupuesto sin aviso.

**Automatización.** `.github/workflows/presupuesto.yml` regenera `ORIGEN_Esencial_Presupuesto_v1.xlsx` en cada push y lo commitea. Está desfasado: espera `ORIGEN_COMPUTO_PROVISORIO.xlsx` y `Aura_Costo_30-9-26.xlsx` en la raíz, pero esos archivos no existen (el real se llama `Aura Costo 30-9-26.xlsx`, con espacios). `AUTOMATIZACION_PRESUPUESTOS.md` y `FLUJO_PRESUPUESTOS.md` describen el flujo pensado.

**Método de negocio (carpeta `URBANSIP/`).** Dos niveles:
- **Modelo de catálogo** (`catalogo/<MODELO>/`): presupuesto congelado con versión y fecha de precios (ej. "Aura Esencial v1, precios al 30/09/26"), en versiones **Esencial** y **Confort**. Se arma una vez; al cambiar precios se crea v2/v3.
- **Obra** (`obras/<MODELO>-<CLIENTE>/`): hereda una versión del modelo más una planilla de cambios (por terreno, opcionales, diseño). Precio final = modelo + cambios aprobados por escrito antes de ejecutar.

Documentos de referencia, por orden de utilidad: `URBANSIP/ESTRUCTURA_CARPETAS.md` (estructura y nomenclatura), `URBANSIP/INSTRUCTIVO_COMPUTO.md` (cómo medir y calcular cantidades), `URBANSIP/Metodologia_Gestion_UrbanSIP.md`, `URBANSIP/HANDOFF_URBANSIP.md` (contexto y criterios validados), `URBANSIP/COMO_CREAR_MODELO_U_OBRA.md`.

Hoy `URBANSIP/AURA/` es el modelo existente (con `pedidos/`) y `URBANSIP/catalogo/ORIGEN/` solo tiene un README; la estructura real todavía no coincide con la descrita en `ESTRUCTURA_CARPETAS.md`.

## Criterios de negocio validados (no cambiar sin que Adrián lo pida)

- **IVA:** materiales con 21%, mano de obra sin IVA. No comentar el IVA de caja.
- **Cómputo:** no se descuentan vanos; los baños no llevan látex; no multiplicar pisos tipo por más que la cantidad real; controlar cantidad de baños/unidades contra la memoria.
- **Antes de comparar totales**, revisar el alcance ítem por ítem; lo que falta o no tiene precio se valúa al precio del objetivo.
- **Compras hacia atrás:** inicio de tarea − fabricación − adjudicación − compulsa − 30 días de documentación. En SIP la compra crítica es el kit de paneles con su flete desde Córdoba.
- **Documentos para contratistas o clientes: sin datos internos** (ni costo objetivo, ni presupuestos previos, ni márgenes).
- **Nomenclatura:** `<MODELO>_<Versión>_Presupuesto_v<N>.xlsx`, `Cotizacion_<PROVEEDOR>_<FECHA>`, `OC_<NUMERO>_<PROVEEDOR>_<FECHA>`, `Certificado_Quincena_<N>`.
- Las casas tradicionales están en stand by: no desarrollarlas salvo pedido.

## Trampas conocidas

- Los `.sh` usan `mkdir -p "dir/{a,b,c}"` con llaves **entre comillas**: bash no las expande y crea una sola carpeta literal `{a,b,c}`. Sacar las llaves de las comillas antes de usarlos.
- Los `.xlsx`, `.pdf` y `.dwg` son binarios grandes (algunos de >10 MB): no leerlos como texto; usar openpyxl/pandas para Excel.
- Los archivos de origen del usuario no se modifican: se lee de ellos y lo generado va en archivos nuevos y versionados.
