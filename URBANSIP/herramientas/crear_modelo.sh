#!/bin/bash

# Crear estructura de carpetas para un modelo nuevo de UrbanSIP

if [ -z "$1" ]; then
    echo "Uso: ./crear_modelo.sh <NOMBRE_MODELO>"
    echo "Ejemplo: ./crear_modelo.sh ORIGEN"
    exit 1
fi

MODELO=$1
BASE_DIR="catalogo/$MODELO"

# Crear carpetas
mkdir -p "$BASE_DIR/{presupuesto,plan,compras,pliegos,fichas}"

# Crear README
cat > "$BASE_DIR/README.md" << EOF
# $MODELO: modelo de catálogo UrbanSIP

Modelo nuevo de vivienda SIP llave en mano.

## Estado

- [ ] Presupuesto base (Excel)
- [ ] Comparación Esencial vs Confort
- [ ] Cálculo de precio de venta
- [ ] Plan de obra (tareas y duraciones)
- [ ] Mano de obra (detalle de jornales)
- [ ] Compras hacia atrás (cuándo pedir cada cosa)
- [ ] Pedidos de cotización
- [ ] Pliegos técnicos
- [ ] Ficha técnico-comercial

## Carpetas

- **presupuesto/**: Excel de costos, comparación Esencial/Confort, precio de venta.
- **plan/**: tareas, duraciones, plazo en días corridos.
- **compras/**: cuándo pedir cada cosa, pedidos de cotización.
- **pliegos/**: especificaciones técnicas para contratistas.
- **fichas/**: ficha técnico-comercial para clientes.

## Siguientes pasos

1. Medir planos en AutoCAD (perímetros, superficies, alturas).
2. Armar planilla de locales (usar ESTRUCTURA_CARPETAS.md e INSTRUCTIVO_COMPUTO.md).
3. Hacer presupuesto de materiales y mano de obra (copiar estructura de AURA y adaptar).
4. Calcular Esencial vs Confort.
5. Hacer plan de obra y compras hacia atrás.
6. Pedir cotizaciones (usar templates de herramientas/pedidos/).
EOF

echo "✓ Modelo $MODELO creado en $BASE_DIR"
echo ""
echo "Archivos a copiar:"
echo "  - Plantilla_Gestion_Obra_UrbanSIP.xlsx → $BASE_DIR/plan/"
echo "  - Excel de costos (copiar de AURA y adaptar) → $BASE_DIR/presupuesto/"
echo ""
echo "Uso de documentos:"
echo "  - ESTRUCTURA_CARPETAS.md: cómo organizar la carpeta"
echo "  - INSTRUCTIVO_COMPUTO.md: cómo medir y calcular materiales"
echo "  - Metodologia_Gestion_UrbanSIP.md: método de gestión de obras"
