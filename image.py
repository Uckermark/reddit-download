from PIL import Image
from io import BytesIO

def convert_to_png(path):
    image = Image.open(path)
    image = image.convert('RGB')
    image = resize_image(image, 512)
    png_data = BytesIO()
    image.save(png_data, format='PNG')
    png_data.seek(0)
    return png_data

def resize_image(image, target_size):
    original_width, original_height = image.size
    if original_width <= original_height:
        new_width = target_size
        new_height = int(target_size * (original_height / original_width))
    else:
        new_height = target_size
        new_width = int(target_size * (original_width / original_height))
    resized_image = image.resize((new_width, new_height))
    return resized_image

if __name__ == '__main__':
    import sys
    import os
    folder_path = sys.argv[1]
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        sys.exit(1)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_path = os.path.join(root, file)
                image = Image.open(image_path)
                resized_image = resize_image(image, 512)
                resized_image.save(image_path)
                print(f"Resized {image_path}", flush=True)