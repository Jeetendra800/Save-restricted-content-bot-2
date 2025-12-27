# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20288395"))
API_HASH = getenv("API_HASH", "1245317c7706166809189b4a7918b79c")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8429266518").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://jeetendra2949_db_user:4FE5y1WlDhZSGV1Y@cluster0.glaqca4.mongodb.net/?appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003531892696")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003450386825"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "gplinks.com")
AD_API = getenv("AD_API", "268d43fa6ba600733f85ba12640ced04d5b1eba8")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
