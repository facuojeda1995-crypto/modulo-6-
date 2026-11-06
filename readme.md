Pipeline de Ingesta, Limpieza y Persistencia de Datos

Este repositorio contiene un pipeline de datos modular y vectorizado desarrollado en Python. 
Su objetivo es automatizar la extracción de un dataset de retail, 
optimizar drásticamente el uso de memoria RAM mediante *downcasting* y tipado categórico, 
limpiar anomalías (duplicados y nulos) 
y exportar el resultado en un formato columnar de alto rendimiento.


Requisitos e Instalación de Dependencias

Asegúrate de contar con **Python 3.8 o superior**. 
Para instalar las librerías requeridas de procesamiento y persistencia, ejecuta en tu terminal:
```bash
pip install pandas numpy pyarrow

📁 Estructura del Repositorio
