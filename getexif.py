#!/usr/bin/env python

import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

ok = ['DateTime', 'DateTimeOriginal', 'DateTimeDigitized', 'GPSInfo']

if len(sys.argv) == 1:
    print 'Pass image filename to analyse exif data'
    sys.exit(0)

img = Image.open(sys.argv[1])
exif_data = img._getexif()
if exif_data:
    for tag, data in exif_data.iteritems():
        tag_decoded = TAGS.get(tag, tag)
        if tag_decoded in ok:
            if tag_decoded == 'GPSInfo':
                gps_data = {}
                for d in data:
                    gps_decoded = GPSTAGS.get(d, d)
                    print gps_decoded, d
            else:
                print tag_decoded, data

# more examples: https://gist.github.com/erans/983821
