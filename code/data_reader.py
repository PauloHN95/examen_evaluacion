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
