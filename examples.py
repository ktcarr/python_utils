from plotting import plot_setup
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cmocean

sst = xr.open_dataarray('sst_may2021.nc')

fig,ax = plot_setup(plot_range=[0,359,-40,40], central_lon=180,figsize=(8,4))
cp     = ax.contourf(sst.lon, sst.lat, sst.mean('time'), cmap='cmo.thermal',
                     levels=np.arange(9,36,3), extend='both', 
                     transform=ccrs.PlateCarree())
cb     = fig.colorbar(cp, orientation='horizontal', label=r'SST$^{\circ}$C',
                      pad=.05)
ax.set_title('Mean SST for May 2021')
plt.show()
