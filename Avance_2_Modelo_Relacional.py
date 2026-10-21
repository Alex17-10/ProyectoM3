# Avance 2 - Modelo Relacional
# DataVision Analytics - TechCore

import os
import sqlite3
import pandas as pd
from IPython.display import display
from tabulate import tabulate

pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

# Cargar dataset

ruta=os.path.dirname(os.path.abspath(__file__))
archivo=os.path.join(ruta,"VentasTransformado.csv")

ventas=pd.read_csv(archivo)

# Conversión de tipos

ventas["FechaVenta"]=pd.to_datetime(
    ventas["FechaVenta"],
    errors="coerce"
)

ventas["HoraVenta"]=pd.to_datetime(
    ventas["HoraVenta"],
    errors="coerce"
).dt.time

# Validación inicial

print("="*80)
print("      AVANCE 2 - MODELO RELACIONAL")
print("      DataVision Analytics - TechCore")
print("="*80)

print("\nArchivo cargado correctamente")
print(f"Archivo   : {os.path.basename(archivo)}")
print(f"Filas     : {ventas.shape[0]:,}")
print(f"Columnas  : {ventas.shape[1]}")
print(f"Duplicados: {ventas.duplicated().sum()}")
print("="*80)

# Ordenar por VentaID

ventas=ventas.sort_values("VentaID").reset_index(drop=True)

# Crear tabla Clientes

clientes=(
    ventas[
        [
            "ClienteNombre",
            "GeneroCliente",
            "EdadCliente",
            "TelefonoCliente",
            "EmailCliente",
            "DireccionCliente"
        ]
    ]
    .drop_duplicates()
    .reset_index(drop=True)
)

clientes.insert(
    0,
    "ClienteID",
    range(1,len(clientes)+1)
)

print(f"\nClientes creados: {len(clientes)}")
print(tabulate(
    clientes.head(10),
    headers="keys",
    tablefmt="grid",
    showindex=False
))

# Crear tabla Ciudades

ciudades=(
    ventas[
        [
            "CiudadSucursal"
        ]
    ]
    .drop_duplicates()
    .sort_values("CiudadSucursal")
    .reset_index(drop=True)
)

ciudades.columns=["NombreCiudad"]

ciudades.insert(
    0,
    "CiudadID",
    range(1,len(ciudades)+1)
)

print("\n"+"="*80)
print("TABLA CIUDADES")
print("="*80)

print(tabulate(
    ciudades,
    headers="keys",
    tablefmt="grid",
    showindex=False
))

print(f"\nTotal de registros: {len(ciudades):,}")

# Crear tabla Sucursales

sucursales=(
    ventas[
        [
            "SucursalNombre",
            "CiudadSucursal"
        ]
    ]
    .drop_duplicates()
    .reset_index(drop=True)
)

sucursales=sucursales.merge(
    ciudades,
    left_on="CiudadSucursal",
    right_on="NombreCiudad",
    how="left"
)

sucursales=sucursales[
    [
        "SucursalNombre",
        "CiudadID"
    ]
]

sucursales=sucursales.drop_duplicates(
    subset="SucursalNombre"
).reset_index(drop=True)

sucursales.insert(
    0,
    "SucursalID",
    range(1,len(sucursales)+1)
)

print("\n"+"="*80)
print("TABLA SUCURSALES")
print("="*80)

print(tabulate(
    sucursales,
    headers="keys",
    tablefmt="grid",
    showindex=False
))

print(f"\nTotal de registros: {len(sucursales):,}")

# Crear tabla Vendedores

vendedores=(
    ventas[
        [
            "VendedorNombre"
        ]
    ]
    .drop_duplicates()
    .sort_values("VendedorNombre")
    .reset_index(drop=True)
)

vendedores.insert(
    0,
    "VendedorID",
    range(1,len(vendedores)+1)
)

print("\n"+"="*80)
print("TABLA VENDEDORES")
print("="*80)

print(tabulate(
    vendedores,
    headers="keys",
    tablefmt="grid",
    showindex=False
))

