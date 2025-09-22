This is a script based off of Ian Horn's Juypter Notebook examples using KyFromAbove's s3 bucket: https://github.com/ianhorn/kyfromabove-on-aws-examples.

s3 buckets can be found in constants.py in Ian Horn's example project.

Before using remove the placeholder ./aoi_raster/rasters.txt and ./aoi_shp/shp.txt files.

If you see this and have any reccomendations for alternatives to qgisforthreejs or the qgis DEMto3D plugin shoot me an email at siobhan@leevesfromthevine.com.

TODO ->
Add mosaic clip process.
Replace aoi_raster directory with mkdir usage.
Look into replacing GeoPandas usage with Rasterio's native s3 I/O.


