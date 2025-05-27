# Errors related to the bot

def error_Format(message_String):
    return "`" + message_String + "`"


# Print an error, based on what the user did wrong
async def print_Error(err_Code, channel):
    if err_Code == "ROLL_ERROR":
        await channel.send(error_Format("[!] Error! roll command used incorrectly! "
                                      "Proper usage is:\n!roll ndx \n"
                                       "Where n is how many dice you want to roll, and x is "
                                       "how many sides each die has."))
    elif err_Code == "ROLL_TOO_BIG_ERROR":
        await channel.send(error_Format("[!] Error! Roll values too big!"))
    else:
        await channel.send(error_Format("[!] An error happened!"))