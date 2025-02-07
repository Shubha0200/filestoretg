import os
import logging
from logging.handlers import RotatingFileHandler

# Fetch environment variables (remove sensitive data from default values)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

OWNER_ID = int(os.environ.get("OWNER_ID"))
DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL"))

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
