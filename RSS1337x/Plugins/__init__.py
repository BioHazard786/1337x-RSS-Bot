from RSS1337x import bot, loop
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import FloodWait
import psutil
import shutil
import re
from time import time
from ..config import *
from ..Helpers import Utils
from ..Helpers.FetchMagnetLink import fetch_magnet_link
from ..Database.Deta import add_users, remove_users
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(2)
