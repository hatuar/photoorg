#
# A simple photo organizer (c) Harri Artinaho 2020.
# 
#

import sys, argparse
from pathlib import Path
from PIL import Image,ExifTags

def getExifCode(tagName):
    """ Returns an Exif Code for given tag name (string). """
    for key,val in ExifTags.TAGS.items():
        if str(val) == tagName:
            return key


def isPathExcluded(curPath,excludePath):
    """ Returns True if excludePath is part of parameter curPath, otherwise False. """
    try:
        curPath.relative_to(excludePath)
        return True
    except ValueError:
        return False


# Entry point

parser = argparse.ArgumentParser(description="Simple photo organizer")
parser.add_argument('source', help="source directory")
parser.add_argument('destination',  help="destination directory")
parser.add_argument('exclude',  help="exclude directory")

args=parser.parse_args()

sourcePath = Path(args.source) 
destPath = Path(args.destination)
excludePath = Path(args.exclude)

print(f"sourcePath:{sourcePath} destPath:{destPath} exclude: {excludePath}.")

pathlist = sourcePath.glob('**/*.jpg')
dtKey = getExifCode('DateTime')

#loop paths with jpg's and process images
for path in pathlist:
    print(f"Processing path {path}.")

    if isPathExcluded(path,excludePath):
        print(f"Path {path} is excluded.")
        continue  #We don't process images which are located under 'excludePath'

    img = Image.open(path)
    exifDict = dict(img.getexif())
    exifDate = exifDict.get(dtKey)    
   
    if exifDate:
        destDate = f"{exifDate[0:4]}_{exifDate[5:7]}_{exifDate[8:10]}" 
    else:
        destDate = "1900_01_01" # A default date for photos without exifDate field

    print(f"Processing image {path} with date: {destDate}")
    destFileName = f"{destDate}_{path.name}"   
    destFolder = destPath / destDate

    if not destFolder.is_dir():
        destFolder.mkdir(parents=True, exist_ok=True)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(destFolder / destFileName)












        



