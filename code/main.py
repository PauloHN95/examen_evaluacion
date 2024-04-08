from data_reader import leer_datos,filtrar_calcular_media
import pandas as pd

def main():
  df = leer_datos('code\..\data\datos_examen.csv')
  alumno = input('Dime el tag del alumno que quieres buscar  formato -> Examen_Nombre: ')
  media = filtrar_calcular_media(df,alumno)
  print('La media del Alumno: ',alumno, 'es:', media)

if __name__ == "__main__":
    main()

