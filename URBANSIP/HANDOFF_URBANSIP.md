# Handoff para la conversación de UrbanSIP (casas SIP llave en mano)

Viene de la conversación "Gestión Obra Formosa 3260" (03 y 04/10/2026). Este documento resume todo lo que sirve para arrancar UrbanSIP sin repetir nada.

---

## 1. Quién es Adrián y cómo trabajar con él
- Constructor y desarrollador. Unidades de negocio: **Urban Green** (CRM de leads y presupuestos de paneles SIP), **UrbanSIP** (casas SIP prediseñadas llave en mano) y **obras de edificios** (hoy Formosa 3260, El Palomar).
- **No es técnico.** Hay que darle pasos literales, en castellano y sin jerga. Sigue el trabajo **desde el celular** (control remoto activado) y pide los archivos en Excel, Word o PDF.
- Le gusta avanzar sin trabas, pero **las decisiones de negocio son suyas**: precios, márgenes, criterios.
- **Regla:** nunca escribir en sus carpetas originales (solo leer). Todo lo generado va a `~/Documents/ClaudeCode/cerebro/`.

## 2. UrbanSIP: el encargo
- **Catálogo de casas SIP prediseñadas llave en mano**, sin cliente por ahora. Empiezan a vender **en los próximos días**.
- **~6 modelos**, cada uno en **dos versiones**: **Esencial** (materiales base) y **Confort** (mejor equipamiento). En total, unos **12 presupuestos**.
- **Aura es el prototipo** y el primer modelo, de unos 78 m².
- **Las casas tradicionales están en stand by.** No desarrollarlas salvo pedido.

### Archivos de Aura
En `~/Downloads/Aura /`. Adrián los iba a mover a **Documentos/Aura**: verificar dónde están.
- **Aura Costo 30-9-26.xlsx**: el más nuevo. En la app de presupuestación está cargada la versión del 9-9.
- **Mano de obra Aura.xlsx**
- **UrbanSIP_Aura_Ficha_Tecnico_Comercial.pdf**. Hay un borrador v3 en `~/Downloads/urbansip/`.
- Planos DWG: Aura Computo, M-02-Aura. Si hace falta medir, pedir exportación a PDF de AutoCAD o DXF.

### Aura en la app de presupuestación
`~/Documents/ClaudeCode/presupuestacion`, modelo "Casa llave en mano en paneles SIP (modelo Aura)", 78 m², 44 líneas. **Rubros:**
- **Fundación:** viga de fundación con pilotines, nylon, contrapisos y carpetas.
- **Mantenimiento de obra:** baño químico y volquetes.
- **Obra gris:**
  - **kit de paneles OSB 11,1 + EPS 15 kg/m³** y **flete desde Córdoba**;
  - sellado, dinteles y pérgola;
  - placa de yeso estándar y RH, cielorraso de baño;
  - **siding LP**, techo de chapa, canaletas y zinguería.
- **Instalaciones:** sanitaria y eléctrica (materiales y mano de obra), artefactos y extractores.
- **Carpinterías:** puertas, puerta principal y aluminio con DVH.
- **Terminaciones:** porcelanato, cemento alisado y zócalos.
- **Pintura**, y **varios**: colocación de artefactos, mueble de cocina, división WPC y mesadas.

⚠ **Esa app tiene 16 cambios de Adrián en espera** (`PENDIENTES_ADRIAN.md`): no tocarla ni reiniciarla sin que él diga "hacelos".

## 3. Método acordado: modelo de catálogo → venta a un cliente
(Está completo en `cerebro/plantillas/tipologias.md`, sección 4.)
- **Modelo de catálogo** (`cerebro/catalogo/URBANSIP/<MODELO>/`):
  - presupuesto base **congelado con versión y fecha de precios**, por ejemplo "Aura Esencial v1, precios al 30/09/26";
  - se arma **una sola vez**: planilla de locales, cómputo, contrataciones con tiempos, pliegos, certificado por etapas SIP y ficha comercial;
  - cuando cambian los precios se actualiza el modelo (v2, v3), no cada venta.
- **Cada venta es una obra** (`cerebro/obras/<MODELO>-<CLIENTE>/`) que **hereda una versión del modelo** y suma una **planilla de cambios del cliente**:
  1. **por terreno:** fundación según suelo, flete según distancia, conexiones, nivelación;
  2. **opcionales:** ítems de Confort en un Esencial, galería, deck;
  3. **modificaciones de diseño**.

  Los cambios se valorizan **con los precios unitarios del modelo**. **Precio final = modelo + cambios aprobados por escrito, con precio, antes de ejecutar.**
- **Ciclo de mejora:**
  - Al cerrar cada obra, se compara el costo real contra el modelo, ítem por ítem.
  - Un desvío que se repite en 2 o 3 casas corrige el modelo.
  - Los cambios frecuentes se vuelven opcionales de catálogo con precio fijo.
- Sugerencia para el contrato con el cliente: "precio del modelo X, versión Y, con precios al [fecha]; todo cambio se cotiza aparte y se aprueba por escrito antes de hacerse".

