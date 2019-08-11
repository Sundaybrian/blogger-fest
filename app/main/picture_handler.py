import os
from PIL import Image 
from flask import url_for,current_app

def add_profile_pic(pic_upload,username):

    filename=pic_upload.filename #sunny.jpg
   
    ext_type=filename.split('.')[-1]  #sunny '.' 'jpg'
 
    storage_filename=str(username)+'.'+ext_type #username.jpg

    filepath=os.path.join(current_app.root_path,'static/photos',storage_filename)

    output_size=(200,200)
    pic=Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
