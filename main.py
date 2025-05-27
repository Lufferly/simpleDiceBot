import discord
import os
from dotenv import load_dotenv
# Our bot commands
from botCommands import *

# Load the environment file for the Simple Dice Bot
load_dotenv()
# Get the token from the environment file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Create the intents, ie what our bot plans on doing
intents = discord.Intents.default()
intents.message_content = True
# Create the bot's client, our connection to discord
diceBot = discord.Client(intents=intents)

@diceBot.event
async def on_ready():
    # When the bot is ready
    print(f"Logged in as {diceBot.user}!")


@diceBot.event
async def on_message(message): # What we do when we see a message
    print(f"[*] Seen message: {message.content}")

    # Check that the message does not come from the bot itself
    if message.author == diceBot.user:
        return

    if message.content.startswith("!test"):
        await message.channel.send(bot_Format("Test received!"))

    if message.content.startswith("!roll"):
        await roll_Command(message)


# Actually run the discord bot
diceBot.run(DISCORD_TOKEN)
