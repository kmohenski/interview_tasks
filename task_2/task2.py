import requests
import json
import pandas as pd
from shapely.geometry import shape


# API
url = "https://plovput.li-st.net/getObjekti/"
response = requests.get(url)
data = response.json()


# Broj zapisa
num_records = len(data['features'])

print(f"Broj zapisa: {num_records}")


# Filter za tip_objekta 16
type_16 = [obj for obj in data['features'] if obj['properties']['tip_objekta'] == 16]
num_type_16 = len(type_16)

print(f"Broj objekta tip 16: {num_type_16}")


# Save
output_geojson_file = "type_16.geojson"
with open(output_geojson_file, 'w') as f:
    json.dump({
        "type": "FeatureCollection",
        "features": type_16
    }, f)
