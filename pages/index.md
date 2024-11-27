---
title: Urbanismo y Vivienda
---

```sql gj
  select * from uyv.geojsoned
  where indice_tasa = 'Variación trimestral'
```
<!-- Failing to get the default value to show -->
<Dropdown
	data={gj}
	name=chosen_year
	value=year
	title='Escoge un año'
	defaultValue=2024
/>

```sql geo_by_year
  select * from ${gj}
  where year = ${inputs.chosen_year.value}
	and quarter = 3
	and ccaa_geojson is not null
```

<!--
	Failing to see the local maps here, too.
	They are available at '../mapas':
		- es.geojson from https://simplemaps.com/gis/country/es.
		- spain.geojson from https://data.metabolismofcities.org/library/maps/35492/view/
	Neither work.
-->
<AreaMap 
    data={geo_by_year} 
    areaCol=ccaa_geojson
    geoJsonUrl='https://github.com/codeforgermany/click_that_hood/blob/main/public/data/spain-provinces.geojson'
    geoId=woe_name
    value=valor
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