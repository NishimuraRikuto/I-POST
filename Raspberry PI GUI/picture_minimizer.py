from PIL import Image
import os

def compress(image_file):

    filepath = os.path.join(os.getcwd(), image_file)

    image = Image.open(filepath)

    image.save("image-file-compressed.PNG",
                 "PNG",
                 optimize = True,
                 quality = 10)
    return

# compress("I-POST_icon.JPEG")