## 4. Plan de trabajo propuesto para UrbanSIP
1. **Aura como modelo:**
   - revisar el **costo del 30/09** contra el modelo de la app del 9/9 y marcar diferencias;
   - armar la **estructura paramétrica**: cantidades por modelo × precios unitarios comunes;
   - definir **Esencial y Confort** como dos listas de materiales (piso, revestimientos, griferías, aberturas, muebles, artefactos, etc.) y mostrar **cuánto suma el Confort**;
   - **pasar del costo al precio de venta:** costo directo → gastos → margen → precio llave en mano, también en u$s/m².
   - armar la **ficha comercial** por modelo y versión.
2. **Los otros 5 modelos** con la misma estructura.
3. **La plantilla de "venta a un cliente"**, con su planilla de cambios.

### Preguntas para hacerle a Adrián al arrancar
- La **lista de los 6 modelos**: nombre, m² y planos.
- **Qué cambia entre Esencial y Confort.** Si no está definido, proponerlo a partir de Aura.
- **Criterio de precio:** margen, gastos generales, comisión de venta.
- ¿Los precios de los paneles salen del **CRM de Urban Green**?
- ¿El flete desde Córdoba es fijo, o depende del destino?

## 5. Criterios que ya validó Adrián (aplican también a UrbanSIP)
De `cerebro/criterios/criterios_obra.md` y `criterio_computo.md`:
- **Costo objetivo como referencia:** toda cotización, comparativa o pedido muestra el objetivo y el desvío.
- **IVA:** los materiales van con IVA del 21%; la mano de obra va sin IVA; el ascensor con 10,5% (no aplica a casas). **No comentar el IVA de caja**, porque él no lo maneja.
- **Antes de comparar totales, revisar el alcance ítem por ítem.** Lo que falta o no tiene precio se valúa al precio del objetivo, porque son los adicionales futuros.
- **Compras hacia atrás:** inicio de la tarea − fabricación − adjudicación − compulsa − **30 días de documentación** (alcance, cómputo, pliego, planos). En SIP, **el kit de paneles con su flete es la compra crítica**.
- **Certificación:**
  - quincenal por avance, fondo de garantía del 5%, cada etapa pesada por **jornales**;
  - la limpieza va aparte y se paga con la aprobación de la Dirección de Obra;
  - la documentación y las habilitaciones se pagan al cumplirse;
  - los adicionales, solo con orden previa y escrita.
- **Documentos para contratistas o clientes:** **sin datos internos** (ni costo objetivo, ni presupuestos previos, ni márgenes). Los internos van aparte.
- **Cómputo:**
  - **no se descuentan vanos**; los **baños no llevan látex**;
  - los pisos tipo se multiplican solo por la cantidad real (en Formosa había un error de Piso 1 × 4: −7,7%);
  - controlar la cantidad de baños y de unidades contra la memoria.
- **Documentos de otras obras** solo como referencia o modelo, salvo que él pida usar sus datos.
- **Planilla de locales:** es la base del cómputo, con las terminaciones de cada local, de la planta baja a la terraza y la vereda.

## 6. Herramientas y plantillas listas para reutilizar
- **Skills:**
  - `nueva-obra`: arrancar obras y ventas;
  - `revisar-cotizacion`: comparar ofertas contra el objetivo y detectar faltantes;
  - `actualizar-cerebro`: mapa de graphify, que corre solo los viernes a las 18.
- **Plantillas:**
  - `cerebro/plantillas/tipologias.md` (casa SIP, sección 3, y método de catálogo, sección 4);
  - `plantillas/obra.json` (datos de la obra o venta para membretes).
- **PDF con membrete:** `cerebro/herramientas/pdf_obra.py`, con `armar(bloques, archivo, obra_json=...)`.
- **Ejemplos de Formosa para adaptar**, en `cerebro/obras/FO3260/`:
  - `pedidos/`: pedidos de cotización con membrete (Word + PDF) y comparativas Excel con fórmulas contra el objetivo;
  - `certificados/`: planilla interna, certificado N° 0 limpio y justificación del aperturado por jornales;
  - `contratos/para_contratistas/`: PDF de rendimientos y brief del contrato;
  - `costo_objetivo_II/`: Objetivo I contra II, ítem por ítem;
  - `simulador/`: Simulador v5, con plan, certificados y compras de todos los rubros, y aviso de los lunes.
- **Medición de planos:** `cerebro/herramientas/medir_plano.py` (PDF de AutoCAD a escala; con una diferencia sistemática de +2%, a ajustar según el criterio de medición).
- **Venv:** `cerebro/herramientas/venv` (openpyxl, pymupdf, shapely, python-docx, fpdf2, formulas).

## 7. Lo que sigue abierto en Formosa (NO es de esta conversación)
Se sigue en "Gestión Obra Formosa 3260":
- compras de hierro y hormigón (pedidos el lunes 05/10, compra el viernes 09/10);
- sanitaria (respuestas el 16/10);
- albañilería (documentación ahora, pedidos en noviembre);
- contratos v5 a firmar;
- Simulador v5;
- plan actualizado.
