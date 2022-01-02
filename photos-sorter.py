import os, random
from PIL import Image
from PIL.ExifTags import TAGS


files = os.listdir(".")

for file in files:

    # check the image format
    if file.endswith(".jpg") or file.endswith(".png"): 
        # read the image data using PIL lib
        image = Image.open(file)
        # extract EXIF data
        exifdata = image.getexif()
        
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)            
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            new_name = ""

            if(tag == "DateTime"):
                # rename file with datetime
                tmp = data.split()[0].split(":")
                new_name = tmp[2] + "-" + tmp[1] + "-" + tmp[0] + "-"
                # add random id for duplicate photos 
                image.save(new_name + str(random.randint(111111, 999999)) + ".jpg", "JPEG")
    
    else:
        continue

