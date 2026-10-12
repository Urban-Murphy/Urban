#!/usr/bin/env python3
"""
Generador automático de presupuestos: Origen + Aura
Mapea TODOS los items de Aura con cantidades inteligentes de Origen
Uso: python3 generar_presupuesto.py --origen archivo.xlsx --aura aura.xlsx --output presupuesto.xlsx
"""

import argparse
import unicodedata
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill
from pathlib import Path

# Cantidades propias de Origen Esencial que NO se pueden derivar de PerimySup.
# Si cambian los planos o el modelo, editar acá (y solo acá).
CANT = {
    "muros": 137.5,       # m2 placa/pintura/revestimiento en muros
    "zocalo": 88.7,       # ml zócalo
    "siding": 136.93,     # m2 siding exterior
    "piso": 62.7,         # m2 pisos
    "techo": 78,          # m2 techo de chapa
    "sanitario": 1,
    "bocas": 47,          # bocas eléctricas totales
    "puerta_principal": 1,
    "puerta_interior": 3,
    "carpinteria": 1,
    "cocina": 1,
    "mesada": 6,
    "division": 1,
}
DOLAR = 1550
# El kit de paneles de Aura es el presupuesto SIPCOR #2790 (73 m2 cubiertos, $26.928.565,49,
# sin flete). Para Origen se estima proporcional a la superficie hasta tener cotización propia.
SUP_AURA = 73

