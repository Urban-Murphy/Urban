# UrbanSIP: estructura de carpetas

Estándar para modelos de catálogo y obras. Copiar y adaptar por cada modelo y cada venta.

## Estructura general

```
URBANSIP/
├── catalogo/
│   └── <MODELO>/
│       ├── presupuesto/
│       ├── plan/
│       ├── compras/
│       ├── pliegos/
│       └── fichas/
├── obras/
│   └── <MODELO>-<CLIENTE>/
│       ├── datos/
│       ├── planos/
│       ├── gestión/
│       ├── compras/
│       ├── certificados/
│       ├── contratos/
│       └── entregas/
└── herramientas/
```

---

## Modelos de catálogo (`catalogo/<MODELO>/`)

**Qué es:** presupuesto congelado con versión y fecha de precios. Se arma **una sola vez** y luego solo se actualiza la versión si cambian los precios.

### `presupuesto/`
- `<MODELO>_Esencial_Presupuesto_v1.xlsx`: ítem por ítem, con errores y dudas marcados.
- `<MODELO>_Esencial_vs_Confort_v1.xlsx`: comparación de costos y diferencia de precio.
- `<MODELO>_Precio_Venta.xlsx`: precio de venta según comisiones y vendedor.
- `<MODELO>_Correcciones_Ficha.md`: cambios a hacer en la ficha comercial.

### `plan/`
- `<MODELO>_Plan_Obra.xlsx`: tareas, duraciones, plazo en días corridos (de la plantilla de gestión).
- `<MODELO>_Mano_de_Obra.xlsx`: detalle de jornales por etapa y tarea.

### `compras/`
- `<MODELO>_Compras_Hacia_Atras.xlsx`: cuándo pedir cada cosa (de la plantilla de gestión).
- `Pedido_Cotizacion_<ITEM>_<MODELO>.docx`: un documento por cada compra crítica o ítem sin cotización.

### `pliegos/`
- `Pliego_<RUBRO>_<MODELO>.docx`: especificaciones técnicas para contratistas, sin datos internos.

### `fichas/`
- `Ficha_Tecnico_Comercial_<MODELO>_v3.pdf`: la versión publicable, lista para clientes.

---

## Obras (`obras/<MODELO>-<CLIENTE>/`)

**Qué es:** copia del modelo de catálogo + planilla de cambios + documentos de la obra específica.

### `datos/`
- `Plantilla_Venta_Cliente_UrbanSIP.xlsx`: datos del cliente, forma de pago, cambios aprobados, opcionales y precios.
- `Contrato_UrbanSIP_<CLIENTE>.docx`: contrato firmado.
- `Orden_de_Compra_<NUMERO>.docx`: órdenes de cambio y adicionales del cliente, numeradas y con precio.

### `planos/`
- `Plano_Implantacion_<CLIENTE>.pdf`: posición en el lote (DWG exportado a PDF).
- `Plano_Fundacion_<CLIENTE>.pdf`: fundación según el estudio de suelos.
- Copias o referencias a los planos estándar del modelo (`Plano_Arquitectura_<MODELO>.pdf`, etc.).

### `gestión/`
- `Plantilla_Gestion_Obra_UrbanSIP.xlsx`: plan, compras hacia atrás, certificación, costos y adicionales (copia de la del catálogo, personalizada con el cliente).

### `compras/`
- `Cotizacion_<PROVEEDOR>_<FECHA>.pdf`: cada respuesta de cotización.
- `Orden_de_Compra_<NUMERO>_<PROVEEDOR>.pdf`: PO emitida, fechada y firmada.
- `Recepción_<NUMERO>.xlsx`: qué llegó, fecha, cantidad, estado.

### `certificados/`
- `Certificado_Quincena_01.xlsx`: certificado N° 1 (formato: hoja de cálculo con cálculo automático).
- `Certificado_Quincena_02.xlsx`: ídem.
- `Certificado_0_Limpio.pdf`: el modelo limpio, para usar como template.
- `Justificación_Aperturado_Jornales.xlsx`: detalle de jornales por tarea (para auditoría).

### `contratos/`
- `Contrato_Encofrado_<CONTRATISTA>_v1.pdf`: uno por cada contratista especializado.
- `Brief_<CONTRATISTA>.pdf`: alcance, materiales, rendimientos, jornales, pagos.
- `Planilla_Seguimiento_<CONTRATISTA>.xlsx`: avance real vs. plan.

