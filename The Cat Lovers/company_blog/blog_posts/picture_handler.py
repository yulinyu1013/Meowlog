import os
# pip install pillow
from PIL import Image

from flask import url_for, current_app

def add_post_pic(pic_upload):

    filename = pic_upload.filename
    # Grab extension type .jpg or .png
    # storage_filename = str(username) + '.'+filename
    filepath = os.path.join(current_app.root_path, 'static/post_pics', filename)

    # Play Around with this size.
    output_size = (300, 300)

    # Open the picture and save it
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return filename;
