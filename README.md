# ncep-data-req

Download and preprocess NCEP GFS 0.25° atmospheric forecast data from NOAA using ASCII interface.

## Overview

This package provides utility functions to directly download and preprocess Global Forecast System (GFS) 0.25-degree resolution data from the NOAA NOMADS server. It supports extraction of pressure-level and surface-level variables for specific forecast hours, structured into usable `xarray.Dataset` objects.
Inspiredby : noaa-gfs-js anf getgfs 

## Features

- Access GFS 0.25° forecast data from NOAA
- Support for both pressure-level and surface variables
- Handles multiple or single forecast hours
- Outputs structured `xarray.Dataset` objects for easy analysis

## Installation

You can install the package from PyPI (after publishing):

```bash
pip install ncep_data_req

from ncep_data_req import get_data_preprocess, get_data_preprocess_s

# Example: Download temperature on pressure levels for 6 forecast hours
ds = get_data_preprocess(
    '2025-05-23', utc=0, ft=6, var='tmpprs', pvar='yes',lon_range=(45,90),lat_range=(10,20)
)

# Example: Download temperature on surface level for 6 forecast hours
ds = get_data_preprocess(
    '2025-05-23', utc=0, ft=6, var='pratesfc', pvar='no',lon_range=(45,90),lat_range=(10,20)
)




# Example: Download  variable at single forecast hour
ds_surface = get_data_preprocess_s(
    '2025-05-23', utc=0, ft=6, var='tmpprs', pvar='yes',lon_range=(45,90),lat_range=(10,20)
)


# Example: Download  variable on surface level at single forecast hour
ds = get_data_preprocess(
    '2025-05-23', utc=0, ft=6, var='pratesfc', pvar='no',lon_range=(45,90),lat_range=(10,20)
)


Parameters
Longitude: 0.00000000000°E to 359.75000000000°E (1440 points, avg. res. 0.25°)
Latitude: -90.00000000000°N to 90.00000000000°N (721 points, avg. res. 0.25°)
Altitude: 1000.00000000000 to 20. (26 points, )

utc: Initialization hour (0, 6, 12, or 18 UTC)

ft: Forecast hour (0 to 384 depending on GFS run)

var: GFS variable name (e.g., tmpprs, rhprs, ugrdprs, etc.)

pvar: 'yes' if pressure-level variable, 'no' for surface

Output
Returns an xarray.Dataset containing:

Dimensions: time/levels, lat, lon

Coordinates: pressure levels, lat/lon grid

Data variables: selected GFS variable 
check this link ( https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/)


contact:subhrjitrath17@gmail.com

