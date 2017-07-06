#Pass in a photo url to the script and it performs 5 label detection on the photo.

import sys
import argparse
import io

from google.cloud import vision


#capture the argument passed in to script
url=sys.argv[1]

client = vision.Client()
#pass commange line url into uri
image = client.image(source_uri=url)
labels = image.detect_labels(limit=5)

for i in range (0,5):
  x=labels[i].description
  y=labels[i].score
  print x
  print y
