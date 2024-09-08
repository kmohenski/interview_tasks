import rasterio
import numpy as np


MUL = 100

tiff_file_path = "data/response_bands.tiff"


with rasterio.open(tiff_file_path) as src:
    bands = src.read()

    # Broj bandova
    band_num = bands.shape[0]

    red_band = bands[3]     # Red = band 4
    nir_band = bands[7]     # NIR = band 8
    swir_band = bands[10]   # SWIR = band 11


nir_band_mul = nir_band * MUL
red_band_mul = red_band * MUL
swir_band_mul = swir_band * MUL

ndvi = (nir_band_mul - red_band_mul) / (nir_band_mul + red_band_mul)
ndmi = (nir_band_mul - swir_band_mul) / (nir_band_mul + swir_band_mul)

# NaN vrijednosti pretvorimo u 0 (rezultat djeljenja sa 0)
ndvi = np.nan_to_num(ndvi)
ndmi = np.nan_to_num(ndmi)

print(f"Prosječni NDVI = {np.mean(ndvi)}")
print(f"Prosječni NDMI = {np.mean(ndmi)}")

print(f"Satelitska snimka sadrži {band_num} kanala.")
