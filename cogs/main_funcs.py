
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
        response = """
        Here is some resources that I found: 

        Learning Resrouces you might want to start: 
        https://www.learnpython.org/

        Python class: 
        https://developers.google.com/edu/python

        Basic Usage of Python: 
        https://docs.python-guide.org/

        Project Ideas:
            - Discord Bot 
            - Microblog
            - Quiz Application """

        await ctx.send(response)
    @commands.command()
    async def Cplusplus (self, ctx):
        response = """
        Here is some resources that I found: 

        Learning Resrouces you might want to start: 
        https://www.learncpp.com/

        C++ class: 
        https://developers.google.com/edu/c++

        What C++ used for: 
        https://www.softwaretestinghelp.com/cpp-applications/

        Project Ideas:
            - Login and Registeration System 
            - Sudoku Game
            - Car Rental System """

        await ctx.send(response)
    @commands.command()
    async def Typescript (self, ctx):
        response = """
        Here is some resources that I found: 

        Learning Resrouces you might want to start: 
        https://www.typescriptlang.org/docs/
        Follow this for Typescript weekly information: 
        https://www.typescript-weekly.com/

        What Typescript used for: 
        https://javascript.plainenglish.io/7-trending-typescript-projects-on-github-675d3fc8ecae

        Project Ideas:
            - Restaunrant Menu
            - Navigation Bar on scroll
            - Countdown clock"""

        await ctx.send(response)
    @commands.command()
    async def Ruby (self, ctx):
        response = """
       Here is some resources that I found: 

        Learning Resrouces you might want to start: 
        https://guides.rubyonrails.org/getting_started.html
        
        Valuable book to learn Ruby:
        https://www.railstutorial.org/

        What makes Ruby different from other: 
        https://javascript.plainenglish.io/7-trending-typescript-projects-on-github-675d3fc8ecae

        Project Ideas:
            - Restaunrant Menu
            - Navigation Bar on scroll
            - Countdown clock"""

        await ctx.send(response)


def setup(bot):
    bot.add_cog(main_funcs(bot))