### `entregas/`
- `Acta_de_Recepcion.pdf`: documento de entrega y conformidad.
- `Manual_de_Uso_y_Mantenimiento_<MODELO>.pdf`: instrucciones para el cliente.
- `Garantia_<CLIENTE>.pdf`: documento de garantía y plazo.
- `Desvios_Reales_vs_Objetivo.xlsx`: comparación final de costos (para el ciclo de mejora).

---

## Herramientas compartidas (`herramientas/`)

**Qué es:** scripts, templates y utilidades que reutilizan todas las obras.

- `plantillas/`
  - `Plantilla_Venta_Cliente_UrbanSIP.xlsx`: copiar a cada obra.
  - `Plantilla_Gestion_Obra_UrbanSIP.xlsx`: copiar a cada obra.
  - `Pliego_Template.docx`: template vacío para armar pliegos nuevos.
  - `Pedido_Cotizacion_Template.docx`: template de pedido de cotización.
  - `Acta_Recepcion_Template.docx`: template de acta de entrega.

- `scripts/`
  - `generar_modelo.py`: crea la estructura de carpetas para un modelo nuevo.
  - `generar_obra.py`: crea la estructura de carpetas para una obra nueva.
  - `calcular_costo_objetivo.py`: recalcula el costo objetivo con dólar nuevo.

- `criterios/`
  - `criterios_obra.md`: criterios validados (IVA, cómputo, documentos internos, etc.).
  - `criterios_computo.md`: no descontar vanos, baños sin látex, etc.

---

## Nomenclatura estándar

| Qué | Formato | Ejemplo |
|---|---|---|
| Modelo | `<NOMBRE>` | `AURA` |
| Obra | `<MODELO>-<CLIENTE>` | `AURA-LOPEZ`, `AURA-GARCIA` |
| Versión presupuesto | `v1`, `v2`, ... | `Aura_Presupuesto_v1.xlsx` |
| Versión de precios | al día | `Aura Esencial v1 · precios al 30/09/26` |
| Cotización | `Cotizacion_<PROVEEDOR>_<FECHA>` | `Cotizacion_SIPCOR_2026-10-04.pdf` |
| Orden de compra | `OC_<NUMERO>_<PROVEEDOR>_<FECHA>` | `OC_001_SIPCOR_2026-10-06.pdf` |
| Certificado | `Certificado_Quincena_<N>` | `Certificado_Quincena_01.xlsx` |
| Contrato | `Contrato_<RUBRO>_<CONTRATISTA>_v<N>` | `Contrato_Kit_Sipcor_v1.pdf` |

---

## Checklist: armar un modelo nuevo

- [ ] Crear carpeta `catalogo/<MODELO>/` con subcarpetas.
- [ ] Copiar `Plantilla_Gestion_Obra_UrbanSIP.xlsx` a `gestión/`.
- [ ] Armar presupuesto (Excel con errores y dudas marcados).
- [ ] Comparación Esencial vs Confort.
- [ ] Cálculo de precio de venta.
- [ ] Correcciones a la ficha comercial.
- [ ] Plan de obra (tareas, duraciones, plazo).
- [ ] Mano de obra (detalle de jornales).
- [ ] Compras hacia atrás (cuándo pedir cada cosa).
- [ ] Pedidos de cotización (aberturas, siding, cocina, climatización, etc.).
- [ ] Pliegos técnicos (sin datos internos).
- [ ] Ficha técnico-comercial.

## Checklist: armar una obra nueva

- [ ] Crear carpeta `obras/<MODELO>-<CLIENTE>/` con subcarpetas.
- [ ] Copiar `Plantilla_Venta_Cliente_UrbanSIP.xlsx` a `datos/`.
- [ ] Copiar `Plantilla_Gestion_Obra_UrbanSIP.xlsx` a `gestión/` y personalizar con cliente y datos.
- [ ] Completar datos del cliente, lote, forma de pago.
- [ ] Copiar planos del modelo y agregar implantación en el lote.
- [ ] Hacer el estudio de suelos y la fundación específica.
- [ ] Hacer presupuesto de cambios si los hay.
- [ ] Empezar a pedir cotizaciones (usar template de `herramientas/`).
- [ ] Crear carpeta de certificados y plantilla de acta de recepción.
