# NAJWAZNIEJSZA RZECZ, PO SKONCZENIU DOKŁADNIE OPISAĆ KAŻDĄ ISTOTNĄ LINIĘ KODU, NAPISAĆ ZA CO ODPOWIADA, CO ROBI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# WAŻNA FUNKCJA ZIP, PAMIETAĆ, ZROZUMIEĆ JAK DZIAŁA (PO JEDNYM Z KAZDEJ LISTY NA PRZEMIAN)

import folium # Wiadomo importuje moduł "folium"
import pandas # Wiadomo importuje moduł "pandas"

data = pandas.read_csv("Volcanoes_USA.txt") # Do zmiennej data przypisuje "read" pliku cvx(txt) Volcanoes_USA.txt
lat = list(data["LAT"]) # Z pliku(data) odczytuje wszystkie latitude i formuje je w liste
lon = list(data["LON"]) # Z pliku(data) odczytuje wsystkie longitude i formuje je w liste
ele = list(data["ELEV"]) # Z pliku(data) weźmiemy wszystkie "elevations" i formujemy je w liste

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

mapa = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright") # Wiadomo potrzebujemy mapę na której rozmieścimy nasze markery

fgv = folium.FeatureGroup(name="Volcanoes") # Opis można znaleźć  dzięki help(folium.FeatureGroup), ta metoda tworzy pojedynczy layer(warstwe), możemy "wkładać" do niego rózne rzeczy a to zrozumie je jako jedna warstwa


for lt, ln, el in zip(lat, lon, ele):  # Ta pętla dodaje lt i ln i el przy użyciu funkcji "zip" (należy wiedzieć jak działa(po jednaym z każdej listy po kolei)) do danej "location" a następnie tworzy marker w podanych współrzędnych
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(str(el)+" m",parse_html=True), fill_color=color_producer(el), color="grey", fill=True, fill_opacity=0.7)) # Przy popup występuje trudna "komenda", która zapobiega możliwości problemu ze stroną, jeżeli jej nie zapamiętam zwyczajnie użyć el(str)

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"})) # Dodanie pliku json, trzeba dodawac część encoding




mapa.add_child(fgv)
mapa.add_child(fgp) # NIE JASNE
mapa.add_child(folium.LayerControl())
mapa.save("Map1.html") # ZAWSZE NALEŻY MAPĘ ZAPISAĆ
