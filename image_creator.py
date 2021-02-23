import textwrap
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def draw_multiple_line_text(image, text, font, text_color, text_start_height, width):
    draw = ImageDraw.Draw(image)

    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=width*0.04)

    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),
                  line, font=font, fill=text_color)
        y_text += line_height

def add_text(background, text, width):
    fontsize = 55
    font = ImageFont.truetype("dosis\\Dosis v1.7\\Dosis-Bold.ttf", fontsize)

    text_color = (255,255,255)

    text_count = text.count('')
    text_count = text_count / 30

    text_start_height = 540 - (28*text_count)

    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.45)

    draw_multiple_line_text(background, text, font, text_color, text_start_height, width)

    return background

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

def image_editor(backgrounds, backgrounds_name, quote_list):
    random.shuffle(quote_list)
    random.shuffle(backgrounds)
    for background in backgrounds:
        background_name = backgrounds_name[backgrounds.index(background)]
        text = quote_list[backgrounds.index(background)]

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

            background = add_text(background, text, width)
            try:
                background.save('image_gallary\\{}'.format(background_name))
            except Exception as e:
                print(e)

            print("{}/{}".format(current_index + 1, len(backgrounds)))

def get_list():
    with open('quote.txt', 'r', encoding="utf8") as lines:
        quotes_list = [line.strip() for line in lines]

    quotes_list = [x for x in quotes_list if '”' in x ]

    return quotes_list

if __name__ == '__main__':
    START_DIRECTORY = os.getcwd()
    QUOTE_LIST = get_list()
    BACKGROUNDS, BACKGROUNDS_NAME = motivation_file(START_DIRECTORY)
    image_editor(BACKGROUNDS, BACKGROUNDS_NAME, QUOTE_LIST)
