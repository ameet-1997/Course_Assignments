"""
Code to go through the folders and pick the image files,
convert them to features and write to a csv file
Some of the code from Professor Boyd's folder has
been modify to be compatible with Pandas Dataframe

Author: Ameet Deshpande
RollNo: CS15B001
"""


from PIL import Image
import glob
import pandas as pd
from pandas import DataFrame

def features(data):
    # Evaluates to 65536, which is 256^2
    rows = len(data)
    cols = len(data[0])
    # All RGB values are stored one after another
    all_features = []
    # Using xrange to evaluate the sequence objects lazily
    for j in xrange(cols):
        # Rescale the 256 pixel intensities into bins and thus 256/8=32 bins are used
        bins = [0]*32
        for i in xrange(rows):
            bins[data[i][j]/8] += 1
        all_features.extend(bins)
    return all_features

splits = ["Test", "Train"]
classes = ["mountain", "forest", "insidecity", "coast"]
labels = {}
labels["mountain"] = [0]
labels["forest"] = [1]
labels["insidecity"] = [2]
labels["coast"] = [3]

for split in splits:
    all_features = []
    class_labels = []
    # features_file =  split + "_features.csv"
    # labels_file = split + "_labels.csv"
    for clas in classes:
        # Read all files from the Train Files and Test files
        for filename in glob.glob(clas + "/" + split + '/*.jpg'): #assuming gif
            im=Image.open(filename)
            # Get the data from the file
            # http://effbot.org/imagingbook/image.htm - getdata() documentation
            data = im.getdata()
            all_features.append(features(data))
            class_labels.append(labels[clas])

    # Convert list of lists to a DataFrame
    all_features = DataFrame(all_features)
    class_labels = DataFrame(class_labels)

    # Appends to a file called DS2-train/test.csv with last column as labels
    all_features = pd.concat([all_features, class_labels], axis=1)
    all_features.to_csv("DS2-"+split.lower()+".csv", header=False, index=False)