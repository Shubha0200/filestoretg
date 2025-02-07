importimport os
import logging
from logging.handlers import RotatingFileHandler

# Fetch bot details from environment variables or default values
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7474955516:AAG6hNIVmwFYtZwi1WW0H3d5GX7Ihh4gQbQ")
API_ID = int(os.environ.get("API_ID", "21459238"))
API_HASH = os.environ.get("API_HASH", "0cef1924d139587654bc18402d2b512d")

# Fetch MongoDB and other settings from environment variables
OWNER_ID = int(os.environ.get("OWNER_ID", "1782088532"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://shubhashankar246:nEWTylzLZpiuysRh@cluster0.kpecd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "shubhashankar246")

# Fetch channel information
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002448726887"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002268761887"))

# Handle file auto delete
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600"))  # auto delete in seconds

# Fetch the port and number of workers
PORT = int(os.environ.get("PORT", "8080"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Parse ADMINS list
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "1782088532").split()]
except ValueError as e:
    raise Exception(f"Invalid ADMINS list format: {e}")

# Optional: Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Bot configuration loaded.")


   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
