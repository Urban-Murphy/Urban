#!/bin/bash

# Crear estructura de carpetas para una obra nueva (venta a cliente)

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Uso: ./crear_obra.sh <MODELO> <CLIENTE>"
    echo "Ejemplo: ./crear_obra.sh ORIGEN LOPEZ"
    exit 1
fi

MODELO=$1
CLIENTE=$2
BASE_DIR="obras/${MODELO}-${CLIENTE}"

# Crear carpetas
mkdir -p "$BASE_DIR/{datos,planos,gestión,compras,certificados,contratos,entregas}"

# Crear README
cat > "$BASE_DIR/README.md" << EOF
# $MODELO - $CLIENTE

Obra nueva: venta a cliente.

## Datos del cliente

- Cliente: $CLIENTE
- Lote: (completar)
- Localidad: (completar)
- Fecha de firma: (completar)
- Plazo estimado: 90-105 días corridos

## Estado

- [ ] Contrato firmado
- [ ] Cambios aprobados (en Plantilla_Venta_Cliente_UrbanSIP.xlsx)
- [ ] Planos de implantación
- [ ] Estudio de suelos y fundación
- [ ] Compras cotizadas
- [ ] Órdenes emitidas
- [ ] Certificados semanales/quincenales
- [ ] Acta de entrega

## Carpetas

- **datos/**: contrato, forma de pago, cambios aprobados.
- **planos/**: implantación, fundación específica.
- **gestión/**: plan, compras, certificación (copia de plantilla personalizada).
- **compras/**: cotizaciones, órdenes de compra.
- **certificados/**: certificados quincenales, acta de recepción.
- **contratos/**: contratos con contratistas.
- **entregas/**: acta de entrega, garantía, desvíos de costos.

## Archivos clave

1. **Plantilla_Venta_Cliente_UrbanSIP.xlsx** (copiar a datos/)
   - Datos del cliente
   - Forma de pago
   - Cambios aprobados
   - Opcionales

2. **Plantilla_Gestion_Obra_UrbanSIP.xlsx** (copiar a gestión/ y personalizar)
   - Plan de obra
   - Compras hacia atrás
   - Certificación
   - Seguimiento de costos

3. **Pedidos de cotización** (usar templates de herramientas/)
   - Aberturas
   - Siding
   - Cocina
   - Climatización
   - Otros ítems

## Cronograma

- Día 0: Firma de contrato, primer 10% del pago.
- Día 1-10: Inicio, pago 50%, pedir compras críticas (kit SIPCOR).
- Día 10-30: Fundación, montaje del kit.
- Día 30-60: Obra gris, instalaciones.
- Día 60-90: Terminaciones, pintura.
- Día 90: Entrega.
EOF

echo "✓ Obra ${MODELO}-${CLIENTE} creada en $BASE_DIR"
echo ""
echo "Archivos a copiar:"
echo "  - Plantilla_Venta_Cliente_UrbanSIP.xlsx → $BASE_DIR/datos/"
echo "  - Plantilla_Gestion_Obra_UrbanSIP.xlsx → $BASE_DIR/gestión/ (personalizar)"
echo ""
echo "Siguientes pasos:"
echo "  1. Completar datos del cliente en datos/Plantilla_Venta_Cliente_UrbanSIP.xlsx"
echo "  2. Hacer estudio de suelos"
echo "  3. Pedir cotizaciones (usar templates de herramientas/)"
echo "  4. Hacer plan personalizado en gestión/Plantilla_Gestion_Obra_UrbanSIP.xlsx"
