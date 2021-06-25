import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.crs as ccrs

def plot_setup_(plot_range = [-125.25,-66,22.5,50], figsize = (7,5), central_lon=0, state_borders=True):
    '''Function sets up plotting environment for continental US. 
	"plot_range" is geographical extent, in format [lon1, lon2, lat1, lat2]
        "figsize" controls size of figure.
	"central_lon" is the longitude around which to center the plot
        " state_borders" is boolean specifying whether to plot borders of states within countries
       The function returns fig and ax objects'''
     
    fig = plt.figure(figsize = figsize)                                       # Set up figure for plotting
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=central_lon))
    states_provinces = cfeature.NaturalEarthFeature(                          # get state outlines
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
    if state_borders:
        ax.add_feature(states_provinces, edgecolor='black')
    ax.coastlines()                                                           # draw coastlines
    ax.set_extent(plot_range, crs=ccrs.PlateCarree())                         # limit geographic extent of plot
    ax.add_feature(cfeature.BORDERS)                                          # draw country borders
    ax.title.set_fontsize(30)
    
    return fig, ax
