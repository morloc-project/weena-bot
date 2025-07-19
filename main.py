import discord
from discord.ext import commands
from pygments import highlight
from morloclexer.lexer import MorlocLexer
from pygments.formatters import TerminalFormatter
import os
from dotenv import load_dotenv

def main():

    description = '''An example bot to showcase the discord.ext.commands extension
    module.
    
    There are a number of utility commands being showcased here.'''
    
    load_dotenv()
    
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    
    bot = commands.Bot(command_prefix='?', description=description, intents=intents)
    
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')
    
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        if message.content.startswith('```morloc'):
            # uncomment to delete message before reformatting
            # await message.delete()
            code = message.content
            code = code.removeprefix('```morloc')
            code = code.removesuffix('```')      
    
            transformed = highlight(code, MorlocLexer(), TerminalFormatter())
            transformed = '```ansi\n'+transformed+'```'
            await message.channel.send(transformed)
    
    bot.run(os.getenv("BOT_KEY"))


if __name__ == "__main__":
    main()
