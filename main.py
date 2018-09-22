#TODO comment this while i still understand

import discord
import sys
#import asyncio
import subprocess

client = discord.Client()


async def run_script(file, channel):
  
    
    print("run_script")
    proc = subprocess.Popen(["python", "-u", f"./scripts/{str(file)}"], stdout=subprocess.PIPE, stderr=sys.stdout.buffer)
    stdout = proc.stdout
    msg = await channel.send(":)")
    
    for line in stdout:
        msg_content = ((msg.content)[10:])[:-3]

        if len(msg_content) < 15:
            msg_content_tosend = msg_content

        else:
            msg_content_tosend = (msg_content.partition("\n"))[2]
            print(msg_content.partition("\n"))

        to_send = f"```python\n{msg_content_tosend}{line.decode('ascii')}```"
        await msg.edit(content=to_send)

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith(client.user.mention):
        await msg.channel.send("aa")
        await run_script("test.py", msg.channel)


@client.event
async def on_ready():
    print("yes")

client.run("NDUxMDgxNDc3MzUxMDE0NDEy.DocG2Q.yLRvGSbY6pbm4Intrt1O7t-3CnU")

