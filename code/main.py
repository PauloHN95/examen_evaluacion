from data_reader import leer_datos,filtrar_calcular_media
import pandas as pd

def main():
  """
  df: es el df que se crea con la informacion del csv
  alumno: es un input y nos pedira por consola el nombre del alumno que queremos sacar su tag
    con el formato Examen_Nombre.
  media: media de la columna value del alumno seleccionado  
  """
  df = leer_datos('code\..\data\datos_examen.csv')
  alumno = input('Dime el tag del alumno que quieres buscar  formato -> Examen_Nombre: ')
  media = filtrar_calcular_media(df,alumno)
  print('La media del Alumno: ',alumno, 'es:', media)

if __name__ == "__main__":
    main()

