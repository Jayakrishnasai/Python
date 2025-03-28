import folium
map = folium.Map(Location = [13.6788, 79.3525], zoom_start = 13)
folium.Marker([13.6788, 79.3525], popup = "Sri Venkateswara Temple, Andhra Predesh, India", icon = folium.Icon(color = "green")).add_to(map)
map.save("map.html")
print(f"Map has been created and saved as map.html {map}")
