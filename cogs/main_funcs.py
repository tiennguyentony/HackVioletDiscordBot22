
from discord.ext import commands


class main_funcs(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):

        response = "hello world"

        await ctx.send(response)

    @commands.command()
    async def python(self, ctx):
        response = ""

        await ctx.send(response)


def setup(bot):
    bot.add_cog(main_funcs(bot))