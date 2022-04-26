
''' ATTENTION: There is a bug related to changing point sizes and colors that can only be fixed by the Napari creators.

 If you want to change the size or color of the points of a gene, you have to:
    - Select the gene in the lower left pannel
    - Click on the mouse pointer icon on the top left pannel
    - Select the area where the points of this transcript should change (if you want to change all points of the transcript, you should be zoomed out first)
    - Change the color/size on the top left pannel
    - Click on the zoom icon (magnifier glass) to be able to navigate again.

### INSTALLATION:
 You need Python installed. Run the following in your command prompt:

 Optional:
    conda create -y -n napari-env -c conda-forge python=3.9
    conda activate napari-env

 pip install "napari[all]"
 pip install "napari[all]" --upgrade
 pip install pandas 
 
More information here: https://napari.org/tutorials/fundamentals/installation.html

### RUNNING:
1) Edit INPUTS AREA with information on the input files and genes of interest
2) Enter a command prompt and change directory (cd) to where the script is located
3) Run the script: python polylux_python.py


Ricardo Guerreiro, Resolve Biosciences 26/01/2022

 '''



from matplotlib import image
import pandas as pd
import random 
import napari
import roifile
from matplotlib import cm
import numpy as np

######### INPUTS AREA ################################

# Files to read      
JPEG_file   = "Panorama_PROJECTNUM-SLIDE_NAME_Channel3_R8_.jpg"  # Don't use tiff files, they are too big
coords_file = "Panorama_PROJECTNUM-SLIDE_NAME_results.txt"
rois = "rois/RoiSet_SLIDE_NAME.zip"                              

# Genes to plot  (First ones go to bottom)
genes = ['Adgre1', 'Cd5l', 'Gpnmb',  
 'Rspo3', 'Stab2', 'Glul', 
 'Igfbp2', 'Cyp2f2', 'Tagln',
 'Acta2', 'Sox9']                

# Change this if you'd like all points to be smaller or bigger
point_size = 20              

######## Preprocessing ###########################

img = image.imread(JPEG_file).T 
df = pd.read_csv(coords_file, sep = '\t')
df.columns = ['x','y','z','name','qual']

# Colours for each gene
colours = cm.rainbow(np.linspace(0, 1, len(genes)))

# Prepare Rois for plotting
cell_rois = roifile.roiread(rois)
polygons = [roi.coordinates() for roi in cell_rois]

########### NAPARI APP ######################################

#Used for the scale
nanometers_per_pixel = [138, 138]

# Start Napari  
viewer = napari.view_image(img, scale = nanometers_per_pixel) 

viewer.scale_bar.unit = "nm"
viewer.scale_bar.events.visible 


# Add rois to image
viewer.add_shapes(polygons, name = "Rois", scale = nanometers_per_pixel,
                  shape_type='polygon', edge_width=4, 
                  edge_color='red')

# Add points to image
for i,gen in enumerate(genes):

    # Filter points for gen
    b = df.name == gen 
    points = list(zip(df.x[b],df.y[b]))

    viewer.add_points(points, name = gen, edge_width = 0.01, scale = nanometers_per_pixel,
        face_color= colours[i], size = point_size)                    # experimental_canvas_size_limits = (30,10000))

napari.run()  # start the "event loop" that maintains window open

