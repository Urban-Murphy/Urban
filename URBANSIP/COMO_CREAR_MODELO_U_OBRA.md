# Cómo crear un modelo nuevo o una obra nueva en UrbanSIP

Dos formas: manual o con scripts automáticos.

---

## Opción 1: Crear un modelo nuevo (manual)

### Carpeta: `catalogo/<MODELO>/`

```bash
mkdir -p catalogo/ORIGEN/{presupuesto,plan,compras,pliegos,fichas}
```

**Subcarpetas:**
- `presupuesto/`: Excel de costos, comparación Esencial/Confort, precio de venta.
- `plan/`: tareas, duraciones, plazo en días corridos.
- `compras/`: cuándo pedir cada cosa, pedidos de cotización.
- `pliegos/`: especificaciones técnicas para contratistas.
- `fichas/`: ficha técnico-comercial para clientes.

### Qué poner en cada carpeta

1. **presupuesto/**
   - `ORIGEN_Esencial_Presupuesto_v1.xlsx` (copiar de Aura y adaptar).
   - `ORIGEN_Esencial_vs_Confort_v1.xlsx`.
   - `ORIGEN_Precio_Venta.xlsx`.
   - `ORIGEN_Correcciones_Ficha.md`.

2. **plan/**
   - `ORIGEN_Plan_Obra.xlsx` (copiar de Plantilla_Gestion_Obra_UrbanSIP.xlsx, hoja Plan).
   - `ORIGEN_Mano_de_Obra.xlsx`.

3. **compras/**
   - `ORIGEN_Compras_Hacia_Atras.xlsx`.
   - `Pedido_Cotizacion_Aberturas_ORIGEN.docx` (copiar de herramientas/pedidos/).
   - `Pedido_Cotizacion_Siding_ORIGEN.docx`.
   - Otros pedidos según necesario.

4. **pliegos/**
   - `Pliego_Estructura_SIP_ORIGEN.docx`.
   - `Pliego_Instalaciones_ORIGEN.docx`.
   - Uno por cada rubro importante.

5. **fichas/**
   - `Ficha_Tecnico_Comercial_ORIGEN_v1.pdf` (versión para clientes).

---

## Opción 2: Crear un modelo nuevo (script automático)

```bash
./herramientas/crear_modelo.sh ORIGEN
```

Crea la estructura de carpetas + README con checklist.

---

## Opción 3: Crear una obra nueva (manual)

### Carpeta: `obras/<MODELO>-<CLIENTE>/`

```bash
mkdir -p obras/ORIGEN-LOPEZ/{datos,planos,gestión,compras,certificados,contratos,entregas}
```

**Subcarpetas:**
- `datos/`: contrato, forma de pago, cambios aprobados.
- `planos/`: implantación en el lote, fundación específica.
- `gestión/`: plan, compras, certificación (copia de plantilla personalizada).
- `compras/`: cotizaciones, órdenes de compra.
- `certificados/`: certificados quincenales.
- `contratos/`: contratos con contratistas.
- `entregas/`: acta de entrega, garantía.

### Qué poner en cada carpeta

1. **datos/**
   - `Plantilla_Venta_Cliente_UrbanSIP.xlsx` (copiar desde raíz y completar).
   - `Contrato_UrbanSIP_LOPEZ.docx`.
   - `Orden_de_Cambio_01.docx`, `Orden_de_Cambio_02.docx`, etc.

2. **planos/**
   - `Plano_Implantacion_LOPEZ.pdf` (posición en el lote).
   - `Plano_Fundacion_LOPEZ.pdf` (según estudio de suelos).
   - Copias de planos estándar del modelo.

3. **gestión/**
   - `Plantilla_Gestion_Obra_UrbanSIP.xlsx` (copiar desde raíz y personalizar con datos del cliente).
   - Plan de obra, compras hacia atrás, certificación (todo aquí).

4. **compras/**
   - `Cotizacion_SIPCOR_2026-10-06.pdf`.
   - `Cotizacion_Aberturas_Aluminio_2026-10-06.pdf`.
   - `OC_001_SIPCOR_2026-10-06.pdf` (orden de compra emitida).
   - `OC_002_Aberturas_2026-10-06.pdf`.
   - Etc., uno por cada compra.

5. **certificados/**
   - `Certificado_Quincena_01.xlsx`.
   - `Certificado_Quincena_02.xlsx`.
   - `Certificado_0_Limpio.pdf` (modelo limpio).
   - `Justificacion_Aperturado_Jornales.xlsx`.

6. **contratos/**
   - `Contrato_Kit_Sipcor_v1.pdf`.
   - `Brief_Sipcor.pdf`.
   - Uno por cada contratista especializado.

7. **entregas/**
   - `Acta_de_Recepcion.pdf`.
   - `Manual_de_Uso_ORIGEN.pdf`.
   - `Garantia_LOPEZ.pdf`.
   - `Desvios_Reales_vs_Objetivo.xlsx` (al cierre).

---

## Opción 4: Crear una obra nueva (script automático)

```bash
./herramientas/crear_obra.sh ORIGEN LOPEZ
```

Crea la estructura de carpetas + README con checklist.

---

## Flujo típico

### Crear modelo ORIGEN

1. `./herramientas/crear_modelo.sh ORIGEN` → crea carpetas y README.
2. Medir planos en AutoCAD.
3. Armar presupuesto (copiar de AURA y adaptar).
4. Calcular Esencial vs Confort.
5. Hacer plan de obra.
6. Pedir cotizaciones.
7. Publicar ficha técnico-comercial.

### Crear obra ORIGEN-LOPEZ

1. `./herramientas/crear_obra.sh ORIGEN LOPEZ` → crea carpetas y README.
2. Copiar `Plantilla_Venta_Cliente_UrbanSIP.xlsx` a `datos/` y completar.
3. Hacer estudio de suelos.
4. Hacer plano de implantación.
5. Personalizar `Plantilla_Gestion_Obra_UrbanSIP.xlsx` en `gestión/`.
6. Pedir cotizaciones (usar templates).
7. Emitir órdenes de compra.
8. Hacer certificados quincenales durante la obra.
9. Acta de entrega al final.

---

## Documentos de referencia

Todos en `URBANSIP/`:

- **ESTRUCTURA_CARPETAS.md**: estructura completa de modelos y obras.
- **INSTRUCTIVO_COMPUTO.md**: cómo medir y calcular cantidades de materiales.
- **Metodologia_Gestion_UrbanSIP.md**: método completo de gestión de obra.

Todos en `URBANSIP/herramientas/`:

- **plantillas/**: templates reutilizables (Excel, Word, etc.).
- **pedidos/**: templates de pedidos de cotización.
- **scripts/**: `crear_modelo.sh`, `crear_obra.sh`.

---

## Convención de nombres

| Qué | Formato | Ejemplo |
|---|---|---|
| Modelo | `<NOMBRE>` | `ORIGEN` |
| Obra | `<MODELO>-<CLIENTE>` | `ORIGEN-LOPEZ` |
| Archivo presupuesto | `<MODELO>_<VERSION>_Presupuesto_v<N>.xlsx` | `Origen_Esencial_Presupuesto_v1.xlsx` |
| Cotización | `Cotizacion_<PROVEEDOR>_<FECHA>.pdf` | `Cotizacion_SIPCOR_2026-10-06.pdf` |
| Orden de compra | `OC_<NUMERO>_<PROVEEDOR>_<FECHA>.pdf` | `OC_001_SIPCOR_2026-10-06.pdf` |
| Certificado | `Certificado_Quincena_<N>.xlsx` | `Certificado_Quincena_01.xlsx` |
| Contrato | `Contrato_<RUBRO>_<CONTRATISTA>_v<N>.pdf` | `Contrato_Kit_Sipcor_v1.pdf` |

---

## Notas

- **Copiar de AURA:** los Excel de Aura son templates. Copiar y cambiar nombres + datos específicos del modelo.
- **Personalizar:** cada obra es diferente. Los datos del cliente, el lote y los cambios van en `Plantilla_Venta_Cliente_UrbanSIP.xlsx`.
- **Scripts:** están en `herramientas/` y se pueden reutilizar para crear cualquier modelo u obra nueva.
- **Sin scripts:** si lo haces a mano, seguir la estructura de `catalogo/AURA/` como referencia.