def sin_tildes(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")

def leer_origen(archivo):
    """Extrae PerimySup de Origen.
    Busca la fila de encabezados (Local / Perímetro / Superficie / Altura) y lee
    las columnas por nombre; si no la encuentra, usa las posiciones fijas B-E."""
    df = pd.read_excel(archivo, sheet_name='PerimySup', header=None)

    cols = None
    for i in range(min(len(df), 15)):
        fila = [sin_tildes(str(x)).strip().lower() if pd.notna(x) else "" for x in df.iloc[i]]
        if "local" in fila:
            def col(clave):
                return next((j for j, v in enumerate(fila) if v.startswith(clave)), None)
            c = (fila.index("local"), col("perim"), col("sup"), col("alt"))
            if None not in c:
                cols = (i + 1, c)
                break

    if cols:
        desde, (cn, cp, cs, ca) = cols
        filas = range(desde, len(df))
    else:
        desde, (cn, cp, cs, ca) = 3, (1, 2, 3, 4)
        filas = range(3, 8)

    locales = []
    for i in filas:
        nombre = df.iloc[i, cn]
        if pd.isna(nombre) or str(nombre).strip().lower().startswith("total"):
            break
        num = lambda c: float(df.iloc[i, c]) if pd.notna(df.iloc[i, c]) else 0
        locales.append({"nombre": nombre, "perim": num(cp), "sup": num(cs), "alt": num(ca)})

    sup_total = sum(l["sup"] for l in locales)
    perim_total = sum(l["perim"] for l in locales)

    return locales, sup_total, perim_total

def leer_aura_todos(archivo):
    """Extrae TODOS los items de Aura"""
    df = pd.read_excel(archivo, sheet_name='Materiales', header=None)

    items = []
    for i in range(5, min(len(df), 100)):
        desc = df.iloc[i, 1]
        unit = df.iloc[i, 2]
        cant_aura = df.iloc[i, 3]
        precio = df.iloc[i, 4]

        if pd.notna(desc) and pd.notna(precio) and precio > 0:
            items.append({
                "desc": str(desc).strip(),
                "unit": str(unit).strip() if pd.notna(unit) else "",
                "cant_aura": float(cant_aura) if pd.notna(cant_aura) else 0,
                "precio": float(precio)
            })

    return items

def calcular_cantidad_origen(desc, sup_total, perim_total):
    """Mapea cantidad de Aura a cantidad de Origen"""
    desc_lower = desc.lower()

    # Materiales basados en superficie
    if any(x in desc_lower for x in ["placa roca", "durlock", "latex", "pintura", "revestimiento"]):
        if "cielorraso" in desc_lower or "cielo" in desc_lower:
            return sup_total  # Superficie cielo = suma de PerimySup
        else:
            return CANT["muros"]

    # Materiales basados en perímetro
    if any(x in desc_lower for x in ["zocalo", "zingueria", "canaleta", "botagua", "dintel"]):
        if "zocalo" in desc_lower:
            return CANT["zocalo"]
        return perim_total

    # Siding exterior
    if "siding" in desc_lower:
        return CANT["siding"]

    # Pisos
    if "piso" in desc_lower or "porcelanato" in desc_lower:
        if "alisado" in desc_lower:
            return 0  # No aplica
        return CANT["piso"]

    # Techos
    if "techo" in desc_lower or "chapa" in desc_lower:
        return CANT["techo"]

    # Sanitarios
    if any(x in desc_lower for x in ["sanitario", "bano", "material sanitario", "extractor", "artefacto"]):
        return CANT["sanitario"]

    # Electricidad
    if "electrico" in desc_lower or "bocas" in desc_lower:
        return CANT["bocas"]

    # Puertas
    if "puerta" in desc_lower:
        if "principal" in desc_lower:
            return CANT["puerta_principal"]
        return CANT["puerta_interior"]

    # Carpintería
    if "alum" in desc_lower or "dvh" in desc_lower or "ventana" in desc_lower:
        return CANT["carpinteria"]

    # Cocina
    if "cocina" in desc_lower or "mueble" in desc_lower:
        return CANT["cocina"]

    # Mesadas
    if "mesada" in desc_lower:
        return CANT["mesada"]

    # Division
    if "division" in desc_lower or "wpc" in desc_lower:
        return CANT["division"]

    # Kit de paneles SIP: estimado proporcional a la superficie de Aura (ver SUP_AURA)
    if "paneles kit" in desc_lower:
        return round(sup_total / SUP_AURA, 4)

    # Flete desde Córdoba: 1 global (depende del destino, confirmar)
    if "flete" in desc_lower:
        return 1

    # Items que no aplican a Esencial
    if any(x in desc_lower for x in ["fundacion", "contrapiso", "quimico", "limpieza", "estudio"]):
        return 0

    return 0

def generar_presupuesto(origen_file, aura_file, output_file):
    """Genera presupuesto con TODOS los items de Aura"""
    locales, sup_total, perim_total = leer_origen(origen_file)
    items_aura = leer_aura_todos(aura_file)

    # Calcular cantidades de Origen para cada item
    for item in items_aura:
        item["cant_origen"] = calcular_cantidad_origen(item["desc"], sup_total, perim_total)
        if "paneles kit" in item["desc"].lower():
            item["desc"] += " [ESTIMADO proporcional a Aura; falta cotización SIPCOR de Origen]"
        elif "flete" in item["desc"].lower():
            item["desc"] += " [valor de Aura; confirmar según destino]"

    # Crear workbook
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # ===== HOJA 1: PerimySup =====
    ws = wb.create_sheet("PerimySup", 0)
    ws['A1'] = "ORIGEN ESENCIAL - PERIMETROS Y SUPERFICIES"
    ws['A1'].font = Font(bold=True, size=12)

    for col, header in enumerate(["Local", "Perímetro (m)", "Superficie (m²)", "Altura (m)"], 1):
        ws.cell(3, col, header).font = Font(bold=True)
        ws.cell(3, col).fill = PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid")

    row = 4
    for local in locales:
        ws.cell(row, 1, local["nombre"])
        ws.cell(row, 2, local["perim"])
        ws.cell(row, 3, local["sup"])
        ws.cell(row, 4, local["alt"])
        row += 1

    ws.cell(row, 1, "TOTAL").font = Font(bold=True)
    ws.cell(row, 3, f"=SUM(C4:C{row-1})").font = Font(bold=True)

    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 16
    ws.column_dimensions['C'].width = 16
    ws.column_dimensions['D'].width = 14

    # ===== HOJA 2: Materiales =====
    ws = wb.create_sheet("Materiales", 1)
    ws['A1'] = "ORIGEN ESENCIAL - MATERIALES Y COSTOS (Estructura Aura)"
    ws['A1'].font = Font(bold=True, size=12)

    headers = ["Item", "Descripción", "Unidad", "Cantidad Origen", "Precio Unitario ARS", "Subtotal ARS", "USD"]
    for col, header in enumerate(headers, 1):
        ws.cell(3, col, header).font = Font(bold=True)
        ws.cell(3, col).fill = PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid")

    row = 4
    item_count = 0
    for item_num, item in enumerate(items_aura, 1):
        if item["cant_origen"] > 0:
            ws.cell(row, 1, item_num)
            ws.cell(row, 2, item["desc"])
            ws.cell(row, 3, item["unit"])
            ws.cell(row, 4, item["cant_origen"])
            ws.cell(row, 5, item["precio"])
            ws.cell(row, 6, f"=D{row}*E{row}")
            ws.cell(row, 7, f"=ROUND(F{row}/{DOLAR}, 2)")
            row += 1
            item_count += 1

    # Totales
    total_row = row
    ws.cell(total_row, 1, "TOTAL").font = Font(bold=True)
    ws.cell(total_row, 6, f"=SUM(F4:F{total_row-1})").font = Font(bold=True)
    ws.cell(total_row, 7, f"=ROUND(F{total_row}/{DOLAR}, 2)").font = Font(bold=True)

    for col in range(1, 8):
        ws.cell(total_row, col).fill = PatternFill(start_color="FFFF99", end_color="FFFF99", fill_type="solid")

    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 45
    ws.column_dimensions['C'].width = 10
    ws.column_dimensions['D'].width = 14
    ws.column_dimensions['E'].width = 18
    ws.column_dimensions['F'].width = 18
    ws.column_dimensions['G'].width = 14

    # ===== HOJA 3: Totales =====
    ws = wb.create_sheet("Totales", 2)
    ws['A1'] = "ORIGEN ESENCIAL - RESUMEN DE COSTOS"
    ws['A1'].font = Font(bold=True, size=12)

    ws['A3'] = "TOTAL MATERIALES"
    ws['B3'] = f"=Materiales!F{total_row}"
    ws['C3'] = f"=Materiales!G{total_row}"

    ws['A3'].font = Font(bold=True, size=11)
    ws['B3'].font = Font(bold=True, size=11)
    ws['C3'].font = Font(bold=True, size=11)

    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 18

    wb.save(output_file)
    print(f"✓ Presupuesto generado: {output_file}")
    print(f"  - {len(locales)} locales")
    print(f"  - {item_count} items de materiales (de {len(items_aura)} totales de Aura)")
    omitidos = [i["desc"] for i in items_aura if i["cant_origen"] == 0]
    if omitidos:
        print(f"  ! {len(omitidos)} items quedaron en cantidad 0 y NO están en el presupuesto (revisar si corresponde):")
        for d in omitidos:
            print(f"      - {d}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de presupuestos Origen+Aura")
    parser.add_argument("--origen", required=True, help="Archivo ORIGEN_COMPUTO.xlsx")
    parser.add_argument("--aura", required=True, help="Archivo Aura_Costo.xlsx")
    parser.add_argument("--output", required=True, help="Archivo output presupuesto.xlsx")

    args = parser.parse_args()
    generar_presupuesto(args.origen, args.aura, args.output)
