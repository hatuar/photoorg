# Photo organizer cmd line tool
A simple photo (jpg) organizer I use for my personal photo collection.

The tool will scan a given directory for *jpg* photos, and move them to destination folder. In the process, the tool will
reorganize, and rename photos based on the Exif date. If the Exif-date is not found, a default *1900_01_01* will be used.


Usage: picorg.py [-h] source destination exclude

Where 
* source = source directory to scan photos
* destination = destination directory to copy photos to
* exclude = a directory which will be excluded from scanning, currently only one location is supported.
