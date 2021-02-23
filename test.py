from instabot import Bot
import shutil
import login

def get_photo():
    

def upload():
    
    bot = Bot()
    bot.login(username=login.username,password=login.password)

    caption = """
    hey!
    """

    bot.upload_photo("adam-borkowski-guAPP-fAZMQ-unsplash.jpg", caption = caption)

def delete_photo():
    shutil.rmtree("config")


if __name__ == "__main__":
    photo = get_photo()
    upload(photo)
    delete_photo()
