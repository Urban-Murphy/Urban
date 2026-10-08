# Flujo Automático de Presupuestos: Origen & Aura

## Instalación (Hacer una sola vez)

```bash
pip install pandas openpyxl
```

---

## Opción 1: Script Manual (Rápido)

**Ejecutar cuando necesites un presupuesto nuevo:**

```bash
python3 generar_presupuesto.py \
  --origen ORIGEN_COMPUTO_PROVISORIO.xlsx \
  --aura Aura_Costo_30-9-26.xlsx \
  --output ORIGEN_Esencial_Presupuesto_v1.xlsx
```

**Tiempo: < 1 minuto**

---

## Opción 2: Automático GitHub (Sin hacer nada)

✓ Cada vez que cambias `ORIGEN_COMPUTO_PROVISORIO.xlsx` o `Aura_Costo.xlsx`:
1. Se regenera automáticamente el presupuesto
2. Se commitea solo
3. Tenés resultado listo en GitHub

**Tiempo: 0 (automático)**

---

## Estructura de Archivos Esperada

```
.
├── ORIGEN_COMPUTO_PROVISORIO.xlsx    ← Tu archivo de cómputo
├── Aura_Costo_30-9-26.xlsx           ← Tu archivo de precios Aura
├── generar_presupuesto.py             ← Script (ya existe)
└── ORIGEN_Esencial_Presupuesto_v1.xlsx ← Resultado (generado)
```

---

## Qué genera el script

**3 hojas en el Excel final:**

1. **PerimySup**: Perímetros, superficies y alturas por local
2. **Materiales**: Desglose de cada material con cantidad y precio
3. **Totales**: Resumen en ARS y USD

---

## Próximos pasos

### Para hoy:
- [ ] Guardá `generar_presupuesto.py` en la raíz del repo
- [ ] Ejecutá: `python3 generar_presupuesto.py --origen ... --aura ... --output ...`

### Para mañana:
- [ ] El workflow automático se dispara cuando cambies archivos
- [ ] No necesitás hacer nada más

---

## Preguntas?

- ¿Script no funciona? Revisa que los archivos Excel tengan las hojas esperadas
- ¿Workflow no se triggeó? Pusheá a GitHub y espera 1 min
- ¿Precios incorrectos? Edita `generar_presupuesto.py` línea ~80 (mapeo de precios)

