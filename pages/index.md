---
title: Urbanismo y Vivienda
---

```sql gj
  select * from uyv.geojsoned
  where indice_tasa = 'Variación trimestral'
```

<Dropdown
	data={gj}
	name=chosen_year
	value=year
	title='Escoge un año'
	defaultValue={2023}
/>

```sql geo_by_year
  select * from ${gj}
  where year = ${inputs.chosen_year.value}
	and quarter = 3
	and ccaa_geojson is not null
```
*Cambia el año escogido arriba para ver la variación trimestral del IPC del tercer trimestre de ese año en el mapa.*
<AreaMap 
    data={geo_by_year} 
    areaCol=ccaa_geojson
    geoJsonUrl='/mapas/spain.geojson'
    geoId=acom_name
    value=valor
    title='Variación trimestral del IPC el tercer trimestre de {inputs.chosen_year.label}'
/>

<Dropdown
	data={gj}
	name=ccaa_geojson
	value=ccaa_geojson
	title="Escoge comunidad autónoma"
	defaultValue='Comunidad Valenciana'
/>

```sql index_by_ccaa
  select 
      fecha,
      valor
  from ${gj}
  where ccaa_geojson = '${inputs.ccaa_geojson.value}'
	and year >= 2020
```

<BarChart
    data={index_by_ccaa}
    title="Variaciones Trimestrales del IPC en {inputs.ccaa_geojson.label}, desde 2020"
    x=fecha
    y=valor
/>