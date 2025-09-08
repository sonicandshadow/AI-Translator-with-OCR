import tesserocr
from PIL import Image


def get_text(lang):
    img = Image.open('../image.png')
    Image._show(img)
    result = tesserocr.image_to_text(img, lang=lang)
    return result
