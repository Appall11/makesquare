from PIL import Image
import os

def make_square(im, min_size=256, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def make_image(directory):
    old_image = Image.open(directory)
    return make_square(old_image)

old_image_directory = "E:/Photos" # Change your old file dir here
new_image_directory = "E:/Photossqr" # Enter your new file dir here

for img in os.listdir(old_image_directory):
    try:
        temp_directory = os.path.join(old_image_directory, img)
        temp_image = make_image(temp_directory)

        temp_directory = os.path.join(new_image_directory, img)
        temp_image.save(temp_directory, 'JPEG')
    except Exception as e:
        pass

print('finished')
