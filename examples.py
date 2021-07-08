'''Note: this file is no longer updated. Please see examples.ipynb for new version.'''

from plotting import plot_setup_platecarree, plot_setup_orthographic
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cmocean
from os.path import join

data_folder = '~/data'
sst = xr.open_dataarray(join(data_folder,'sst_may2021.nc'))

# Plot of global SST using PlateCarree projection
fig,ax = plot_setup_platecarree(plot_range=[0,359,-40,40], central_lon=180,figsize=(8,4))
cp     = ax.contourf(sst.lon, sst.lat, sst.mean('time'), cmap='cmo.thermal',
                     levels=np.arange(9,36,3), extend='both', 
                     transform=ccrs.PlateCarree())
cb     = fig.colorbar(cp, orientation='horizontal', label=r'SST$^{\circ}$C',pad=.05)
ax.set_title('Mean SST for May 2021')
plt.show()


# Plot of North Atlantic SST using Orthographic projection
fig,ax = plot_setup_orthographic(figsize=(8,7))
cp     = ax.contourf(sst.lon, sst.lat, sst.mean('time'), cmap='cmo.thermal',
                     levels=np.arange(0,36,3), extend='both', transform=ccrs.PlateCarree())
cb     = fig.colorbar(cp, orientation='horizontal', label=r'SST$^{\circ}$C', pad=.05)
plt.show()
