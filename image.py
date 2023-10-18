from PIL import Image
from io import BytesIO

def convert_to_png(path):
    image = Image.open(path)
    image = image.convert('RGB')
    png_data = BytesIO()
    image.save(png_data, format='PNG')
    png_data.seek(0)
    return png_data