import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents = intents)
import nest_asyncio
nest_asyncio.apply()
from discord.ext import commands
import discord
#developing bot functionality
bot = commands.Bot(command_prefix="^",intents = intents)
def run():

    @bot.event
    async def on_message(message: discord.Message):

        content = message.content
        mentions = message.mentions
        author = message.author
        #print(mentions)
        if 'fuck' or 'shit' or 'bitch' or 'fucker' or 'motherfucker' or 'nigger' or 'nigga' or 'dick' or 'dickhead' or 'cunt' or 'fatso' or 'bastard' or 'whore' or 'slut' in content:
          if message.author.bot == False:
            await message.channel.send("{} please refrain from using offensive content".format(author.name))
            print(message)

    bot.run(token)

run()