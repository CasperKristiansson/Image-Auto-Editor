import textwrap
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def motivation_file(start_directory):
    backgrounds = []
    backgrounds_name = []

    os.chdir('create_photos')
    directory = os.listdir(os.curdir)

    for file in directory:
        backgrounds.append(Image.open(file))
        backgrounds_name.append(file)

    os.chdir(start_directory)

    return backgrounds, backgrounds_name

def image_editor(backgrounds, backgrounds_name):
    random.shuffle(backgrounds)
    for background in backgrounds:
        try:
            background_name = backgrounds_name[backgrounds.index(background)]

            current_index = backgrounds.index(background)
            width, height = background.size

            if width >= 1080 or height >= 1080:
                if width < height:
                    size_parameter = (1080 / width)
                else:
                    size_parameter = (1080 / height)

                width = int(size_parameter * width)
                height = int(size_parameter * height)
                background = background.resize((width, height))

            if width >= 1080 and height >= 1080:
                width_correction = 0
                height_correction = 0
                if width < height:
                    height_correction = (height - 1080) / 2
                else:
                    width_correction = (width - 1080) / 2
                
                left = width_correction
                top = height_correction
                right = width - width_correction
                bottom = height - height_correction

                background = background.crop((left, top, right, bottom))
                width, height = background.size
            
                background.save('image_gallary\\{}'.format(background_name))

                print("{}/{}".format(current_index + 1, len(backgrounds)))

        except Exception as e:
            print(e)
        
if __name__ == '__main__':
    START_DIRECTORY = os.getcwd()
    BACKGROUNDS, BACKGROUNDS_NAME = motivation_file(START_DIRECTORY)
    image_editor(BACKGROUNDS, BACKGROUNDS_NAME)