print(f"\nTotal de registros: {len(vendedores):,}")

# Crear tabla Productos

productos1=(
    ventas[
        [
            "NombreProducto1",
            "MarcaProducto1",
            "PrecioUnitarioProducto1"
        ]
    ]
    .rename(columns={
        "NombreProducto1":"Nombre",
        "MarcaProducto1":"Marca",
        "PrecioUnitarioProducto1":"Precio"
    })
)

productos2=(
    ventas[
        [
            "NombreProducto2",
            "MarcaProducto2",
            "PrecioUnitarioProducto2"
        ]
    ]
    .rename(columns={
        "NombreProducto2":"Nombre",
        "MarcaProducto2":"Marca",
        "PrecioUnitarioProducto2":"Precio"
    })
)

productos3=(
    ventas[
        [
            "NombreProducto3",
            "MarcaProducto3",
            "PrecioUnitarioProducto3"
        ]
    ]
    .rename(columns={
        "NombreProducto3":"Nombre",
        "MarcaProducto3":"Marca",
        "PrecioUnitarioProducto3":"Precio"
    })
)

productos=pd.concat(
    [
        productos1,
        productos2,
        productos3
    ],
    ignore_index=True
)

productos=productos[
    productos["Nombre"]!="No especificado"
]

productos=(
    productos
    .drop_duplicates()
    .sort_values(
        [
            "Marca",
            "Nombre"
        ]
    )
    .reset_index(drop=True)
)

productos.insert(
    0,
    "ProductoID",
    range(1,len(productos)+1)
)

print("\n"+"="*80)
print("TABLA PRODUCTOS")
print("="*80)

print(tabulate(
    productos.head(15),
    headers="keys",
    tablefmt="grid",
    showindex=False
))

print("\n...")

print(f"\nTotal de registros: {len(productos):,}")

# Resumen de dimensiones

print("\nDimensiones creadas")

print(f"Clientes   : {len(clientes)}")
print(f"Ciudades   : {len(ciudades)}")
print(f"Sucursales : {len(sucursales)}")
print(f"Vendedores : {len(vendedores)}")
print(f"Productos  : {len(productos)}")

# Crear tabla Facturas

facturas=ventas[
    [
        "VentaID",
        "FechaVenta",
        "HoraVenta",
        "Año",
        "Mes",
        "SucursalNombre",
        "ClienteNombre",
        "GeneroCliente",
        "EdadCliente",
        "TelefonoCliente",
        "EmailCliente",
        "DireccionCliente",
        "VendedorNombre"
    ]
].copy()

facturas=facturas.merge(
    clientes,
    on=[
        "ClienteNombre",
        "GeneroCliente",
        "EdadCliente",
        "TelefonoCliente",
        "EmailCliente",
        "DireccionCliente"
    ],
    how="left"
)

facturas=facturas.merge(
    sucursales,
    on="SucursalNombre",
    how="left"
)

facturas=facturas.merge(
    vendedores,
    on="VendedorNombre",
    how="left"
)

facturas=facturas[
    [
        "VentaID",
        "FechaVenta",
        "HoraVenta",
        "Año",
        "Mes",
        "SucursalID",
        "ClienteID",
        "VendedorID"
    ]
].drop_duplicates()

facturas=facturas.rename(columns={
    "VentaID":"FacturaID",
    "FechaVenta":"Fecha",
    "HoraVenta":"Hora"
})

print("\n"+"="*80)
print("TABLA FACTURAS")
print("="*80)

print(tabulate(
    facturas.head(15),
    headers="keys",
    tablefmt="grid",
    showindex=False
))

print("\n...")

print(f"\nTotal de registros: {len(facturas):,}")

# Crear DetalleFacturas

