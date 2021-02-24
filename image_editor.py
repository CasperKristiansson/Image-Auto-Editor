import textwrap
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

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

def logo(start_directory):
    os.chdir('logo')
    directory = os.listdir(os.curdir)

    logo_image = Image.open(directory[0])
    logo_image = logo_image.resize((220, 77))
    os.chdir(start_directory)

    return logo_image

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

def add_images(backgrounds, logo_image, backgrounds_name, quote_list):
    random.shuffle(quote_list)
    random.shuffle(backgrounds)
    for background in backgrounds:
        current_logo = logo_image
        background_name = backgrounds_name[backgrounds.index(background)]
        text = quote_list[backgrounds.index(background)]

        current_index = backgrounds.index(background)
        width, height = background.size

        width_location = int(width / 2.5)
        height_location = int(height * 0.93)

        background = add_text(background, text, width)

        background.paste(current_logo, (width_location, height_location), current_logo)
        background.save('images\\{}'.format(background_name))

        print("{}/{}".format(current_index + 1, len(backgrounds)))

def get_list():
    with open('quote.txt', 'r', encoding="utf8") as lines:
        quotes_list = [line.strip() for line in lines]

    quotes_list = [x for x in quotes_list if '”' in x ]

    return quotes_list

if __name__ == '__main__':
    START_DIRECTORY = os.getcwd()
    BACKGROUNDS, BACKGROUNDS_NAME = motivation_file(START_DIRECTORY)
    LOGO = logo(START_DIRECTORY)
    QUOTE_LIST = get_list()
    add_images(BACKGROUNDS, LOGO, BACKGROUNDS_NAME, QUOTE_LIST)
    
