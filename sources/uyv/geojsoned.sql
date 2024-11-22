
-- testing stuff
with base as (
    select
        * exclude (periodo),
        cast(substr(periodo, 1, 4) as int) as year,
        cast(substr(periodo, 6, 1) as int) as quarter
    from raw.table25171
    where comunidad_autonoma is not null
        and tipo_vivienda = 'General'
        and indice_tasa = 'Índice'
),

geojsoned as (
    select
        *,
        case comunidad_autonoma
            when '01 Andalucía' then 'Andalucía'
            when '02 Aragón' then 'Aragón'
            when '03 Asturias, Principado de' then 'Principado de Asturias'
            when '04 Balears, Illes' then 'Islas Baleares'
            when '05 Canarias' then 'Palmas'
            when '06 Cantabria' then 'Cantabria'
            when '07 Castilla y León' then 'Castilla y león'
            when '08 Castilla - La Mancha' then 'Castilla-La Mancha'
            when '09 Cataluña' then 'Cataluña'
            when '10 Comunitat Valenciana' then 'Comunidad Valenciana'
            when '11 Extremadura' then 'Extremadura'
            when '12 Galicia' then 'Galicia'
            when '13 Madrid, Comunidad de' then 'Comunidad de Madrid'
            when '14 Murcia, Región de' then 'Región de Murcia'
            when '15 Navarra, Comunidad Foral de' then 'Comunidad Foral de Navarra'
            when '16 País Vasco' then 'País Vasco'
            when '17 Rioja, La' then 'La Rioja'
            else null
        end as ccaa_geojson
    from base
)

select
    ccaa_geojson,
    year,
    quarter,
    valor
from geojsoned
