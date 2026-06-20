productos = [
    {"nombre": "Café molido", "stock_actual": 4, "stock_minimo": 10},
    {"nombre": "Leche sin lactosa", "stock_actual": 15, "stock_minimo": 8},
    {"nombre": "Servilletas", "stock_actual": 2, "stock_minimo": 5},
    {"nombre": "Vasos takeaway", "stock_actual": 20, "stock_minimo": 12},
]

print("REVISIÓN DE STOCK")
print("-----------------")

for producto in productos:
    nombre = producto["nombre"]
    stock_actual = producto["stock_actual"]
    stock_minimo = producto["stock_minimo"]

    if stock_actual < stock_minimo:
        unidades_faltantes = stock_minimo - stock_actual
        print(f"ALERTA: {nombre} está bajo de stock. Faltan {unidades_faltantes} unidades.")
    else:
        print(f"OK: {nombre} tiene stock suficiente.")