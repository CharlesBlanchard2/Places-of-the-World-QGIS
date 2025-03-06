# Places-of-the-World-QGIS 
## Made for Assignment 2 of PROG 5000 (Programming Fundamentals for Geographic Sciences) at NSCC - Centre of Geographic Sciences

### This code is produced by Charles Blanchard as a student project towards the completion of the Geographic Information Systems Program at the Centre of Geographic Sciences, NSCC, Lawrencetown, Nova Scotia. <br> This product is unedited, unverified, and intended for educational purposes only. <br> ©2024 COGS. 

## How to Run – placesWorld_CB.py within QGIS
### Step 1
Begin by opening QGIS 3.38.2-Grenoble, and make sure you have Python version 3.x installed. Navigate to Project > New, then click to create a new project. 
### Step 2
In your new project, navigate to Layer > Add Layer > Add Vector Layer. Click the ellipses next to Source > Vector Dataset(s), then browse your computer for your valid places shapefile(s). 

### Step 3
Click on your selected layer(s) for analysis in the Layers pane to set it as your active layer. The layer should be highlighted blue once you have selected it. 

### Step 4
Select any points on the map you want to analyze via right clicking your selected layer(s) and clicking Open Attribute Table. From this screen you can use selection queries to select your desired points, or simply select manually by clicking on a row.

If no points are selected the script will default to all points available.

### Step 5
Save your project. Next, navigate to Plugins > Python Console. Click Show Editor within the Python Console. A new editor pane should open at the bottom right of your screen. Within the editor pane click Open Script. Browse to placesWorld_CB.py and open it. 







### Step 6
Click Run Script. A window will open asking for an output working directory for your place report. Enter any valid Windows path to a folder and click OK.

Caution: If you enter an invalid path the script will default to C:\temp. See Appendix A for examples of valid and invalid paths.

### Step 7
Another window will open asking for a file name for the output report text file. Enter any Windows-permitted name for a file and click OK. If your file name does not contain a .txt extension, one will be appended to the end of the name.

 




### Step 8
A report file stating the number of selected places in each global quadrant as well as the total population by quadrant and highest/lowest population places will be created in your selected directory. Open this file in your text editor of choice and view your results! A selection of reports are located in Appendix B for further viewing.



## Appendix A
Examples of valid and invalid path names for output directory
Valid:
  Default directory
  A copied path from an accesible folder
Invalid:
  Random text string
  Forward slash instead of backslash
  Double backslashes

## Appendix B
Final Reports
Three different shapefiles selected as active layer; no points selected:  
One shapefile selected as active layer; no points selected:
  
One shapefile selected as active layer; five points selected:
  
  


