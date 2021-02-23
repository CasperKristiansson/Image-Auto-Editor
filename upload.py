from instabot import Bot
import shutil
import login
import os

def get_photo(start_directory):
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
    #motivation #motivationalquotes #motivational #motivationmonday #motivationalquote #MotivationalSpeaker #motivationalmonday #motivations #motivationquotes #motivationquote #motivationalwords #MotivationMafia #motivationalpost #motivationdaily #motivationforfitness #motivationmondays #motivationalfitness #motivationgym #motivation101 #motivationalquoteoftheday #motivationoftheday #MotivationFitness #motivationalspeakers #motivationmusic #motivationalmondays #motivationiskey #motivationtuesday #motivationalquotesoftheday #motivationalspeaking #motivationforlife
    """

    bot.upload_photo(image, caption = caption)

def delete_photo(start_directory):
    os.chdir(start_directory)
    directory = os.listdir(os.curdir)
    for file in directory:
        if ".REMOVE_ME" in file:
            os.remove(file)

if __name__ == "__main__":
    START_DIRECTORY = os.getcwd()
    IMAGE = get_photo(START_DIRECTORY)
    upload(IMAGE)
    delete_photo(START_DIRECTORY)
