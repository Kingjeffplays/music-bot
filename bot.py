import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
 
startup_extensions = ["Music"]

bot = commands.Bot("!")



@bot.event
async def on_ready():
    print ("bot online")
    await bot.change_presence(game=discord.Game(type=0, name='Coded by: AήimeṨhαmαn'))


                              
class Main_Commands():
        def __init__(self, bot):
         self.bot = bot
         
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")
 
 
@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi :wave:")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
 
bot.run("NDAzMzQzMDA5MzEzNDU2MTI4.DUIHmA.gGMrd4eB7yULSCQmA2Lvx4zbqLA")
