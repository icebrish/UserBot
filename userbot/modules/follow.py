# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the social media. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.follow$")
async def follow(follow):
    """ For .follow command, check if the bot is running.  """
    await follow.edit(
                     f"`FOLLOW {DEFAULTUSER} ON` \n\n"
                     f"[InstaGram💬](https://www.instagram.com/icecold.br/) \n\n"
                     f"[Telegram💬](https://www.telegram.dog/z_chaos) \n\n"
                     f"[sololearn👨🏻‍💻](https://www.sololearn.com/Profile/15538701) \n\n"
                     f"[github👨🏻‍💻](https://github.com/icebrish/) \n\n"
                     f"[Wattpad📖](https://www.wattpad.com/user/Beammerboy) "
                     )    



CMD_HELP.update({
    "follow":
    ".follow\
    \nUsage: Type .follow to provide your follow links."
    })
