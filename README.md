# Polylux_python                

*A Napari app to visualize microscopy images with spatial coordinates of transcripts and cell boundries (roifiles)*

**Resolve Biosciences**
_________________
    

### INSTALLATION:
 You need Python installed. Run the following in your command prompt:    
 - To create a separate conda environment (Optional):     
    -   ```   conda create -y -n napari-env -c conda-forge python=3.9 ```     
    -   ```   conda activate napari-env      ```  
   
  - Install napari library     
    - ```pip install "napari[all]"     ```      
    - ```pip install "napari[all]" --upgrade    ```       
    - ```pip install pandas ```      
 
More information here: https://napari.org/tutorials/fundamentals/installation.html
### RUNNING:
1) Edit INPUTS AREA of the script path to the input files and genes of interest
2) Enter a command prompt and change directory (cd) to where the script is located
3) Run the script: python polylux_python.py          
 


___________________________________

 ATTENTION: There is a bug related to changing point sizes and colors that can only be fixed by the Napari creators.
 If you want to change the size or color of the points of a gene, you have to:
    - Select the gene in the lower left pannel
    - Click on the mouse pointer icon on the top left pannel
    - Select the area where the points of this transcript should change (if you want to change all points of the transcript, you should be zoomed out first)
    - Change the color/size on the top left pannel
    - Click on the zoom icon (magnifier glass) to be able to navigate again.
