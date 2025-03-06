#
# Program: placesWorld_CB.py
# Programmer: Charles Blanchard
# Date: November 2024
# Purpose: Create a report file based on user-selected points from a shapefile
#

# import os module
import os

# main function
def main():
    # setting directory/filename

    ## user prompt for output working directory
    qI = QInputDialog()
    title = 'Output Working Directory'
    label = 'Please enter your output directory for the report'
    mode = QLineEdit.Normal
    defVal = 'C:\\temp'

    ### get a value for directory
    outputDir, okDir = QInputDialog.getText(qI,title,label,mode,defVal)

    ### set working directory
    try:
        os.chdir(outputDir)
    except: 
        os.chdir(defVal)

    ## use prompt for output filename
    title = 'Report Filename'
    label = 'Please enter a filename for the report'
    mode = QLineEdit.Normal
    defVal = 'worldplacesreport.txt'

    ### get a value for filename
    filename, okFile = QInputDialog.getText(qI,title,label,mode,defVal)

    ### add .txt extension to filename if not there already
    name, ext = os.path.splitext(filename)
    if ext != ".txt":
        filename += ".txt"
    
    # select active layer as layer
    layer = iface.activeLayer()
    
    # count of selected features, select all points as default
    feature_count = layer.selectedFeatureCount()
    if feature_count < 1:
        layer.selectAll()
        feature_count = layer.selectedFeatureCount()
    
    # store selected points
    features = layer.getSelectedFeatures()
    
    # create data dictionary to store values
    place_dict = {'placesNE':0,'popNE':0, \
            'placesNW':0, 'popNW':0, \
            'placesSE':0, 'popSE':0, \
            'placesSW':0, 'popSW':0, \
            'highPlace':'', 'highPop':0, 'highQuad':'', \
            'lowPlace':'', 'lowPop':0, 'lowQuad':''}
    
    # create list to store place populations
    placePop_list = []
    
    # loop through selected features to determine lat and long of each point
    for place in features:
    
        place_geom = place.geometry()
        long = place_geom.asPoint().x()
        lat = place_geom.asPoint().y()
        
        # call hemisphere functions and concatenate them to determine quadrant
        place_quadrant = getNSHemi(lat) + getEWHemi(long)

        # append population for each place to list
        placePop_list.append(place['pop_max'])
        
        #logic to determine which counter/sum to increment by quadrant
        if place_quadrant == "Northeastern":
            place_dict['placesNE'] += 1
            place_dict['popNE'] += place['pop_max']
            
        elif place_quadrant == "Northwestern":
            place_dict['placesNW'] += 1
            place_dict['popNW'] += place['pop_max']
            
        elif place_quadrant == "Southeastern":
            place_dict['placesSE'] += 1
            place_dict['popSE'] += place['pop_max']
            
        else:
            place_dict['placesSW'] += 1
            place_dict['popSW'] += place['pop_max']
        
        # determine min and max population places
        # if list length = 1, all dictionary fields will be set as only feature
        if len(placePop_list) == 1:
            place_dict['highPlace'] = place['nameascii']
            place_dict['highPop'] = place['pop_max']
            place_dict['highQuad'] = place_quadrant
            place_dict['lowPlace'] = place['nameascii']
            place_dict['lowPop'] = place['pop_max']
            place_dict['lowQuad'] = place_quadrant
        
        else:
            if place['pop_max'] > place_dict['highPop']:
                place_dict['highPlace'] = place['nameascii']
                place_dict['highPop'] = place['pop_max']
                place_dict['highQuad'] = place_quadrant
            
            elif place['pop_max'] < place_dict['lowPop']:
                place_dict['lowPlace'] = place['nameascii']
                place_dict['lowPop'] = place['pop_max']
                place_dict['lowQuad'] = place_quadrant
            
    # clear selected features for next run
    layer.removeSelection()
    
    # setting header/separator string variables for output
    header = "Report of Selected World Places\n" + "="*75 + "\n"
    separator = "="*75 + "\n"
    
    # open and write to report file
    with open(filename, "w") as output:
        
        output.write(header)
        
        output.write("%i northeastern places have a total population of %i\n" % (place_dict['placesNE'], place_dict['popNE']))
        output.write("%i northwestern places have a total population of %i\n" % (place_dict['placesNW'], place_dict['popNW']))
        output.write("%i southeastern places have a total population of %i\n" % (place_dict['placesSE'], place_dict['popSE']))
        output.write("%i southwestern places have a total population of %i\n" % (place_dict['placesSW'], place_dict['popSW']))
        
        output.write(separator)
        
        output.write("The %s place of %s has the highest population of %i\n" % (place_dict['highQuad'], place_dict['highPlace'], place_dict['highPop']))
        output.write("The %s place of %s has the lowest population of %i\n" % (place_dict['lowQuad'], place_dict['lowPlace'], place_dict['lowPop']))

# latitude function
def getNSHemi(y):
    # return N/S for each lat (y) coordinate
    if y >= 0:
        return "North"
    
    else:
        return "South"


# longitude function
def getEWHemi(x):
    # return E/W for each long (x) coordinate
    if x >= 0:
        return "eastern"
    
    else:
        return "western"
# call main function
main()