import os
import logging
from logging.handlers import RotatingFileHandler

# Fetch environment variables (remove sensitive data from default values)
BOT_TOKEN = os.environ.get("7474955516:AAG6hNIVmwFYtZwi1WW0H3d5GX7Ihh4gQbQ")
API_ID = int(os.environ.get("21459238"))
API_HASH = os.environ.get("0cef1924d139587654bc18402d2b512d")

OWNER_ID = int(os.environ.get("1782088532"))
DB_URL = os.environ.get("mongodb+srv://shubhashankar246:nEWTylzLZpiuysRh@cluster0.kpecd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("shubhashankar246")

CHANNEL_ID = int(os.environ.get("1002448726887"))
FORCE_SUB_CHANNEL = int(os.environ.get("-1002268761887aa"))

FILE_AUTO_DELETE = int(os.environ.get("FILE_AUTO_DELETE", "600"))  # auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Ensure ADMINS is correctly populated from environment variables
ADMINS = [int(x) for x in os.environ.get("ADMINS", "1782088532").split()]

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION")

# Convert PROTECT_CONTENT and DISABLE_CHANNEL_BUTTON to booleans
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "True") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True"

# Messages
BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"
START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")

# Log file name
LOG_FILE_NAME = "filesharingbot.txt"

# Setup logging configuration
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

   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
