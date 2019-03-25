from redbot.core import commands
<<<<<<< HEAD:qotd/qotd.py

class Mycog:
=======
        
class qotd:
>>>>>>> 4d1f631a9ccacf6ba5d87bb3f49c38e0292fffee:qotd/qotd.py
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

     @commands.command()
  async def mycom(self, ctx):
      """This does stuff!"""
      # Your code will go here
      await ctx.send("I can do stuff!")
