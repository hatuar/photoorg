#
# A simple duplicate photo remover based on MD5 hashing
#


import io,sys, argparse
import hashlib
from pathlib import Path
from PIL import Image

def getImageHash(img):
    """ Calculates md5 hash for a given Pillow image. """
    md5hash =  hashlib.md5(img.tobytes())
    return md5hash.hexdigest()


# Entry point

parser = argparse.ArgumentParser(description="A Simple duplicate remover")
parser.add_argument('source', help="source directory")
parser.add_argument('destination',  help="destination (dump) directory")


args=parser.parse_args()

sourcePath = Path(args.source) 
destPath = Path(args.destination)
imgHashMap = set()  #in-memory store of image hash. BerkeleyDb could be used for a large image set
movedCounter = 0

print(f"sourcePath:{sourcePath} destPath:{destPath}")

if not destPath.is_dir():
    destPath.mkdir(parents=True, exist_ok=True)


pathlist = sourcePath.glob('**/*.jpg')

for path in pathlist:

    hashCode = getImageHash(Image.open(path))
    print(f"Processing image {path} with hash {hashCode}...")

    if hashCode in imgHashMap:  #if True, we have a duplicate
        print(f"** Image {path} found to be a duplicate, moving to {destPath}.")
        path.rename(destPath / path.name)
        movedCounter = movedCounter + 1
    else:  # do not move the file, but add hashcode to set instead
        imgHashMap.add(hashCode)

print(f"Done! {len(imgHashMap)} photos were processed and {movedCounter} duplicates were moved to {destPath}.")



        


