from .qotd import qotd

def setup(bot):
    bot.add_cog(qotd(bot))
