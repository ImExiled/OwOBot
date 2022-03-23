#
#
#    OwOBot by Exile.
#   Please do not redis
#
#

# Here, we'll set up some basic variables.
#
# commandSyntax is the command code to use within Discord to call upon the bot. Default: $o
commandSyntax = '$o'

# The token generated by Discord so we can have a Bot user. (Could technically be your user token OwO)
#
# Note: If using a service such as Replit, this token can be seen publically. To hide this token in Replit, use an Environment Variable.
#
# See: https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables
# for more information.
botToken = "" # DO NOT LET THIS BE PUBLIC!!

# Should NSFW content be allowed on this instance?
NSFW = False

# Enable enhanced logging?
#
# Enhanced logging will log more information then the essentials, including all requests to get an image!
# Enhanced Logging will not display some information, such as when a command is run, or the user who called it.
EnhancedLogging = True

from aiohttp import request
import discord
import requests
import json
##### We import `os` because Replit needs it for Environment Variables. ######
import os


client = discord.Client()

# Standard `def`s. Also known as functions.
def getNSFWNeko():
    # Is NSFW enabled?
    if NSFW == False:
        if EnhancedLogging == True:
            print("[EXTERNAL] [WARN] A user tried to call an NSFW command when NSFW mode is disabled.")
        return "Uh-oh! NSFW content is disabled on this instance. You're lewd!! (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)"
    else:
        response = requests.get("https://nekos.life/api/v2/img/hentai")
        json_data = json.loads(response.text)
        img = json_data['url']
        print("[EXTERNAL] [INFO] User requested image: " + img + " [NSFW]")
        return img

def getNSFWByType(type):
    if NSFW == False:
        if EnhancedLogging == True:
            print("[EXTERNAL] [WARN] A user tried to call and NSFW command when NSFW mode is disabled.")
        return "Uh-oh! NSFW content is disabled on this instance. You're lewd!! (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)"
    else:
        response = requests.get("https://nekos.life/api/v2/img/" + type)
        json_data = json.loads(response.text)
        img = json_data['url']
        print("[EXTERNAL] [INFO] User requested image: " + img + " [NSFW]")
        return img

def getSFWNeko():
  response = requests.get("https://nekos.life/api/v2/img/neko")
  json_data = json.loads(response.text)
  #print(json_data['url'])
  img = json_data['url']
  return img
clear = lambda: os.system('clear')
clear()
print("######## OwOBot ########")
print("Created by Exile#1931")
print("\n")
print("[INTERNAL] [INFO] Connecting to Discord...")

@client.event
async def on_ready():
  print("[INTERNAL] [INFO] Successfully logged into Discord as {0.user}".format(client))
  if EnhancedLogging == True:
      # Enhanced Logging enabled!
      print("[INTERNAL] [INFO] ### Enhanced Logging is enabled! ###")
  print("[INTERNAL] [INFO] Ready!")
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith(commandSyntax + " help"):
      await message.channel.send("Hi there! (* ^ ω ^)\nHere's a list of commands you can use!\n```help: Displays this message\nneko: Post a random (Safe) image of a neko!\nping: Pong!```")
  if message.content.startswith(commandSyntax + " ping"):
    # Simple ping command. Used to confirm Bot is online.
    await message.channel.send('Pong!')
  if message.content.startswith(commandSyntax + " neko"):
    # Get a random (SFW) neko!
    img = getSFWNeko()
    await message.channel.send(img)
  if message.content.startswith(commandSyntax + " nsfw"):
      img = getNSFWNeko()
      await message.channel.send(img)
  if message.content.startswith(commandSyntax + " lewd"):
      typeToUse = message.content.lstrip(commandSyntax + " lewd")
      img = getNSFWByType(typeToUse)
      await message.channel.send(img)
# Check if `botToken` is defined.
if botToken == "":
  # If botToken is not defined, we'll assume we're using replit, and pull our token from the TOKEN Environment Variable.
  client.run(os.getenv('TOKEN'))
else:
  # If botToken IS defined, we'll use it.
  client.run(botToken)
