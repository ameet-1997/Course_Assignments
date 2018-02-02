from PIL import Image
import glob

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

def write_d(file_name, data):
    f = open(file_name, "w")
    f.write(header)
    f.write("%d %d\n"%(len(data),len(data[0])))
    for j  in xrange(len(data[0])):
        for i in xrange(len(data)):
            f.write("%d\n"%data[i][j])

splits = ["Test", "Train"]
classes = ["mountain", "forest"]
labels = {}
labels["mountain"] = -1
labels["forest"] = 1

# The header present at the start of the file
header = "%%MatrixMarket matrix array real general\n"
for split in splits:
    all_features = []
    class_labels = []
    features_file =  split + "_features"
    labels_file = split + "_labels"
    for clas in classes:
        # Read all files from the Train Files and Test files
        for filename in glob.glob(clas + "/" + split + '/*.jpg'): #assuming gif
            im=Image.open(filename)
            # Get the data from the file
            # http://effbot.org/imagingbook/image.htm - getdata() documentation
            data = im.getdata()
            all_features.append(features(data))
            class_labels.append([labels[clas]])
    write_d(features_file, all_features)
    write_d(labels_file, class_labels)
