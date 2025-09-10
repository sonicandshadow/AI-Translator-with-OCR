import tesserocr
from PIL import Image, ImageGrab


# def get_screenshot(selected_zone):
#     screenshot = ImageGrab.grab(selected_zone)
#     screenshot.save("image.png")

# def get_text(lang):
#     img = Image.open('../image.png')
#     Image._show(img)
#     result = tesserocr.image_to_text(img, lang=lang)
#     return result