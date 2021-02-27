import shutil
import os
from instabot import Bot
import login

def check_images(start_directory):
    os.chdir('images')
    directory = os.listdir(os.curdir)
    os.chdir(start_directory)

    if len(directory) == 0:
        #os.system('python image_creator.py')
        os.system('python image_editor.py')

def get_images(start_directory):
    os.chdir('images')
    directory = os.listdir(os.curdir)

    image = directory[0]
    shutil.move(image, start_directory)
    os.chdir(start_directory)

    return image

def upload(image):
    shutil.rmtree("config")
    bot = Bot()
    bot.login(username=login.username, password=login.password)

    caption = """
    ...
    —————————————————
    #quotes #quote #quoteoftheday #quotestoliveby #quotestagram #quotesoftheday #quotesdaily #quotesaboutlife #quotestags #quotesgram #motivation #motivationalquotes #motivational #motivationmonday #motivationalquote #MotivationalSpeaker #motivationalmonday #motivations #inspiration #inspirationalquotes #inspirational #inspirationalquote #inspirations #inspirationoftheday #inspirationalwords #inspirationcultmag
    """
    try:
        bot.upload_photo(image, caption = caption)
    except:
        delete_photo()
        main()

def delete_photo(start_directory):
    os.chdir(start_directory)
    directory = os.listdir(os.curdir)
    for file in directory:
        if ".REMOVE_ME" in file:
            os.remove(file)

def main():
    START_DIRECTORY = os.getcwd()
    check_images(START_DIRECTORY)
    IMAGE = get_images(START_DIRECTORY)
    upload(IMAGE)
    delete_photo(START_DIRECTORY)

if __name__ == "__main__":
    main()
