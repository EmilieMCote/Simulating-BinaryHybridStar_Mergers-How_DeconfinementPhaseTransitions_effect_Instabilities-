#import libraries
import numpy as np
from kuibit import timeseries as ts
from kuibit import unitconv as uc
from kuibit.simdir import SimDir
import matplotlib
from matplotlib import rcParams
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import rc
import pylab
import imageio.v2 as imageio
import os
import sys
from PIL import Image, ImageDraw

##set matplotlib latex and runtime parameters
#rcParams.update({'figure.autolayout': True})
#matplotlib.rc('text', usetex = True)
#matplotlib.rc('font', **{'family': 'serif', 'serif':['Computer Modern'], 'size':11})
#matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
#matplotlib.rcParams['xtick.minor.size'] = 1
#matplotlib.rcParams['xtick.minor.width'] = 1
#matplotlib.rcParams['xtick.labelsize'] = 20
#matplotlib.rcParams['ytick.labelsize'] = 20
#matplotlib.rc('legend', fontsize=20)

#set constants and plot line/font sizes
universal_linewidth=2
universal_fontsize=25
geo_units=uc.geom_umass_msun(1.0)
convMsoltokm=geo_units.length*1e-3
convMsoltoms=geo_units.time*1e3

#specify the data directory
datadir = "%s"%sys.argv[1]
print(datadir)
SD = SimDir(datadir, max_depth=2)

#make a directory to hold the frames
isdir = os.path.isdir('%s/temp_frames'%datadir)
if(isdir==False):
    print("Storing simulation frames in \"temp_frames/\"")
    os.mkdir('%s/temp_frames'%datadir)

#load the 2D and maximum data
RHODATA   = SD.gf.xy['rho_b']
rho_max = SD.ts.maximum['rho_b'].y[0]

#get the simulation times
times=RHODATA.available_times

#set the color map
cmap_rho='gnuplot'

#set the limits on the colorbar
climlo=-5
climhi=0

#set the interpolation method and labels
int_mthd='bilinear'
cblab = r'$\log(\rho_{\rm b}/\rho_{\rm b, max}(0))$'
xlab = "$x$ (km)"
ylab = "$y$ (km)"

#set the spatial extrema and number of gridpoints for visualization
xmax=20.0
xmin=-xmax
ymin=xmin
ymax=xmax
npoints = 200

extent = [xmin, xmax, ymin, ymax]
filenames=[]
print("Simulation has %d frames" %len(times))
for i in range(0,len(times),1):
#for i in range(0,1,1):
    print("it: %04d   t:%1.5f" %(i, times[i]))
    
    #get the density variable
    #RHOVAR = RHODATA.get_time(times[i]).finest_level.data
    RHOVAR=(RHODATA.get_time(times[i]).to_UniformGridData([npoints, npoints], x0=[xmin/convMsoltokm, ymin/convMsoltokm], x1=[xmax/convMsoltokm, ymax/convMsoltokm], resample=False).data)
    
    #set the fig and axes size
    fig, axs= plt.subplots(nrows=1, ncols=1,figsize=(10,10))

    #plot the density
    rhoplot=axs.imshow(np.log10(RHOVAR/rho_max).T, extent=extent, cmap=cmap_rho, interpolation=int_mthd, vmin=-5, vmax=0)
    
    #set the plot and axes title
    axs.set_title('%s, $t=%1.2f$'%(cblab,times[i]*convMsoltoms), fontsize=universal_fontsize)
    axs.set_xlabel(r'$x$ (km)', fontsize=universal_fontsize)
    axs.set_ylabel(r'$y$ (km)', fontsize=universal_fontsize)
    fig.colorbar(rhoplot, ax=axs, shrink=0.725)

    plt.savefig('%s/temp_frames/temp_frame_%03d.png' %(datadir,i), facecolor='white', edgecolor='white')
    filenames.append('%s/temp_frames/temp_frame_%03d.png' %(datadir,i))
    plt.close(fig)

with imageio.get_writer('%s/rho_b.gif'%datadir, mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
#os.system('convert %s/temp_frames/temp_frame*png %s/rho.gif'%(datadir, datadir))

print("Done")
