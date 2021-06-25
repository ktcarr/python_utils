
from plotting import plot_setup
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cmocean

sst = xr.open_dataarray('sst_may2021.nc')

fig,ax = plot_setup(plot_range=[0,359,-40,40], central_lon=180)
ax.plot(sst.longitude, sst.latitude, sst.mean('time')
