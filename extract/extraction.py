import pandas as pd
import duckdb
from datetime import datetime
from pathlib import Path
from typing import Tuple

DATABASE_PATH = '../.duckdb/analytics.duckdb'
TABLE_NAME = "table25171"
SCHEMA_NAME = "raw"
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
	df.valor = df.valor.replace(",", ".", regex=True)
	df.valor = df.valor.astype(float)
	df['_loaded_at'] = datetime.now()
	df['_batch_id'] = datetime.now().strftime('%Y%m%d')
	df['year'] = df.periodo.str.slice(0, 4).astype(int)
	df['quarter'] = df.periodo.str.slice(5, 6).astype(int)
	df.drop(columns=['periodo'])
	return df

"""Connect to database"""
def connect_to_db_and_load() -> Tuple[int, datetime]:
	df = get_dataframe()
	# Make sure path exists
	Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)
	with duckdb.connect(DATABASE_PATH) as conn:
		conn.sql(f"create schema if not exists {SCHEMA_NAME}")
		conn.sql(f"create or replace table {SCHEMA_NAME}.{TABLE_NAME} as select * from df")
		
		# Check data was loaded properly
		result = conn.sql(f"""
			select
				count(1) as rows,
				max(_loaded_at) as last_load 
			from {SCHEMA_NAME}.{TABLE_NAME}
		""").fetchone()
		return result
	
def main() -> int:
	print("Ejecutando proceso...")
	try:
		rows, last_load = connect_to_db_and_load()
		print(f"Cargadas {rows:,} filas en {last_load}")
		return 0
	except Exception as e:
		print(f"Error en el proceso: {e}")
		return 1

if __name__ == '__main__':
	exit(main())
