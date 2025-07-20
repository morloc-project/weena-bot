import discord
from discord.ext import commands
from pygments import highlight
from morloclexer.lexer import MorlocLexer
from pygments.formatters import TerminalFormatter
import os
from dotenv import load_dotenv

def highlight_morloc_code(msg):
    '''
    Highlight all blocks of morloc code
    '''

    block_heads = msg.split("```morloc")

    if(len(block_heads) <= 1):
        return msg

    for i in range(1,len(block_heads)):
        (morloc_code, non_morloc_code) = block_heads[i].split("```", maxsplit=1)  
        morloc_code = highlight(code, MorlocLexer(), TerminalFormatter())
        block_heads[i] = morloc_code + non_morloc_code 

    return ''.join(block_heads)


def main():

    description = '''An friendly native'''

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

        new_message = highlight_morloc_code(message.content)

        if new_message != message.content:
            await message.delete()
            await message.channel.send(new_message)

    bot.run(os.getenv("BOT_KEY"))

if __name__ == "__main__":
    main()
