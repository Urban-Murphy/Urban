#!/usr/bin/env python3
"""
Generador automático de presupuestos: Origen + Aura
Uso: python3 generar_presupuesto.py --origen archivo.xlsx --aura aura.xlsx --output presupuesto.xlsx
"""

import argparse
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill
from pathlib import Path

def leer_origen(archivo):
    """Extrae PerimySup y especificaciones de Origen"""
    df = pd.read_excel(archivo, sheet_name='PerimySup', header=None)

    # Locales: filas 3-7, columnas B-D
    locales = []
    for i in range(3, 8):
        nombre = df.iloc[i, 1]
        if pd.notna(nombre):
            locales.append({
                "nombre": nombre,
                "perim": df.iloc[i, 2],
                "sup": df.iloc[i, 3],
                "alt": df.iloc[i, 4]
            })

    # Totales de materiales: fila 8
    materiales = {
        "durlock": df.iloc[8, 6],
        "impermeables": df.iloc[8, 7],
        "pisos": df.iloc[8, 8],
        "revestimiento": df.iloc[8, 9],
        "zocalo": df.iloc[8, 10],
        "siding": df.iloc[8, 11],
        "pintura_muros": df.iloc[8, 12],
        "pintura_cielo": df.iloc[8, 13],
    }

    return locales, materiales

def leer_aura(archivo):
    """Extrae precios unitarios de Aura"""
    df = pd.read_excel(archivo, sheet_name='Materiales', header=None)

    precios = {}
    for i in range(5, min(len(df), 50)):
        desc = str(df.iloc[i, 1]).lower()
        precio = df.iloc[i, 4]

        if pd.notna(precio) and precio > 0:
            # Mapear descripciones genéricas
            if "roca" in desc and "standard" in desc:
                precios["durlock"] = precio
            elif "siding" in desc:
                precios["siding"] = precio
            elif "porcelana" in desc:
                precios["pisos"] = precio
            elif "pintura" in desc:
                precios["pintura"] = precio

    return precios

def generar_presupuesto(origen_file, aura_file, output_file):
    """Genera presupuesto en Excel"""
    locales, mat_origen = leer_origen(origen_file)
    precios = leer_aura(aura_file)

    # Valores por defecto si faltan
    precios.setdefault("durlock", 7273)
    precios.setdefault("siding", 18055)
    precios.setdefault("pisos", 5000)
    precios.setdefault("pintura", 2500)
    precios.setdefault("zocalo", 1000)

    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # ===== HOJA 1: PerimySup =====
    ws = wb.create_sheet("PerimySup", 0)
    ws['A1'] = "PERIMETROS Y SUPERFICIES"
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
    ws['A1'] = "MATERIALES Y COSTOS"
    ws['A1'].font = Font(bold=True, size=12)

    headers = ["Item", "Descripción", "Unidad", "Cantidad", "P.U. ARS", "Subtotal ARS", "USD"]
    for col, header in enumerate(headers, 1):
        ws.cell(3, col, header).font = Font(bold=True)
        ws.cell(3, col).fill = PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid")

    items = [
        ("Placa Roca Yeso (Durlock)", "m2", mat_origen.get("durlock", 0), precios.get("durlock", 7273)),
        ("Pisos", "m2", mat_origen.get("pisos", 0), precios.get("pisos", 5000)),
        ("Revestimiento", "m2", mat_origen.get("revestimiento", 0), precios.get("durlock", 7273)),
        ("Zócalos", "ml", mat_origen.get("zocalo", 0), precios.get("zocalo", 1000)),
        ("Siding Exterior", "m2", mat_origen.get("siding", 0), precios.get("siding", 18055)),
        ("Pintura", "m2", mat_origen.get("pintura_muros", 0), precios.get("pintura", 2500)),
    ]

    row = 4
    for item_num, (desc, unit, cant, precio) in enumerate(items, 1):
        ws.cell(row, 1, item_num)
        ws.cell(row, 2, desc)
        ws.cell(row, 3, unit)
        ws.cell(row, 4, cant)
        ws.cell(row, 5, precio)
        ws.cell(row, 6, f"=D{row}*E{row}")
        ws.cell(row, 7, f"=ROUND(F{row}/1550,2)")
        row += 1

    ws.cell(row, 1, "TOTAL").font = Font(bold=True)
    ws.cell(row, 6, f"=SUM(F4:F{row-1})").font = Font(bold=True)
    ws.cell(row, 7, f"=ROUND(F{row}/1550,2)").font = Font(bold=True)

    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 30
    ws.column_dimensions['C'].width = 10
    ws.column_dimensions['D'].width = 12
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 12

    wb.save(output_file)
    print(f"✓ Presupuesto generado: {output_file}")
    print(f"  - {len(locales)} locales")
    print(f"  - {len(items)} items de materiales")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de presupuestos Origen+Aura")
    parser.add_argument("--origen", required=True, help="Archivo ORIGEN_COMPUTO.xlsx")
    parser.add_argument("--aura", required=True, help="Archivo Aura_Costo.xlsx")
    parser.add_argument("--output", required=True, help="Archivo output presupuesto.xlsx")

    args = parser.parse_args()
    generar_presupuesto(args.origen, args.aura, args.output)
