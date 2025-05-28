# Handles What we do on certain commands
from error import print_Error
from random import randint


# Format the message for this bot
def bot_Format(message_String):
    return "`" + message_String + "`"


# Print a help message to the user
async def help_Command(message):
    help_String = "[!help]: Displays this help message.\n"
    help_String += "[!roll ndx]: Rolls n dice, each with x sides counting up from 1.\n"
    await message.channel.send(bot_Format(help_String))

# What we do when a roll is requested
#   message is the message object that requested this
async def roll_Command(message):
    # We are trying to roll a dice, using standard [n]d[x] rules
    command_Array = message.content.split()
    try:
        dice_Request = command_Array[1].split('d')  # Get the [n]d[x] in array form
    except IndexError:
        await print_Error("ROLL_ERROR", message.channel)
        return

    # Check that the [n]d[x] was properly formatted
    if len(dice_Request) != 2:
        await print_Error("ROLL_ERROR", message.channel)
        return

    # Figure out how many of each dice we are rolling, and their sizes
    num_Dice = 0
    if len(dice_Request[0]) == 0:
        num_Dice = 1  # Default size
    else:
        if not dice_Request[0].isdigit():
            await print_Error("ROLL_ERROR", message.channel)
            return
        else:
            num_Dice = int(dice_Request[0])

    dice_Size = 0
    if len(dice_Request[1]) == 0:
        dice_Size = 20  # Lets say this is the default size
    else:
        if not dice_Request[1].isdigit():
            await print_Error("ROLL_ERROR", message.channel)
            return
        else:
            dice_Size = int(dice_Request[1])

    if num_Dice > 100000 or dice_Size > 999999999:
        # Stop ridiculous things
        await print_Error("ROLL_TOO_BIG_ERROR", message.channel)
        return

    if num_Dice == 1:
        await message.reply(bot_Format(f"{randint(1, dice_Size)}"))
    else:
        # We are rolling multiple dice
        final_String = ""
        total = 0  # All of the dice added together
        for i in range(num_Dice):
            if len(final_String) > 1950:
                await message.reply(final_String)
                final_String = ""
            roll = randint(1, dice_Size)
            total += roll
            final_String += bot_Format(f"{roll}") + " "
        final_String += "\n" + bot_Format(f"total:{total}")
        await message.reply(final_String)
