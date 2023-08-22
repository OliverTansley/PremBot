import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging

from Cogs.BasicCog import BasicCog
from Cogs.FplCog import FplCog
from Cogs.ReminderCog import ReminderCog

load_dotenv()
TOKEN: str = str(os.getenv('DISCORD_TOKEN'))

intents: discord.Intents = discord.Intents.default()
intents.message_content = True

client: commands.Bot = commands.Bot(command_prefix='!', intents=intents)

logger: logging.Logger = logging.getLogger('discord')


@client.event
async def on_ready():
    '''
    Manually add cogs below
    '''
    logger.info(f'Reloading Cogs')
    try:
        await client.add_cog(BasicCog(client))
        await client.add_cog(ReminderCog(client))
        await client.add_cog(FplCog(client))
    except discord.errors.ClientException:
        logger.info(f'Error Loading Cogs')
        exit()
    logger.info(f'Loaded Cogs')

client.run(TOKEN)
