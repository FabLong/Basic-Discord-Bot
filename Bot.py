# Made by: Fab Long ©
# https://github.com/FabLong/Basic-Discord-Bot << more info here

#imports
import discord
import time


#Keep track of your bot version here
version = "1.0.0"

# Read from server configuration file [server.txt]
# Required#####################################################
def read_token():
    with open("servers/server.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
def read_server_id():
    with open("servers/server.txt", "r") as f:
        lines = f.readlines()
        return lines[1].strip()
# Not required# But useful######################################
def read_channels():
    with open("servers/server.txt", "r") as f:
        lines = f.readlines()
        return lines[2].strip()
def read_users():
    with open("servers/server.txt", "r") as f:
        lines = f.readlines()
        return lines[3].strip()
################################################################

# Store important server information
token = read_token()
server_id = int(read_server_id())
channels = str(read_channels())
valid_users = str(read_users())

# ease of use
client = discord.Client()

########################################################################################################################

# Checking Messages in Discord Chat
@client.event
async def on_message(message):

    if message.content == "!help":
        embed = discord.Embed(title="Bot Commands Help", description="Available commands")
        embed.add_field(name="!help", value="shows help menu")
        embed.add_field(name="?bothelp", value="Admin {Bot configuration GitHub}")
        embed.add_field(name="!test", value="Checks Bot's status")
        await message.channel.send(content=None, embed=embed)


    # can be used to gather server info // [guild == server]
    id = client.get_guild(server_id)


    # Bot Commands
    if message.content == "?bothelp":
        await message.channel.send("visit: https://github.com/FabLong/Basic-Discord-Bot")
    # get time and version printed in server
    elif message.content == "!test":
        # the message below is embedded into the Discord chat using ```[TEXT-HERE]```
        await message.channel.send(f"```Server: Online\nTime: {time.ctime()}\nVersion: {version}```")

########################################################################################################################

# Starts Bot
client.run(token)
