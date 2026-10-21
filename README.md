# DataVision Analytics — TechCore

## Descripción del proyecto
Como parte del proceso de selección para el rol de Analista de Datos Junior, DataVision Analytics ha asignado al candidato la primera fase del proyecto para TechCore, una cadena de tiendas minoristas especializada en la venta y distribución de computadores y accesorios tecnológicos [0.1.1].

En esta fase, el candidato debe importar la base de datos original de facturas en Power BI Desktop y realizar un proceso completo de transformación y estandarización utilizando Power Query [0.1.1].

El primer paso consiste en uniformar los nombres de las columnas (por ejemplo, cambiar `Prod_Name` a `ProductoNombre`) y asegurarse de que cada campo tenga el tipo de dato correcto: las fechas deben convertirse al formato *Date*, los precios a *Decimal Number*, y los identificadores a *Text* [0.1.1].

Luego, es necesario detectar y tratar valores nulos, duplicados o inconsistentes [0.1.1]. Los registros de facturas exactamente iguales deben eliminarse, y los valores faltantes deben reemplazarse según su naturaleza: si el campo `MétodoPago` está vacío, se completará con “No especificado”, mientras que los valores numéricos nulos se imputarán con cero cuando sea pertinente [0.1.1].

El proceso también incluye la normalización de categorías y campos textuales para evitar variaciones que dificulten el análisis [0.1.1].

## Objetivos
* Preparar los datos para su análisis [0.1.1].
* Corregir inconsistencias presentes en la información [0.1.1].
* Estructurar los datos de manera adecuada para el análisis [0.1.1].
* Generar una fuente de datos organizada para Power BI [0.1.1].
* Facilitar el análisis de las ventas, clientes, productos y demás entidades relacionadas [0.1.1].
* Desarrollar una base estructurada que permitiera posteriormente construir un dashboard interactivo [0.1.1].

## Tecnologías utilizadas
* Python [0.1.2]
* Pandas [0.1.2]
* NumPy [0.1.2]
* Tabulate [0.1.2]
* SQLite [0.1.2]
* Microsoft Excel [0.1.2]
* Power BI Desktop [0.1.2]
* DAX [0.1.2]

## Datos de origen y limpieza
El dataset original contenía 30.000 registros y 30 columnas con información relacionada con ventas, clientes, productos, vendedores, ciudades, sucursales, fechas, cantidades, precios, descuentos y valores de las transacciones [0.1.2].

La información se encontraba inicialmente en una estructura plana, donde los datos correspondientes a diferentes entidades aparecían dentro de los mismos registros de venta [0.1.2]. Para poder utilizar la información de manera adecuada, primero se realizó una revisión general de la calidad de los datos y posteriormente se preparó la información para su estructuración [0.1.2].

Durante esta etapa se revisaron y corrigieron diferentes tipos de inconsistencias, entre ellas:
* Tipos de datos incorrectos [0.1.2].
* Valores nulos [0.1.2].
* Registros duplicados [0.1.2].
* Inconsistencias en campos numéricos [0.1.2].
* Diferencias de escritura en campos de texto [0.1.2].
* Nombres de productos y marcas [0.1.2].
* Nombres de ciudades y sucursales [0.1.2].
* Mayúsculas y minúsculas [0.1.2].
* Acentos [0.1.2].
* Espacios innecesarios [0.1.2].
* Formatos de fechas y horas [0.1.2].

### Normalización de datos

Entre las principales correcciones se normalizaron ciudades como:
* `cali` → Cali [0.1.3]
* `pereira` → Pereira [0.1.3]
* `Bogota` → Bogotá [0.1.3]
* `bogota` → Bogotá [0.1.3]
* `Medellin` → Medellín [0.1.3]
* `medellin` → Medellín [0.1.3]

También se estandarizaron marcas con errores de escritura, por ejemplo:
* `Aple` → Apple [0.1.3]
* `Samsng` → Samsung [0.1.3]
* `Lenvo` → Lenovo [0.1.3]
* `Acr` → Acer [0.1.3]
* `Azus` → Asus [0.1.3]
* `Del` → Dell [0.1.3]
* `HPP` → HP [0.1.3]

También se encontraron diferencias en los nombres de sucursales, ocasionadas por variaciones en mayúsculas, acentos y espacios, que fueron corregidas para evitar que una misma entidad apareciera como diferentes registros durante el análisis [0.1.3].

Como parte de la preparación temporal, se incorporaron dos campos adicionales relacionados con la fecha y el año, necesarios para facilitar posteriormente el análisis cronológico en Power BI [0.1.3].

La preparación de los datos no se limitó a una única herramienta [0.1.3]. Después de la preparación inicial, también se realizaron ajustes adicionales en Power Query dentro de Power BI cuando fue necesario corregir formatos o tipos de datos para que determinados campos pudieran utilizarse correctamente [0.1.3].

## Python
Una vez preparados los datos, Python se utilizó principalmente para organizar y estructurar la información, no para reemplazar el proceso de limpieza realizado previamente [0.1.3].

El código tomó el dataset preparado y permitió separar la información en una estructura organizada para representar las diferentes entidades del negocio, evitando mantener toda la información repetida dentro de una única tabla plana [0.1.4].

Mediante este proceso se preparó la información necesaria para representar clientes, ciudades, vendedores, productos y transacciones, además de organizar la información correspondiente a las facturas y sus respectivos detalles [0.1.4].

