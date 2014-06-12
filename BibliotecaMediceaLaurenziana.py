#!/bin/python

# 1. Save this file to your local machine where you want to save the files
# 2. Change 'manuscript' to the one you want
# 3. Change 'lastItem' to the last numbered item of the text section of the manuscript
# 4. Add a directory 'jpgs' that the images will be stored in
# 5. Run "python PennInHand_grabber.py"

import sys
import urllib

manuscript = raw_input('Enter a TECA number (six digits, including leading zeroes): ')
count = int(raw_input('How many items do you want to get? '))
firstItem = int(raw_input('Which number do you want to start with? '))

#manuscript="mscodex728"
#firstItem=1
#lastItem=3

def grabber(manuscript, count, firstItem = 1):

  for n in range(firstItem , firstItem + count):
    print 'Getting %(man)s-%(num)04d' % {"man": manuscript, "num": n}
    goFetch = "http://teca.bmlonline.it/ImageViewer/servlet/ImageViewer?idr=TECA%(man)s%(num)04d&azione=showImg&sequence=7&reduce=2&mode=2&height=539" % {"man": manuscript , "num": n}
    filename = "jpgs/%(man)s-%(num)04d.jpg" % {"man":manuscript, "num":n}
    urllib.urlretrieve(goFetch, filename)

grabber(manuscript, count, firstItem)