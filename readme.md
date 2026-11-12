Proyecto modular en Python diseñado para automatizar la extracción, 
optimización de memoria (downcasting y tipos categóricos), 
limpieza integral (nulos y duplicados) y carga en formato eficiente Parquet de datasets masivos.

Estructura del Proyecto
- `main.py`: Archivo principal que orquesta la ejecución completa del pipeline llamando a las funciones del módulo de procesamiento.
- `src/`: Carpeta que contiene la lógica de negocio.
- `__init__.py`: Inicializador del paquete modular.
- `pipeline.py`: Módulo que agrupa las etapas de extracción, transformación y carga.
- `requirements.txt`: Listado de dependencias del proyecto.
- `README.md`: Documentación oficial y guía de uso.

Dependencias
El proyecto requiere las siguientes librerías para su correcto funcionamiento:
- `pandas`
- `numpy`
- `pyarrow`

Instalación y Configuración
Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:
```bash
pip install -r requirements.txt
