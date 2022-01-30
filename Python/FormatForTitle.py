import os
import re

# Rules for correct title formatting taken from http://www.superheronation.com/2011/08/16/words-that-should-not-be-capitalized-in-titles/

uncapitalised = ["the", "a", "an", "for", "and", "nor", "but", "yet", "so", "at", "around", "by", "after", "along", "for", "from", "of", "on", "to", "with", "without"]

# Formats the supplied string as to be suitable as a title
# e.g "star wars: return of the jedi" -> Star Wars: Return of the Jedi
def formatForTitle(title):
    title=re.split(', | |_|\n|: ',title)
    # Always capitalise first and last words
    title[0] = title[0].capitalize()
    title[-1] = title[-1].capitalize()
    # Iterate over remaining words
    i=1
    while i < len(title) - 1:
        if title[i] not in uncapitalised:
            title[i] = title[i].capitalize()
        i+=1
    return " ".join(title)


path = "C:\\Users\\damia\\Documents\\VideoColourAnalyser\\VideoColourAnalyser\\VideoData" 

# format all the file names in path to be titles
[os.rename(os.path.join(path, filename), os.path.join(path, formatForTitle(filename)).replace('_', ' ')) for filename in os.listdir(path)]

for file in os.listdir(path):
    file = path + "\\" + file
    if (os.path.isdir(file)):
        [os.rename(os.path.join(path, filename), os.path.join(path, formatForTitle(filename)).replace('_', ' ')) for filename in os.listdir(path)]

       

