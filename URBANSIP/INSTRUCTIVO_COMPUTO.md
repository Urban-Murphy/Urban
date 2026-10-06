# UrbanSIP: instructivo de cómputo

Metodología para medir y calcular cantidades de materiales en un modelo SIP, basada en Aura (73 m²). Aplica a cualquier modelo nuevo.

---

## 1. BASE: planilla de locales (PERIMSUP)

**Qué es:** una tabla con cada local, sus medidas y qué materiales van en cada uno. Es el punto de partida de todo cómputo.

### Columnas

| Local | Perímetro (m) | Superficie (m²) | Altura promedio (m) | Notas |
|---|---|---|---|---|
| Estar-comedor-cocina | 33,6 | 39,5 | 2,73 | Piso, revestimiento, siding exterior |
| Baño | 8,5 | 4,1 | 2,89 | Piso, impermeabilización ducha, revestimiento |
| Dormitorio 1 | 15,1 | 12,9 | 3,18 | Piso, durlock, siding exterior |
| Dormitorio 2 | 14,1 | 11,5 | 2,93 | Piso, durlock, siding exterior |
| **TOTAL CUBIERTA** | — | **68 m²** | — | Suma de superficies de piso |

### Cómo se mide

1. **Perímetro:** suma de los 4 lados del local (medido en el plano o en AutoCAD). Se usa para:
   - Revestimiento de durlock (altura prom. × perímetro).
   - Pintura de muros (altura prom. × perímetro).
   - Zócalos (perímetro, sin descontar vanos).

2. **Superficie:** largo × ancho del local. Se usa para:
   - Pisos (piso está incluido en la superficie base).
   - Revestimiento de baño (solo la ducha, medida aparte).
   - Cielorraso (igual que la superficie del piso).

3. **Altura promedio:** altura libre del local. Se calcula como:
   - Si el local tiene techo plano de durlock: altura de piso a durlock.
   - Si tiene techo de chapa: altura de piso a la viga más baja (o a la línea de gotele).
   - En Aura: ronda 2,73 a 3,18 m según el local.

### Criterios de Aura

- **Superficie total cubierta: 68 m²** (no se descuentan vanos ni aberturas).
- **Revestimiento Durlock:**
  - Estándar (12,5 mm, impacto): 137,5 m² (en muros de estar y dormitorios).
  - RH (resistente a humedad, en baño): 29,2 m² (solo baño).
  - **Criterio:** perím. × altura + ajuste local. No se descuentan ventanas.

---

## 2. CALCULO DE MATERIALES POR TIPO

### Revestimiento de durlock interior

```
Cantidad (m²) = perímetro del local × altura promedio
Ejemplo: Dormi 1: 15,1 m × 3,18 m = 48,0 m² (aprox.)

Cálculo por m²:
- Placa de yeso Knauf 12,5 mm: 1,15 m²/m² (incluye desperdicio 15%)
- Tornillos: 12,5 u/m²
- Cinta microperforada: 4,32 ml/m²
- Masilla: 0,9 kg/m²
```

### Pisos

```
Cantidad (m²) = superficie del local (sin descontar vanos)
Ejemplo: Estar 39,5 m² de porcelanato + cocina 4 m² revestimiento

Cálculo por m²:
- Pegamento: 4,73 kg/m²
- Pastina: 0,32 kg/m²
- Porcelanato 19×120: 1,15 placas/m² (incluye desperdicio 15%)

Criterio especial: si un piso tipo se repite, se multiplica por cantidad real
(En Formosa había un error de "Piso 1 × 4": −7,7%)
```

### Pintura interior

```
Cantidad (m²) = perímetro × altura promedio

Ejemplo: Dormi 1: 15,1 m × 3,18 m = 48,0 m² de muro

Cálculo por m²:
- Látex interior: 0,41 l/m²
- Fijador al agua: 0,07 l/m²
- Enduido: 0,33 l/m²
- Materiales varios (30%): 0,3 kg/m²

Criterio: los baños NO llevan látex en muros (llevan pintura poliuretánica en mampara/ducha)
```

### Techo de chapa

```
Cantidad (m²) = superficie cubierta (72-78 m², según modelo)

En Aura: 78 m² de chapa C25 zinc

Cálculo por m²:
- Cabios pino 3×8: 168 m lineales para 78 m² → 2,15 ml/m²
- Alfajías 2×1: 2,8 ml/m²
- Clavaderas 2×2: 2,2 ml/m²
- Chapa ondulada C25 3mm: 1,0 m²/m² (sin desperdicio, ajustado por medida)
- Tornillos autoperforantes: 10 u/m²

Criterio: los cabios, alfajías y clavaderas forman estructura de techo.
La cubierta SIP 50 (paneles) está incluida en el kit SIPCOR y no se detalla acá.
```

### Siding LP exterior

```
Cantidad (m²) = superficie exterior de muros (medida de panel SIP exterior)

En Aura: 136,9 m² de fachada

Cálculo por m²:
- Placa LP Smart Panel 11,1 mm (2,44×1,22): 1,2 u/m² (incluye 20% desperdicio)
- Tornillos fijación: 16 u/m²

Criterio: se mide la proyección exterior de los paneles SIP.
No se descuentan ventanas en el cómputo (se cortan in situ).
```

### Pisos de cemento alisado exterior

```
Cantidad (m²) = vereda + galería + patio (medida real)

En Aura: 88,7 m² de patio/vereda

Cálculo por m²:
- Cemento Avellaneda 25 kg: 2,73 kg/m²
- Arena: 0,02331 m³/m²
- Cal hidráulica: 4,809 kg/m²

Criterio: se calcula como carpeta de 2 cm sobre contrapiso existente.
La propuesta más económica es un piso exterior separado con junta de EPS.
```

