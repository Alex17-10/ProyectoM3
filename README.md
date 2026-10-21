# DataVision Analytics — TechCore

## Descripción del proyecto

Como parte del proceso de selección para el rol de Analista de Datos Junior, DataVision Analytics ha asignado al candidato la primera fase del proyecto para TechCore, una cadena de tiendas minoristas especializada en la venta y distribución de computadores y accesorios tecnológicos.

En esta fase, el candidato debe importar la base de datos original de facturas en Power BI Desktop y realizar un proceso completo de transformación y estandarización utilizando Power Query.

El primer paso consiste en uniformar los nombres de las columnas (por ejemplo, cambiar Prod_Name a ProductoNombre) y asegurarse de que cada campo tenga el tipo de dato correcto: las fechas deben convertirse al formato Date, los precios a Decimal Number, y los identificadores a Text.

Luego, es necesario detectar y tratar valores nulos, duplicados o inconsistentes. Los registros de facturas exactamente iguales deben eliminarse, y los valores faltantes deben reemplazarse según su naturaleza: si el campo MétodoPago está vacío, se completará con “No especificado”, mientras que los valores numéricos nulos se imputarán con cero cuando sea pertinente.

El proceso también incluye la normalización de categorías y campos textuales para evitar variaciones que dificulten el análisis.

## Objetivos

- Preparar los datos para su análisis.
- Corregir inconsistencias presentes en la información.
- Estructurar los datos de manera adecuada para el análisis.
- Generar una fuente de datos organizada para Power BI.
- Facilitar el análisis de las ventas, clientes, productos y demás entidades relacionadas.
- Desarrollar una base estructurada que permitiera posteriormente construir un dashboard interactivo.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Tabulate
- SQLite
- Microsoft Excel
- Power BI Desktop
- DAX

## Datos de origen y limpieza

El dataset original contenía 30.000 registros y 30 columnas con información relacionada con ventas, clientes, productos, vendedores, ciudades, sucursales, fechas, cantidades, precios, descuentos y valores de las transacciones.

La información se encontraba inicialmente en una estructura plana, donde los datos correspondientes a diferentes entidades aparecían dentro de los mismos registros de venta. Para poder utilizar la información de manera adecuada, primero se realizó una revisión general de la calidad de los datos y posteriormente se preparó la información para su estructuración.

Durante esta etapa se revisaron y corrigieron diferentes tipos de inconsistencias, entre ellas:

- Tipos de datos incorrectos.
- Valores nulos.
- Registros duplicados.
- Inconsistencias en campos numéricos.
- Diferencias de escritura en campos de texto.
- Nombres de productos y marcas.
- Nombres de ciudades y sucursales.
- Mayúsculas y minúsculas.
- Acentos.
- Espacios innecesarios.
- Formatos de fechas y horas.

Entre las principales correcciones se normalizaron ciudades como:

```
cali → Cali
pereira → Pereira
Bogota → Bogotá
bogota → Bogotá
Medellin → Medellín
medellin → Medellín
```

También se estandarizaron marcas con errores de escritura, por ejemplo:

```
Aple → Apple
Samsng → Samsung
Lenvo → Lenovo
Acr → Acer
Azus → Asus
Del → Dell
HPP → HP
```

También se encontraron diferencias en los nombres de sucursales, ocasionadas por variaciones en mayúsculas, acentos y espacios, que fueron corregidas para evitar que una misma entidad apareciera como diferentes registros durante el análisis.

Como parte de la preparación temporal, se incorporaron dos campos adicionales relacionados con la fecha y el año, necesarios para facilitar posteriormente el análisis cronológico en Power BI.

La preparación de los datos no se limitó a una única herramienta. Después de la preparación inicial, también se realizaron ajustes adicionales en Power Query dentro de Power BI cuando fue necesario corregir formatos o tipos de datos para que determinados campos pudieran utilizarse correctamente.

## Python

Una vez preparados los datos, Python se utilizó principalmente para organizar y estructurar la información, no para reemplazar el proceso de limpieza realizado previamente.

El código tomó el dataset preparado y permitió separar la información en una estructura organizada para representar las diferentes entidades del negocio, evitando mantener toda la información repetida dentro de una única tabla plana.

Mediante este proceso se preparó la información necesaria para representar clientes, ciudades, vendedores, productos y transacciones, además de organizar la información correspondiente a las facturas y sus respectivos detalles.

Python también permitió generar identificadores para relacionar las diferentes entidades y preparar una estructura que pudiera ser utilizada posteriormente como fuente de datos en Power BI.

Otro propósito importante del código fue automatizar la generación de la fuente de datos final, evitando tener que construir manualmente las diferentes tablas cada vez que se necesitara reproducir el modelo.

Las principales herramientas utilizadas fueron:

- pandas para manipulación y transformación de datos.
- numpy para operaciones numéricas.
- tabulate para presentar resultados de las tablas durante la ejecución.
- sqlite3 para generar una copia del modelo en una base de datos SQLite.

Como resultado del proceso de preparación y estructuración se generó el archivo:

