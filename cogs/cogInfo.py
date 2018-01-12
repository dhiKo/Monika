import discord
from discord.ext import commands
import random

class Info():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def ping(self, ctx):
        ping = random.randrange(1,287)
        await bot.say("**:ping_pong: Pong! Time taken: ``{}``ms.**".format(ping))

    @commands.command(pass_context=True, no_pm=True)
    async def icon(self, ctx, user:discord.Member=None):
        if user is None:
            return await self.bot.say("**:x: Please tag someone to get his/her avatar!**")

        else:
            await self.bot.say("**:frame_photo: Here you go!~\n{}**".format(user.avatar_url))

    @commands.command(pass_context=True, no_pm=True)
    async def userinfo(self, ctx, user:discord.Member=None):
        if user is None:
            uInfo = """__**{}'s User Information**__

**- <> -**
__Username:__ **{}**
__User ID:__ **{}**
__Status:__ **{}**

__Top role:__ **{}**
__Joined at:__ **{}**

__Administrator:__ **{}**
__View audit logs:__ **{}**
__Manage emojis:__ **{}**
__Manage roles:__ **{}**
__Manage nicknames:__ **{}**
__Kick members:__ **{}**
__Ban members:__ **{}**
__Mute members:__ **{}**
__Deafen members:__ **{}**
**- <> -**""".format(ctx.message.author.name,
                    ctx.message.author.name,
                    ctx.message.author.id,
                    ctx.message.author.status,
                    ctx.message.author.top_role,
                    ctx.message.author.joined_at,
                    ctx.message.author.server_permissions.administrator,
                    ctx.message.author.server_permissions.view_audit_logs,
                    ctx.message.author.server_permissions.manage_emojis,
                    ctx.message.author.server_permissions.manage_roles,
                    ctx.message.author.server_permissions.manage_nicknames,
                    ctx.message.author.server_permissions.kick_members,
                    ctx.message.author.server_permissions.ban_members,
                    ctx.message.author.server_permissions.mute_members,
                    ctx.message.author.server_permissions.deafen_members)
            await self.bot.say(uInfo)
        else:

            uInfo = """__**{}'s User Information**__

**- <> -**
__Username:__ **{}**
__User ID:__ **{}**
__Status:__ **{}**

__Top role:__ **{}**
__Joined at:__ **{}**

__Administrator:__ **{}**
__View audit logs:__ **{}**
__Manage emojis:__ **{}**
__Manage roles:__ **{}**
__Manage nicknames:__ **{}**
__Kick members:__ **{}**
__Ban members:__ **{}**
__Mute members:__ **{}**
__Deafen members:__ **{}**
**- <> -**""".format(user.name,
                     user.name,
                     user.status,
                     user.top_role,
                     user.joined_at,
                     user.server_permissions.administrator,
                     user.server_permissions.view_audit_logs,
                     user.server_permissions.manage_emojis,
                     user.server_permissions.manage_roles,
                     user.server_permissions.manage_nicknames,
                     user.server_permissions.kick_members,
                     user.server_permissions.ban_members,
                     user.server_permissions.mute_members,
                     user.server_permissions.deafen_members)
            await bot.say(uInfo)

def setup(bot):
    bot.add_cog(Info(bot))