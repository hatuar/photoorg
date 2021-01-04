# Photo organizer cmd line tools

These are some tools I use organizing my photo collection. No warranty, use at your own risk.

## picorg

A simple photo (jpg) organizer I use for my personal photo collection.

The tool will scan a given directory for *jpg* photos, and move them to destination folder. In the process, the tool will
reorganize, and rename photos based on the Exif date. If the Exif-date is not found, a default *1900_01_01* will be used.


Usage: python3 picorg.py [-h] source destination exclude

Where 
* source = source directory to scan photos
* destination = destination directory to copy photos to
* exclude = a directory which will be excluded from scanning, currently only one location is supported.

## dupremover

Removes duplicate photos from a given source directory by moving them to a given (destination) directory (aka 'dump' folder). Duplicate identification is done by calculating MD5 hash for image content (excl. exif).

Usage: python3 dupremover [-h] source destination

Where
* source = source directory to scan photos (duplicates will be moved out!)
* destintion = a directory where duplicate photos will be moved to
