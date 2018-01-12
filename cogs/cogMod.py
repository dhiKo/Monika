import discord
from discord.ext import commands

class Mod():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def ban(self, ctx, user:discord.Member=None):
        if ctx.message.author.server_permissions.ban_members is False:
            return await self.bot.say("**:x: You are not allowed to ban anyone!**")

        if user is None:
            return await self.bot.say("**:x: Please specify a user to ban!**")

        else:
            try:
                await self.bot.ban(user)
            except discord.Forbidden as e:
                if 'Privilege is too low' in str(e):
                    await self.bot.say("**:x: Privilege is too low!**")

    @commands.command(pass_context=True, no_pm=True)
    async def kick(self, ctx, user:discord.Member=None):
        if ctx.message.author.server_permissions.kick_members is False:
            return await self.bot.say("**:x: You are not allowed to kick anyone!**")

        if user is None:
            return await self.bot.say("**:x: Please specify a user to kick!**")

        else:
            try:
                await self.bot.kick(user)
            except discord.Forbidden as e:
                if 'Privilege is too low' in str(e):
                    await self.bot.say("**:x: Privilege is too low!**")

def setup(bot):
    bot.add_cog(Mod(bot))