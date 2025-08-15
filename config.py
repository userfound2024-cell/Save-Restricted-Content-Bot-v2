# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "23643076"))
API_HASH = getenv("API_HASH", "25bf494f099ade9f98697850843d8d0d")
BOT_TOKEN = getenv("BOT_TOKEN", "8204023740:AAH9C07_UVMws_PDrOuou3UyJrnW_Rw_oog")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8487565900").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://usernotfound7603:3yWa4gxUVKxrIkkp@cluster0.jdgnbaz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "https://t.me/loggroup2p")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002509173982"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
