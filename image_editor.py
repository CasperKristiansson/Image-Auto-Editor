import os
from PIL import Image

def motivation_file(start_directory):
    backgrounds = []
    backgrounds_name = []

    os.chdir('image_gallary')
    directory = os.listdir(os.curdir)

    for file in directory:
        backgrounds.append(Image.open(file))
        backgrounds_name.append(file)

    os.chdir(start_directory)

    return backgrounds, backgrounds_name

def logo(start_directory):
    os.chdir('logo')
    directory = os.listdir(os.curdir)

    logo_image = Image.open(directory[0])
    logo_image = logo_image.resize((220, 77))
    os.chdir(start_directory)

    return logo_image

def add_images(backgrounds, logo_image, backgrounds_name):
    for background in backgrounds:
        current_logo = logo_image
        background_name = backgrounds_name[backgrounds.index(background)]

        current_index = backgrounds.index(background)
        width, height = background.size

        width_location = int(width / 2.5)
        height_location = int(height * 0.93)

        background.paste(current_logo, (width_location, height_location), current_logo)
        background.save('images\\{}'.format(background_name))

        print("{}/{}".format(current_index + 1, len(backgrounds)))

if __name__ == '__main__':
    START_DIRECTORY = os.getcwd()
    BACKGROUNDS, BACKGROUNDS_NAME = motivation_file(START_DIRECTORY)
    LOGO = logo(START_DIRECTORY)
    add_images(BACKGROUNDS, LOGO, BACKGROUNDS_NAME)
