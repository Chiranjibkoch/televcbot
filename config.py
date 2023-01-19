## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "AQB_lYGE3_cDF5o_b34GOUM9DnAhCmQeSXN4Rn_OcLT8LppTm9RdyAAd_SlkXgcbfcDnJfuEw25NdJKU6BfUsIbQ0BmTIkOQBzY1H3qKVdUD1P23yH1HwD6ULRT0E591dkUyRio3IZYlzyQw6WE4gBIJym6ysO6pOyHZMTXnt6x4C6YqLakETnbGTL9dv5i3wI8eOoI9o9kn3MqG9yJZ25bQOra2fZwLjoSEn-zsqbitilPTd9AK7v_rNPW80F3gjwHd4oXiwJ2-688YwDz2l1jPcYJ7lSC9jRxYy7InKdioe9G5T1sjHY2Ez88-44pDSKCeT5pr-kZthqbCQznpBamEAAAAATkDVoAA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5637535086:AAFZgINmneBrW1DvnPnT1hOFSjUFzUjTnIM")
BOT_NAME = getenv("BOT_NAME", "SUKOON MUSIC ASSISTANT")

API_ID = 21309577
API_HASH = getenv("API_HASH", "df2554b54a9eb9e572979b5db2d0cc79")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://acha:acha@cluster0.pjq3j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "ZONEY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ITSZONEY")
ALIVE_NAME = getenv("ALIVE_NAME", "ZONEY MUSIC ROBOT ASSISTANT")
BOT_USERNAME = getenv("BOT_USERNAME", "Krutika_X_BOT")
OWNER_ID = 5218610039
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Krutika_X_BOT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "INDIAN_SINGING_GROUPP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "IND_BRAND")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5169088527").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = 300
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Chiranjibkoch/Chiranjibkoch")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