### Canaletas y zinguería

```
Canaletas: 12 ml (perímetro superior aproximadamente)
Bajadas: 8 ml (2 puntos de desagüe)
Zinguería de carga (perímetro soporte): 30 ml
Botagua arranque panel: 50 ml (perímetro base)
Zinguería de dinteles: 13 ml (sobre las aberturas)

Criterio: se mide lineal, sin descontar las esquinas (se juntan en obra).
```

---

## 3. CRITERIOS GENERALES

### No se descuentan

- **Vanos:** ventanas, puertas y aberturas quedan en el cómputo de durlock, pintura, siding.
- **Esquinas:** las medidas lineales incluyen todas las esquinas.
- **Pequeños huecos:** tomacorrientes, interruptores, radiadores, no se descuentan de revestimiento.

### Se descuentan

- **Baños sin látex:** la pintura de baño es poliuretánica en la ducha, no látex.
- **Revestimiento de baño:** solo la zona de ducha y alrededor (11,56 m² en Aura), no todo el baño.
- **Puertas interiores:** el cómputo no descuenta el espacio que ocupan (se corta el durlock in situ).

### Márgenes de desperdicio incluidos

- **Durlock:** +15% (cortes, roturas, ajuste de juntas).
- **Pisos:** +15% (ajustes, roturas).
- **Siding:** +20% (cortes en vanos y esquinas).
- **Chapa de techo:** 0% (se mide exacto por medidas de panel).

### Redondeo

- **Siempre redondear al alza** para mayor seguridad en stock.
- **Fracciones de local:** si un local suma 12,9 m² pero se especifica 13 en la ficha (para stock), usar 13.

---

## 4. PROCESO DE CÓMPUTO PASO A PASO

### Para un modelo nuevo

1. **Medir el plano en AutoCAD o PDF a escala:**
   - Perímetro de cada local.
   - Superficie de cada local.
   - Altura promedio de piso a techo.
   - Zona de siding exterior (m² de fachada).

2. **Armar planilla de locales** (PerimySup del Excel):
   - Una fila por cada local.
   - Suma de superficies = superficie total cubierta.

3. **Calcular cantidad de cada material:**
   - Durlock: perímetro × altura.
   - Pisos: superficie local.
   - Pintura: perímetro × altura.
   - Siding: superficie exterior.
   - Techo: superficie cubierta.

4. **Validar:**
   - Total durlock debe estar cerca de perímetro total × altura promedio.
   - Total pisos = total piso del modelo.
   - Total pintura similar a durlock.
   - Total siding ≈ (perímetro total / 4) × altura × lado externo.

5. **Agregar márgenes de desperdicio** según el ítem.

### Para una obra con cambios

1. **Partir del cómputo del modelo.**
2. **Agregar/restar cambios:**
   - Si se pide agregar 10 m² de galería: +10 m² de piso, +perímetro siding, etc.
   - Si se reduce durlock en un dormitorio: restar perímetro × altura.

3. **Revalidar totales.**

---

## 5. HOJA AUX: detalles de composición

La hoja `Aux` del Excel de costos tiene el desglose de cada material:

**Ejemplo: Placa de yeso estándar por m²**

```
Placa de yeso Knauf 120×240 impact 12,5 mm: 1,15 m²/m²
Tornillo fix madera 3,5×50 ×500: 12,5 u/m²
Cinta papel microperforada Knauf 75 m: 4,32 ml/m²
Masilla multiuso 32 kg: 0,9 kg/m²

Precio total unitario: $7.272,76/m² (al 30/09/26)
```

**Cómo usarla:**
- Si el cómputo da 137 m² de durlock estándar, multiplico 137 × $7.272,76 = $996.268.
- Los consumos (1,15 placas, 12,5 tornillos, etc.) son el detalle; no se cotizan por separado.

---

## 6. VALIDACIÓN RÁPIDA

| Elemento | Aura Esencial (73 m²) | Fórmula aproximada |
|---|---|---|
| Durlock interior total | 166,7 m² | Perim. × alt. promedio ≈ 110 m × 2.9 m |
| Pisos cubierta | 68 m² | Igual a superficie cubierta |
| Pintura interior muros | 166,7 m² | Similar a durlock |
| Siding exterior | 137 m² | (Perim. × 4 / 4) × alt. × factor fachada |
| Techo | 72–78 m² | Igual a superficie cubierta |
| Zócalos | 110 ml | ≈ Perímetro total |

---

## 7. EJEMPLO: armar cómputo de un modelo de 100 m²

1. **Medir planos:** digamos 4 locales, promedio 25 m² cada uno.
2. **Perímetro aproximado:** ~125 m total (suma de los 4 locales).
3. **Altura:** 3 m promedio.
4. **Cálculos:**
   - Durlock: 125 m × 3 m = 375 m².
   - Pisos: 100 m² (superficie).
   - Pintura: 125 m × 3 m = 375 m² (similar a durlock).
   - Siding exterior: ~100 m² (superficie fachada).
   - Techo: 100 m² de chapa + estructura de cabios.

5. **Validar:** los números tienen proporción razonable. Durlock ≈ 3.75× la superficie cubierta.

---

## Notas

- **Este cómputo asume un modelo SIP estándar:** muros panel SIP 70, techo SIP 50 cubierto con chapa, durlock interior, siding LP exterior.
- **Cambios de diseño:** si se agrega un mezzanine, una bóveda de techo o muros curvos, el cómputo cambia significativamente.
- **Exportar de AutoCAD a PDF:** asegurarse que la escala esté correcta (1:50 o 1:100) para medir linealmente.
