#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7483356409:AAHTmIlwRqGhzCdir8UnDVyK_y2BLjz1J_g")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28723622"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1a997c00c1209441a20c0b0f13fdfa54")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002218265816"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6038637868"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://rjkundra:Kayamkhani@cluster0.s6lvxxs.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "primeurl.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "949d9d69a9b11a5ab02ba9ad3f955fcfa7131a80")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 3600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/howtoopenlinkksss/9")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002000107085"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1466271043").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5837577167)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
