# ---------------------------------------------------
# File Name: func.py
# Updated: Fixed WebpageMediaEmpty & Start Response Issue
# ---------------------------------------------------

import math
import time, re
from pyrogram import enums
from config import CHANNEL_ID, OWNER_ID 
from devgagan.core.mongo.plans_db import premium_users
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import cv2
from pyrogram.errors import FloodWait, InviteHashInvalid, InviteHashExpired, UserAlreadyParticipant, UserNotParticipant
from datetime import datetime as dt
import asyncio, subprocess, os

async def chk_user(message, user_id):
    user = await premium_users()
    if user_id in user or user_id in OWNER_ID:
        return 0
    else:
        return 1

async def gen_link(app, chat_id):
    try:
        link = await app.export_chat_invite_link(chat_id)
        return link
    except Exception:
        return f"https://t.me/{chat_id}"

async def subscribe(app, message):
    update_channel = CHANNEL_ID
    if not update_channel:
        return 0
    
    url = await gen_link(app, update_channel)
    try:
        user = await app.get_chat_member(update_channel, message.from_user.id)
        if user.status == "kicked":
            await message.reply_text("You are Banned. Contact -- @Pre_contact_bot")
            return 1
    except UserNotParticipant:
        # यहाँ फोटो हटा दी गई है ताकि आपका बॉट अटके नहीं
        caption = "👋 **हेलो!**\n\nआगे बढ़ने के लिए कृपया हमारे चैनल को जॉइन करें।"
        await message.reply_text(
            text=caption,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Now...", url=f"{url}")]])
        )
        return 1
    except Exception as e:
        print(f"Subscribe Error: {e}")
        return 0
    return 0

async def get_seconds(time_string):
    def extract_value_and_unit(ts):
        value = ""
        unit = ""
        index = 0
        while index < len(ts) and ts[index].isdigit():
            value += ts[index]
            index += 1
        unit = ts[index:].lstrip()
        if value:
            value = int(value)
        return value, unit

    value, unit = extract_value_and_unit(time_string)
    if unit == 's': return value
    elif unit == 'min': return value * 60
    elif unit == 'hour': return value * 3600
    elif unit == 'day': return value * 86400
    elif unit == 'month': return value * 86400 * 30
    elif unit == 'year': return value * 86400 * 365
    else: return 0

PROGRESS_BAR = """\n
│ **__Completed:__** {1}/{2}
│ **__Bytes:__** {0}%
│ **__Speed:__** {3}/s
│ **__ETA:__** {4}
╰─────────────────────╯
"""

async def progress_bar(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff if diff > 0 else 0
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000 if speed > 0 else 0
        estimated_total_time = elapsed_time + time_to_completion
        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
        progress = "{0}{1}".format(
            ''.join(["♦" for i in range(math.floor(percentage / 10))]),
            ''.join(["◇" for i in range(10 - math.floor(percentage / 10))]))
        tmp = progress + PROGRESS_BAR.format( 
            round(percentage, 2), humanbytes(current), humanbytes(total),
            humanbytes(speed), estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(text="{}\n│ {}".format(ud_type, tmp))             
        except: pass

def humanbytes(size):
    if not size: return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " "
        
