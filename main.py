#TODO comment this while i still understand

import discord
import sys
import asyncio
import subprocess

client = discord.Client()


async def run_script(file, channel):

    async def send_log(stdout, msg):
        print("send_log")
        
    
    print("run_script")
    proc = subprocess.Popen(["python", "-u", f"./scripts/{str(file)}"], stdout=subprocess.PIPE, stderr=sys.stdout.buffer)
    stdout = proc.stdout
    msg = await channel.send(":)")
    
    for line in stdout:
        to_send = f"```python\n{((msg.content)[9:])[:-3]}{line.decode('ascii')}```"
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

