import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.crs as ccrs

def plot_setup_platecarree(plot_range = [-125.25,-66,22.5,50], figsize = (7,5), central_lon=0, state_borders=True):
    '''Function sets up plotting environment for continental US. 
	"plot_range" is geographical extent, in format [lon1, lon2, lat1, lat2]
        "figsize" controls size of figure.
	"central_lon" is the longitude around which to center the plot
        " state_borders" is boolean specifying whether to plot borders of states within countries
       The function returns fig and ax objects'''
     
    fig = plt.figure(figsize = figsize)                                       # Set up figure for plotting
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=central_lon)) # Use map background
    ax.coastlines()                                                           # draw coastlines
    ax.set_extent(plot_range, crs=ccrs.PlateCarree())                         # limit geographic extent of plot
    ax.add_feature(cfeature.BORDERS)                                          # draw country borders
    ax.title.set_fontsize(30)
    if state_borders:
        ax.add_feature(cfeature.NaturalEarthFeature(category  ='cultural',    # Get state outlines
                                                    name      ='admin_1_states_provinces_lines',
                                                    scale     ='50m',
                                                    facecolor ='none'),
                       edgecolor='black')
    return fig, ax

def plot_setup_orthographic(plot_range=[-100,20,0,60], central_lon=-40, central_lat=30, figsize=(7,5)):
    '''Set up figure for plotting an orthographic projection (curved globe).
    "central_lon" and "central_lat" specify where to center the projection. Function returns fig,ax'''
    fig = plt.figure(figsize = figsize)                                       
    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=central_lon, 
                                               central_latitude=central_lat)) # Use map background
    ax.coastlines()                                                           # draw coastlines
    ax.add_feature(cfeature.BORDERS)                                          # draw country borders
    ax.set_extent(plot_range, crs=ccrs.PlateCarree())
    return fig,ax