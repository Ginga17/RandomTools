import os

directory = "C:\\Users\\damia\\Downloads\\VideoData"
# Replaces all underscores in file names with spaces in the target directory
# Replaces underscores in directory
[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('_', ' ').lower()) for f in os.listdir(directory)]

# Replaces underscores in subdirectories
for file in os.listdir(directory):
    file = directory + "\\" + file
    if (os.path.isdir(file)):
        [os.rename(os.path.join(file, filename), os.path.join(file, filename).replace('_', ' ')) for filename in os.listdir(file)]


