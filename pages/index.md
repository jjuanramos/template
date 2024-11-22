---
title: Welcome to Evidence
---

```sql gj
  select * from geojsoned
```
<Dropdown data={gj} name=year value=year>
    <DropdownOption value="%" valueLabel="Escoge año"/>
</Dropdown>

```sql geo_by_year
  select * from geojsoned
  where year = ${input.year.value}
```

<AreaMap 
    data={geo_by_year} 
    areaCol=ccaa_geojson
    geoJsonUrl='https://github.com/codeforgermany/click_that_hood/blob/main/public/data/spain-provinces.geojson'
    geoId=woe_name
    value=valor
/>

<Dropdown data={gj} name=ccaa_geojson value=ccaa_geojson>
    <DropdownOption value="%" valueLabel="Todas las Comunidades Autónomas"/>
</Dropdown>

```sql index_by_ccaa
  select 
      year,
      valor,
      ccaa_geojson
  from uyv.geojsoned
  where ccaa_geojson like '${inputs.ccaa_geojson.value}'
  order by year
```

<BarChart
    data={index_by_ccaa}
    title="Índices por año en {inputs.ccaa_geojson.label}"
    x=year
    y=valor
/>