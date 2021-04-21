import sys
import os
from PIL import Image

#grab the first and second argument ( pokedex 1 and new folder for putting that jpg to png converted images in that folder)
image_folder = sys.argv[1]
output_folder = sys.argv[2]



# check if new folder exists if not then we have to create to put the images
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


for filename in os.listdir(image_folder):
  img = Image.open(f'{image_folder}{filename}')
  clean_name = os.path.splittext(filename)[0]
  img.save(f'{output_folder}{clean_name}.png', 'png')
  print('all done!')

# loop through the pokedex1 
#convert images to png
# save to the new folder. 


