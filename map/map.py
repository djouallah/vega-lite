import altair as alt
floor_Plan = alt.topo_feature('https://raw.githubusercontent.com/djouallah/R_leaflet_MAP/master/foundation.json', 'foundation')
source = 'https://raw.githubusercontent.com/djouallah/R_leaflet_MAP/master/data/data.csv'
map = alt.Chart(floor_Plan).mark_geoshape().encode(
color='progress:Q',
tooltip=['properties.id:N','progress:N']).transform_lookup(
    lookup='properties.id',
    from_=alt.LookupData(source, 'id', ['progress']))

map.save('map.html')
map
