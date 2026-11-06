#ejecucion de pipelines 
# 1. Indicamos el nombre exacto de tu archivo CSV en Colab
ruta_csv_entrada = "datos_ingesta.csv"
ruta_parquet_salida = "datos_salida.parquet"

print("=== INICIANDO PIPELINE DE DATA ENGINEERING (ETL) ===\n")

# 2. Aquí es donde la función va a buscar los datos al CSV y optimiza la memoria
df_raw = extraer_datos(ruta_csv_entrada)
print("-" * 50)

# 3. Limpia duplicados y nulos de forma vectorizada
df_procesado = transformar_datos(df_raw)
print("-" * 50)

# 4. Guarda el resultado final en formato Parquet
cargar_datos(df_procesado, ruta_parquet_salida)
print("-" * 50)

print("\n=== PIPELINE EJECUTADO CON ÉXITO ===")
