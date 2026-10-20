# Automatización de Presupuestos: Aura & Origen

## Problema Actual
1. Cargar Excel manualmente
2. Parsear datos a mano
3. Generar presupuesto con scripts ad-hoc
4. Pushear resultados

**Tiempo promedio: 20-30 min por presupuesto**

---

## Solución Propuesta: Flujo Automático

### OPCIÓN 1: Python Script Reutilizable (HOY)
**Más fácil. Cero config.**

```bash
python3 generar_presupuesto.py --origen "/ruta/ORIGEN_COMPUTO.xlsx" --aura "/ruta/Aura_Costo.xlsx" --output presupuesto.xlsx
```

**Ventajas:**
- Ejecutable desde CLI
- Aplica las mismas reglas cada vez
- Rápido (< 2 min)

**Cómo funciona:**
1. Lee Excel de Origen (PerimySup + especificaciones)
2. Lee precios de Aura
3. Aplica cómputos automáticamente
4. Genera presupuesto en 3 hojas

---

### OPCIÓN 2: GitHub Workflow (Nivel Medio)
**Automático cuando pusheás archivos a GitHub**

```yaml
# .github/workflows/presupuesto.yml
- Si cambias ORIGEN_COMPUTO.xlsx → se regenera automáticamente
- Resultado se commitea
- 0 trabajo manual
```

**Ventajas:**
- Sin intervención humana
- Historial automático en GitHub
- Ejecuta cada vez que cambias archivos

---

### OPCIÓN 3: Sincronización Mac → GitHub → Presupuesto (Nivel Avanzado)
**Full automático.**

1. Cambias archivo en Mac
2. Se sube automático a GitHub (iCloud sync)
3. Workflow genera presupuesto
4. Descargás resultado

---

## Recomendación Inmediata

**Empezamos con OPCIÓN 1** (Script Python):
- Creas el script una sola vez
- Lo ejecutas cada día/semana en < 1 minuto
- Resultado automático

**Después → OPCIÓN 2** (GitHub Workflow):
- Ni siquiera ejecutas nada manualmente
- Todo se hace solo

---

## Próximos Pasos

1. ¿Querés que cree el script Python reutilizable?
2. ¿Después automatizamos con GitHub Workflow?
3. ¿O directamente configuramos sincronización Mac?

