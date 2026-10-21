> 🌐 **Note:** The Spanish version of this README is available as a PDF. Some content (charts, diagrams, screenshots) is easier to follow in the PDF version.
>
> 🌐 **Nota:** La versión en español de este README está disponible en formato PDF. Algunos contenidos (gráficas, diagramas, capturas) se ven más claros en la versión PDF.

---

# DataVision Analytics: TechCore

## Project Description

As part of the selection process for the Junior Data Analyst role, DataVision Analytics assigned the candidate the first phase of the project for TechCore, a retail chain specialized in selling and distributing computers and tech accessories.

In this phase, the candidate must import the original invoice database into Power BI Desktop and carry out a complete transformation and standardization process using Power Query.

The first step is to standardize column names (for example, changing `Prod_Name` to `ProductoNombre`) and make sure each field has the correct data type: dates must be converted to Date, prices to Decimal Number, and identifiers to Text.

Next, null, duplicate or inconsistent values must be detected and handled. Exactly identical invoice records must be removed, and missing values must be replaced according to their nature: if the `MétodoPago` (payment method) field is empty, it is filled with "No especificado" (not specified), while null numeric values are imputed with zero where appropriate.

The process also includes normalizing categories and text fields to avoid variations that make analysis harder.

## Objectives

- Prepare the data for analysis.
- Correct inconsistencies in the information.
- Structure the data appropriately for analysis.
- Generate an organized data source for Power BI.
- Facilitate analysis of sales, customers, products and other related entities.
- Build a structured foundation that later allows an interactive dashboard to be created.

## Technologies Used

- Python
- Pandas
- NumPy
- Tabulate
- SQLite
- Microsoft Excel
- Power BI Desktop
- DAX

## Source Data and Cleaning

The original dataset contained 30,000 records and 30 columns with information on sales, customers, products, salespeople, cities, branches, dates, quantities, prices, discounts and transaction values.

The information was initially in a flat structure, where data corresponding to different entities appeared within the same sales records. To use the information properly, a general review of data quality was done first, and the data was then prepared for structuring.

During this stage, different types of inconsistencies were reviewed and corrected, including:

- Incorrect data types.
- Null values.
- Duplicate records.
- Inconsistencies in numeric fields.
- Spelling differences in text fields.
- Product and brand names.
- City and branch names.
- Upper and lower case.
- Accents.
- Unnecessary spaces.
- Date and time formats.

Among the main corrections, cities were normalized, for example:

- `cali` → `Cali`
- `pereira` → `Pereira`
- `Bogota` → `Bogotá`
- `bogota` → `Bogotá`
- `Medellin` → `Medellín`
- `medellin` → `Medellín`

Brands with spelling errors were also standardized, for example:

- `Aple` → `Apple`
- `Samsng` → `Samsung`
- `Lenvo` → `Lenovo`
- `Acr` → `Acer`
- `Azus` → `Asus`
- `Del` → `Dell`
- `HPP` → `HP`

Differences in branch names caused by variations in capitalization, accents and spaces were also found and corrected, so that the same entity would not appear as different records during analysis.

As part of the temporary preparation, two additional fields related to date and year were added to make later chronological analysis in Power BI easier.

Data preparation was not limited to a single tool. After the initial preparation, additional adjustments were made in Power Query inside Power BI when formats or data types needed correcting so that certain fields could be used properly.

## Python

Once the data was prepared, Python was used mainly to organize and structure the information, not to replace the cleaning process done earlier.

The code took the prepared dataset and split the information into an organized structure representing the different business entities, avoiding repeating all the information inside a single flat table.

Through this process, the information needed to represent customers, cities, salespeople, products and transactions was prepared, along with the information for invoices and their respective line items.

Python also generated identifiers to relate the different entities and prepared a structure that could later be used as a data source in Power BI.

Another important purpose of the code was to automate the generation of the final data source, avoiding having to build the different tables manually each time the model needed to be reproduced.

Main tools used:

- `pandas` for data manipulation and transformation.
- `numpy` for numeric operations.
- `tabulate` to present table results during execution.
- `sqlite3` to generate a copy of the model in a SQLite database.

The preparation and structuring process produced the file:

**`modeloVentas.xlsx`**

The `modeloVentas.xlsx` file consisted of seven main tables, organized to represent the different entities of the model:

| Table | Content |
|---|---|
| **Clientes** (Customers) | Customer information and identification. |
| **Ciudades** (Cities) | Identifier and name of each city. |
| **Facturas** (Invoices) | General information for each sale: invoice, customer, date, time and salesperson. |
| **DetalleFacturas** (Invoice Details) | Products associated with each invoice, with quantity, unit price, subtotal and discount. |
| **Productos** (Products) | Product identifier, name, brand and price. |
| **Sucursales** (Branches) | Relates each branch to its city. |
| **Vendedores** (Salespeople) | Salesperson identifier and name. |

This organization moved the information from a flat sales structure to a related model that could be used properly in Power BI.

## Entity-Relationship Model

> **Figure (see PDF):** the relational model in Power BI, showing the tables Ciudades, Sucursales, Facturas, DetalleFacturas, Productos, Vendedores and Clientes with their relationships.

After preparing the data, the information was organized into a relational model within Power BI. The model connects the different entities through identifiers, making it possible to relate geographic, commercial, customer, salesperson and product information to the transactions carried out.

The cities table relates to the branches, allowing each point of sale to be associated with its city. Branches relate to invoices, while invoices hold the general information of each transaction and relate to the corresponding customers and salespeople.

Each invoice can contain one or more records in the invoice details table. This table stores the specific information about the products sold, including quantity, unit price, subtotal and discount. In turn, each detail record relates to the products table, which holds the descriptive information of each product.

This structure separates descriptive information from transactional information, reduces data repetition, and makes analysis easier through the relationships established between the different entities.

## Final Dashboard

> **Figure (see PDF):** screenshot of the "Sales Dashboard | TechCore" executive summary in Power BI.

The dashboard was designed as an executive panel to make it easier to consult and analyze TechCore's commercial performance. It uses a clear visual structure, with the main indicators at the top and the filtering tools available to dynamically change the information displayed.

Cards were added for the indicators Total Sales, Average Ticket and Products Sold, giving a quick view of the main results.

The visual analysis includes monthly sales evolution, sales by brand, geographic distribution through a map by city, and a year-over-year sales comparison. A performance table by city was also added, combining total sales, percentage share, products sold and average ticket.

The dashboard has slicers for City, Brand, Year/Month/Date and Age, allowing the different elements to be filtered interactively.

For the age analysis, five-year ranges were used, starting at 15–19 years, followed by 20–24, 25–29 and so on. This grouping makes customer segmentation easier without presenting an excessive number of individual categories.

Headline figures shown in the dashboard:

| Indicator | Value |
|---|---|
| Total Sales | COP 468.03bn |
| Average Ticket | COP 15.60M |
| Products Sold | 90.01K |

Performance by city (from the dashboard table):

| City | Share of Sales |
|---|---|
| Medellín | 44.68% |
| Bogotá | 30.57% |
| Pereira | 12.41% |
| Cali | 12.34% |

Key insights shown in the dashboard:

- Medellín leads sales with 44.68% of the total.
- Medellín and Bogotá together account for 75.25% of sales.
- Lenovo is the brand with the highest sales volume.

Finally, an insights section was included to present the main findings of the analysis in summary form. The design uses an organized layout, independent cards, rounded borders, differentiated colors for the indicators and defined spacing between elements, aiming for a clear presentation focused on business analysis.

## Conclusion

The project turned commercial information into an analysis tool oriented toward facilitating interpretation and decision making. The final solution integrates different perspectives of the business in an interactive environment, allowing results to be explored dynamically by different criteria.

The organization of the indicators and visualizations allows for quick reading of performance and makes it possible to drill into the data when needed. In this way, the final result combines clarity, interactivity and analytical usefulness, providing a solid base to support future analyses and Business Intelligence processes at TechCore.