Python también permitió generar identificadores para relacionar las diferentes entidades y preparar una estructura que pudiera ser utilizada posteriormente como fuente de datos en Power BI [0.1.4].

Otro propósito importante del código fue automatizar la generación de la fuente de datos final, evitando tener que construir manualmente las diferentes tablas cada vez que se necesitara reproducir el modelo [0.1.4].

Las principales herramientas utilizadas fueron:
* **pandas** para manipulación y transformación de datos [0.1.4].
* **numpy** para operaciones numéricas [0.1.4].
* **tabulate** para presentar resultados de las tablas durante la ejecución [0.1.4].
* **sqlite3** para generar una copia del modelo en una base de datos SQLite [0.1.4].

Como resultado del proceso de preparación y estructuración se generó el archivo: `modeloVentas.xlsx` [0.1.4]

El archivo `modeloVentas.xlsx` estaba compuesto por siete tablas principales, organizadas para representar las diferentes entidades del modelo [0.1.4]:
1. **Clientes:** Contenía la información e identificación de los clientes [0.1.4].
2. **Ciudades:** Almacenaba el identificador y nombre de cada ciudad [0.1.4].
3. **Facturas:** Contenía la información general de cada venta, como factura, cliente, fecha, hora y vendedor [0.1.4].
4. **DetalleFacturas:** Registraba los productos asociados a cada factura, junto con cantidad, precio unitario, subtotal y descuento [0.1.4].
5. **Productos:** Contenía el identificador, nombre, marca y precio de los productos [0.1.4].
6. **Sucursales:** Relacionaba cada sucursal con su ciudad [0.1.4].
7. **Vendedores:** Contenía el identificador y nombre de los vendedores [0.1.4].

Esta organización permitió llevar la información desde una estructura de ventas plana hacia un modelo relacionado que pudiera ser utilizado correctamente en Power BI [0.1.4].

## Modelo entidad-relación
Después de preparar los datos, la información se organizó en un modelo relacional dentro de Power BI [0.1.5]. El modelo conecta las diferentes entidades mediante identificadores, permitiendo relacionar la información geográfica, comercial, de clientes, vendedores y productos con las transacciones realizadas [0.1.5].

La tabla de ciudades se relaciona con las sucursales, permitiendo asociar cada punto de venta con su respectiva ciudad [0.1.5]. Las sucursales se relacionan con las facturas, mientras que las facturas contienen la información general de cada transacción y se relacionan con los clientes y vendedores correspondientes [0.1.5].

Cada factura puede contener uno o varios registros en la tabla de detalle de facturas [0.1.5]. Esta tabla almacena la información específica de los productos vendidos, incluyendo cantidad, precio unitario, subtotal y descuento [0.1.5]. A su vez, cada registro de detalle se relaciona con la tabla de productos, que contiene la información descriptiva de cada producto [0.1.5].

Esta estructura permite separar la información descriptiva de la información transaccional, reducir la repetición de datos y facilitar el análisis mediante las relaciones establecidas entre las diferentes entidades [0.1.5].

## Dashboard final
El dashboard fue diseñado como un panel ejecutivo para facilitar la consulta y el análisis del desempeño comercial de TechCore [0.1.6]. Se organizó mediante una estructura visual clara, con los principales indicadores en la parte superior y las herramientas de filtrado disponibles para modificar dinámicamente la información mostrada [0.1.6].

Se incorporaron tarjetas con los indicadores de **Ventas Totales**, **Ticket Promedio** y **Productos Vendidos**, proporcionando una vista rápida de los principales resultados del modo [0.1.6].

El análisis visual incluye la evolución mensual de las ventas, el comportamiento de las ventas por marca, la distribución geográfica mediante un mapa por ciudad, y la comparación de ventas por año [0.1.6]. También se incorporó una tabla de desempeño por ciudad que reúne ventas totales, participación porcentual, productos vendidos y ticket promedio [0.1.6].

El dashboard cuenta con segmentadores para Ciudad, Marca, Año/Mes/Fecha y Edad, permitiendo filtrar los diferentes elements de forma interactiva [0.1.6].

Para el análisis de edad se utilizaron rangos de cinco años, comenzando en 15–19 años, seguido de 20–24, 25–29 y así sucesivamente [0.1.6]. Esta agrupación facilita la segmentación de los clientes sin presentar una cantidad excesiva de categorías individuales [0.1.6].

Finalmente, se incorporó una sección de insights para presentar de forma resumida los principales hallazgos obtenidos a partir del análisis [0.1.7]. El diseño utiliza una distribución organizada, tarjetas independientes, bordes redondeados, colores diferenciados para los indicadores y espacios definidos entre los elementos, buscando mantener una presentación clara y orientada al análisis empresarial [0.1.7].

## Conclusión
El proyecto permitió convertir información comercial en una herramienta de análisis orientada a facilitar la interpretación y toma de decisiones [0.1.7]. La solución final integra diferentes perspectivas del negocio en un entorno interactivo, permitiendo explorar los resultados de forma dinámica según distintos criterios [0.1.7].

La organización de los indicadores y visualizaciones facilita una lectura rápida del desempeño y permite profundizar en los datos cuando sea necesario [0.1.7]. De esta manera, el resultado final combina claridad, interactividad y utilidad analítica, proporcionando una base sólida para apoyar futuros análisis y procesos de Business Intelligence en TechCore [0.1.7].
