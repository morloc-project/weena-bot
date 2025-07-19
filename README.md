# Morloc Utility Bot - 'Weena'

A simple discord bot that waits for a new morloc codeblock:

> ```morloc

and reformats the output to ansi formatted text for displaying in discord

Other features are TBD

## Getting Started
This project is built using uv

[installation instructions for uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

Once uv has been installed, `uv sync` will install all the required packages.

Create an .env file with the format:

```
BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```

and then start the project with `uv run main.py` 


Bot requires send message permissions in the channels it joins, view history and edit message permissions are also useful if setting the bot to delete reformatted messages
