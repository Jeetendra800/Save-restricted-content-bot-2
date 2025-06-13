# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28036362"))
API_HASH = getenv("API_HASH", "84e4bd8457dab2f065801bde8874842a")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7782401729").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://vevob65684:CBT55WcRjWUf0GvN@cluster0.dfd6s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002596328286")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002413032052"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", ""))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "gplinks.com")
AD_API = getenv("AD_API", "268d43fa6ba600733f85ba12640ced04d5b1eba8")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
