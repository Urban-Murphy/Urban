// FUENTE ÚNICA DE DATOS DE LA APP. Para actualizar precios o fichas, editar solo este archivo.
// Fuente: PLANILLA-MODELOS-URBANSIP-F CON PRECIOS.xlsx (Drive de UrbanSIP) + ficha Aura v3.
// Después de editar, subir de número "version" para que los celulares se actualicen.
window.DATOS = {
  version: "2026-10-21",
  preciosAl: "21/10/2026",
  usdM2: { esencial: 1200, confort: 1500 },
  semicubierto: 600,
  // Primera versión: solo los 6 modelos con renders listos. Los demás están en "pendientes" (se pasan a "modelos" cuando tengan fotos).
  modelos: [
    { id: "trama35", nombre: "Trama 35", linea: "Cubic", cub: 35, sem: 33, total: 68, dorm: 1, banos: 1, vestidor: false, lavadero: "No", exteriores: "Porch y galería", esencial: 42800, confort: 53300, revisar: "La planilla dice 42.800 / 53.300; por m² daría 42.000 / 52.500." },
    { id: "origen", nombre: "Origen 63", linea: "Cubic", cub: 63, sem: 17, total: 80, dorm: 2, banos: 1, vestidor: false, lavadero: "Incluido", exteriores: "Galería trasera", esencial: 80300, confort: 99200, revisar: "La planilla dice 80.300 / 99.200; por m² daría 75.600 / 94.500." },
    { id: "umbral64", nombre: "Umbral 64", linea: "Cubic", cub: 64, sem: 36, total: 100, dorm: 1, banos: 1, vestidor: true, lavadero: "Incluido", exteriores: "Galería y cochera", esencial: 76800, confort: 96000, revisar: "Dormitorios: 1 en una planilla, 2 en otra." },
    { id: "aura", nombre: "Aura 72", linea: "Cubic", cub: 72, sem: 8, total: 80, dorm: 2, banos: 1, vestidor: false, lavadero: "Sí", exteriores: "Galería trasera", esencial: 86400, confort: 108000, plazo: "90-105 días", ficha: true },
    { id: "refugio", nombre: "Refugio 79", linea: "Wing", cub: 79, sem: 32, total: 111, dorm: 2, banos: 1, vestidor: false, lavadero: "No", exteriores: "Porch, galería y parrilla", esencial: 94800, confort: 118500 },
    { id: "umbral80", nombre: "Umbral 80", linea: "Cubic", cub: 80, sem: 32, total: 112, dorm: 2, banos: 1, vestidor: false, lavadero: "Incluido", exteriores: "Galería y cochera", esencial: 96000, confort: 120000 }
  ],
  // Comparación Esencial vs Confort. Hoy solo está la ficha de Aura; se aplica como referencia al resto.
  comparacion: {
    titulo: "Esencial vs Confort (ficha Aura)",
    rubros: [
      ["Muros", "Panel SIP 70", "Panel SIP 70"],
      ["Cubierta", "SIP EPS 50 mm · chapa C25 zinc", "SIP EPS 50 mm · chapa C25 color a elección"],
      ["Cielorrasos", "Placa de yeso plana o panel ranurado visto según diseño", "Placa de yeso plana o panel ranurado visto según diseño"],
      ["Fachada", "Siding + chapa", "Siding + chapa + revestimiento plástico"],
      ["Aberturas", "Aluminio Módena + DVH", "PVC + DVH + mosquiteros"],
      ["Pisos", "SPC símil madera o porcelánico", "SPC símil madera o porcelanato rectificado"],
      ["Puertas interiores", "Placorr moldurada · marco MDF · para pintar", "Placorr Plac-Full texturada · contramarcos regulables"],
      ["Puerta exterior", "Madera", "PVC"],
      ["Zócalos", "PVC 7 cm · blanco o negro", "PVC 7 cm · blanco o negro"],
      ["Cocina", "Bajo mesada · granito · bacha inox.", "Bajo mesada + alacena · cuarzo · bacha superior"],
      ["Grifería cocina", "Hidromet Minicucina Curvo", "Hidromet Pro Flex"],
      ["Cocción", "Cocina eléctrica", "Anafe + horno eléctrico empotrado"],
      ["Extractor cocina", "No incluido", "Incluido"],
      ["Sanitarios", "Roca Capea", "Roca Mónaco"],
      ["Grifería baño", "Hidromet Small", "Hidromet Raptor"],
      ["Vanitory", "Campi · selección UrbanSIP", "Campi · selección superior UrbanSIP"],
      ["Complementos baño", "Sin espejo, mampara ni accesorios", "Espejo LED + mampara + accesorios + extractor"],
      ["Placares", "Espacio previsto · sin frente ni interior", "Frente incluido · interior opcional"],
      ["Climatización", "Preinstalación de aire acondicionado", "Aires acondicionados incluidos e instalados"],
      ["Electricidad", "Jeluz · línea estándar", "Cambre Siglo XXII"],
      ["Iluminación", "Puntos completos · artefactos no incluidos", "Artefactos incluidos según selección UrbanSIP"],
      ["Agua caliente", "Termotanque eléctrico Señorial", "Termotanque eléctrico Ariston"],
      ["Presurización", "Opcional", "Presurizadora incluida"],
      ["Exterior", "Sin camino perimetral", "Camino perimetral de 0,80 m"]
    ],
    nota: "Marcas y modelos pueden reemplazarse por equivalentes según disponibilidad."
  },
  pago: [
    { etapa: "Contratación", pct: 10 },
    { etapa: "Inicio de ejecución", pct: 50 },
    { etapa: "Avance certificado 1", pct: 15 },
    { etapa: "Avance certificado 2", pct: 10 },
    { etapa: "Avance certificado 3", pct: 10 },
    { etapa: "Entrega", pct: 5 }
  ],
  info: [
    ["Plazo estimado", "90-105 días."],
    ["Vigencia de la propuesta", "10 días corridos. El cliente tiene hasta 30 días desde la contratación para completar el segundo pago. El precio queda fijado al alcanzar el 60%, siempre que el cliente no pida modificaciones."],
    ["Moneda", "Dólares estadounidenses. Pagos en USD billete o en pesos al tipo de cambio de la operación, vigente el día de cada pago."],
    ["Logística", "Incluida hasta 50 km desde UrbanSIP Ituzaingó."],
    ["Semicubiertos", "USD 600 por m²."],
    ["Gas", "Opcional, a pedido y con cotización particular."],
    ["Fundación y estudio de suelo", "Incluidos. Si se requiere una fundación especial, se cotiza solo la diferencia."],
    ["Proyecto y dirección", "Proyecto del modelo, implantación en el terreno, documentación técnica y dirección de obra UrbanSIP."],
    ["Instalaciones", "Eléctrica y sanitaria completas hasta los puntos de conexión exterior. Conexión a redes o medidores se cotiza aparte."],
    ["Terreno", "El lote debe estar apto. Movimientos de suelo, rellenos, desmontes, nivelaciones o retiro de árboles se cotizan aparte."],
    ["Municipio", "UrbanSIP puede coordinar la gestión. Tasas, derechos, visados y aranceles de terceros no están incluidos."],
    ["Personalizaciones", "El precio desde es del modelo estándar. Ampliaciones, cambios de proyecto y terminaciones fuera de la selección UrbanSIP se cotizan aparte."]
  ],
  pendientes: [
    { id: "nido", nombre: "Nido 33", linea: "Wing", cub: 33, sem: 12.5, total: 45.5, dorm: 1, banos: 1, vestidor: false, lavadero: "No", exteriores: "Deck y porch", esencial: 39600, confort: 49500 },
    { id: "senda", nombre: "Senda 73", linea: "Cubic", cub: 73, sem: 25, total: 98, dorm: 2, banos: 1, vestidor: true, lavadero: "Sí", exteriores: "Galería", esencial: 87600, confort: 109500, revisar: "m²: 73 en una planilla, 80 en otra." },
    { id: "lumbre117", nombre: "Lumbre 117", linea: "Cubic", cub: 117, sem: 30, total: 147, dorm: 2, banos: 2, vestidor: true, lavadero: "Sí", exteriores: "Galería y porch", esencial: 140400, confort: 175500 },
    { id: "lumbre135", nombre: "Lumbre 135", linea: "Cubic", cub: 135, sem: 37, total: 172, dorm: 3, banos: 2, vestidor: true, lavadero: "Sí", exteriores: "Galería y porch", esencial: 162000, confort: 202500 }
  ]
};
