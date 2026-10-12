# Instructivo: cómo trabajar con Claude en este repo

Guía corta, sin jerga. Para consultar cuando no recuerdes cómo se hace algo.

## 1. Conceptos básicos

- **Repo (repositorio):** la carpeta del proyecto guardada en GitHub. El nuestro es `Urban-Murphy/Urban`. Todo lo que está ahí lo ve Claude Code.
- **Claude Code:** la parte de Claude que trabaja sobre el repo: lee archivos, los crea, los corrige y los sube.
- **Sesión (conversación):** cada vez que abres una conversación nueva en Code. **No recuerda las anteriores.**
- **`CLAUDE.md`:** el manual del repo. Claude lo lee solo al empezar cada sesión. Es lo único que "recuerda". Si quieres que recuerde algo, hay que pedir que se agregue ahí.
- **`main`:** la versión principal del repo. Lo que está en `main` lo ven todas las sesiones nuevas.
- **Rama / pull request / merge:** una copia aparte para probar cambios y el paso de aceptarlos para pasarlos a `main`. Para uso personal, Claude puede subir directo a `main` si se lo pides.

## 2. Qué usar para cada cosa

| Quiero… | Dónde |
|---|---|
| Pedir algo del repo (presupuesto, obra nueva, precios) | Conversación **nueva** en Code, repo `Urban-Murphy/Urban` |
| Una pregunta suelta que no toca archivos | Un chat común de Claude |
| Ver un informe de uso | `/insights` (es un informe, no sirve para hacer pedidos) |
| Que Claude recuerde una regla | Pedirle: "agregalo al CLAUDE.md" |

Conviene **una conversación por tema** (una para precios, otra para una obra). Las cortas funcionan mejor.

## 3. Carpetas principales

- `URBANSIP/`: modelos de catálogo (Aura, Origen), obras, método y plantillas.
- `PRECIOS/`: lista de precios única y análisis de costos, para SIP y tradicional.
- `generar_presupuesto.py`: arma el presupuesto de Origen a partir de la planilla de Aura.

## 4. Tareas frecuentes

- **Obra nueva:** "obra nueva, modelo Aura, cliente López". Se crea en `URBANSIP/obras/AURA-LOPEZ/`.
- **Modelo nuevo:** "modelo nuevo llamado X". Se crea en `URBANSIP/catalogo/X/`.
- **Actualizar precios:** subir el Excel nuevo; la lista anterior pasa a `PRECIOS/historico/`.
- **Subir un archivo al repo:** adjuntarlo en el chat, o en github.com/Urban-Murphy/Urban con "Add file" > "Upload files".

## 5. Reglas del negocio que Claude ya conoce

- IVA: materiales 21%, mano de obra sin IVA.
- Cómputo: no se descuentan vanos; los baños no llevan látex.
- Los documentos para clientes y contratistas no llevan datos internos (costos, márgenes).
- Precio de una venta = precio del modelo + cambios aprobados por escrito.
- Claude no escribe en tus carpetas originales, solo lee.

## 6. Qué conviene recordar

- Una sesión nueva sabe solo lo que dice el `CLAUDE.md` y lo que hay en el repo.
- Decisiones nuevas (criterios, precios, márgenes) hay que anotarlas en el `CLAUDE.md` o en un archivo del repo; si no, se pierden al cerrar la sesión.
- Si Claude propone algo de negocio, la decisión final es tuya.
- Las cantidades estimadas en un presupuesto (por ejemplo el kit de paneles de Origen) están marcadas "ESTIMADO" hasta tener cotización.
- Claude nunca pide cotizaciones a proveedores por su cuenta.
