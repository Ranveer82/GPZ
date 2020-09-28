# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# well_augmentation.py
# Reguirements: esri arcpy API

# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
well_point = "well_point"
well_point_PointToRaster1 = "C:\\Users\\shishir gaur\\Documents\\ArcGIS\\Default.gdb\\well_point_PointToRaster1"
well_point_PointToRaster1_Re = "C:\\Users\\shishir gaur\\Documents\\ArcGIS\\Default.gdb\\well_point_PointToRaster1_Re"
RasterT_well_po1 = "C:\\Users\\shishir gaur\\Documents\\ArcGIS\\Default.gdb\\RasterT_well_po1"

# Set Geoprocessing environments
arcpy.env.snapRaster = "DEM"

# Process: Point to Raster
#          Raster of cell size 4 times the reference Raster
arcpy.PointToRaster_conversion(well_point, "yield", well_point_PointToRaster1, "MOST_FREQUENT", "NONE", "277.9220779")

# Process: Resample
#           Cell Size should be set as orriginal data to subdivide the Raster in 4*4 cells
arcpy.Resample_management(well_point_PointToRaster1, well_point_PointToRaster1_Re, "DEM", "NEAREST")

# Process: Raster to Point
arcpy.RasterToPoint_conversion(well_point_PointToRaster1_Re, RasterT_well_po1, "")

