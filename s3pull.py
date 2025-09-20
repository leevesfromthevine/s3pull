import boto3
from botocore import UNSIGNED
from botocore.client import Config
import geopandas as gpd
from typing import Optionals
import os

# replace '/aws/s3/bucket/' with s3 bucket
gdf_tiles = gpd.read_file('/aws/s3/bucket/')
gdf_tiles = gdf_tiles.to_crs(crs=3857)

# replace './aoi_shp/...' with area of interest
aoi_shp = './aoi_shp/...'
gdf_aoi = gpd.read_file(aoi_shp)

def clip_tiles_to_aoi(gdf_tiles, gdf_aoi):
    gdf_tiles_clipped = gpd.clip(gdf_tiles, gdf_aoi)
    return gdf_tiles_clipped

gdf_tiles_clipped = clip_tiles_to_aoi(gdf_tiles, gdf_aoi)

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
bucket = 'kyfromabove'

# Keep the download path the same or replace it.
download_path = './aoi_raster/'

def download_tiles(s3, bucket, gdf_tiles_clipped, download_path):
    
    downloaded_files = []
    try:
        for i, row in enumerate(gdf_tiles_clipped.itertuples()):
            key = row.key
            file_name = key.split('/')[-1]
            local_file_path = os.path.join(download_path, file_name)
            downloaded_files.append(file_name)
            
            if not os.path.exists(local_file_path):
                s3.download_file(bucket, key, local_file_path)
                print(f'Downloaded {file_name}')
    except Exception as e:
        print(f"Error occurred: {e}")


    return downloaded_files

download = download_tiles(s3, bucket, gdf_siles_clipped, download_path)
