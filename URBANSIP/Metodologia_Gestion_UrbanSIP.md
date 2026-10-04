# UrbanSIP: metodología de gestión de obra

Adaptación a casas SIP de lo validado en Formosa 3260 (fuente: `HANDOFF_URBANSIP.md`, secciones 3, 5 y 6). Herramienta: `Plantilla_Gestion_Obra_UrbanSIP.xlsx`, una copia por obra.

## 1. Del catálogo a la obra
- **Modelo de catálogo** (`catalogo/URBANSIP/<MODELO>/`): presupuesto congelado con versión y fecha de precios, más cómputo, plan, compras, pliegos y ficha. Se arma **una sola vez**.
- **Cada venta es una obra** (`obras/<MODELO>-<CLIENTE>/`):
  - hereda una versión del modelo;
  - suma la **planilla de cambios** (terreno, opcionales y diseño), que está en `Plantilla_Venta_Cliente_UrbanSIP.xlsx`;
  - lleva su propia copia de la plantilla de gestión.
- **Precio final = modelo + cambios aprobados por escrito, con precio, antes de ejecutarse.**

## 2. Plan de obra (hoja Plan)
- **Las tareas y las duraciones** salen de la planilla de mano de obra, con una cuadrilla de 3 personas.
- **Las etapas** son 1 Fundación, 2 Kit SIP, 3 Obra gris, 4 Terminaciones y 5 Entrega.
- **Aura da unos 64 días hábiles, 88 días corridos.** La ficha promete 90 a 105 días: queda un margen de unos 2 días contra el mínimo y de 17 contra el máximo.

## 3. Compras hacia atrás (hoja Compras)
- **Cuándo hay que empezar cada compra:** se parte del día en que la obra la necesita y se restan, en este orden:
  1. la fabricación;
  2. la adjudicación;
  3. la compulsa (pedir y comparar cotizaciones);
  4. la documentación.
- **La compra crítica es el kit de paneles con su flete.** SIPCOR cotiza en dólares, el precio vale 5 días y el flete no está incluido.
- **Ventaja del catálogo:** en Formosa la documentación llevaba 30 días; en un modelo de catálogo ya está hecha, así que se pone 0 salvo que haya cambios del cliente.
- **Las medidas de los vanos** se cierran antes de pedir los paneles.
- **El mueble de cocina** se mide en obra después del durlock.
- **Estado de cada compra:** la hoja la marca *ATRASADA* o *ESTA SEMANA* contra la fecha de hoy.

## 4. Certificación (hoja Certificación)
- **Quincenal por avance:** el peso de cada etapa es su cantidad de **jornales**, como en Formosa.
- **Fondo de garantía del 5%:** se devuelve con la recepción.
- **La limpieza** se paga con la aprobación de la Dirección de Obra.
- **Los adicionales** se pagan solo con orden escrita previa.

## 5. Costo objetivo vs real (hoja Costo objetivo vs real)
- **Objetivo y desvío:** cada compra muestra los dos. Un desvío de más del 3% se marca en rojo.
- **Antes de comparar totales:** se revisa el alcance ítem por ítem. Lo que falta o no tiene precio se valúa al precio objetivo, porque son los adicionales futuros.
- **Ciclo de mejora:** un desvío que se repite en 2 o 3 casas corrige el modelo y genera una nueva versión (v2, v3). Un cambio que piden muchos clientes pasa a ser un opcional de catálogo con precio fijo.

## 6. Adicionales (hoja Adicionales)
- **Sin orden escrita no se hace:** sin orden firmada, la hoja muestra *NO EJECUTAR*.
- **Los adicionales que pide el cliente** también se cargan en la hoja Cambios de la venta.

## 7. Documentos
- **Para contratistas y clientes:** van **sin datos internos**, es decir sin costo objetivo, sin presupuestos previos y sin márgenes.
- **Documentos internos:** se guardan aparte.
- **IVA:** los materiales llevan 21%; la mano de obra va sin IVA.
- **Cómputo:**
  - no se descuentan vanos;
  - los baños no llevan látex;
  - la planilla de locales es la base del cómputo.

## Pendiente de traer de Formosa
Los originales están en la Mac (`cerebro/obras/FO3260/`). Si se suben, se pueden adaptar directamente:
- **Pedidos de cotización** con membrete (Word + PDF).
- **Comparativas en Excel** contra el objetivo.
- **Certificado N° 0** limpio.
- **Brief de contrato** para contratistas.
- **Simulador v5.**
