#!/bin/python

# 1. Save this file to your local machine where you want to save the files
# 2. Change 'manuscript' to the one you want
# 3. Change 'lastItem' to the last numbered item of the text section of the manuscript
# 4. Add a directory 'jpgs' that the images will be stored in
# 5. Run "python PennInHand_grabber.py"

import sys
import urllib

manuscript = raw_input('Enter a manuscript id (ex: mscodex728): ')
count = int(raw_input('How many items do you want to get? '))
firstItem = int(raw_input('Which number do you want to start with? '))

#manuscript="mscodex728"
#firstItem=1
#lastItem=3

def grabber(manuscript, count, firstItem = 1):

  for n in range(firstItem , firstItem + count):
    print 'Getting %(man)s-%(num)04d.jpg.' % {"man": manuscript, "num": n}
    goFetch = "https://repo.library.upenn.edu/djatoka/resolver?url_ver=Z39.88-2004&svc_id=info:lanl-repo/svc/getRegion&svc_val_fmt=info:ofi/fmt:kev:mtx:jpeg2000&svc.format=image/jpeg&rft_id=medren_%(man)s_wk1_body%(num)04d&svc.level=7&svc.rotate=0" % {"man": manuscript , "num": n}
    filename = "jpgs/%(man)s-%(num)04d.jpg" % {"man":manuscript, "num":n}
    urllib.urlretrieve(goFetch, filename)

grabber(manuscript, count, firstItem)
