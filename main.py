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
    blocks = []
    while True:
        (left, sep, right) = msg.partition("```morloc")
        blocks.append(left)
        if not sep:
            break
        else:
            (left2, sep2, right2) = right.partition("```")
            if not sep2:
                blocks.append(left2)
                break
            morloc_code = highlight(left2, MorlocLexer(), TerminalFormatter())
            blocks.extend(["```ansi\n", morloc_code, "```"])
            msg = right2
    return ''.join(blocks)


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
            #  await message.delete()
            await message.channel.send(new_message)

    bot.run(os.getenv("BOT_KEY"))

if __name__ == "__main__":
    main()
