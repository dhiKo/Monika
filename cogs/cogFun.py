import discord
from discord.ext import commands
import random

class Fun():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def password(self, ctx):
        firstPart = ["altrox",
                     "memolp",
                     "asusoa",
                     "loaiso",
                     "vsmeir",
                     "bittia",
                     "laosli",
                     "vutrix",
                     "alpoal",
                     "nizreg",
                     "beleht"]
        secondPart = ["127821",
                      "127348",
                      "148929",
                      "7524890",
                      "231677",
                      "1642789",
                      "12356",
                      "1623478",
                      "146872",
                      "126496",
                      "145685",
                      "1249863",
                      "147908",
                      "1324679",
                      "142358"]
        f1 = firstPart[random.randrange(len(firstPart))]
        s2 = secondPart[random.randrange(len(secondPart))]
        await self.bot.send_message(ctx.message.author, "Here's your random generated password!\n\n{}{}".format(f1, s2))
        await self.bot.say("**:white_check_mark: Your random generated password has been sent!**")

    @commands.command(pass_context=True, no_pm=True)
    async def pickpocket(self, ctx, user:discord.Member=None):
        if user is None:
            return await self.bot.say("**:x: You are not allowed to pickpocket yourself!**")
        money = random.randrange(1,236478)
        await self.bot.say(":white_check_mark: **{} has pickpocketed ${} from {}!**".format(ctx.message.author.name, money, user))

    @commands.command(pass_context=True, no_pm=True)
    async def roll(self, ctx):
        var = int(random.random() * 6)
        await self.bot.say("**:game_die: You rolled a ``{}``!**".format(var+1))

    @commands.command(pass_context=True, no_pm=True)
    async def ratewaifu(self, ctx, waifu=None):
        if waifu is None:
            return await self.bot.say("**:x: You didn't let me rate your waifu!**")

        else:
            msg = await self.bot.say(":heart: **Rating waifu...**")
            rate = random.randrange(1,100)
            waifu = ctx.message.content[12:]
            await self.bot.edit_message(msg, ":heart_decoration:   :heart_decoration:   :heart_decoration:   :heart_decoration: \n**:heart: I rated your waifu!: ``{}%``!**\n**:heart_exclamation: Waifu: {}**\n:heart_decoration:   :heart_decoration:   :heart_decoration:   :heart_decoration: ".format(rate, waifu))

def setup(bot):
    bot.add_cog(Fun(bot))