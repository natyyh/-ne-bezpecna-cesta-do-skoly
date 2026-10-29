import json   #importuju json abychom mohli pracovat s daty ve formatu json 
import pandas as pd    #importuju knihovnu ktera zpracovava data v tabulkach, pd je zkratka
import streamlit as st    #importuju knihovnu pomoci ktere udelame webovku s mapou

#nacteni geojson souboru
with open("datova sada/pocit-nebezpeci-olomouc-2.geojson",     #otevru soubor s daty a ulozim jej do promenne f
    encoding="utf-8") as f:     #encoding je jen nejake kodovani aby se to zobrazilo spravne
    geojson = json.load(f)     #nactu data z json souboru a prevedu je na py objekty a ulozim do promenne geojson

#souradnice jednotlivych bodu
rows = []    #vytvorim prazdny seznam
for feature in geojson["features"]:    #prochazim prvky v geojson (kazdy prvek se nazyva feature)
    geometry = feature.get("geometry")    #ziska geometrii daneho prvku napr. jeho bod

    if geometry and geometry["type"] == "Point":    #overi, zda geometrie existuje a ze jde o bod typu point
        lon, lat = geometry["coordinates"][:2]    #ziska souradnice bodu (lon a lat)

        if 16.8 <= lon <= 17.7 and 49.3 <= lat <= 49.9:
           rows.append({
                "latitude": lat,
                 "longitude": lon,
                 "typ_ident": feature["properties"].get("typ_ident")
                 })    #prida do seznamu rows slovnik s informacemi o bodu (souradnice a typ identifikace)

#prevod na tabulku a vykresleni mapy

df = pd.DataFrame(rows)

# Barva podle kategorie
barvy = {
    "a": "#7B61A8",  # noc – fialová
    "b": "#E5A000",  # den – žlutá
}

df["barva"] = df["typ_ident"].map(barvy)

# Filtr v postranním panelu
vyber = st.sidebar.selectbox(
    "Zobrazit místa:",
    [
        "Vše",
        "Noc",
        "Den"
    ]
)

# Vybereme body podle volby
if vyber == "Noc":
    df_mapa = df[df["typ_ident"] == "a"]
elif vyber == "Den":
    df_mapa = df[df["typ_ident"] == "b"]
else:
    df_mapa = df

# Vykreslení mapy
st.map(
    df_mapa,
    latitude="latitude",
    longitude="longitude",
    color="barva"
)
