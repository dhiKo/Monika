import discord
from discord.ext import commands

class General():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def invite(self):
        await self.bot.say("**:love_letter: Here you go!~\nhttps://discordapp.com/oauth2/authorize?client_id=400555904103350282&scope=bot&permissions=2146958591**")

    @commands.command(pass_context=True, no_pm=True)
    async def report(self, ctx, message:str=None):
        if message is None:
            return await self.bot.say("**:x: There's no bug/problem to report!**")\

        else:
            console = self.bot.get_channel("400569314333425675")
            message = ctx.message.content[9:]
            await self.bot.send_message(console, "{} has reported a bug/problem!\n{}\n\nFrom the server: {}".format(ctx.message.author.name, message, ctx.message.author.server.name))
            await self.bot.say("**:white_check_mark: The bug/problem has been successfully sent to the console!**")

    @commands.command(pass_context=True, no_pm=True)
    async def suggest(self, ctx, message:str=None):
        if message is None:
            return await self.bot.say("**:x: You can't suggest nothing!**")

        else:
            console = self.bot.get_channel("400569314333425675")
            message = ctx.message.content[10:]
            await self.bot.send_message(console, "{} has suggested something!\n{}\n\nFrom the server: {}".format(ctx.message.author.name, message, ctx.message.author.server.name))
            await self.bot.say("**:white_check_mark: Your suggestion has been successfully sent to the console!**")

def setup(bot):
    bot.add_cog(General(bot))