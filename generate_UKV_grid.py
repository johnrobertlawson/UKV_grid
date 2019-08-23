""" This script generates the latitude-longitude grid used by the UKV model.

Run with:

python generate_UKV_grid.py

after changing any settings 

You will need:

Python 3.5+
Numpy
Matplotlib (and Basemap, if not included)

It is recommended to use Anaconda and "conda install x".

John R. Lawson, CIMMS/NSSL, 2019
john.lawson@noaa.gov
"""

from mpl_toolkits.basemap import Basemap
import numpy as N
import matplotlib.pyplot as plt

def create_basemap():
    # NE corner lat/lon
    urcrnrlat = 60.622
    urcrnrlon = 6.371

    # SW corner lat/lon
    llcrnrlat = 47.926
    llcrnrlon = -10.562

    # Central latitude and longitude
    # JRL: NEED TO KNOW THIS
    # lat_0 = 0.0
    # lon_0 = 0.0
    lat_0 = 50.0
    lon_0 = -0.0

    # While we're here, create a figure axis for plotting, if desired 
    fig, ax = plt.subplots(1)
    m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,urcrnrlon=urcrnrlon,
                urcrnrlat=59.5,resolution='i',projection='tmerc',
                lon_0=lon_0,lat_0=lat_0,ax=ax)
    return fig, ax, m

def plot_domain(fig,m):
    m.drawcoastlines()
    m.fillcontinents(color='coral',lake_color='aqua')
    m.drawparallels(N.arange(-40.0,61.0,2.0))
    m.drawmeridians(N.arange(-20.0,21.0,2.0))
    m.drawmapboundary(fill_color='aqua')
    ax.set_title("Transverse Mercator Projection")

    # This will save to the current directory
    fig.tight_layout()
    fname = "check_domain.png"
    fig.savefig(fname)
    plt.close(fig)
    return

def export_latlon_to_npy(m,lats=True,lons=True):
    """ This function will export a .npy file
    (a 2D array of the lats/lons) that can be loaded with
    
    N.load('/path/to/the/file/latlons_UKV.npy')

    replacing the path to suit.
    """
    # From uk_model_data_sheet_lores1.pdf, by UKMO
    nx = 1096
    ny = 1408
    
    # Can also return x,y if needed for plotting etc?
    lons,lats = m.makegrid(nx=nx,ny=ny,)#returnxy=True)
    
    # This will save to the current directory
    N.save(file='lats.npy',arr=lats)
    N.save(file='lons.npy',arr=lons)
    return

# Procedure
fig, ax, m = create_basemap()
plot_domain(fig,m)
export_latlon_to_npy(m)

    