detalle1=ventas[
    [
        "VentaID",
        "NombreProducto1",
        "MarcaProducto1",
        "CantidadProducto1",
        "PrecioUnitarioProducto1",
        "SubtotalProducto1",
        "DescuentoVenta"
    ]
].rename(columns={
    "VentaID":"FacturaID",
    "NombreProducto1":"Nombre",
    "MarcaProducto1":"Marca",
    "CantidadProducto1":"Cantidad",
    "PrecioUnitarioProducto1":"PrecioUnitario",
    "SubtotalProducto1":"Subtotal",
    "DescuentoVenta":"Descuento"
})

detalle2=ventas[
    [
        "VentaID",
        "NombreProducto2",
        "MarcaProducto2",
        "CantidadProducto2",
        "PrecioUnitarioProducto2",
        "SubtotalProducto2",
        "DescuentoVenta"
    ]
].rename(columns={
    "VentaID":"FacturaID",
    "NombreProducto2":"Nombre",
    "MarcaProducto2":"Marca",
    "CantidadProducto2":"Cantidad",
    "PrecioUnitarioProducto2":"PrecioUnitario",
    "SubtotalProducto2":"Subtotal",
    "DescuentoVenta":"Descuento"
})

detalle3=ventas[
    [
        "VentaID",
        "NombreProducto3",
        "MarcaProducto3",
        "CantidadProducto3",
        "PrecioUnitarioProducto3",
        "SubtotalProducto3",
        "DescuentoVenta"
    ]
].rename(columns={
    "VentaID":"FacturaID",
    "NombreProducto3":"Nombre",
    "MarcaProducto3":"Marca",
    "CantidadProducto3":"Cantidad",
    "PrecioUnitarioProducto3":"PrecioUnitario",
    "SubtotalProducto3":"Subtotal",
    "DescuentoVenta":"Descuento"
})

detalleFacturas=pd.concat(
    [
        detalle1,
        detalle2,
        detalle3
    ],
    ignore_index=True
)

detalleFacturas=detalleFacturas[
    detalleFacturas["Nombre"]!="No especificado"
]

detalleFacturas=detalleFacturas.merge(
    productos,
    on=[
        "Nombre",
        "Marca"
    ],
    how="left"
)

detalleFacturas=detalleFacturas[
    [
        "FacturaID",
        "ProductoID",
        "Cantidad",
        "PrecioUnitario",
        "Subtotal",
        "Descuento"
    ]
]

detalleFacturas.insert(
    0,
    "DetalleID",
    range(1,len(detalleFacturas)+1)
)

detalleFacturas=detalleFacturas.sort_values(
    [
        "FacturaID",
        "DetalleID"
    ]
).reset_index(drop=True)

print("TABLA DETALLE FACTURAS")
print("="*80)

print(tabulate(
    detalleFacturas.head(15),
    headers="keys",
    tablefmt="grid",
    showindex=False
))

print("\n...")

print(f"\nTotal de registros: {len(detalleFacturas):,}")

# Validación de integridad referencial

print("\nValidando integridad referencial...\n")

errores=[]

if not detalleFacturas["FacturaID"].isin(facturas["FacturaID"]).all():
    errores.append("Existen FacturaID sin correspondencia en Facturas.")

if not detalleFacturas["ProductoID"].isin(productos["ProductoID"]).all():
    errores.append("Existen ProductoID sin correspondencia en Productos.")

if not facturas["ClienteID"].isin(clientes["ClienteID"]).all():
    errores.append("Existen ClienteID inválidos.")

if not facturas["SucursalID"].isin(sucursales["SucursalID"]).all():
    errores.append("Existen SucursalID inválidos.")

if not facturas["VendedorID"].isin(vendedores["VendedorID"]).all():
    errores.append("Existen VendedorID inválidos.")

if facturas["FacturaID"].duplicated().any():
    errores.append("FacturaID duplicado.")

if detalleFacturas["DetalleID"].duplicated().any():
    errores.append("DetalleID duplicado.")

if productos["ProductoID"].duplicated().any():
    errores.append("ProductoID duplicado.")

if clientes["ClienteID"].duplicated().any():
    errores.append("ClienteID duplicado.")

if len(errores)==0:
    print("Integridad referencial validada correctamente.")
