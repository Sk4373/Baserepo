import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '21655449'))
API_HASH = environ.get('API_HASH', '112be9974e163f6dbd645ce4b94f4e6a')
BOT_TOKEN = environ.get('BOT_TOKEN', '6722766243:AAGh6qSkH27OjahN-3JcGeh5XLtsMQpzcMw')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1229852181').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/IllegalDeveloperBot')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002107365899'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+4RB2-U2o9yE4ZmQ9')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001856885647 -1001818726355').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://bqyrtxzl:7ExafpH6u8D74QbC@cluster0.ohzeohu.mongodb.net/?retryWrites=true&w=majority")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://mtqlfehk:LTAQxuGodluAG6cQ@cluster0.dr1fphj.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "bqyrtxzl")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'mtqlfehk')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '1001799594060'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/ccb9db43e62a2e524928e.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1001799594060'))
URL = environ.get('URL', 'illegal-testbot-308325bcba17.herokuapp.com')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002107365899'))
TUTORIAL = environ.get("TUTORIAL", "https://illegaldevelopers.blogspot.com/p/file.html?link=NTQwNDc2MjEzMw==_MTA1OQ==")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "e9c14ecc179245950a51803d50966fd1567f57c0")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "urlspay.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "9225b2f48ed01c4520a026d285b6c3932bf3bf88")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "moneykamalo.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "63c07aa03d3489c3e4448ff8ef8b36fe85b5f801")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "upshrink.com")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002078663926')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002008705346'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1002078663926')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# bot settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
