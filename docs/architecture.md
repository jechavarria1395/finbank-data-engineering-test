\# Arquitectura de la Solución



Este proyecto implementa un pipeline de datos end-to-end utilizando servicios de Azure y siguiendo la arquitectura Medallion (Bronze, Silver y Gold).



El objetivo es simular un escenario bancario donde se procesan datos de clientes, transacciones y créditos para generar métricas analíticas.



---



\# Servicios Azure Utilizados



\## Azure SQL Database



Se utiliza como base de datos transaccional que almacena los datos generados por el script de Python.



Tablas utilizadas:



\- dim\_clientes

\- dim\_productos

\- fact\_transacciones

\- fact\_creditos

\- dim\_sucursales



---



\## Azure Data Factory



Se utiliza para la orquestación del pipeline de datos y para la ingesta desde Azure SQL hacia el Data Lake.



---



\## Azure Data Lake Storage Gen2



Se utiliza como almacenamiento central del Data Lake.



Se implementa una arquitectura Medallion con tres capas:



Bronze: datos crudos  

Silver: datos limpios  

Gold: datos agregados para análisis



---



\## Azure Databricks



Se utiliza como motor de procesamiento basado en Apache Spark.



Se encarga de:



\- limpieza de datos

\- transformaciones

\- aplicación de reglas de negocio

\- generación de datasets analíticos



---



\## Azure Key Vault



Se utiliza para almacenar secretos y credenciales de forma segura, evitando incluir información sensible en el código.



---



\## Monitoreo



El sistema incluye monitoreo para registrar ejecución de pipelines, errores y métricas de procesamiento.



---



\# Flujo del Pipeline



1\. Generación de datos dummy con Python  

2\. Carga de datos en Azure SQL Database  

3\. Ingestión hacia ADLS Gen2 mediante Azure Data Factory  

4\. Almacenamiento inicial en capa Bronze  

5\. Transformaciones en Databricks hacia capa Silver  

6\. Generación de tablas analíticas en capa Gold

