# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20373203"))
API_HASH = getenv("API_HASH", "8962717c7c708e210f66ea658db58d85")
BOT_TOKEN = getenv("BOT_TOKEN", "8079880677:AAF4RECXE9B2on3l-jJPDb_gUw8zl9_0j5M")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7369976226").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://dafeh64648:dxkiXApD489QKbjN@ramsingh.o0kha.mongodb.net/?retryWrites=true&w=majority&appName=Ramsingh")
LOG_GROUP = getenv("LOG_GROUP", "-1002380048510")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002302432707"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
