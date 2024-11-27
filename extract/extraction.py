import pandas as pd
import duckdb
from datetime import datetime
from pathlib import Path
from typing import Tuple

FILE_PATH = '../sources/uyv/analytics.parquet'
URL = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/25171.csv"

"""Download data and do basic renamings and castings"""
def get_dataframe() -> pd.DataFrame:
	df = pd.read_csv(URL, sep=";")
	df = df.rename(columns={
		'Total Nacional': 'total_nacional',
		'Comunidades y Ciudades Autónomas': 'comunidad_autonoma', 
		'General, vivienda nueva y de segunda mano': 'tipo_vivienda',
		'Índices y tasas': 'indice_tasa',
		'Periodo': 'periodo',
		'Total': 'valor'
	})
	df.valor = df.valor.replace(",", ".", regex=True).astype(float)
	df.drop(columns=['periodo'])
	return df
	
def main() -> int:
	print("Ejecutando proceso...")
	try:
		df = get_dataframe()
		df.to_parquet(
			FILE_PATH,
			compression='snappy',  # Compresión eficiente y rápida
			index=False,          # Evitar incluir el índice si no es necesario
			engine='pyarrow',     # Usar explícitamente PyArrow
			write_statistics=False # Evitar metadatos variables
		)
		print(f"Cargadas {df.shape[0]} filas en {datetime.now()}")
		return 0
	except Exception as e:
		print(f"Error en el proceso: {e}")
		return 1

if __name__ == '__main__':
	exit(main())
