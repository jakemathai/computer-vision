#This python script loads a photo and performs landmark detection
from google.cloud import vision

client = vision.Client()
image = client.image(source_uri='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Golden_Gate_Bridge_as_seen_from_Fort_Point.jpg/1920px-Golden_Gate_Bridge_as_seen_from_Fort_Point.jpg')

landmarks = image.detect_landmarks()
print landmarks[0].description