else:
    print("Se encontraron inconsistencias:\n")
    for error in errores:
        print("-",error)

# Reporte 1
# Total de ventas por marca

ventasMarca=(
    detalleFacturas
    .merge(
        productos,
        on="ProductoID",
        how="left"
    )
    .groupby(
        "Marca",
        as_index=False
    )["Subtotal"]
    .sum()
    .sort_values(
        "Subtotal",
        ascending=False
    )
)

print("\nTotal de ventas por marca")

display(ventasMarca)

# Reporte 2
# Top 10 productos más vendidos

topProductos=(
    detalleFacturas
    .merge(
        productos,
        on="ProductoID",
        how="left"
    )
    .groupby(
        "Nombre",
        as_index=False
    )["Cantidad"]
    .sum()
    .sort_values(
        "Cantidad",
        ascending=False
    )
    .head(10)
)

print("\nTop 10 productos más vendidos")

display(topProductos)

# Estadísticas generales

print("\n"+"="*80)
print("RESUMEN DEL MODELO RELACIONAL")
print("="*80)

print(f"{'Clientes':<20}{len(clientes):>10,}")
print(f"{'Ciudades':<20}{len(ciudades):>10,}")
print(f"{'Sucursales':<20}{len(sucursales):>10,}")
print(f"{'Vendedores':<20}{len(vendedores):>10,}")
print(f"{'Productos':<20}{len(productos):>10,}")
print(f"{'Facturas':<20}{len(facturas):>10,}")
print(f"{'DetalleFacturas':<20}{len(detalleFacturas):>10,}")

# Exportar modelo relacional a Excel

archivo_excel=os.path.join(ruta,"modeloVentas.xlsx")

with pd.ExcelWriter(
    archivo_excel,
    engine="openpyxl"
) as writer:

    clientes.to_excel(
        writer,
        sheet_name="Clientes",
        index=False
    )

    ciudades.to_excel(
        writer,
        sheet_name="Ciudades",
        index=False
    )

    sucursales.to_excel(
        writer,
        sheet_name="Sucursales",
        index=False
    )

    vendedores.to_excel(
        writer,
        sheet_name="Vendedores",
        index=False
    )

    productos.to_excel(
        writer,
        sheet_name="Productos",
        index=False
    )

    facturas.to_excel(
        writer,
        sheet_name="Facturas",
        index=False
    )

    detalleFacturas.to_excel(
        writer,
        sheet_name="DetalleFacturas",
        index=False
    )

# Base de datos SQLite (Opcional)

archivo_db=os.path.join(ruta,"modeloVentas.db")

conexion=sqlite3.connect(archivo_db)

clientes.to_sql(
    "Clientes",
    conexion,
    if_exists="replace",
    index=False
)

ciudades.to_sql(
    "Ciudades",
    conexion,
    if_exists="replace",
    index=False
)

sucursales.to_sql(
    "Sucursales",
    conexion,
    if_exists="replace",
    index=False
)

vendedores.to_sql(
    "Vendedores",
    conexion,
    if_exists="replace",
    index=False
)

productos.to_sql(
    "Productos",
    conexion,
    if_exists="replace",
    index=False
)

facturas.to_sql(
    "Facturas",
    conexion,
    if_exists="replace",
    index=False
)

detalleFacturas.to_sql(
    "DetalleFacturas",
    conexion,
    if_exists="replace",
    index=False
)

conexion.close()

print("\n"+"="*80)
print("EXPORTACIÓN DEL MODELO")
print("="*80)

if os.path.exists(archivo_excel):
    print("✓ modeloVentas.xlsx generado correctamente.")
else:
    print("✗ Error al generar modeloVentas.xlsx.")

if os.path.exists(archivo_db):
    print("✓ modeloVentas.db generado correctamente.")
else:
    print("✗ Error al generar modeloVentas.db.")

print("\nArchivos generados")

print(f"Excel  : {archivo_excel}")
print(f"SQLite : {archivo_db}")

print("\nModelo relacional listo para Power BI.")

print("="*80)

print("\n" + "="*80)