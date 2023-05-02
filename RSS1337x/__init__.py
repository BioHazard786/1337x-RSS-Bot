import asyncio
import glob
from os.path import dirname, basename, isfile, join
from .config import *
from pyrogram import Client, enums
from importlib import import_module
from subprocess import Popen

__all__ = ['bot', 'loop']

loop = asyncio.get_event_loop()

bot = Client(
    "1337xRSS",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=enums.ParseMode.HTML,
).start()

server = Popen(f"gunicorn web.app:app --bind 0.0.0.0:8000", shell=True)


files = glob.glob(join(join(dirname(__file__), 'Plugins'), '*py'))
plugins = [basename(f)[:-3] for f in files if isfile(f)
           and not f.endswith('__init__.py')]

files = glob.glob(join(join(dirname(__file__), 'Helpers'), '*py'))
feeds = [basename(f)[:-3] for f in files if isfile(f)
         and not f.endswith('__init__.py')]

for plug in plugins:
    import_module('RSS1337x.Plugins.'+plug)

for feed in feeds:
    import_module('RSS1337x.Helpers.'+feed)
