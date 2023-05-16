from RSS1337x import bot, loop
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from concurrent.futures import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ..config import *
import json
import asyncio
import requests
from bs4 import BeautifulSoup
from ..Database.MongoDB import *
executor = ThreadPoolExecutor(10)
