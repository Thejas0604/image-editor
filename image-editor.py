from PIL import Image, ImageEnhance, ImageFilter
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(script_dir, "images")
editedImagesPath = os.path.join(script_dir, "edited-images")

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    if img.mode == 'P':
        img = img.convert('RGB')
    
    edit = img.filter(ImageFilter.SHARPEN)
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(1.5)  
    enhancer = ImageEnhance.Brightness(edit)
    edit = enhancer.enhance(1.2)  
    enhancer = ImageEnhance.Sharpness(edit)
    edit = enhancer.enhance(2.0)  
    #refer docuentation: https://pillow.readthedocs.io/en/stable/index.html
    
    clean_name = f"{os.path.splitext(filename)[0]}_edited.jpg"
    if edit.mode == 'RGBA':
        edit = edit.convert('RGB')
    edit.save(f"{editedImagesPath}/{clean_name}")