"""COMMAND : .peep"""

from telethon import events

import asyncio

from userbot.events import register 
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot



@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "peep":

        await event.edit(input_str)

        animation_chars = [
            
            "\n 🖤🖤LILPEEP BEAMERBOY🖤🖤 ",
            "\n Man, I don't know what the fuck goin' on lately,\nbro Everybody actin' real different and shit",
            "\n Ain't nobody,nobody was talkin'to me like a few months ago \n And now everybody hittin' my phone up and shit",    
            "\n I'm a mothafuckin' schema boy, I'm a dreamer boy\nI love a girl that don't even fuckin' need a boy",
            "\n Baby, I'm a beamer boy, I need a beamer, boy\nI want a Z3, that's a two-seater, boy",
            "\n Okay, I pull my cash out, shawty pass out\nTake her ass out, then I spaz out ",    
            "\n Okay, yeah, I hit that, shawty,get back\nI got death notes, where my list at?",
            "\n Yeah, I'm in my zone now, I put my phone down \n I'm on my own now, I'm on my own now",
            "\n Ya girl, she wanna go down on a real one\nI hit JGRXXN, like \"What's the deal bruh?\"",    
            "\n You see me doin' shows now, I'm a pro now\nI got hoes now and I got some dough now",
            "\n But they don't wanna hear that, they want that real shit\nThey want that drug talk, that \"I can't feel shit\"",
            "\n I'm never comin' home now, all alone now \n Can't let my bros down, can't let my bros down",
            "\n I feel like I'm a no one, that's what they told me\nI'ma show ya, baby, I was chosen, ayy",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])
CMD_HELP.update({
        "peep": 
        ".peep"
        "\nUsage: LIL🖤PEEP Beamerboy animated lyric.\n"
    })
