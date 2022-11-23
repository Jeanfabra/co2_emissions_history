# co2_emissions_history
ETL and Data Visualization using Power BI for CO2 emissions dataset.

## 1. Where did I get the data from?

The dataset was obtained through the official website of Our World in Data (OWID). You can download it from the following links:

[Oficial OWID webpage](https://ourworldindata.org/co2-and-other-greenhouse-gas-)emissions
[OWID Github](https://github.com/owid/co2-data)

## **2. ETL**

A small ETL was performed, it can be seen in the ETL notebook. For the analysis only the CO2 and Countries columns were taken into account. At the end a .csv file was exported.

## **3. Power BI**

In PowerBI the data from the exported .csv is loaded and the year column is transformed. This column is changed to a date type. 

A calendar table is created with the DAX function calendarauto(). The necessary connections are made.

Three visualizations were made, which can be seen below:

### **Map Visualization: All history**

<div align="center">
    <img src="img\map_viz.png" alt="Project Screenshot" width="80%">
</div>
<br>

### **Plotly Barchart: 2000 vs 2020**

<div align="center">
    <img src="img\barchart.png" alt="Project Screenshot" width="80%">
</div>
<br>

### **Line Chart: All history**

<div align="center">
    <img src="img\linechart.png" alt="Project Screenshot" width="80%">
</div>
<br>

## **4. Insights**

Most countries show a growth in the production of greenhouse gases. China leads the way with 210% growth compared to 2000.

Some countries such as the USA are reducing their carbon footprint in the last 2 years.

The countries that emitted the most CO2 in 2000 are the same countries that will emit the most CO2 in 2020.

Approximately 40% of CO2 emissions are due to activities carried out in the 21st century.

## **5. Contact Information**

<div align="center">
    <img src="img\contact.png" alt="Project Screenshot" width="80%">
</div>
<br>

### Author: [Jean Paul Fabra](https://www.linkedin.com/in/jeanfabra)