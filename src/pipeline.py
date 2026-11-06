#funcion de extraccion y optimizacion de la memoria
def extraer_datos(ruta_archivo: str) -> pd.DataFrame:
    print(f"📡 Leyendo datos desde: {ruta_archivo}...")
    df = pd.read_csv(ruta_archivo)
    
    # Optimización de enteros y flotantes
    cols_int = df.select_dtypes(include=['int64']).columns
    df[cols_int] = df[cols_int].astype(np.int32)
    
    cols_float = df.select_dtypes(include=['float64']).columns
    df[cols_float] = df[cols_float].astype(np.float32)
    
    # Optimización de texto repetitivo a categoría
    cols_obj = df.select_dtypes(include=['object']).columns
    for col in cols_obj:
        if df[col].nunique() / len(df) < 0.5:
            df[col] = df[col].astype('category')
            
    print(f"✅ Extracción completada. Dimensiones iniciales: {df.shape}")
    return df            

# TRANSFORMACIÓN Y LIMPIEZA 
def transformar_datos(df: pd.DataFrame) -> pd.DataFrame:
    print("🧹 Iniciando proceso de transformación y limpieza...")
    df_clean = df.copy()
    
    # Normalización de columnas a snake_case
    df_clean.columns = (
        df_clean.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )
    
    # Eliminación de duplicados
    duplicados_iniciales = df_clean.duplicated().sum()
    df_clean = df_clean.drop_duplicates()
    print(f"  - Se eliminaron {duplicados_iniciales} registros duplicados.")
    
    # Imputación de nulos numéricos por la mediana
    cols_num = df_clean.select_dtypes(include=[np.number]).columns
    for col in cols_num:
        if df_clean[col].isnull().sum() > 0:
            mediana = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(mediana)
            print(f"  - Columna numérica '{col}': nulos imputados con la mediana ({mediana:.2f}).")
            
    # Imputación de nulos categóricos
    cols_cat = df_clean.select_dtypes(include=['object', 'category']).columns
    for col in cols_cat:
        if df_clean[col].isnull().sum() > 0:
            if isinstance(df_clean[col].dtype, pd.CategoricalDtype):
                df_clean[col] = df_clean[col].cat.add_categories(['Sin Información'])
            df_clean[col] = df_clean[col].fillna('Sin Información')
            print(f"  - Columna categórica '{col}': nulos reemplazados por 'Sin Información'.")
            
    print(f"Transformación completada. Dimensiones finales: {df_clean.shape}")
    return df_clean


#FUNCIÓN DE CARGA / PERSISTENCIA EN PARQUET ---
def cargar_datos(df: pd.DataFrame, ruta_salida: str) -> None:
    print(f"Guardando el archivo procesado en formato Parquet en: {ruta_salida}...")
    df.to_parquet(ruta_salida, engine='pyarrow', compression='snappy', index=False)
    print("¡Proceso de Carga (ETL) finalizado exitosamente!")
