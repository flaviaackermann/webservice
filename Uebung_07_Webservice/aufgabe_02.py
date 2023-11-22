import uvicorn
from fastapi import FastAPI
from pyproj import Transformer

app = FastAPI()

@app.get("/transformlv95towgs84/")
async def transform(E: float = 2600000, N: float = 1200000):

    transformer = Transformer.from_crs("epsg:2056", "epsg:4326")
    resultat = transformer.transform(E,N)
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": resultat
        },
        "properties": {
            "about": "Punkt Breitengrad, Längengrad"
        }
    }
    return geojson


@app.get("/transformwgs84tolv95/")
async def transform(B: float = 47, L: float = 7):

    transformer = Transformer.from_crs("epsg:4326", "epsg:2056")
    resultat = transformer.transform(B,L)
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": resultat
        },
        "properties": {
            "about": "Punkt Rechtswert, Hochwert"
        }
    }
    return geojson

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Eingabe http://127.0.0.1:8000/transformlv95towgs84/?E=2600000&N=1200000
# Eingabe http://127.0.0.1:8000/transformwgs84tolv95/?B=47.53488551579538&L=7.642147239438931
