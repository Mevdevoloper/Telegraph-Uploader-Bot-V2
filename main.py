# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Telegraph-Uploader-Bot-V2/blob/main/LICENSE

import os
import time
import math
import json
import string
import random
import traceback
import asyncio
import datetime
import aiofiles
from random import choice 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from telegraph import upload_file
from database import Database


UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
BOT_OWNER = int(os.environ["BOT_OWNER"])
DATABASE_URL = os.environ["DATABASE_URL"]
db = Database(DATABASE_URL, "FnTelegraphBot")

Bot = Client(
    "Telegraph Uploader Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

START_TEXT = """**Hello {}  ❤️
I am small media or file to telegra.ph link uploader bot.**

>> `I can convert under 5MB photo or video to telegraph link.`

Made by @CodeMasterTG"""

HELP_TEXT = """**Hey, Follow these steps:**

➠ Just give me a media under 5MB
➠ Then I will download it
➠ I will then upload it to the telegra.ph link

**Available Commands**

/start - Checking Bot Online
/help - For more help
/status - For bot updates

Made by @Mo_Tech_YT"""

ABOUT_TEXT = """--**About Me**-- 😎

🤖 **Name :** [Telegraph Uploader](https://telegram.me/{})\n
👨‍💻 **Developer :** [Fayas](https://github.com/FayasNoushad)\n
👨‍💻 **Editor :** [Muhammed](https://github.com/Mrk_yt)\n
📢 **Channel :** [Mo Tech Channel](https://telegram.me/Mo_Tech_YT)\n
👥 **Group :** [Mo Tech Group](https://telegram.me/Mo_Tech_Group)\n
🌐 **Source :** [👉 Click here](https://github.com/MRK-YT/Telegraph-Uploader-Bot-V2)\n
📝 **Language :** [Python3](https://python.org)\n
🧰 **Framework :** [Pyrogram](https://pyrogram.org)\n
📡 **Server :** [Heroku](https://heroku.com)"""

FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"

START_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton('⚙ Help', callback_data='help'),
    InlineKeyboardButton('Close ✖️', callback_data='close')
    ]]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton('🏘 Home', callback_data='home'),
    InlineKeyboardButton('Close ✖️', callback_data='close')
    ]]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
