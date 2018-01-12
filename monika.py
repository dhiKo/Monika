# Discord
import discord
from discord.ext import commands
from discord.ext.commands import Bot

# Essentials
import asyncio
import random
import time
import datetime
import requests

botPrefix = 'm:'
bot = commands.Bot(command_prefix=botPrefix)
bot.remove_command('help')

console = bot.get_channel("400559879690911745")
startup_extensions = ["cogs.cogGeneral",
                      "cogs.cogInfo",
                      "cogs.cogFun",
                      "cogs.cogMod"]

owners = ["361305893255512076"]

@bot.event
async def on_ready():
    server_count = len(bot.servers)
    member_count = 0
    for server in bot.servers:
        for member in server.members:
            member_count += 1
    cmd = len(bot.commands)
    cgs = len(bot.cogs)
    ver = discord.__version__
    botU = str(bot.user)
    startUp = """Date: {}
 
- <> -
Ready to delete the server!
Logged in as: {}
Running in Discord v{}!
- <> -
Servers: {}
Users: {}
- <> -
Loaded up '{}' commands in '{}' cogs.
- <> -""".format(datetime.datetime.now(), botU, ver, server_count, member_count, cmd, cgs)
    print(startUp)
    await bot.change_presence(game=discord.Game(name="m:help | {} members |".format(member_count)))

# On Server Join
@bot.event
async def on_server_join(server):
    servers = len(bot.servers)
    members = 0
    for server in bot.servers:
        for member in server.members:
            members += 1
    await bot.change_presence(game=discord.Game(name="m:help | {} members |".format(members)))
    msgJoin = """__**Monika is now on {} servers!**__

*Note: If you didn't add this bot, maybe one of your staff members did.*

**Thank you for adding Monika!**
``She is ready to delete your server!``

**What is this bot all about?**
``This is the first DDLC-themed bot to be made!``

**Want to join our support server?**
``Here is the link to our support server!
(link)``

**We hope that you'll enjoy Monika!**""".format(servers)
    await bot.send_message(server.owner, msgJoin)

# Help
@bot.command(pass_context=True, no_pm=True)
async def help(ctx):
    helpManual = """__**Monika Command Manual**__

__**Developers**__
**m:load** - Loads an extension.
**m:unload** - Unloads an extension.

__**Info**__
**m:ping** - Checks the user's latency (but in reality it's just a randomizer).
**m:userinfo <user>** - Checks the user's info.
**m:icon <user>** - Links the avatar's icon.

__**General**__
**m:invite** - Sends an invite.
**m:help** - Shows this list.
**m:suggest <message>** - Suggest an idea!
**m:report <message>** - Report a bug/problem!

__**Fun**__
**m:password** - Generates a random secure password!
**m:pickpocket <user>** - Pickpockets a random amount of money from a user.
**m:roll** - Roll a die!
**m:ratewaifu <waifu>** - Let the bot rate your waifu!

__**Moderation**__
**m:kick <user>** - Kicks a member (requires KICK_MEMBERS permission)
**m:ban <user>** - Bans a member (requires BAN_MEMBERS permission)

More commands coming soon!

Do ``m:about`` for information about the bot!"""
    await bot.say(helpManual)

@bot.command(pass_context=True, no_pm=True)
async def about(ctx):
    em = discord.Embed(color=ctx.message.author.color)
    em2 = discord.Embed(color=ctx.message.author.color)
    em3 = discord.Embed(color=ctx.message.author.color)
    em.add_field(name="What is this bot all about?", value="This is the first DDLC-themed bot, this bot does normal bot stuff and there are more commands to come!")
    em2.add_field(name="Does it run 24/7?", value="Yes it runs 24/7.")
    em3.add_field(name="Who is the developer of this bot?", value="His Discord name is japanese-y but it means 'cute person', you can add him: かわいい♡人#3295")
    await bot.say(embed=em)
    await bot.say(embed=em2)
    await bot.say(embed=em3)

@bot.command()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    if ctx.message.author.id not in owners:
        return
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    if ctx.message.author.id not in owners:
        return
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(bot_token)