
''' ATTENTION: There is a bug related to changing point sizes and colors that can only be fixed by Napari itself.

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
from matplotlib import cm
import numpy as np

######### INPUTS AREA ################################

# Files to read
JPEG_file   = "../08_sample_comparinson/Panorama_32542-slide5_A2_5_Channel3_R8_.jpg"
coords_file = "../08_sample_comparinson/Panorama_32542-slide5_A2_5_results.txt"


# Genes to plot  (First ones go to bottom)
genes = ['Adgre1', 'Cd5l', 'Gpnmb',  
 'Rspo3', 'Stab2',                    
 'Glul', 'Igfbp2', 'Cyp2f2',            
 'Tagln', 'Acta2',                    
 'Sox9']                

# Change this if you'd like all points to be smaller or bigger
 point_size = 20              


######## Preprocessing ###########################

img = image.imread(JPEG_file).T 
df = pd.read_csv(coords_file, sep = '\t')
df.columns = ['x','y','z','name','qual']


# Colours for each gene
colours = cm.rainbow(np.linspace(0, 1, len(genes)))


########### NAPARI APP ######################################

nanometers_per_pixel = [138, 138]

# Start Napari  
viewer = napari.view_image(img, scale = nanometers_per_pixel) 

viewer.scale_bar.unit = "nm"
viewer.scale_bar.events.visible 


# Add points to image
for i,gen in enumerate(genes):

    # Filter points for gen
    b = df.name == gen 
    points = list(zip(df.x[b],df.y[b]))

    viewer.add_points(points, name = gen, edge_width = 0.01, scale = nanometers_per_pixel,
        face_color= colours[i], size = point_size)                    # experimental_canvas_size_limits = (30,10000))


napari.run()  # start the "event loop" that maintains window open
