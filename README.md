# Urbanismo y Vivienda

[Mapa](https://github.com/ufoe/d3js-geojson/blob/master/Spain.json), `woe_name` es el nombre de la columna que indica la CCAA.

De [GeoJSON Spec](https://gist.github.com/sgillies/1233327#file-geojson-spec-1-0-L50):

2. GeoJSON Objects
==================

GeoJSON always consists of a single object. This object (referred to as the
GeoJSON object below) represents a geometry, feature, or collection of
features.

* The GeoJSON object may have any number of members (name/value pairs).

* The GeoJSON object must have a member with the name "type". This member's
  value is a string that determines the type of the GeoJSON object.

* The value of the type member must be one of: "Point", "MultiPoint",
  "LineString", "MultiLineString", "Polygon", "MultiPolygon",
  "GeometryCollection", "Feature", or "FeatureCollection". The case of the type
  member values must be as shown here.

* A GeoJSON object may have an optional "crs" member, the value of which must
  be a coordinate reference system object (see `3. Coordinate Reference System
  Objects`_).

* A GeoJSON object may have a "bbox" member, the value of which must be a
  bounding box array (see `4. Bounding Boxes`_).


[Area Map Evidence](https://docs.evidence.dev/components/area-map/).
Apuntes:
- Probablemente, con apuntar a la url de Github nos valga en GeoJSONUrl
- areaCol tendrá que indicar la Comunidad Autónoma, con el mismo formato que el GeoJSON.
- geoId apunta a la columna equivalente en el GeoJSON, en nuestro caso `woe_name`.


[Leaflet Providers](https://leaflet-extras.github.io/leaflet-providers/preview/).

