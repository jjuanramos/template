
-- testing stuff
select * from raw.table25171
where comunidad_autonoma is not null

-- TODO: Rename comunidad_autonoma so naming fits the GeoJSON. Maybe create new column instead, geojson_ccaa
-- TODO: Having done that, we are ready to test AreaMap Evidence's feature.
