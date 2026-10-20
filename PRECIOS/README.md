# PRECIOS

Lista de precios y análisis de costos compartidos por todas las obras y modelos (SIP y construcción tradicional).

## Estructura

- `Lista_Precios_<AAAA-MM-DD>.xlsx`: la lista vigente (una sola), con fecha. Hoy: `Lista_Precios_2026-09-30.xlsx` (v1, armada desde Aura Costo 30-9-26; falta proveedor y revisar "Aplica a"). Partir de `Lista_Precios_PLANTILLA.xlsx` para listas nuevas.
- `historico/`: listas anteriores.
- `analisis_costos/sip/` y `analisis_costos/tradicional/`: análisis de costo (ej. 1 m² de contrapiso). Cada uno toma sus precios de la lista vigente.

## Reglas

- Materiales con IVA 21%, mano de obra sin IVA.
- Al actualizar precios, mover la lista anterior a `historico/` antes de reemplazarla.
- Los presupuestos de modelos y obras leen de la lista vigente.
