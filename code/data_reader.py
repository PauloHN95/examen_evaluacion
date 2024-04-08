import pandas as pd

def leer_datos(filepath):
    """
    Una función llamada leer_datos para leer el CSV y convertir TS en formato datetime.
    Estaria bien poner un if, por si no hay ninguna columna en el df llamada TS.
    filepath : Tenemos que poner la ruta del fichero csv, para leerlo.
    df: Devielve un data frame con los datos del csv
    """
    df = pd.read_csv(filepath)
    df['TS'] = pd.to_datetime(df['TS'])
    return df 

def filtrar_calcular_media(df,tag):
    """
    funcion llamada filtrar_calcular_media que filtre los datos de la columna Tag para tu nombre Examen_NOMBRE_ALUMNO
    y calcula la media de la columna value.
    df: DataFrame que contiene los datos.
    tag: Tag específico por el cual filtrar los datos.
    df_tag_alumno: se crea un df nuevo que solo contiene los datos del alumno seleccionado
    media: calcula la media de la columna 'Value' del dataframe df_tag_alumno .
    """
    df_tag_alumno = df[df['Tag'] == tag]
    media = df_tag_alumno['Value'].mean()
    return media