**modeloVentas.xlsx**

El archivo modeloVentas.xlsx estaba compuesto por siete tablas principales, organizadas para representar las diferentes entidades del modelo: Clientes, Ciudades, Facturas, DetalleFacturas, Productos, Sucursales y Vendedores. La tabla Clientes contenía la información e identificación de los clientes; Ciudades almacenaba el identificador y nombre de cada ciudad; Facturas contenía la información general de cada venta, como factura, cliente, fecha, hora y vendedor; DetalleFacturas registraba los productos asociados a cada factura, junto con cantidad, precio unitario, subtotal y descuento; Productos contenía el identificador, nombre, marca y precio de los productos; Sucursales relacionaba cada sucursal con su ciudad; y Vendedores contenía el identificador y nombre de los vendedores. Esta organización permitió llevar la información desde una estructura de ventas plana hacia un modelo relacionado que pudiera ser utilizado correctamente en Power BI.

> **[Imagen del PDF: diagrama del modelo relacional en Power BI, con las tablas Ciudades, Sucursales, Facturas, Vendedores, DetalleFacturas, Productos y Clientes y sus relaciones.]**

## Modelo entidad-relación

Después de preparar los datos, la información se organizó en un modelo relacional dentro de Power BI. El modelo conecta las diferentes entidades mediante identificadores, permitiendo relacionar la información geográfica, comercial, de clientes, vendedores y productos con las transacciones realizadas.

La tabla de ciudades se relaciona con las sucursales, permitiendo asociar cada punto de venta con su respectiva ciudad. Las sucursales se relacionan con las facturas, mientras que las facturas contienen la información general de cada transacción y se relacionan con los clientes y vendedores correspondientes.

Cada factura puede contener uno o varios registros en la tabla de detalle de facturas. Esta tabla almacena la información específica de los productos vendidos, incluyendo cantidad, precio unitario, subtotal y descuento. A su vez, cada registro de detalle se relaciona con la tabla de productos, que contiene la información descriptiva de cada producto.

Esta estructura permite separar la información descriptiva de la información transaccional, reducir la repetición de datos y facilitar el análisis mediante las relaciones establecidas entre las diferentes entidades.

> **[Imagen del PDF: captura del dashboard "DASHBOARD DE VENTAS | TECHCORE – Resumen ejecutivo de desempeño comercial", con filtros de Ciudad, Marca, Año/Mes/Fecha y Edad; tarjetas de Ventas Totales (COP 468.03bn), Ticket Promedio (COP 15.60M) y Productos Vendidos (COP 90.01K); gráficos de evolución mensual, ventas por marca, ventas por ciudad (mapa) y ventas por año; tabla por ciudad (Medellín, Bogotá, Pereira, Cali) y sección de insights: "Medellín lidera las ventas con 44.68% del total", "Medellín y Bogotá concentran el 75.25% de las ventas", "Lenovo es la marca con mayor volumen de ventas".]**

## Dashboard final

El dashboard fue diseñado como un panel ejecutivo para facilitar la consulta y el análisis del desempeño comercial de TechCore. Se organizó mediante una estructura visual clara, con los principales indicadores en la parte superior y las herramientas de filtrado disponibles para modificar dinámicamente la información mostrada.

Se incorporaron tarjetas con los indicadores de Ventas Totales, Ticket Promedio y Productos Vendidos, proporcionando una vista rápida de los principales resultados del modo.

El análisis visual incluye la evolución mensual de las ventas, el comportamiento de las ventas por marca, la distribución geográfica mediante un mapa por ciudad, y la comparación de ventas por año. También se incorporó una tabla de desempeño por ciudad que reúne ventas totales, participación porcentual, productos vendidos y ticket promedio.

El dashboard cuenta con segmentadores para Ciudad, Marca, Año/Mes/Fecha y Edad, permitiendo filtrar los diferentes elementos de forma interactiva.

Para el análisis de edad se utilizaron rangos de cinco años, comenzando en 15–19 años, seguido de 20–24, 25–29 y así sucesivamente. Esta agrupación facilita la segmentación de los clientes sin presentar una cantidad excesiva de categorías individuales.

Finalmente, se incorporó una sección de insights para presentar de forma resumida los principales hallazgos obtenidos a partir del análisis. El diseño utiliza una distribución organizada, tarjetas independientes, bordes redondeados, colores diferenciados para los indicadores y espacios definidos entre los elementos, buscando mantener una presentación clara y orientada al análisis empresarial.

## Conclusión

El proyecto permitió convertir información comercial en una herramienta de análisis orientada a facilitar la interpretación y toma de decisiones. La solución final integra diferentes perspectivas del negocio en un entorno interactivo, permitiendo explorar los resultados de forma dinámica según distintos criterios.

La organización de los indicadores y visualizaciones facilita una lectura rápida del desempeño y permite profundizar en los datos cuando sea necesario. De esta manera, el resultado final combina claridad, interactividad y utilidad analítica, proporcionando una base sólida para apoyar futuros análisis y procesos de Business Intelligence en TechCore.
